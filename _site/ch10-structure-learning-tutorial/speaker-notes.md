# Chapter 10 Speaker Notes — Can the Computer Just Tell Us?

**Commander's Intent:** Data alone cannot tell you the direction of a causal arrow. Data plus a few expert assumptions can — and that is what structure learning really is.

**Plot:** Creativity — a clever way to use a database, plus the lesson that the cleverness has limits.

**Protagonist:** Esther, 36, data scientist at the Tanzania Ministry of Health. Composite from publicly available DHIS2 case studies.

**Estimated runtime:** 24–28 minutes. This is the closing lecture; do not rush. Leave time for the wrap-up.

---

## Overview (before slide 1)

Welcome to the last chapter. *(pause)*

Ten chapters ago, we met Almaz in Tigray. A young mother, a baby, a Health Extension Worker, a new road, a longer school year. We asked one question: *which of those things saved her baby?* And we admitted that we did not yet know how to answer it. *(pause)*

Today, we are going to ask a question that sounds like it should be the *easiest* question of all: **can a computer just tell us?** *(pause)*

Sixty thousand rows of data. Forty columns. A modern algorithm. Can the algorithm just look at all of it and discover which arrows point which way? *(pause)*

The answer is going to be subtle. **Partly yes, mostly no, and the no is more important than the yes.** We are going to spend this whole chapter on exactly *what* a machine can do, *what* it cannot, and how to combine the two — and that will turn out to be the most useful skill you will ever learn for a data-rich workplace. *(pause)*

We go to Tanzania one last time. To meet a data scientist named Esther.

---

## Slide: Meet Esther

Esther is thirty-six years old. She is a data scientist at the Ministry of Health in Tanzania. *(pause)*

Same disclosure. Esther is a composite drawn from publicly available DHIS2 case studies — the role and the tools are real, the name is not. *(pause)*

Esther sits in front of ten years of monthly data from every health facility in Tanzania. The data lives in **DHIS2** — the District Health Information System version 2. It is an open-source national health information system, originally developed at the University of Oslo, now used by more than seventy countries. Tanzania has been on it since the early 2010s. The data is real, deep, and detailed. *(pause)*

Sixty thousand rows. Forty columns. Every district, every month, every indicator from antenatal coverage to drug stockouts to staff attendance to delivery outcomes. *(pause)*

This is the kind of dataset that ten years ago would have required a research team and a year. Esther has it on her laptop. *(pause)*

Her director walks in one Monday morning. *"Just run an algorithm on this and tell us what's causing what."* *(pause)*

Now look at the box on the screen. **Can a computer actually discover causal arrows from data alone? Or is there a hidden limit nobody warned her about?** *(pause)*

That is the question of this final chapter. And the answer is going to bring us back to almost everything we learned in Chapters 1 through 9.

---

## Slide: And here is the puzzle

Modern algorithms can do remarkable things with this kind of data. *(pause)*

*Bullet by bullet.* They can find correlations between any two columns. Trivially. Compute every pairwise correlation, sort them by strength, look at the top ten. That is a one-line script. *(pause)*

They can find conditional independences — that is, they can ask whether two columns become independent once you hold a third constant. This is the test from Chapter 5, rule three, and a computer can do millions of them in seconds. *(pause)*

They can find clusters of districts that behave similarly. Regions that all have rising stockouts at the same time, regions that share staffing patterns, regions that move together. *(pause)*

And they can predict next month's value for any indicator — using machine learning models that we will not go into here, because they are not the point. *(pause)*

Look at the orange box. **But there is one thing they fundamentally cannot do, and it is the thing Esther was hired to figure out.** The next eight slides explain what — and why. *(pause)*

The "what they cannot do" is the most important thing in this chapter. So I am going to walk us up to it slowly. First, what they *can* do.

---

## Slide: What machines can do (section divider)

*(pause for transition)*

---

## Slide: Conditional independence — the algorithm's superpower

Remember the three shapes from Chapter 2? Chain, fork, collider. *(pause)*

Each of those three shapes leaves a *specific fingerprint* in the data. Let me walk through them.

*Bullet by bullet.* **Chain.** A causes B causes C. A and C are correlated — because B is passing the influence along. But — and this is the magic — *if you hold B constant*, A and C become *independent*. The chain breaks at the middle box. We saw this in Chapter 2 with Beatrice's danger-signs example. *(pause)*

