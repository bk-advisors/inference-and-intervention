# Chapter 5 Speaker Notes — When New Evidence Arrives

**Commander's Intent:** Bayesian updating is just redistributing your "out of 100" between explanations — keeping the total at 100 — based on which ones the new evidence fits.

**Plot:** Challenge — an analyst updating her beliefs in real time as evidence trickles in over a week.

**Protagonist:** Hiwot, 47, regional health director in Amhara Region, Ethiopia. Composite from FMOH quarterly reports.

**Estimated runtime:** 22–24 minutes.

---

## Overview (before slide 1)

Welcome back. *(pause)*

Last chapter we put numbers on the picture. We learned that a picture from Chapter 2, plus a lookup table on every arrow, equals a Bayesian network. Joyce in Mwanza counted her hundred mothers and turned them into a working tool.

But there is one piece still missing. What do you do when **new evidence arrives**? *(pause)*

Picture-with-numbers is a snapshot. Real life is not a snapshot. Real life is a stream of new information — phone calls, reports, facility visits, surprise findings — and an analyst's job is to update her picture as the stream comes in. *(pause)*

This chapter teaches that updating. It is what people mean when they say *"Bayesian"*. And — I promise you this — there is no formula. There are only counts, and a redistribution rule, and a few warnings. *(pause)*

Today we go back to Ethiopia. To meet a regional health director named Hiwot.

---

## Slide: Meet Hiwot

Hiwot is forty-seven years old. She is the regional health director for Amhara Region in northern Ethiopia. *(pause)*

Same disclosure. Hiwot is a composite drawn from publicly available Federal Ministry of Health quarterly reports. The details are real, the name is not. *(pause)*

It is Monday morning. Hiwot opens her email. *(pause)*

The latest quarterly report from one of her districts — and there are dozens of districts in Amhara — shows maternal deaths jumped from nine last quarter to fourteen this quarter. *(pause)* Fifty-six percent increase. In a single district. In a single quarter. *(pause)*

Her phone is already ringing. *(pause)*

Now look at the box on the screen. **What is the most likely explanation — and how should new evidence arriving over the next two weeks change her answer?** *(pause)*

That question is the heart of this chapter. And the answer is going to teach you almost everything about how to think under uncertainty.

---

## Slide: And here is the puzzle

Within an hour, three explanations are sitting on Hiwot's desk. *(pause)*

*Bullet by bullet.* Explanation one: the new district hospital lost two midwives in the last six weeks. Personnel attrition. *(pause)*

Explanation two: there has been a measles outbreak elsewhere in the region. Maybe it is overwhelming the inpatient ward and pulling resources away from the maternity unit. A surge. *(pause)*

Explanation three: the district just started reporting deaths it had been quietly missing. Reporting improvement. The number went up because the *measurement* got better, not because the underlying reality got worse. *(pause)*

Look at the orange box. **They cannot all be the main story. But Hiwot does not yet know which one is.** *(pause)*

And here is the harder problem. Different evidence will arrive in a different order. A phone call here. An email there. A facility visit on Friday. Her belief has to update *each time*. So the question is not just *"which explanation is right?"*. The question is *"how should she think about this so that each new piece of evidence moves her belief in the right direction?"*. *(pause)*

That question has a clean answer. Let me show you.

---

## Slide: How belief actually works (section divider)

*(pause for transition)*

---

## Slide: Start with what you already believe

Before any new evidence arrives, Hiwot already has an *opinion*. *(pause)*

She has been running this region for years. She knows the district. She knows the staffing situation. She has seen reporting reforms come and go. She is not starting from zero. *(pause)*

So she writes down — even just on a sticky note — what she believes *before* the new evidence arrives. And she thinks all three explanations are roughly equally likely. About thirty-three out of one hundred, for each. *(pause)*

Look at the box. **That is her starting belief.** *(pause)*

This sticky note has a fancy name in statistics. It is called the **prior**. Look at the definition box. *Prior is just a fancy word for "what I believed before the new evidence arrived."* *(pause)*

Some people get scared by the word "Bayesian". It sounds technical. The whole technical part is just this: *write down your prior*. That is the hard discipline. The math after that is just bookkeeping.

---

## Slide: Then evidence arrives

Tuesday morning. The chief of staff at the district hospital calls Hiwot. *(pause)*

Two pieces of information come out in the call. *(pause)* One: the two midwives leaving is real. They did leave. The personnel story has *some* support. *(pause)* Two: the chief of staff also confirms that there has been *no unusual measles activity in the district* this quarter. The measles surge story just lost its support. *(pause)*

Look at the green box. **Two pieces of information at once.** One makes "personnel" more likely. The other makes "measles" less likely. *(pause)*

So Hiwot updates her sticky note. The numbers move.

---

## Slide: Counts, not formulas

Here is how the numbers move.

