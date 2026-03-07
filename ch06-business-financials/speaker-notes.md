# Speaker Notes -- Chapter 6: Simpson's Paradox & Cost-Effectiveness

## Overview
This is the chapter that will blow your mind. I am not exaggerating. We are going to look at a dataset where the same numbers, sliced two different ways, give you completely opposite conclusions. An intervention that looks harmful when you combine the data, but helps in every single country when you look separately. Same data. Opposite answers. And if you pick the wrong one, you send resources to the wrong places and people die. So pay attention -- this one matters.

## Slide: Learning Objectives
Five things for today. *(pause)* First, identifying Simpson's Paradox and explaining why aggregated data can show the opposite of what disaggregated data reveals. Second, distinguishing confounders from mediators -- because the causal model determines which answer is correct. Third, recognizing the Prosecutor's Fallacy, which is a bonus trap we will cover near the end. Fourth, applying causal reasoning to cross-country MNH comparisons. And fifth, using R to visualize Simpson's Paradox with aggregated versus stratified plots.

## Slide: Chapter Overview
Look at the flow on the slide. *(pause)* The paradox revealed, how aggregation lies, the causal key -- which is all about confounders versus mediators -- MNH across four countries, and an R workshop where you will see the paradox emerge from simulated data. And the core insight is right there in the callout box: the same dataset can produce two completely opposite conclusions depending on how you slice it. This is not a statistical curiosity. It is a real-world trap.

## Slide: The Setup -- A Training Program Across Four Countries
Here is the setup. *(pause)* Imagine you are evaluating a new emergency obstetric care training program for midwives across four East African countries: Ethiopia, Rwanda, Kenya, and Tanzania. You have outcome data from facilities that received the training and facilities that did not. And the combined data across all four countries shows this: facilities with training have a maternal mortality ratio of 310 per 100,000. Facilities without training have 285 per 100,000. *(pause)* The training program appears to increase maternal deaths. Should we shut it down?

## Slide: The Reveal -- Country-by-Country
Wait. Before you cancel the program, look at each country separately. *(pause)* Ethiopia: training reduces mortality by 40 points. Rwanda: minus 40. Kenya: minus 50. Tanzania: minus 40. The training reduces maternal mortality in every single country. *(pause)* Same data. Opposite conclusions. Combined, training looks harmful. Country by country, training helps everywhere. This is Simpson's Paradox.

Let that sink in. Not one country, not two -- all four. The training helps in every single place where we can make a fair comparison. Yet when you mush the data together, the signal reverses. If you were the program director and you only looked at the combined number, you might shut down a program that is saving lives in every country it operates in. That is the danger.

## Slide: How Is That Possible?
The secret is in who gets trained. *(pause)* Countries with higher baseline mortality -- more severe conditions, weaker health systems -- received more training, because they needed it most. Ethiopia and Kenya have higher baseline MMR and received the bulk of training slots. Rwanda and Tanzania have lower baseline MMR and received fewer slots. When you combine the data, the high-mortality countries dominate the training group, dragging the average up. *(pause)* The hidden third variable is baseline severity. It determines both who gets trained and what the outcomes look like. It is a confounder -- and ignoring it reverses the true effect.

Think about it this way. If you put a lifeguard at the most dangerous beach and a different lifeguard at the safest beach, and then compare drowning rates, the dangerous beach will still have more drownings. Does that mean lifeguards cause drowning? Of course not. The dangerous beach was selected precisely because it needed help. The comparison is unfair from the start.

## Slide: The Composition Effect
Let me show you the mechanics of the reversal. *(pause)* Look at the left table -- the aggregated view. It looks like training is worse. But now look at the right side. 70 percent of trained facilities are in high-mortality countries -- Ethiopia plus Kenya. Only 35 percent of untrained facilities are. The groups being compared are fundamentally different, and the difference is driven by the confounder, not the treatment. It is like comparing the swimming speed of fish and cats and concluding that having fins does not help.

## Slide: Visual -- Combined vs. Separated
Think of it as two pictures of the same data. *(pause)* Picture 1: one big bar chart. Two bars -- "Trained" versus "Untrained." The trained bar is taller. Looks worse. You conclude training hurts. But you are comparing apples to oranges. *(pause)* Picture 2: four side-by-side charts, one per country. In every single chart, the trained bar is shorter. Training helps. Now you are comparing apples to apples. Aggregation hides the confounder.

## Slide: The Confounder in the DAG
Look at the DAG on the slide. *(pause)* Baseline severity sits at the top -- it is a fork. It has arrows going down to both Training Received and Maternal Mortality. Severity causes both who gets trained and what outcomes look like. Training also has a direct arrow to Mortality -- that is the true causal effect, and it is negative. Training actually reduces mortality. But the backdoor path through the confounder creates a spurious association that overwhelms the true effect when you look at the combined data. *(pause)* The resolution is always the same: condition on the confounder. Stratify by country. The confounding disappears.

