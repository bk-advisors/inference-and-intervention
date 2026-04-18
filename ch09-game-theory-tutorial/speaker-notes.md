# Chapter 9 Speaker Notes — When the Other Side Reacts

**Commander's Intent:** Your decisions change how other people behave — and unless you write that down, your forecast of impact will be wrong.

**Plot:** Challenge — same offer, opposite responses, and the picture that explains why.

**Protagonists:** Wangari (Nakuru, accepts) and Patrick (Kakamega, redirects). Both composites from County Treasury reports.

**Estimated runtime:** 22–25 minutes.

---

## Overview (before slide 1)

Welcome back. *(pause)*

We are in the final stretch of the course. Two chapters left. *(pause)*

In Chapters 7 and 8, we made decisions assuming the world was passive. David picked where to put a midwife. Grace split a budget across countries. Both calculated expected values. Both made defensible choices. *(pause)*

But there was a hidden assumption underneath all of it. **Both of them assumed they were the only one making a decision.** *(pause)*

They were not. *(pause)*

The world is full of *other people* who make decisions in response to what you do. Counties redirect their budgets when donors offer matching grants. Other donors fill or do not fill the gaps you leave. Governments respond to incentives — sometimes the way you wanted, often not. *(pause)*

Today's chapter is about that. The tool is called **game theory**. And it is not as scary as it sounds. It is just decision theory with one new rule: *write down what the other side will do, before you compute your expected value*. *(pause)*

Let's meet two county budget directors who got the same offer and made opposite choices.

---

## Slide: Meet Wangari and Patrick

For only the second time in this course, we have *two* protagonists. *(pause)*

Wangari is forty-four. She is the county budget director for Nakuru County, Kenya. *(pause)*

Patrick is fifty. He is the county budget director for Kakamega County, also in Kenya. *(pause)*

Both are composites drawn from publicly available County Treasury reports. The details are real, the names are not. *(pause)*

Now here is the situation. A donor — let's say a large international development organisation — offers *both counties the same deal*. **A one-to-one matching grant for maternal health.** Every shilling the county puts into its maternal health budget, the donor matches with one of its own. *(pause)*

Same offer. Same paperwork. Same conditions. Same dollar amounts. *(pause)*

*Bullet by bullet.* Wangari accepts enthusiastically. She doubles her existing maternal health line. She unlocks the full match. The total maternal health budget in Nakuru roughly doubles. *(pause)*

Patrick — wait for it — quietly redirects his existing maternal health budget *to road repairs*. He knows the donor will fund maternal health anyway. So he uses the donor money to free up his own money for something else. *(pause)*

Look at the box on the screen. **Same deal. Opposite responses. What predicts who does what — and how should the donor have designed the deal differently?** *(pause)*

That is the question of this chapter. And the answer is going to teach you something important about why a lot of well-designed development programmes do not work the way they were supposed to.

---

## Slide: And here is the puzzle

The donor's expected-value calculation — the kind we did in Chapter 7 — said the matching grant would *double* maternal health spending in both counties. Simple. Clean. Defensible at any board meeting. *(pause)*

In Nakuru, that is exactly what happened. *(pause)*

In Kakamega — *look at the red box* — **it produced almost no new maternal health spending**. The donor's money replaced the county's money, and the county's money went to roads. The total didn't change. The donor was paying for roads, indirectly, while believing it was paying for maternal health. *(pause)*

This phenomenon has a name. *(pause)* In economics it is called **crowding out**. In game theory it is called **fungibility**. The principle is the same: when you give someone money for a specific thing they were already paying for, the money you give them frees up their own money for other things. The total amount spent on the *specific thing* doesn't change. *(pause)*

This is one of the most common failures of development assistance. Billions of dollars get crowded out every year. And the donors often *do not realise* until much later. *(pause)*

So how do we think about this properly? Game theory.

---

## Slide: Decisions are not made in isolation (section divider)

*(pause for transition)*