**Fork.** A and C share a parent B. A and C look correlated — because they have the same cause. But if you hold the parent B constant, A and C become independent. The fork closes when you observe the parent. *(pause)*

**Collider.** A and B both cause C. A and B are *not* correlated — they are independent — *until* you condition on the collider C. Then they suddenly look correlated. The strange one. *(pause)*

Three shapes. Three different fingerprints in the data. *(pause)*

Look at the green box. **The algorithm can detect every one of these fingerprints automatically.** *This is the part where machines really shine.* It runs through every triple of variables, checks for the chain, the fork, and the collider, and builds up a network from the fingerprints it finds. *(pause)*

This is genuinely powerful. It is the kind of work that once required a careful epidemiologist and a stack of cross-tabs. Now it is a one-line function call.

---

## Slide: Esther runs the algorithm

So Esther does it. She hands the DHIS2 data to a structure-learning algorithm — there are several — *bnlearn* in R, *pgmpy* in Python. The most famous underlying method is called the **PC algorithm**, named for Peter Spirtes and Clark Glymour, who invented it at Carnegie Mellon in the early nineties. The original paper is open-access online. *(pause)*

She runs it. And it returns a picture. *(pause)*

Look at the box. **An automatically discovered network** of nodes and edges, based purely on the conditional independences it found in the data. No interviews. No expert input. Just the data. *(pause)*

This is genuinely impressive. Twenty years ago, doing this for sixty thousand rows of data would have taken a research team months. Now Esther does it in an afternoon. *(pause)*

And for a moment, she thinks her director was right. *Maybe the algorithm really can just tell us.* *(pause)*

Then she looks more carefully at what came back. And she runs into the wall.

---

## Slide: What machines cannot do (section divider)

*(pause for transition)*

---

## Slide: The wall

The algorithm gave Esther a network with about fifteen edges. Reasonable number. About what she expected. *(pause)*

But then she looked at the edges. *(pause)*

Every single one of them is *undirected*. A *line*, not an arrow. *(pause)*

The algorithm could tell her that "stockouts" and "maternal deaths" are *related*. It could not tell her *which way the arrow points*. *(pause)*

Look at the red box. **Why?** *(pause)*

Because three different pictures — A points to B, B points to A, and A and B sharing a hidden parent C — produce the *same* conditional-independence fingerprint. **The data alone cannot tell them apart.** *(pause)*

I want you to read that twice. *(pause)*

Three different causal stories. The same statistical fingerprint. The data — *no matter how much of it you have* — cannot distinguish them. *(pause)*

Look at the definition box. **This is not a flaw in the algorithm. It is a fundamental mathematical limit of what data can do without help.** *(pause)*

This sentence is the most important sentence in the chapter. Because it explains a thing that most people in the AI age refuse to believe. *They believe that with enough data, the algorithm will figure it out.* It will not. The limit is not about *quantity* of data. It is about the *structure of inference*. Some questions cannot be answered by data alone, even in principle. They can only be answered by data plus assumptions.

---

## Slide: A picture of the limit

Let me show you the wall.

*Look at the diagram.* Two boxes. Stockouts on the left, maternal deaths on the right. A line between them — undirected. *(pause)*

The algorithm tells Esther those two are *related*. It cannot tell her *which one of these three stories* the data is telling. *(pause)*

*Bullet by bullet.* Story one: stockouts cause deaths. Missing drugs lead to maternal deaths. The arrow points right. *(pause)*

Story two: deaths cause stockouts. A wave of maternal deaths triggers emergency restocking, which uses up next month's normal supply, which creates the *next* month's shortage. The arrow points left. *(pause)*

Story three: both share a hidden parent. A budget cut at the regional level reduces drug supply *and* overburdens staff *and* causes deaths and stockouts together. There is no arrow between stockouts and deaths at all — they just share an upstream cause that is not in the dataset. *(pause)*

Look at the orange box. **All three explanations are mathematically equivalent for the algorithm.** *(pause)*

The arrow direction has to come from outside. From a clinician who can tell you *"in our facility, the stockout is what hits us first, and then the bad outcomes follow"*. From a budget officer who can tell you *"the regional cut last quarter is what set this off"*. From a piece of expert knowledge that the algorithm does not have. *(pause)*