This is where everything we learned in earlier chapters clicks into place. Remember the fork structure from Chapter 2? Two variables that share a common cause look correlated even when there is no direct link between them. That is exactly what is happening here. Training and mortality look positively correlated -- more training, more death -- because they share the common cause of baseline severity. The DAG told us this would happen.

## Slide: The Lawsuit That Wasn't -- UC Berkeley
Let me give you the most famous illustration before we come back to MNH. *(pause)* In 1973, UC Berkeley was accused of gender discrimination in graduate admissions. Aggregated numbers: men admitted at 44 percent, women at 35 percent. A 9 percentage-point gap. Looked like clear discrimination. *(pause)* But then someone looked department by department. In four out of six departments, women were admitted at equal or higher rates than men. Department A: women 82 percent versus men 62 percent. Department B: women 68 percent versus men 63 percent. *(pause)* What was going on? Women disproportionately applied to the most competitive departments -- the ones with low admission rates for everyone. Department choice was the confounder. Once you stratified by department, the apparent bias vanished. Keep this example in mind -- the exact same mechanism shows up in our MNH data.

## Slide: The Berkeley DAG
Look at the DAG. *(pause)* Gender influences which department you apply to. Department influences whether you get admitted. The overall gap is driven by application patterns, not by discrimination within departments. *(pause)* And here is a subtlety worth mentioning. Is department a confounder or a mediator? If gender causes department choice, then department is technically a mediator. The correct analysis depends on the question you are asking. We will return to this distinction in the next section.

## Slide: The Critical Distinction -- Confounder vs. Mediator
This is the decision rule you need to internalize. *(pause)* Look at the two columns on the slide. On the left, confounder -- a common cause of both the treatment and the outcome. It creates a spurious association. Adjust for it. Conditioning removes the bias. On the right, mediator -- a variable on the causal path between treatment and outcome. It is part of how the treatment produces its effect. Do NOT adjust for it. Conditioning blocks the real effect. *(pause)* Getting this wrong leads to either Simpson's Paradox on one side or underestimation of treatment effects on the other. The data alone cannot tell you which role a variable plays. You need the DAG.

Let me give you a memory trick. A confounder is a back door -- it creates a sneaky path between treatment and outcome that has nothing to do with the treatment's actual effect. You want to close that door. A mediator is the front door -- it is the hallway through which the treatment actually reaches the outcome. You want to keep that door open. Close the back door, keep the front door open.

## Slide: Confounder Example -- Baseline Severity
In the EmOC training example, baseline severity is a confounder. *(pause)* Look at the DAG. Baseline severity is not caused by the training -- it existed before the program started. It influences who gets trained and what outcomes look like. We should adjust for it to see the true effect of training. When we stratify by baseline severity, the confounding disappears and we see training's true benefit.

## Slide: Mediator Example -- Skill Level
Now consider a different variable -- skill level after training. *(pause)* Training causes improved skills, and improved skills cause lower mortality. Skill level is on the causal path. It is the mechanism through which training works. We should NOT adjust for it. If we compare trained and untrained facilities among those with the same skill level, we have removed the very effect we are trying to measure. Training would appear to do nothing -- because we controlled away its mechanism.

I know this feels counterintuitive. "We should not control for skill level? But it is right there in the data." Yes -- and that is exactly the trap. Not every variable that is correlated with treatment and outcome should be controlled for. Only confounders should. Mediators should be left alone. The DAG is the only thing that tells you which is which.

## Slide: The Decision Rule
The causal model settles the debate. *(pause)* The data alone cannot tell you whether to adjust for a variable. You need to know the causal structure. Is this variable a confounder? Adjust for it. Stratify. Condition on it. Is it a mediator? Leave it alone. Do not condition on it. Get this wrong, and you can reach exactly the wrong conclusion. *(pause)* This is why we spent Chapters 2 through 5 building causal models. Without a DAG, Simpson's Paradox is unresolvable. The data is genuinely consistent with both stories -- training helps and training hurts. Only the causal model breaks the tie.

Let me say that once more because it is so important. The data does not resolve the paradox. Two perfectly smart analysts looking at the same spreadsheet can reach opposite conclusions and both be internally consistent. The DAG is the tiebreaker. If you do not have a causal model, you are guessing.

