# Chapter 4 Speaker Notes — Putting Numbers on the Picture

**Commander's Intent:** A picture from Chapter 2 plus a lookup table on every arrow is a Bayesian network — and natural frequencies (counts out of 100) are how you make the numbers human-readable.

**Plot:** Creativity — turning words into testable counts.

**Protagonist:** Joyce, 41, midwife in Mwanza Region, Tanzania. Composite from the Tanzania Service Provision Assessment 2014/15.

**Estimated runtime:** 22–25 minutes.

---

## Overview (before slide 1)

Welcome back. *(pause)*

Three chapters in and you can now do something most people in global health cannot. You can draw a picture of how a programme works. You learned the grammar in Chapter 2. You learned the interview method in Chapter 3.

But there is still something missing. Pictures alone cannot answer the question *"how much?"*. A picture says *"anaemia raises the risk of bleeding"*. It does not say *"by how much"*. *(pause)*

This chapter is where we put numbers on the arrows. And we are going to do it in a way that does not make you reach for a textbook. We are going to do it with **counts out of 100**. Because that is how human brains were built to think about chance. *(pause)*

Today we go to Tanzania. To meet a midwife named Joyce.

---

## Slide: Meet Joyce

Joyce is forty-one years old. She works at a rural facility in Mwanza Region, on the southern shore of Lake Victoria, in Tanzania. *(pause)*

Same disclosure. Joyce is a composite drawn from the Tanzania Service Provision Assessment for 2014 and 2015 — that is publicly available — and the details are real, the name is not. *(pause)*

Joyce has delivered hundreds of babies in her career. She knows the work the way you know the route home from work — without thinking. *(pause)*

Last week she did something almost no clinician does. She opened her stockroom logbook and *counted*. Out of the hundred women she has delivered in the last twelve months — about a hundred is the typical caseload for a small rural facility — fifty-five came in with at least one major risk factor. Bleeding history. Anaemia. Prior caesarean. Eclampsia signs. *(pause)*

Out of those fifty-five, six ended badly. Either the mother or the baby did not come home. *(pause)*

Now look at the box on the screen. **A new mother walks in tomorrow with anaemia. What is the chance she has a bad outcome — and how do we get an answer that is actually useful to Joyce, in plain numbers, not in formulas?** *(pause)*

That is the question of this chapter.

---

## Slide: And here is the puzzle

Here is the trap.

Tanzania's national surveys give us numbers like *"the maternal mortality ratio is five hundred and twenty-four per one hundred thousand live births"*. WHO 2017. Big number. Famous number. Cited everywhere. *(pause)*

But Joyce does not deliver one hundred thousand births. She delivers about a hundred a year. *(pause)*

A number that is *right at the country level* can be *useless at the bedside*. The country number is averaging across two thousand facilities. Joyce works in one of them. The country number cannot tell her what is going to happen tomorrow. *(pause)*

Look at the orange box. **What we need is a way to take the picture from Chapters 2 and 3 and turn each arrow into a number Joyce can actually use.** *(pause)*

The trick to doing this is older than statistics. It is so simple it is almost embarrassing. Let me show you.

---

## Slide: Counts before formulas (section divider)

*(pause for transition)*

---

## Slide: Forget probability for a minute

People say *"the probability is zero point zero six"* and most of the room glazes over. *(pause)*

People say *"six out of a hundred"* and everybody gets it. *(pause)*

That is not because some people are smart and others are not. It is because human brains were built to count people, not to do decimal arithmetic. The technical term for this is **natural frequencies**, and there is a whole literature showing that when you teach probability this way, doctors get the right answer ten times more often. Gerd Gigerenzer wrote a whole book about it. We will use natural frequencies for the entire chapter. *(pause)*

If you ever get lost in this chapter — at any point — translate everything back into "X out of 100". Promise me. *(pause)* OK. Let me show you Joyce's last hundred mothers.

---

## Slide: Joyce's last 100 mothers

This is the table I want you to learn to read.

*Look at the table.* Across the top: anaemia, no anaemia. Down the side: bad outcome, good outcome. Four cells in the middle. Plus the totals. *(pause)*

Out of Joyce's hundred mothers, forty had anaemia and sixty did not. That is the bottom row. *(pause)*

Of the forty with anaemia, five had bad outcomes and thirty-five had good outcomes. Of the sixty without anaemia, one had a bad outcome and fifty-nine had good outcomes. *(pause)*

Look at the grey box. **That is the whole picture in one table. Every row, every column, every cell — people, not probabilities.** *(pause)*

