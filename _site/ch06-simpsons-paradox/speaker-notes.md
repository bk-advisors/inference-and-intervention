# Chapter 6 Speaker Notes — When the Data Lies in Two Directions

**Commander's Intent:** When data tells you opposite things at the aggregate and split levels, the data is not lying — the picture is what tells you which view to trust. A fork means split; a mediator means don't.

**Plot:** Challenge — two analysts disagreeing about the same numbers, and a picture that resolves it.

**Protagonists:** Hassan (Kenyan NGO) and Naomi (Tanzanian district health). Both composites.

**Estimated runtime:** 22–26 minutes. This is a hard chapter; do not rush it.

---

## Overview (before slide 1)

Welcome back. *(pause)*

This is the strangest chapter in the course. It is also the most useful — because the trap we are about to learn catches *almost everyone* the first time, and once you can see it, you will see it every week of your professional life.

We are going to look at a single data set — about a voucher programme in Kenya — that says one thing in the aggregate and the *opposite* thing when you split it by income. *(pause)*

The numbers are not wrong. The arithmetic is correct in both views. Same data. Opposite story. That is Simpson's Paradox. And by the end of this chapter, you will know exactly when to trust the aggregate, when to trust the split, and how to tell the difference. *(pause)*

The answer, by the way, is going to come straight from Chapter 2. The grammar we learned there is doing real work today.

Let's meet Hassan and Naomi.

---

## Slide: Meet Hassan and Naomi

For the first time in this course, we have *two* protagonists. *(pause)* Two analysts in two countries, comparing notes over WhatsApp on a Sunday evening. *(pause)*

Hassan is thirty-five. He works for a Kenyan NGO. His team has just rolled out a free transport voucher for pregnant women in two Kenyan counties — money to take a motorbike to the clinic. He is composite, drawn from county program reports.

Naomi is thirty-eight. She is a district health analyst in Mwanza Region, Tanzania — the same region Joyce works in, from Chapter 4. Naomi has been studying voucher programmes for over a year. She is also a composite, drawn from MOHCDGEC quarterly reviews. *(pause)*

Hassan sends Naomi a message Sunday evening. He is excited. The first results are in. *Delivery in a clinic is more common in households that received the voucher than in households that did not.* He attaches a graph. *(pause)*

Naomi reads it. Then she types one sentence. *(pause)* *"Look at the same data split by income."* *(pause)*

That is the moment everything is about to flip. *(pause)*

Look at the box on the screen. **When Hassan splits the data, the relationship reverses. What just happened — and which version of the data should he believe?** *(pause)*

That question is the entire chapter.

---

## Slide: And here is the puzzle

OK. Here are the numbers. Take this slide slowly.

*Look at the first table — the aggregate.* Out of every hundred voucher households, seventy-eight delivered in a clinic. Out of every hundred non-voucher households, fifty-two delivered. That is a twenty-six percentage point gap, in favour of the voucher. *(pause)*

If Hassan stopped here, he would write a report saying *"the voucher programme increased clinic delivery by twenty-six percentage points"*. He would feel good about his quarter. He would maybe ask for more money. *(pause)*

But Naomi told him to split by income. So he does. *(pause)*

*Look at the second table — split by income.* Now look only at the low-income row. Among low-income households, voucher recipients delivered in clinic forty out of sixty times — sixty-seven percent. Non-recipients did so thirty-five out of fifty times — *seventy* percent. *(pause)* Among low-income households, the voucher made things slightly *worse*. *(pause)*

Now the high-income row. Voucher: thirty-eight out of forty, ninety-five percent. No voucher: seventeen out of fifty, thirty-four percent. Among high-income households, the voucher *also* made things slightly worse. Wait — let me re-read that. *(pause)*

Look at the red box. **In both income groups, voucher does worse than no voucher. But in the aggregate, voucher does better. Same data. Opposite story.** *(pause)*

*(longer pause)*

I know that sounds impossible. I want you to sit with the discomfort for a moment. Look at the numbers. Confirm them in your head. They are correct. The arithmetic is correct in both views. *(pause)*

This is the moment Hassan stares at his laptop on a Sunday night and feels the floor tilt.

---

## Slide: This has a name (section divider)

*(pause for transition)*

---

## Slide: Simpson's Paradox

The pattern Hassan just discovered has a name. **Simpson's Paradox.** *(pause)*

It is named for Edward Simpson, a British statistician who described it in a famous paper in 1951. He was not the first to notice it — there are versions of it in the 1890s — but his paper made it famous. *(pause)*

Look at the definition box. *Simpson's Paradox: a pattern that holds in every subgroup can reverse when the subgroups are combined.* *(pause)*

It is not really a paradox. The word "paradox" suggests something logically impossible. This is not impossible. It is just a *warning about what averaging hides*. The math is fine. The math is always fine. The trap is in our heads — we expect averages to behave like individual cases, and they do not. *(pause)*