---

## Slide: The hidden assumption of Chapter 7

Chapter 7's expected-value calculation assumed David was the only one making a decision. The world responded passively to him. He placed a midwife, the midwife saved lives, end of story. *(pause)*

Look at the bad-example box. **The world is not passive.** Everyone else is also making decisions. And many of those decisions depend on what they think *you* will do. *(pause)*

The county finance officer in Kakamega did not redirect his budget by accident. He looked at the donor's offer and *thought through what would happen*. He calculated. He optimised. From his perspective, redirecting was the rational move. *(pause)*

Look at the definition box. **Game theory is just decision theory with one new addition: you write down what the other side will do in response, before you compute your expected value.** *(pause)*

That is the whole shift in this chapter. The math is the same as Chapter 7. The picture is bigger — it now includes the *other player*. And that one addition is enough to change which strategy is best. *(pause)*

Look at the green box. *The math is the same. The picture is bigger.* That is it.

---

## Slide: A payoff matrix in plain language

The simplest tool in game theory is something called a **payoff matrix**. It is a small grid. Two players. Two choices each. Four cells in the middle. Each cell tells you what happens if both players make those choices. *(pause)*

Let me walk through the one on screen.

*Look at the table.* The columns are the donor's choices: match, or walk away. The rows are the county's choices: fund maternal health, or redirect to roads. *(pause)*

Top-left cell: county funds, donor matches. *Both get what they wanted.* The county gets the match, the donor saves lives. *(pause)*

Top-right: county funds, donor walks away. The county still gets some lives saved on its own dime, but at the cost of fewer roads. The donor walked away — no spending. *(pause)*

Bottom-left: county redirects to roads, donor matches. The county gets *both* roads and the donor's match. The donor's money gets spent on maternal health, but the *new* maternal health funding is lower than expected — because the county's money walked. The donor's investment is partly wasted. *(pause)*

Bottom-right: county redirects, donor walks away. Roads get repaired. No new maternal health. Donor avoided a wasted match. *(pause)*

Look at the orange box. **The county would prefer to fund maternal health if the donor walks away** — because lives are at stake and the county knows it. *(pause)* **But it would also prefer to redirect to roads if the donor is going to fund maternal health anyway.** *(pause)*

That single sentence is the entire problem with naive matching grants. The county's best move *depends on what the donor does*. And the donor's best move depends on what the county does. They are stuck in a loop.

---

## Slide: Nash equilibrium, in plain language (section divider)

*(pause for transition)*

OK. There is a way to think clearly about that loop. It is called Nash equilibrium. Don't get scared by the name.

---

## Slide: The "nobody wants to move" point

Look at all four cells. For each one, ask yourself: *given what the other player is doing, would I switch?* If the answer is yes, the cell is unstable. If the answer is no for both players, the cell is *stable* — and that is the equilibrium. *(pause)*

*Bullet by bullet.* **County funds, donor matches.** Would the county switch? *Yes.* It could redirect to roads, get the match anyway, and have road repair on top. The county would gain by switching. *Unstable.* *(pause)*

**County redirects, donor matches.** Would the donor switch? *Yes.* The donor sees that its money was wasted — the county's funding walked. The donor would gain by walking away next year. *Unstable.* *(pause)*

**County funds, donor walks.** Would the county switch? *Yes.* Without the match, the county is bearing the full cost of maternal health and not getting roads. It would prefer to redirect. *Unstable.* *(pause)*

**County redirects, donor walks.** Would either side switch? *(pause)* The county is getting roads. The donor is not wasting money. Neither side has a reason to move. *Stable.* *(pause)*

Look at the definition box. **A cell where no player wants to move is called a Nash equilibrium. It is not necessarily the *best* outcome — it is just where the game settles.** *(pause)*

That is John Nash's insight. He was a mathematician at Princeton. He won a Nobel Prize for this idea. The idea itself is just *"find the cell where nobody has an incentive to leave"*. The math behind it can get complicated. The principle is something a child can understand.