*Look at the table.* On the left, before Tuesday: thirty-three, thirty-three, thirty-three. Even split. *(pause)* On the right, after Tuesday: personnel jumps to fifty-five, measles drops to eight, reporting nudges up to thirty-seven. *(pause)*

Notice — and this is the only mechanical thing you need to learn in this entire chapter — the totals always still add to one hundred. *(pause)* The total is always one hundred. The numbers shuffle around. But they always add to one hundred. *(pause)*

Look at the box. **The numbers shifted. Nobody changed Hiwot's mind for her. The new facts made some scenarios more plausible and others less plausible, and the totals still add to a hundred.** *(pause)*

That is the entire mechanism. If you can re-distribute one hundred between three buckets while keeping the total at one hundred, you have already understood Bayesian updating.

---

## Slide: What just happened, in one sentence

So let me say it as cleanly as I can. *(pause)*

Look at the definition box. **Bayesian updating is just this: when new evidence arrives, you redistribute your "out of one hundred" between the explanations — keeping the total at one hundred — based on which explanations the evidence fits.** *(pause)*

That is the whole idea. There is no formula you need to memorise. There is no complicated calculation. There is just this redistribution rule, applied carefully. *(pause)*

If anyone tells you Bayesian thinking is complicated, ask them to explain it without using a formula. If they can't, they don't really understand it. The formula is just a way to be precise about the redistribution. The redistribution itself is something a child can do.

---

## Slide: Information flows along the picture (section divider)

*(pause for transition)*

OK. There is one more piece. So far we talked about updating between three *explanations*. But each explanation is really a *picture* — a set of boxes and arrows from Chapters 2 and 3. So when new evidence arrives, the question is: *which boxes does it touch?*

---

## Slide: The picture decides where evidence flows

Hiwot's three explanations live on a picture. Each one has its own boxes — *personnel* has staffing, scheduling, caseload boxes; *measles* has outbreak, inpatient strain, maternity competition boxes; *reporting* has HMIS pipeline, training, software boxes. *(pause)*

When new evidence arrives, it enters the picture at one specific box. And from that box, it spreads outward along the arrows. *(pause)*

Look at the box. **This is why we drew the picture in Chapters 2 and 3. The picture tells you which boxes the new evidence is allowed to update — and which boxes it is not.** *(pause)*

The picture is doing real work here. Without it, you would update everything when any new piece of evidence arrived, and that is exactly the wrong thing to do.

---

## Slide: Three rules for how evidence flows

There are three rules for how evidence flows along the picture. They map exactly onto the three shapes from Chapter 2 — chain, fork, collider. *(pause)*

*Bullet by bullet.* **Rule one. Along a chain, evidence flows freely.** New evidence about a midstream box updates everything upstream and downstream. Bleeding goes up at the facility? That updates your belief about danger-sign recognition (upstream) and about bad outcomes (downstream). The chain is open in both directions. *(pause)*

**Rule two. Across a fork, evidence flows freely until you observe the parent.** Two children of the same parent will look correlated *until* you look at the parent. Once you know the parent's value, the two children become independent again. *(pause)*

**Rule three. Across a collider, evidence does *not* flow — *unless* you observe the collider, in which case it suddenly does.** *(pause)*

I know rule three sounds weird. It is weird. It is the most counterintuitive thing in the entire course. We will see it cause an actual problem in Chapter 6, with Simpson's Paradox. For now, just file it away. *(pause)*

Look at the orange box. **Rule three is the strange one we warned you about in Chapter 2.** It is also the rule that catches almost everyone. Mark it.

---

## Slide: Hiwot's most useful trick — explaining away

Now we are going to see the most useful trick in the whole chapter. It has a name. It is called **explaining away**.

Wednesday. A second piece of evidence arrives. The district HMIS officer — that is the person who runs the district health information system — confirms that the reporting pipeline was indeed cleaned up last quarter. And four of this quarter's fourteen deaths had been previously unrecorded. *(pause)*

So part of the rise — the four extra deaths — was a *measurement* improvement, not a real increase. *(pause)*

Now look at the example block. **The reporting explanation just got more likely.** Of course. *(pause)* **And — this is the strange bit — the personnel explanation got *less* likely**, even though no new evidence about personnel arrived. *(pause)*

Why? Because if reporting is suddenly carrying more of the rise, *less of the rise needs to be carried by anything else*. The total rise is fixed. If the reporting bucket grew, the personnel bucket must have shrunk to compensate. *(pause)*

Look at the green box. **This is called explaining away.** One cause becoming more likely automatically makes its competitors less likely — even without new evidence about them. *(pause)*

This is a real, deep, slightly counterintuitive feature of how belief works. And it falls out naturally from the redistribution rule. The total has to stay at one hundred. So if one bucket grows, others have to shrink. That is all "explaining away" really is.