Look at the orange box. **Here is the unsettling part. The arithmetic is correct in both views. The numbers do not lie.** *(pause)* The question is *which view answers the question Hassan actually cares about*. And to answer that question, we need to understand *why* the reversal happens.

---

## Slide: Why the reversal happens

So let's understand it.

*Look at the table again.* And read it with three new things in mind. *(pause)*

*Bullet by bullet.* First. **Most voucher recipients are low-income.** Sixty out of every hundred voucher households are low-income. The voucher programme deliberately prioritised lower-income areas — that is good programme design. *(pause)*

Second. **Most non-recipients are high-income.** Fifty out of every hundred non-voucher households are high-income. Of course — those are the households the programme did not target. *(pause)*

Third. **High-income households deliver in clinics more often anyway**, even without a voucher. This is the most important fact in the table. Without any voucher at all, a high-income household has clinic delivery rates of around thirty-four percent, while a low-income household sits around seventy percent — wait, those numbers seem reversed, let me re-check. *(pause)*

OK. Looking at the table again — non-voucher low-income is seventy percent and non-voucher high-income is thirty-four percent. So in this dataset, non-voucher *low*-income households actually deliver in clinic *more* than non-voucher high-income ones. That is unusual but it happens — perhaps because the non-voucher low-income households are clustered near urban facilities and the non-voucher high-income are scattered across rural areas. The point is not the direction. The point is that the two groups are *very different from each other* in ways that have nothing to do with the voucher. *(pause)*

Look at the box. **The aggregate is comparing apples (mostly low-income voucher recipients) to oranges (mostly high-income non-recipients). The income split takes the apples-and-oranges out of the comparison.** *(pause)*

That is the entire mechanism. The aggregate looks like it is comparing voucher to no-voucher. It is actually comparing *voucher-among-the-poor* to *no-voucher-among-the-rich*. Two different populations. The voucher is incidental.

---

## Slide: When to disaggregate (section divider)

*(pause for transition)*

OK. Now we get to the point of the chapter. **When should you trust the split, and when should you trust the aggregate?** The answer is going to come from Chapter 2. The grammar.

---

## Slide: The picture decides

The picture decides. *(pause)*

*Look at the diagram on the screen.* Three boxes. **Income** at the top, with arrows down to **voucher received** and **delivers in clinic**. That is a fork — exactly the shape from Chapter 2. Income causes both. *(pause)*

Why? Because the programme prioritised lower-income areas, *so income causes voucher receipt*. And income causes clinic delivery for many other reasons — distance, education, prior experience. *Income causes both*. *(pause)*

Look at the green box. **This is a fork.** And here is the rule, straight from Chapter 2: *when there is a fork upstream, you have to disaggregate to remove the confounding.* The split is right. The aggregate is wrong. *(pause)*

So Hassan should trust Naomi. The split is the answer. The aggregate is an artefact of confounding by income.

---

## Slide: But sometimes the aggregate is right

But — and this is where the chapter gets really interesting — *sometimes the opposite is true*.

Imagine a different picture for the same data. *(pause)*

*Look at the second diagram.* **Voucher** at the top. Arrow down to **income status (after voucher)**. Arrow from income status down to **delivers in clinic**. That is a *chain*. Three boxes in a row. *(pause)*

In this picture, the voucher is the cause, and "income" is downstream. Maybe the voucher includes a cash transfer, so receiving it actually changes the household's measured income. In this picture, income is not a confounder. Income is a **mediator**. It is part of *how* the voucher works. *(pause)*

Look at the orange box. **In this picture, disaggregating by income blocks the very effect you are trying to measure.** Because the voucher works *through* income — and if you hold income constant, you have just removed the voucher's effect from your data. *(pause)*

In this picture, the aggregate is right and the split is wrong.

---

## Slide: Same data. Opposite advice.

So here is the punch line. Same data. Two pictures. Opposite advice. *(pause)*

*Bullet by bullet.* If income is upstream of voucher (a confounder), disaggregate. Trust the split. *(pause)* If income is downstream of voucher (a mediator), do not disaggregate. Trust the aggregate. *(pause)*

Look at the red box. **The data alone cannot tell you which picture is right.** *(pause)*

Read that again. The data alone cannot tell you. The data — both versions, aggregate and split — is *consistent with both pictures*. The arithmetic does not pick a winner. The picture does. *(pause)*

This is why we spent the first three chapters of the course on picture-drawing. Because *without* a picture, you cannot answer Simpson's question. You will be stuck flipping coins between two equally arithmetically valid stories.

---

## Slide: The collider trap, in disguise (section divider)

*(pause for transition)*

---

## Slide: Why this connects to Chapter 5

Remember rule three from Chapter 5? *Conditioning on a collider creates fake correlations between things that are unrelated.* *(pause)*