If the table feels obvious to you, good. That is the point. Tables of counts are obvious. Tables of probabilities are not. We are going to do everything from now on with tables of counts, and translate to probabilities only at the end if anyone asks.

---

## Slide: Reading the table

Now let's read the table for what it tells us.

*Bullet by bullet.* Out of every hundred mothers Joyce sees, forty have anaemia. *(pause)* Of those forty with anaemia, five have a bad outcome — that is five out of forty, or about one in every eight. *(pause)* Of the sixty without anaemia, only one has a bad outcome — that is one in sixty. *(pause)*

So a mother with anaemia is roughly *eight times more likely* to end badly than a mother without. One-in-eight versus one-in-sixty is roughly an eight-fold difference. *(pause)*

Look at the green box. **Notice what we just did.** We answered Joyce's question — *a new mother walks in with anaemia, what is the chance?* — without using a formula. We just counted. *(pause)*

That is the whole magic of natural frequencies. The brain that wakes you up to your child crying in the night is also the brain that handles five-out-of-forty effortlessly. The brain that does decimal arithmetic is a much later, much weaker brain. We use the older one whenever we can.

---

## Slide: Putting counts on the picture (section divider)

*(pause for transition)*

OK. Now here is the move that puts this chapter together with Chapters 2 and 3.

---

## Slide: From a chain to a lookup table

Remember Faith's bleeding chain from Chapter 3? Bleeding starts → family decides → permission → motorbike → arrives → survives. Six boxes. Five arrows. *(pause)*

Now imagine that *each arrow* on that chain carries a small table. Not a big table. A small one. Just three numbers maybe: out of every hundred women who reach this point, *X* go this way and *Y* go that way. *(pause)*

That is a **lookup table**. One per arrow. And a picture with a lookup table on every arrow has a name. We call it a **Bayesian network**. *(pause)*

Look at the green box. *Don't be intimidated by the name.* "Bayesian network" sounds like something a computer science PhD would invent. It is actually just a picture from Chapter 2 with counts attached. The name comes from a man named Thomas Bayes who lived in the eighteenth century, and we will explain what he actually did in Chapter 5. For now, the name is just a label for *picture-plus-numbers*. *(pause)*

Let me show you the smallest possible Bayesian network — just two arrows from Joyce's facility.

---

## Slide: Joyce's two-arrow picture

Two boxes. One arrow. One lookup table.

*Look at the diagram.* On the left: anaemia (a factor — Joyce cannot choose it). In the middle: bleeding at delivery. On the right: bad outcome. *(pause)*

And below the picture, a small table. *Look at the table.* Out of every forty anaemia mothers, twenty-four had bleeding at delivery and sixteen did not. Out of every sixty non-anaemia mothers, only twelve had bleeding and forty-eight did not. *(pause)*

Look at the box. *That table says "out of every forty anaemia mothers, twenty-four had bleeding at delivery; out of every sixty non-anaemia mothers, only twelve did."* *(pause)*

That is one arrow with one lookup table. If we had a third box — say, *bad outcome* — we would have a second lookup table for the second arrow. That is what a Bayesian network is. Pictures plus tables.

---

## Slide: Why this is a big deal

Now here is why this is the big chapter of Part 2 of the course.

Once each arrow has a table, you can ask the picture *brand-new questions* — questions you could not answer with the picture alone, and could not answer with the table alone. *(pause)*

*Bullet by bullet.* A mother walks in with anaemia. What is the chance of bleeding? Twenty-four out of forty — sixty out of every hundred anaemia mothers. *(pause)*

But now flip it. A mother bled at delivery. What is the chance she had anaemia? Twenty-four divided by thirty-six — because twenty-four anaemia mothers bled and twelve non-anaemia mothers also bled, so thirty-six bled in total — and twenty-four of them had anaemia. So two out of every three women who bleed had anaemia. *(pause)*

That is a *different question*. That is asking the arrow to run *backwards*. The picture-plus-table lets you do that. *(pause)*

And there is a third trick. A new district reports a lot of bleeding but does not measure anaemia at all. With a Bayesian network you can use the bleeding numbers and the picture to *estimate* the missing anaemia numbers. We will do this for real in Chapter 5. *(pause)*

Look at the green box. **The picture *with* numbers can answer questions the picture *without* numbers cannot.** That is the entire reason we are doing this.

---

## Slide: Where do the numbers come from?

But Joyce did not invent her numbers. She got them from somewhere. So where do *you* get yours? *(pause)*

*Bullet by bullet.* The facility logbook. Joyce literally counted the last hundred mothers. Most clinics keep a logbook. Most logbooks have everything you need. Almost nobody actually counts. Be the person who counts. *(pause)*