## Slide: Maternal Mortality Across East Africa
Here are the most recent WHO estimates for our four countries. *(pause)* Ethiopia: about 267 per 100,000. Rwanda: about 248. Kenya: about 342 -- the highest despite relatively strong urban infrastructure. Tanzania: about 238 -- the lowest despite a large rural population. These differences reflect dozens of underlying factors, and they make naive country comparisons treacherous.

Now, does the fact that Kenya has the highest MMR mean Kenya's health system is the worst? Not necessarily. Kenya also has the widest urban-rural divide, a massive population, and specific challenges in the arid northern counties. The raw number tells you the outcome, not the cause. To understand efficiency, you need to adjust for starting conditions -- which is exactly the point of this chapter.

## Slide: The Naive Comparison Trap
Suppose a program runs EmOC training in all four countries. After two years, you measure the reduction in MMR. *(pause)* Look at the table. Tanzania gets the biggest reduction relative to spending. Looks most efficient. Ethiopia gets the smallest reduction. Looks worst. Tempting conclusion: shift spending from Ethiopia to Tanzania. *(pause)* Why this is wrong: Ethiopia's lower apparent efficiency reflects its harder starting conditions -- larger population, lower baseline coverage, weaker infrastructure. The same dollar buys less visible improvement, but may save more lives at the margin because the unmet need is so much larger.

## Slide: The Confounder -- Baseline Health System Strength
Baseline burden -- MMR, health system capacity, population size, geographic access -- is the confounder. *(pause)* Look at the DAG. Baseline burden determines both where programs invest heavily and what raw outcomes look like. High-burden countries receive more investment and have worse outcomes. Without adjustment, the investment appears to cause worse outcomes -- when it actually causes better ones. The pattern is identical to our training example.

## Slide: What Correct Adjustment Reveals
Look at the side-by-side comparison. *(pause)* On the left, the naive ranking: Tanzania first, Ethiopia last. "Shift funds from Ethiopia to Tanzania." On the right, the adjusted ranking: Ethiopia first, Rwanda last. "Ethiopia is where the next dollar saves the most lives." *(pause)* Rankings reverse completely when you adjust for the confounder. The country that looks least efficient on paper may be the best investment at the margin -- because it has the most room to improve.

I want to be clear about what is happening here. We are not saying Tanzania's program is bad. It is doing well. We are saying that Ethiopia's program, which looked like a failure in the raw numbers, is actually delivering the highest marginal impact per dollar invested because the need is so much greater. The naive comparison punished Ethiopia for having harder starting conditions. The adjusted comparison rewards it for making the most progress given those conditions.

## Slide: The Lesson for Program Leaders
Three rules for cross-country MNH comparisons. *(pause)* One: never compare raw cost-effectiveness across countries without adjusting for baseline conditions. Different starting points make raw numbers incomparable. Two: always ask what is the confounder. In MNH, it is almost always some combination of baseline mortality, health system capacity, population size, and geographic access. Three: use the causal model to determine what to adjust for. Baseline burden is a confounder -- adjust for it. Quality improvement is a mediator -- do not adjust for it. The DAG tells you which is which. *(pause)* This is not just about statistics. Getting this wrong means shifting resources away from the countries that need them most.

I want to be very direct about the stakes. If a funder looks at naive cost-effectiveness rankings and says "Ethiopia is underperforming, shift the money to Tanzania," the funder is making the Simpson's Paradox mistake in real life. They are punishing the hardest-working program for having the hardest job. Causal reasoning is the antidote.

## Slide: The Fallacy in One Slide -- The Prosecutor's Fallacy
Now for the bonus insight. *(pause)* A diagnostic test for a rare complication is 99 percent accurate. You test positive. What is the probability you actually have the condition? Most people say 99 percent. *(pause)* But the answer depends entirely on how rare the condition is. If the condition affects 1 in 1,000 people, then out of 100,000 tested, 100 have it and 99 test positive -- true positives. But 99,900 do not have it, and 999 of them test positive anyway -- false positives. Total positive tests: 1,098. Chance you actually have it: 99 out of 1,098, which is about 9 percent. *(pause)* A "99 percent accurate" test gives you only a 9 percent chance of actually having the condition. That is the Prosecutor's Fallacy.

## Slide: Why This Matters
The Prosecutor's Fallacy is about confusing two different probabilities. *(pause)* P(positive given disease) -- how well the test works -- is not the same as P(disease given positive) -- what the test result means for you. When the disease is rare, most positives are false positives. You need Bayes' rule and the base rate to convert one probability into the other. *(pause)* The connection to Simpson's Paradox: both fallacies share the same root cause. Ignoring a crucial piece of context. The confounder in Simpson's, the base rate in the Prosecutor's Fallacy. In both cases, the causal model tells you what context you need.