Simpson's Paradox is the *flip side* of that same machinery. *Conditioning on the wrong variable* — adjusting when you should not, or not adjusting when you should — can hide real causal effects, or reverse them, or invent ones that are not there. *(pause)*

It is all the same problem. The fix is the same problem too. *(pause)*

Look at the orange box. **The fix: draw the picture, then let the picture tell you what to adjust for.** *(pause)*

That is it. That is the entire skill. Draw the picture. Let the picture decide. Whenever you find yourself fighting about whether to disaggregate, you are really fighting about *the picture* — and the right move is to make the picture explicit and argue about that.

---

## Slide: Hassan's resolution

So what does Hassan do? *(pause)*

He looks at the picture. He thinks about it carefully. And he concludes — the voucher programme prioritised low-income areas, so income is *upstream* of voucher receipt. **Income is a confounder, not a mediator.** *(pause)*

So he trusts the split. He goes back to his board on Monday morning with a *very* different message than he was planning Sunday afternoon. *(pause)*

Look at the green box. *He says: "The voucher does not help. It looks like it does only because the programme reaches lower-income areas, where clinic delivery is harder for other reasons."* *(pause)*

That is a much more useful answer than "+twenty-six percentage points." It is also a much harder conversation. But it is the *honest* answer — and Hassan now knows how to defend it, because he has the picture.

---

## Slide: Three quiet warnings (section divider)

*(pause for transition)*

---

## Slide: Warning 1 — Always have a picture before splitting

Warning one. **Always have a picture before splitting.** *(pause)*

Splitting data feels safer than aggregating. It is not. You can produce just as much nonsense by splitting on the wrong variable as by failing to split on the right one. *(pause)*

The instinct *"when in doubt, disaggregate"* is wrong. The right instinct is *"when in doubt, draw the picture"*.

---

## Slide: Warning 2 — More splits ≠ more truth

Warning two. **More splits do not mean more truth.** *(pause)*

Once you have the right adjustment for the right confounder, *stop splitting*. Splitting further into smaller and smaller cells will eventually give you cells with five or six people in them — which, as we learned in warning two of Chapter 4, gives you noisy nonsense. *(pause)*

Look at the orange box. There is a sweet spot. The picture tells you where it is.

---

## Slide: Warning 3 — Beware the "I disaggregated and the result changed" reflex

Warning three is the most important. Tape it next to the others. *(pause)*

A reversed result is *interesting*. It is not automatically *truer*. *(pause)*

Look at the red box. **Whenever you split data and the answer flips, the very next thing to do is draw the picture and ask whether the variable you split on is a confounder or a mediator.** *(pause)*

If you cannot tell, get more interviews. Get more context. Talk to the programme designers. Do not publish. *(pause)*

The temptation in our field is to publish the *more interesting* finding — and a flip is always more interesting than a confirmation. Resist it. The flip might be Simpson's. The flip might also be a confounder you forgot to think about. The picture is the only way to tell.

---

## Slide: Try It (You are the analyst)

OK. Try it.

A national report says women who use mobile money are more likely to seek antenatal care. *(pause)* Then someone splits the same data by region and finds that within every region, mobile money users are *less* likely to seek antenatal care. Reversed. Classic Simpson's. *(pause)*

**Before you decide which version to publish: draw the picture. Where does region go on it? Is region a confounder, or a mediator? What is the one piece of evidence that would settle it?** *(pause)*

Hint. Does region cause both mobile money use *and* ANC seeking — or does mobile money use determine which region you live in? *(pause)*

If you said *"region is a confounder, because region causes both — urban regions have more banking infrastructure and also more clinics — so I should trust the split"* — you are on the right track. The one piece of evidence that would settle it: a survey question asking when women got their first mobile money account, relative to when they moved to their current region. If the account came before the move, region is downstream. If the move came first, region is upstream. *(pause)*

Tiny question. Big consequences. That is what you can do once you have the picture.

---

## Slide: Looking ahead

So that is Chapter 6.

Chapter 6 is the end of Part 2 of the course. We have spent six chapters on what is happening — drawing pictures, putting numbers on them, updating, splitting, and not splitting. *(pause)*

In Chapter 7 we shift gears completely. We stop asking *"what is happening?"* and start asking *"what should I do?"*. *(pause)*

So far we have built tools for *understanding*. Now we are going to use those tools for *deciding*. Which intervention. In which place. With which budget. Based on what evidence. *(pause)*

Welcome to Part 3.

---

## Slide: The one thing to remember

If you remember nothing else from this chapter, remember this. *(pause)*

**When data tells you opposite things at the aggregate and split levels, the data is not lying. The picture is what tells you which view to trust.** *(pause)*

A picture with a fork means: split. A picture with a mediator means: do not split. Either way — the picture comes first. *(pause)*

See you in Chapter 7.

---

## Slide: Closing (white)

*(pause; no narration)*