The DHIS2 database. Tanzania's national health information system. Free, public, district-level data on bleeding rates, maternal outcomes, drug stockouts. You can download it. The link is in the further-reading section. *(pause)*

The Service Provision Assessment. A facility readiness survey done every few years — anaemia screening rates, drug availability, staffing levels. Also free. *(pause)*

And — this matters — the *interviews from Chapter 3*. Mary, Lokol, and Esther can give you rough fractions even when no database exists. *"About half the women here bleed for more than thirty minutes before the family decides."* That is a number. It is a rough one. It is good enough to start. *(pause)*

Look at the orange box. **You almost never need to estimate a number perfectly. You need to estimate it well enough that the picture starts giving useful answers. Better to be roughly right than precisely wrong.** *(pause)*

That sentence is from Keynes. Tape it next to Chapter 3's three rules.

---

## Slide: Three quiet warnings (section divider)

*(pause for transition)*

OK. Three warnings before you go off and do this on your own.

---

## Slide: Warning 1 — Your numbers will be local

Joyce's hundred mothers are not the same as Mwanza Region's thousand mothers, which are not the same as Tanzania's one-point-eight million births a year. *(pause)*

A lookup table you build from one facility will be true for *that facility*. It may be very wrong for the country. *(pause)*

Look at the orange box. **Use it locally.** When you need national numbers, get national counts. When you need facility numbers, count the facility. Do not extrapolate from a hundred mothers to a country. That is one of the most common analytic mistakes in global health.

---

## Slide: Warning 2 — Small counts lie

Joyce had *six* bad outcomes out of a hundred. That sounds solid. But six is a small number. *(pause)*

If two of those six bad outcomes had happened on different days — if the dice had rolled slightly differently — the picture would have looked very different. With six events, the difference between "rare" and "common" can be a coincidence. *(pause)*

Look at the orange box. **With small counts, your numbers are noisy.** We mark this on the picture by putting a *range* on each cell — not just "five out of forty" but "five out of forty, somewhere between two and ten." *(pause)*

You will learn how to compute that range properly in a stats course one day. For now, the rule of thumb is: if the cell has fewer than ten events in it, do not trust it on its own.

---

## Slide: Warning 3 — Numbers can hide a missing arrow

The third warning is the most important.

You can put a beautiful lookup table on every arrow you drew — and still be wrong. Because there is an arrow you forgot to draw. *(pause)*

Look at the red box. **The picture has to be right first.** A wrong picture with perfect numbers is *worse* than a right picture with rough numbers. *(pause)*

This is why we did Chapters 2 and 3 first. The grammar matters. The interviews matter. Adding numbers comes *last*, because numbers are convincing — and an unconvincing picture is much easier to challenge than a convincing one with numbers. *(pause)*

Always come back to the grammar before you start counting.

---

## Slide: Try It (You are the analyst)

OK. Try it.

In a Tanzanian district, one hundred women were tested for HIV during antenatal care last month. Twenty tested positive. *(pause)* Of those twenty, three had a low-birth-weight baby. Of the eighty who tested negative, six had a low-birth-weight baby. *(pause)*

**Build a tiny lookup table. Then answer: a new HIV-positive mother is how many times more likely to have a low-birth-weight baby than an HIV-negative mother?** *(pause)*

A hint. Count the rates first — three out of twenty versus six out of eighty — then divide them. *(pause)*

If you got "twice as likely", you are right. Three out of twenty is fifteen percent. Six out of eighty is seven and a half percent. The HIV-positive mother is twice as likely. *(pause)* Notice you did not need a single formula. You counted, then divided.

---

## Slide: Looking ahead

So that is Chapter 4.

In Chapter 5, you will take a picture-with-numbers like Joyce's and learn what to do when **new evidence arrives**. A new test result comes back. A new survey lands on your desk. A new patient walks in. *(pause)*

You do not throw out your picture. You *update* it. That is what the word "Bayesian" actually means. Not the algebra — the act of updating. We will do it in counts, the same way we did everything else.

---

## Slide: The one thing to remember

If you remember nothing else from this chapter, remember this. *(pause)*

**A picture from Chapter 2 plus a lookup table on every arrow is a Bayesian network.** *(pause)*

The picture tells you the structure. The counts tell you the strengths. Together, they answer questions neither could answer alone. *(pause)*

And the counts are always counts of *people*. Out of a hundred. Never percentages, never decimals, until the very end. *(pause)*

See you in Chapter 5.

---

## Slide: Closing (white)

*(pause; no narration)*
