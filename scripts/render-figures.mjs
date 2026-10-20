// Renders every */*/figures/*.mmd (Mermaid) to an .svg next to it with Pele,
// in the repo's monochrome look. GitHub shows the SVGs as images, so page CSS
// cannot reach them: the theme is baked into each file.
//
//   npm install            (once, installs the pinned pele version)
//   npm run figures        render all figures
//   npm run figures:check  fail if any .svg is out of date with its .mmd
import { readFileSync, writeFileSync, globSync } from "node:fs";
import { render } from "pele";

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

// Pele themes through CSS custom properties. Some SVG renderers (link previews,
// Apple's CoreSVG) ignore them, so resolve every var() to a literal value.
function resolveVars(svg) {
  // 1. the public theme: var(--pele-x, fallback) -> THEME value or its fallback
  svg = svg.replace(/var\(--pele-([a-z-]+),((?:[^()]|\([^()]*\))*)\)/g, (_, name, fallback) => THEME[name] ?? fallback.trim());
  // 2. the private aliases Pele declares on the root, such as --_fg:#121212
  const aliases = {};
  for (const [, name, value] of svg.matchAll(/(--_[a-z]+):([^;"]+)/g)) aliases[name] = value.trim();
  svg = svg.replace(/var\((--_[a-z]+)\)/g, (whole, name) => aliases[name] ?? whole);
  svg = svg.replace(/--_[a-z]+:[^;"]+;?/g, "");
  // 3. rounded corners set through CSS become plain attributes
  svg = svg.replace(/style="rx:([\d.]+)px"/g, 'rx="$1" ry="$1"');
  if (/var\(/.test(svg)) throw new Error("unresolved var() left in figure");
  return svg;
}

function renderFigure(source) {
  const { svg } = render(source, { fontFamily: FONT, fontSize: 15, padding: 20, responsive: false, autoDirection: false });
  return (
    resolveVars(svg)
      // a white page behind the diagram keeps it readable in GitHub dark mode
      .replace(/^(<svg[^>]*>)/, '$1<rect class="paper" width="100%" height="100%" fill="#ffffff"/>') + "\n"
  );
}

const check = process.argv.includes("--check");
const stale = [];
for (const mmd of globSync("*/*/figures/*.mmd").sort()) {
  const svgPath = mmd.replace(/\.mmd$/, ".svg");
  const svg = renderFigure(readFileSync(mmd, "utf8"));
  let current = "";
  try {
    current = readFileSync(svgPath, "utf8");
  } catch {}
  if (current === svg) continue;
  if (check) stale.push(svgPath);
  else {
    writeFileSync(svgPath, svg);
    console.log("rendered", svgPath);
  }
}
if (check && stale.length) {
  console.error(`out of date (run npm run figures): ${stale.join(", ")}`);
  process.exit(1);
}
if (check) console.log("figures are up to date");