---

## Slide: And here is the unsettling result

So look where the matching grant settles. *(pause)*

The Nash equilibrium of the simple matching grant is the *worst* outcome for everyone. *(pause)*

Look at the red box. **The county redirects, the donor walks away, no maternal health gets funded, the road gets repaired, lives are lost.** *(pause)*

Read that twice. The donor designed the game. The county is responding rationally — given the structure of the game, redirecting is the right move for the county. The donor walking away is the right move for the donor, given that the county is redirecting. Both sides are optimising. Both sides are rational. *(pause)*

**And the bad outcome is the rational outcome.** *(pause)*

This is the most important insight in this chapter. *Bad outcomes are not always caused by bad people or bad intentions.* They are sometimes caused by *games where the rational equilibrium is bad*. The fix is not to lecture the players. The fix is to *redesign the game*. *(pause)*

Look at the green box. **This is why intelligent grant design matters.** The structure of the game determines the equilibrium. Change the structure, change the outcome. *(pause)*

Let me show you how.

---

## Slide: How to fix the game (section divider)

*(pause for transition)*

---

## Slide: Three classic moves

There are three classic moves to fix a bad-equilibrium game. They show up everywhere. Once you can name them, you will see them.

*Bullet by bullet.* **Conditionality.** *"Match only if total maternal health spending is at least X."* This adds a floor. The county cannot redirect, because if total spending falls below X, the match disappears. The redirect cell becomes much less attractive. *(pause)*

**Commitment device.** *"Funds will be released annually based on the prior year's verified maternal health spending."* This creates a future cost to today's redirection. Even if the county wants to redirect now, doing so cuts off next year's match. The temporal structure of the game changes. *(pause)*

**Joint review.** *"Both donor and county sign off on a published spending plan, with quarterly public reviews."* This adds a *reputational* cost to redirection. The county's senior leadership has to publicly defend the spending. Most political systems make redirection embarrassing once it is in public view. *(pause)*

Look at the orange box. **Each move changes the payoffs.** And changing the payoffs changes the equilibrium. *(pause)*

That is the whole game theory toolkit in one sentence. *Change the payoffs, change the equilibrium.* If you walk into a meeting with a bad-equilibrium grant on the table, this is the framework you bring.

---

## Slide: Why Wangari accepted and Patrick didn't

Now let's go back to the original puzzle. *Why did Wangari accept and Patrick redirect?* *(pause)*

The donor offered them the *same deal*. So the math was the same. But the *surrounding payoffs* were different. *(pause)*

*Bullet by bullet.* Nakuru's county finance committee had public quarterly review meetings. Wangari faced direct, regular, on-the-record public pressure on health spending. The cost of redirecting maternal health funds — for her career, her reputation, her relationship with civil society — was *high*. So her optimal response was to accept and use the match. *(pause)*

Kakamega's road network had visible, immediate political pressure from voters who had been promised repairs for years. Patrick was facing a *different game*. The cost of *not* redirecting — politically, in his county — was high. The cost of redirecting was low, because the donor's reporting was annual and not public. So his optimal response was to redirect. *(pause)*

Look at the box. **Same deal. Different surrounding payoffs. Different equilibrium.** *(pause)*

This is a really important point. Game theory is not about what people should *want*. It is about what they will *do*, given what they actually face. *Game theory is the chapter where context becomes mathematical.* *(pause)*

If the donor had paid attention to the surrounding payoffs in each county *before* designing the grant, it could have built in different conditions for the two counties. Instead it offered the same deal to both — and got the same outcome only in the place where the surrounding game already happened to favour acceptance.

---

## Slide: Three quiet warnings (section divider)

*(pause for transition)*

---

## Slide: Warning 1 — The game theory model is also a model

Warning one. **The payoff matrix is a model.** *(pause)*

It is a simplified picture. Many real-world decisions have more than two options, more than two players, and cells whose values you do not actually know. *(pause)*

