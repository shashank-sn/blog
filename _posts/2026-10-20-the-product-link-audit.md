---
layout: post
lane: operate
order: 1
title: a broken link is a content bug with a customer attached
description: six customers said the link was broken. the real picture was six written complaints, nineteen written reviews and thirty-eight ratings. how to audit a product library and fix it at the source.
skill:
  name: deliverable-audit
  summary: classifies every review, maps each complaint to a deliverable, finds the canonical file, checks each fix logged out, drafts the replies and reports what is still missing, with honest counts.
  zip: /downloads/deliverable-audit.zip
---

# a broken link is a content bug with a customer attached

six customers said the link was broken. the real picture was six written complaints, nineteen written reviews, and thirty-eight ratings. the difference matters.

i give away eleven free products. each one is a page, a promise, and a file at the end of a link. over time some of those links broke. files move and get renamed, and the link on the product page doesn't follow them. nobody noticed until a customer left a review saying "the link doesn't work".

it's tempting to treat that as a support ticket: send the person the file, say sorry, move on. but the next person who downloads the product hits the same dead link. the bug is in the product, not in the conversation. so fix it there.

## count honestly first

before fixing anything, i needed to know how big the problem was. that turned out to be harder than it looked.

the store showed 38 ratings across the eleven products. only 19 of those came with written text. the other 19 were bare star ratings, with no way to know why someone gave three stars instead of five. of the 19 written reviews, six were specifically about a broken or missing link.

so "how many people hit a broken link" has no clean answer. six said so in writing. some of the bare ratings might be the same problem, but i can't read a star. the honest report says exactly that, instead of rounding the six up to make the audit look important or down to make the products look fine.

<figure class="fig">
{% include figs/review-funnel.svg %}
<figcaption>six is the number you can prove. the 19 bare ratings stay in the report as unreadable, not as zero.</figcaption>
</figure>

## the process

1. **export the product list and every review.** all of them, not just the low ones.
2. **classify each review.** written complaint, written praise, or bare rating. read the five-star reviews too, because people often say "great, but the link was broken" and still give five stars.
3. **name the deliverable for each complaint.** which product, and what file was the customer supposed to get?
4. **check the public page and the delivery.** open the product page and the delivery email or file the way a customer would.
5. **find the canonical file.** search your workspace by title, by any older title, and by content. not just the exact filename, because the file that moved usually got renamed too.
6. **fix the product and the delivery link.** update the source, not just the one customer.
7. **verify the fix properly.** open the link while logged out. check the file type. confirm the content matches the product. a link that returns a page is not the same as a link that delivers the right file.
8. **reply to every relevant review.** with the corrected link, in the same words each time if that's your policy.
9. **report the full inventory.** total reviews, relevant reviews, fixed, still missing, and the ratings you couldn't read.

## "it loads" is not "it works"

step 7 is where most fixes quietly fail.

a link can load and still be broken. it can open a sign-in page, because you're logged in and the customer isn't. it can open the right folder with the wrong file in it. it can open an older version of the guide. every one of those looks fine when you click it from your own account.

so the check is three questions, asked logged out. does it open without a sign-in? is it the right kind of file? is the content the thing the product page promised?

<figure class="fig">
{% include figs/link-checks.svg %}
<figcaption>a fix counts only when all three pass in a logged-out window.</figcaption>
</figure>

## close the loop

the last two steps are what turn a repair into trust.

the reply goes to every person who reported the problem, with the working link. it doesn't matter that the review is weeks old. a public reply also tells the next reader that the product is maintained.

then the report lists what's still missing and why. if a file is gone and can't be rebuilt, say so. a residual-gap list is not a failure. it's the part of the audit that stops you from finding the same problem again in six months.

## download the skill

i packaged this as a skill. give it your product list, your review export and where your files live. it classifies the reviews and maps each complaint to a deliverable. it finds the canonical file, checks each fix logged out, and drafts the replies. it won't call a link fixed without opening it, and it won't inflate the counts. download it below and run it in claude code or any agent that reads skills.