That is the wall. And the way through the wall is the rest of the chapter.

---

## Slide: The expert + algorithm loop (section divider)

*(pause for transition)*

---

## Slide: A better recipe

Esther's first instinct was *"let the algorithm do it all"*. Her second, after the wall, is much more powerful. *(pause)*

*Bullet by bullet.* **Step one.** Draw a partial picture from interviews. Use the method from Chapter 3. Talk to clinicians, supply chain officers, district medical officers. Build a sketch of what the experts think the arrows are. It will be incomplete, of course. *(pause)*

**Step two.** Run the algorithm on the data to find the conditional independence fingerprints. The algorithm will surface relationships you missed. *(pause)*

**Step three.** Compare. Where the algorithm and the picture *agree*, you have found something solid. Where they *disagree*, you have found a question worth investigating — either the experts are wrong about a particular arrow, or the algorithm is hallucinating because of a hidden variable. Either way, the disagreement is the gold. *(pause)*

**Step four.** Use experiments — or, when experiments are impossible, careful domain knowledge — to *orient* the undirected edges the algorithm leaves behind. The experts are the only thing that can break the wall. *(pause)*

**Step five.** Iterate. Updated picture, re-run algorithm, repeat. *(pause)*

Look at the green box. **This is the loop that actually works.** Pure algorithm misses too much. Pure interviews miss too much. The two together find what neither could alone. *(pause)*

That sentence is the practical takeaway from the chapter. Tape it to your monitor next to the rules from Chapter 3 and the redistribution rule from Chapter 5.

---

## Slide: What Esther actually delivers

So Esther goes back to her director the next week. And she delivers *two pictures*, not one. *(pause)*

*Bullet by bullet.* Picture A is the algorithm-only network. The beautiful, mostly undirected web of fifteen edges. The thing the algorithm produced on its own. *(pause)*

Picture B is the same network, *with directions added* by interviewing four district medical officers and one supply-chain manager. Some directions are confident. Some are tentative. Some are explicitly marked as guesses with dotted lines, exactly as we did in Chapter 3. *(pause)*

Look at the box. *Picture B is not "more accurate" in some abstract sense. It is **decision-useful** in a way Picture A is not.* *(pause)*

Picture A is a wall ornament. The director cannot act on it. He cannot use it to plan an intervention, because every edge could go either way. *(pause)*

Picture B is a working tool. The director can pick an edge and ask *"if I cut this — if I fix this stockout problem — does the maternal death rate go down or not?"*. The picture tells him whether the question is even askable. *(pause)*

This is the difference. And it is exactly the difference we have been building toward for ten chapters.

---

## Slide: Three quiet warnings (section divider)

*(pause for transition)*

---

## Slide: Warning 1 — The algorithm is loud about uncertainty in the wrong way

Warning one. **The algorithm is loud about uncertainty in the wrong way.** *(pause)*

A structure-learning algorithm will happily report a network even when the data is far too thin to support it. It does not say *"I am not sure about this edge"*. It just draws the edge. *(pause)*

Look at the orange box. **It will give you an answer with confidence even when the answer is wrong.** *(pause)*

Always check sample sizes per node. If a particular variable only has fifty observations behind it, the algorithm's claims about that variable are not trustworthy — but it will not flag them. You have to check yourself. *(pause)*

The rule of thumb: cells with fewer than fifty observations are not reliable. Treat them as suggestions, not findings.

---

## Slide: Warning 2 — Hidden variables break everything

Warning two. **Hidden variables.** *(pause)*

If two of your "discovered" variables are both caused by something you did *not* measure, the algorithm will draw an edge between them. A *spurious* edge. An edge that does not represent a real causal connection — it represents a missing variable. *(pause)*

Look at the orange box. **The algorithm assumes you measured everything that matters.** You did not. *Nobody ever does.* *(pause)*

The fix is to check the picture against domain knowledge, looking for *"edges that should not be there"*. When you find one, your first hypothesis should be *"what variable did we forget to measure that would explain this edge?"*. The forgotten variable is almost always the answer. *(pause)*

In the DHIS2 case, the most common forgotten variables are things like the regional budget cycle, election years, weather, and roads — none of which are columns in the database, all of which drive multiple things in the database simultaneously.

---

## Slide: Warning 3 — Even with directions, "correlation in observational data" ≠ "intervention will work"