Look at the orange box. **Use the payoff matrix to clarify your thinking, not to replace it.** The grid is a sketch, not a calculation engine. *(pause)*

The most valuable thing about the matrix is that it forces you to *write down* what you think will happen in each scenario. The act of writing it down often reveals that you do not know what the other player will do — which is a useful realisation, even if the matrix itself stays imprecise.

---

## Slide: Warning 2 — Reputational cost is real but hard to measure

Warning two. **Reputational cost is real but hard to measure.** *(pause)*

A lot of game-theory matrices in development have cells that depend on phrases like *"the official will lose face"* or *"the public will react"*. Those phrases describe real things — *real* in the sense that they actually shape behaviour. But they are hard to put numbers on. *(pause)*

Look at the orange box. **The hardest cells in any game theory matrix are the ones whose values come from reputation.** They are easy to write down. They are hard to defend with data. *(pause)*

The fix is to be honest about which cells are evidence-based and which are guesses, and to interview people *before* assuming a particular reputational dynamic.

---

## Slide: Warning 3 — Equilibrium is not destiny

Warning three is the deepest one. *(pause)*

Game theory tells you *where the game settles*. It does not tell you *whether the game has to be played*. *(pause)*

Look at the red box. **The most powerful move is sometimes to refuse to play the game as designed.** *(pause)*

A donor that walks away from a bad-equilibrium grant is sending a stronger signal than one who keeps trying to redesign it. Sometimes the right move is *"we do not fund here this year, and we will be back when conditions change"*. That sentence is rare. It is also more credible than the fifth re-design of a grant nobody wants. *(pause)*

Always ask the question: *do we need to play this game at all? Or can we wait?*

---

## Slide: Try It (You are the analyst)

OK. Try it.

A donor wants to launch a free emergency obstetric kit programme in three districts. The kits cost the donor money but cost the district nothing. *(pause)*

One district happily accepts and reports good outcomes. Another reports good outcomes but has actually been *selling* the kits to neighbouring private clinics. A third refuses the kits entirely. *(pause)*

**Draw a payoff matrix for the second district. What did the donor's incentive structure miss? Which of the three classic fixes — conditionality, commitment, joint review — would you use?** *(pause)*

Hint. Think about what the second district *gains* from "accept and use", "accept and sell", and "refuse" — and what the donor can actually *verify*. *(pause)*

If you said *"the donor missed the side market for the kits, and the fix is joint review with random spot-checks"* — you have got it. The accept-and-sell strategy beats accept-and-use as long as the side market exists *and* nobody verifies which kits actually reach mothers. The fix is to add verification — which changes the payoff of "accept and sell" by adding a risk of being caught. That changes the equilibrium.

---

## Slide: Looking ahead

So that is Chapter 9. Almost there.

In Chapter 10 — the final chapter of the course — we ask the question that almost sounds too good to be true. **Can a computer just *discover* causal arrows from data?** *(pause)*

The answer turns out to be *partly yes, mostly no, and the "no" is more important than the "yes"*. We will see exactly when machines can help, when they cannot, and why the picture-drawing skill from Chapters 2 and 3 is the *only* thing that will save you from the seductive lie of *"the algorithm found this for us"*. *(pause)*

It is the most important chapter in the course for anyone who works with big datasets. See you there.

---

## Slide: The one thing to remember

If you remember nothing else from this chapter, remember this. *(pause)*

**Your decisions change how other people behave — and unless you write that down, your forecast of impact will be wrong.** *(pause)*

The payoff matrix is the picture from Chapter 2, with one new rule: every box is something *somebody chose*, and somebody else is choosing *in response*. *(pause)*

Wangari and Patrick faced the same offer. They responded differently. Both responses were rational. *The donor's design was the variable that mattered, and it ignored the surrounding game.* *(pause)*

See you in Chapter 10.

---

## Slide: Closing (white)

*(pause; no narration)*