This fallacy has real consequences. In courtrooms, prosecutors have convicted innocent people by presenting a match probability as a guilt probability. In medicine, patients have undergone unnecessary procedures because a positive screening result was misinterpreted. The fix is the same every time: use Bayes' rule, account for the base rate, and do not confuse the direction of the conditional.

## Slide: R Block 1 -- Simulate the Paradox
Now let us move to R. *(pause)* We simulate an EmOC training program across four countries. The confounder -- country -- determines both training allocation and baseline MMR. High-burden countries get more training and have higher baseline mortality. Training has a genuine positive effect in every country. When you run the aggregated summary, training will appear harmful. When you run the country-level summary, training helps everywhere. The paradox emerges right from the simulation.

Pay close attention to the simulation setup. Ethiopia gets 70 percent of facilities trained, Tanzania gets only 25 percent. That is the confounder at work -- training is allocated based on need. And Ethiopia has a baseline mortality rate about double Tanzania's. When you mix them together, Ethiopia's high mortality rate drags the trained group upward.

## Slide: R Block 2 -- The Aggregated View (Misleading)
Here is the misleading picture. *(pause)* One aggregated bar chart. Two bars: "Trained" and "Not Trained." The trained bar is taller. Training appears harmful. If you stopped here, you would cancel a life-saving program. The aggregated chart tells a false story because it mixes together countries with very different baselines.

## Slide: R Block 3 -- The Stratified View (Correct)
Now the true picture. *(pause)* Four panels, one per country. In every panel, the blue bar -- trained -- is lower than the orange bar -- not trained. Training reduces mortality in every country. The aggregated chart lied because it mixed countries together without accounting for baseline severity.

When you put these two charts next to each other in a presentation, the impact is immediate. People get it. You do not need a statistics degree to see that one big chart says "harmful" while four small charts all say "helpful." The visualization does the persuading for you.

## Slide: R Block 4 -- Side-by-Side Comparison
This is the visualization you should remember from this chapter. *(pause)* On the left, the misleading aggregated view. On the right, the correct stratified view. One dataset, two visualizations, opposite conclusions. The causal model tells you which one to trust.

## Slide: R Block 5 -- The Regression Comparison
Here we connect to something many of you may have seen before -- regression. *(pause)* The naive model regresses mortality on training alone. The coefficient is positive -- training appears to increase mortality. That is Simpson's Paradox in regression form. The adjusted model adds country as a control variable. Now the training coefficient flips to negative -- training is beneficial. The sign of the coefficient literally changes when you add the confounder. This is omitted variable bias -- the statistical fingerprint of a missing confounder.

This is a powerful demonstration. The exact same data, the exact same outcome variable, the exact same predictor -- the only difference is whether you include the confounder. And the conclusion flips from "training kills" to "training saves." If you ever want to convince someone that confounders matter, show them this regression output.

## Slide: R Block 6 -- Visualizing the Confounder's Role
This scatter plot shows why the paradox occurs. *(pause)* On the x-axis, the percentage of facilities trained. On the y-axis, baseline mortality. Countries with higher baseline mortality also have the highest training rates. The positive correlation between severity and training is the hallmark of the confounder. When you aggregate, the high-mortality countries dominate the trained group, making training look harmful.

## Slide: Key Takeaways
Three core lessons. *(pause)* First, Simpson's Paradox is not a curiosity -- it is a trap. Aggregated data can show the exact opposite of what is really happening. The resolution is causal, not statistical. You need a DAG to identify whether a variable is a confounder or a mediator. *(pause)* Second, the Prosecutor's Fallacy confuses P(Evidence given Hypothesis) with P(Hypothesis given Evidence). Base rates matter. Always use Bayes' rule. *(pause)* Third, in MNH cost-effectiveness, naive cross-country comparisons mislead because baseline burden is a confounder. Adjusting for it can reverse which countries and interventions look most effective -- and that reversal can save thousands of lives.

## Slide: Key Takeaways (Recap)
Let me bring it all home. *(pause)* Simpson's Paradox is real, it happens in actual health data, and it has fooled real decision-makers. The antidote is a causal model -- the DAG tells you which variables to adjust for. Confounders get adjusted; mediators do not. The Prosecutor's Fallacy is the same kind of mistake applied to individual cases rather than groups. And the R workshop showed you how to simulate, visualize, and detect these traps with code you can run yourself.

## Slide: Looking Ahead
Next chapter, we shift from understanding to deciding. *(pause)* We have learned how to correctly estimate causal effects -- seeing through Simpson's Paradox to the truth. Chapter 7 takes those estimates and asks: now what do we do with them? We will learn about decision maps, expected value, the difference between watching and doing, and how much it is worth to learn something before you commit. This is where causal thinking becomes a superpower. See you next time.