---

## Slide: The picture after explaining away

Here is the table after Wednesday.

*Look at the table.* Before Wednesday: personnel fifty-five, measles eight, reporting thirty-seven. After Wednesday: personnel thirty-two, measles five, reporting sixty-three. *(pause)*

Look at the personnel row. It dropped from fifty-five to thirty-two. *Twenty-three points*. Nothing new about personnel arrived. The drop was entirely because reporting absorbed more of the rise. *(pause)*

Look at the box. **Personnel dropped — not because anything new about personnel came in, but because reporting absorbed more of the rise.** *(pause)*

That is explaining away. Tape it next to the redistribution rule.

---

## Slide: Three quiet warnings (section divider)

*(pause for transition)*

OK. Three warnings before you go and do this on your own.

---

## Slide: Warning 1 — Your prior matters

Warning one. **Your prior matters.** *(pause)*

If Hiwot had started with *"personnel never matters here"* — say, ten percent for personnel and forty-five each for measles and reporting — the *same Tuesday call* would have moved her to a *different place*. *(pause)*

That is not a flaw. That is honest. Two people with different starting beliefs can see the same evidence and end up with different conclusions. *(pause)*

Look at the orange box. **The fix is to write down your prior so others can challenge it.** *(pause)*

This is the one piece of professional discipline that takes the most practice. Most people do not write down their prior. They just have one in their head, and they pretend the evidence "speaks for itself". The evidence never speaks for itself. The evidence speaks *to* a prior. Make yours visible.

---

## Slide: Warning 2 — Updating is not the same as overreacting

Warning two. **Updating is not the same as overreacting.** *(pause)*

Each new piece of evidence shifts the picture. But evidence has *weight*. Strong evidence should produce a big shift. Weak evidence should produce a small shift. *(pause)*

A single anecdote should not flip your belief from thirty-three-thirty-three-thirty-three all the way to five-five-ninety. If it did, your weights were wrong — you treated weak evidence like strong evidence. *(pause)*

Look at the orange box. **Strong shifts require strong evidence.** *(pause)*

The shorthand version: a single phone call should move you a little. A randomised trial should move you a lot. Five facility visits should move you somewhere in between. Calibrate the shift to the weight of the evidence.

---

## Slide: Warning 3 — Rule 3 (colliders) catches almost everyone

Warning three. **Rule three.** *(pause)*

I keep coming back to it, because it is the rule that breaks the most analyses in the world. *(pause)*

Conditioning on a collider — that is, looking only at cases where two arrows have already collided — creates *fake correlations* between things that are actually unrelated. *(pause)*

Look at the red box. **If you find yourself surprised by a sudden correlation in your data, ask: did I just filter on a downstream collider?** *(pause)*

This error hides inside half the famous "paradoxes" in epidemiology. We are going to see one of them in Chapter 6.

---

## Slide: Try It (You are the analyst)

OK. Try it. *(pause)*

A regional director in Kenya sees that antenatal coverage in one county jumped from sixty-five percent to seventy-eight percent in a single quarter. Three explanations. *(pause)*

One: the new SMS reminder programme is working. Two: a coding change in DHIS2 reclassified some clinic visits. Three: a measles vaccination drive brought more women to clinics, where they were also screened for ANC. *(pause)*

Start with thirty-three-thirty-three-thirty-three. *(pause)* A phone call confirms the DHIS2 coding change is real. **How do your numbers move? What is the *next* piece of evidence you should ask for?** *(pause)*

Hint. Which one of the three explanations does the coding change support — and which does it weaken via *explaining away*? *(pause)*

If you said *"the coding change is now much more likely, and the SMS programme is now less likely because reclassification absorbs some of the apparent rise"* — you have got it. The next piece of evidence I would ask for is the raw clinic visit logs. Do they show more individual women, or just more recorded visits per woman? That single number would resolve the next round of redistribution.

---

## Slide: Looking ahead

So that is Chapter 5.

In Chapter 6 we are going to look at one of the strangest patterns in all of statistics: when the same data tells you opposite things at the country level and at the regional level. *(pause)*

It has a name. **Simpson's Paradox.** And it is closely related to the collider trap from rule three. We will see exactly how. We will see when to disaggregate. And — just as importantly — we will see *when not to*. *(pause)*

It is one of the most useful chapters in the course. See you there.

---

## Slide: The one thing to remember

If you remember nothing else from this chapter, remember this. *(pause)*

**Bayesian updating is just redistributing your "out of one hundred" between explanations — keeping the total at one hundred — based on which ones the new evidence fits.** *(pause)*

Hiwot did not throw out her picture when new evidence arrived. She updated the numbers on it. *(pause)*

That is what an analyst does all day. *(pause)*

See you in Chapter 6.

---

## Slide: Closing (white)

*(pause; no narration)*
