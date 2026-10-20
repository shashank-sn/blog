// Renders every */*/figures/*.mmd (Mermaid) to an .svg next to it with Pele,
// in the repo's monochrome look, and embeds Google Sans in every figure and in
// the hand-made assets/*.svg. GitHub shows SVGs as images, which cannot load
// web fonts or page CSS, so the font and the theme are baked into each file.
//
//   npm install            (once)
//   npm run figures        render figures and embed fonts
//   npm run figures:check  fail if any .svg is out of date
//
// Fonts: fonts/GoogleSans-{400,500,700}.ttf are Latin static instances of
// Google Sans (SIL Open Font License 1.1, see fonts/OFL.txt). Each SVG embeds a
// WOFF2 subset with only the characters and weights it uses.
import { readFileSync, writeFileSync, globSync } from "node:fs";
import { render } from "pele";
import opentype from "opentype.js";
import subsetFont from "subset-font";

const THEME = {
  bg: "#ffffff",
  fg: "#121212",
  muted: "#6b6b6b",
  line: "#121212",
  surface: "#ffffff",
  "surface-alt": "#f5f5f5",
  border: "#121212",
  accent: "#121212",
  critical: "#121212",
  error: "#121212",
  radius: "10px",
};
const FONT = "'Google Sans', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif";
const WEIGHTS = [400, 500, 700];
const FONT_FILES = Object.fromEntries(WEIGHTS.map((w) => [w, readFileSync(`fonts/GoogleSans-${w}.ttf`)]));
const FONTS = Object.fromEntries(
  WEIGHTS.map((w) => {
    const buf = FONT_FILES[w];
    return [w, opentype.parse(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength))];
  }),
);

// Pele lays out boxes from text widths, so measure with the real font.
// style bits: 1 bold, 2 italic, 4 monospace.
const measurer = {
  width(text, size, style) {
    if (style & 4) return text.length * size * 0.6;
    return FONTS[style & 1 ? 700 : 400].getAdvanceWidth(text, size);
  },
};

// Pele themes through CSS custom properties. Some SVG renderers (link previews,
// Apple's CoreSVG) ignore them, so resolve every var() to a literal value.
function resolveVars(svg) {
  svg = svg.replace(/var\(--pele-([a-z-]+),((?:[^()]|\([^()]*\))*)\)/g, (_, name, fallback) => THEME[name] ?? fallback.trim());
  const aliases = {};
  for (const [, name, value] of svg.matchAll(/(--_[a-z]+):([^;"]+)/g)) aliases[name] = value.trim();
  svg = svg.replace(/var\((--_[a-z]+)\)/g, (whole, name) => aliases[name] ?? whole);
  svg = svg.replace(/--_[a-z]+:[^;"]+;?/g, "");
  svg = svg.replace(/style="rx:([\d.]+)px"/g, 'rx="$1" ry="$1"');
  if (/var\(/.test(svg)) throw new Error("unresolved var() left in figure");
  return svg;
}

function decode(text) {
  return text
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;|&apos;/g, "'")
    .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)))
    .replace(/&amp;/g, "&");
}

// Embed a WOFF2 subset of each weight the SVG uses, with only its characters.
async function embedFont(svg) {
  svg = svg.replace(/<style id="embedded-font">[\s\S]*?<\/style>/, "");
  const body = svg.replace(/<title[\s\S]*?<\/title>/g, "");
  const chars = new Set();
  for (const [, inner] of body.matchAll(/<text\b[^>]*>([\s\S]*?)<\/text>/g)) {
    for (const ch of decode(inner.replace(/<[^>]+>/g, ""))) chars.add(ch);
  }
  if (!chars.size) return svg;
  const text = [...chars].join("");
  const used = new Set([400]);
  if (/font-weight(?:=|:)\s*"?(?:bold|700)/.test(body) || /<tspan[^>]*font-weight="bold"/.test(body)) used.add(700);
  if (/font-weight(?:=|:)\s*"?500/.test(body)) used.add(500);
  let faces = "";
  for (const w of WEIGHTS.filter((w) => used.has(w))) {
    const woff2 = await subsetFont(FONT_FILES[w], text, { targetFormat: "woff2" });
    faces += `@font-face{font-family:'Google Sans';font-weight:${w};font-style:normal;src:url(data:font/woff2;base64,${woff2.toString("base64")}) format('woff2')}`;
  }
  return svg.replace(/^(<svg[^>]*>)/, `$1<style id="embedded-font">${faces}</style>`);
}

async function renderFigure(source) {
  const { svg } = render(source, {
    fontFamily: FONT,
    fontSize: 15,
    padding: 20,
    responsive: false,
    autoDirection: false,
    measurer,
  });
  const themed = resolveVars(svg).replace(
    /^(<svg[^>]*>)/,
    '$1<rect class="paper" width="100%" height="100%" fill="#ffffff"/>',
  );
  return (await embedFont(themed)) + "\n";
}

const check = process.argv.includes("--check");
const stale = [];
async function update(path, next) {
  let current = "";
  try {
    current = readFileSync(path, "utf8");
  } catch {}
  if (current === next) return;
  if (check) stale.push(path);
  else {
    writeFileSync(path, next);
    console.log("wrote", path);
  }
}

for (const mmd of globSync("*/*/figures/*.mmd").sort()) {
  await update(mmd.replace(/\.mmd$/, ".svg"), await renderFigure(readFileSync(mmd, "utf8")));
}
for (const asset of globSync("assets/*.svg").sort()) {
  const current = readFileSync(asset, "utf8");
  await update(asset, (await embedFont(current.trimEnd())) + "\n");
}

if (check && stale.length) {
  console.error(`out of date (run npm run figures): ${stale.join(", ")}`);
  process.exit(1);
}
if (check) console.log("figures are up to date");