Warning three is the deepest, and it brings us all the way back to Chapter 7. *(pause)*

Even when Esther's final picture has all the right arrows — even when the experts have done their work and the directions are all confidently set — the picture is built from *observational* data. It describes Tanzania's existing patterns. It does not, by itself, predict what an intervention will *do*. *(pause)*

Look at the red box. **The intervention vs observation distinction from Chapter 7 still applies.** *(pause)*

A picture built from data can describe the world. To predict what an intervention will *do*, you still need the graph-surgery move from Chapter 7 — cut the incoming arrows of the box you are intervening on, then propagate. *(pause)*

The algorithm cannot do graph surgery for you. The graph surgery comes from your *intent to act*. It is your job, not the machine's. *(pause)*

This is why structure learning, by itself, is not enough. It gives you a *picture*. To turn the picture into a *decision*, you need everything we built in Chapters 7, 8, and 9 — the decision maps, the expected values, the risk shapes, the game theory. The algorithm is one input. The decision is yours.

---

## Slide: Try It (You are the analyst)

OK. Try it. One last time.

You run a structure-learning algorithm on a Kenyan county dataset. It finds a strong undirected edge between *facility births* and *newborn deaths*. *(pause)*

**What are at least three different stories the data could be telling?** *(pause)*

Hint: review chains, forks, colliders, and hidden variables. And do not forget that the most dangerous explanation is *"the algorithm picked up a reporting artefact, not a real causal link"*. *(pause)*

Story one: more facility births means more deaths *recorded*, because deaths at home are not in the dataset. Reporting artefact. *(pause)*

Story two: facilities are where the high-risk pregnancies end up — selection. The facility birth is downstream of the high-risk status, the death is downstream of the high-risk status. A fork with a hidden parent. *(pause)*

Story three: facilities truly are *causing* deaths through some mechanism — a real but uncomfortable possibility, perhaps in facilities with poor staffing or hygiene problems. *(pause)*

All three are *consistent with the same edge* the algorithm produced. The way to tell them apart is not more data. The way to tell them apart is *interviews*, *audits*, and *triangulation* with separate datasets. The same Chapter 3 tools.

---

## Slide: Looking ahead — and looking back

This is the last lecture of the course. *(pause)*

So I want to step back for a moment. *(pause)*

You started with Almaz in Tigray, ten chapters ago, and a question. *Did the Health Extension Worker save her baby — or would the baby have been fine anyway?* *(pause)*

We did not answer that question on day one. We could not. *(pause)*

But you now have an answer. Not "yes" or "no". A *toolkit*. *(pause)*

You can draw the picture. *(Chapters 2 and 3.)* You can put numbers on it. *(Chapter 4.)* You can update those numbers when new evidence arrives. *(Chapter 5.)* You know when to disaggregate and when not to. *(Chapter 6.)* You can convert the picture into a decision with expected value. *(Chapter 7.)* You can spread your decisions across many places and see the shape of the risk. *(Chapter 8.)* You can account for the way other people will respond to what you do. *(Chapter 9.)* And you know exactly what a machine can and cannot tell you about all of it. *(Chapter 10.)* *(pause)*

That is the toolkit. And it is the toolkit Almaz's question deserves. *(pause)*

Look at the green box. **That toolkit is what the next thirty years of your career will run on. Use it well.** *(pause)*

I am going to tell you the same thing I tell every cohort. Pick one programme you actually work on. Just one. Sit down with a pen. And draw the picture. Go interview three people. Put rough numbers on the arrows. See what the picture tells you that you did not already know. *(pause)*

That single exercise will change how you think about your work. Not in five years. *Tomorrow.* *(pause)*

That is the entire point of this course.

---

## Slide: The one thing to remember

If you remember nothing else from this chapter — or from this course — remember this. *(pause)*

**Data alone cannot tell you the direction of a causal arrow. Data plus a few expert assumptions can — and that is what structure learning really is.** *(pause)*

Esther's algorithm was powerful. The expert was indispensable. The two together did what neither could do alone. *(pause)*

The same is true of you. The data is not enough. The intuition is not enough. *Together, they are enough.* *(pause)*

Thank you for taking this course. Go and draw the picture.

---

## Slide: Closing (white)

*(pause; let the closing slide breathe; no narration)*
