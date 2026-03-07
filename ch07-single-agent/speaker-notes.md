# Speaker Notes -- Chapter 7: Decision Analysis & Value of Information

## Overview
Now we move from understanding to deciding. This is where causal thinking becomes a superpower. For six chapters we have been building up our ability to figure out what is going on -- inference, diagnosis, understanding the system. Today we flip the question entirely. Instead of asking "What is happening?" we are going to ask "What should I do about it?" We will learn decision maps, expected value, the difference between watching and doing, cutting the arrows, and the value of information. By the end, you will have a complete framework for choosing among interventions under uncertainty.

## Slide: Learning Objectives
Five objectives that take you from passive analysis to active decision-making. *(pause)* First, drawing decision maps that lay out your options, the uncertain events, and the outcome you care about. Second, calculating expected value using the "100 times" rule. Third, explaining why watching is different from doing -- seeing an umbrella is not the same as giving someone an umbrella. Fourth, using graph surgery to figure out the true effect of an intervention. And fifth, estimating the value of information -- how much is it worth to learn something before you commit.

## Slide: Chapter Overview -- From Understanding to Deciding
Look at the five-step flow on the slide. *(pause)* Decision maps, expected value, watching versus doing, cutting the arrows, and value of information. And look at that callout at the bottom. This is the big shift. Chapters 1 through 6 asked "What is happening and why?" That is inference. Starting now, the question changes to "What should I do about it?" That is intervention. Decision maps are the bridge between the two.

## Slide: What Is a Decision Map?
A decision map takes the causal models we have been building and adds two new ingredients. *(pause)* A choice you control, drawn as a rectangle. And a goal you want to achieve, drawn as a hexagon. Everything else -- the uncertain stuff you cannot control -- stays as ovals, just like before. *(pause)* Look at the table on the slide. Uncertain events are ovals -- things like neonatal mortality rate and staffing levels. Choices are rectangles -- things like which intervention to fund. Goals are hexagons -- things like neonatal lives saved. Think of it this way: Chapters 2 through 6 gave us a map of the territory. A decision map adds you to the map -- it shows where you are standing and which roads you can choose to take.

## Slide: A Simple Decision Map
Look at this diagram. *(pause)* On the left, a rectangle -- the county health director's choice. That flows to neonatal outcomes in the middle, which flows to the hexagon on the right -- newborn lives saved. Below, county baseline conditions feeds into outcomes. The director controls her choice. She does not control the baseline conditions. The arrow from her choice to outcomes is the causal effect of the decision. *(pause)* Notice something important. The arrow from baseline conditions to outcomes? That is a contextual influence she cannot control. She can only decide what to do given whatever conditions exist.

Why three shapes instead of one? Because the distinction matters. In the old causal diagrams, everything was a circle -- everything was uncertain. Now we are separating things into what you control, what you do not control, and what you want to achieve. That separation forces clarity. You cannot optimize what you do not control. You can only optimize what you choose.

## Slide: The Kenya MNH Decision
Here is the scenario. *(pause)* A county health director in Kenya has limited resources. She must choose between two options. Option A: purchase and install CPAP machines in 10 facilities -- cost about KES 15 million. Option B: fund EmONC training for 50 midwives across 25 facilities -- same cost. Both options cost the same. The question is: which one will save more newborn lives? *(pause)* Why is this hard? The answer depends on things she does not know for certain. Will the CPAP machines be maintained? Will the trained midwives stay in their posts? The decision map helps her think through the uncertainty before committing.

This is a real-world dilemma that county health directors across Kenya face constantly. Fixed budget. Multiple worthy options. Genuine uncertainty about which one will work better. Without a framework, people go with gut instinct or political pressure. With a framework, they can at least make the assumptions explicit and do the math.

## Slide: The "100 Times" Rule
Here is expected value in plain language. *(pause)* If you could make the same decision 100 times under the same conditions, the expected value is the average outcome you would get. It weights each possible outcome by how likely it is to happen. Imagine the county health director could run the same year 100 times. In some runs, things go well -- equipment works, midwives stay. In some runs, things go badly -- equipment breaks, midwives leave. The expected value is the average across all 100 runs. *(pause)* We do not need fancy formulas. Expected value is just: add up probability of each scenario times outcome in that scenario. That is it.

## Slide: Option A -- CPAP Equipment for 10 Facilities
What could happen if the director buys CPAP machines? *(pause)* Three scenarios. Best case: machines work and staff are trained to use them -- 40 out of 100 times, saving 120 lives. Partial success: machines work but staff struggle -- 35 out of 100 times, saving 50 lives. Failure: machines break down, no maintenance -- 25 out of 100 times, saving only 10 lives. *(pause)* Expected value: 0.40 times 120 plus 0.35 times 50 plus 0.25 times 10 equals 48 plus 17.5 plus 2.5 equals 68 lives. On average, Option A saves about 68 newborn lives per year.

Notice the range here. Best case is 120 lives. Worst case is only 10 lives. That is a 12-to-1 ratio. The outcome depends enormously on whether someone is around to maintain the machines. Equipment without maintenance is expensive furniture.

## Slide: Option B -- EmONC Training for 50 Midwives
Now the training option. *(pause)* Best case: most midwives stay and apply skills -- 30 out of 100 times, saving 150 lives. Partial success: about half stay, skills fade -- 50 out of 100 times, saving 80 lives. Failure: high turnover, training wasted -- 20 out of 100 times, saving 20 lives. *(pause)* Expected value: 0.30 times 150 plus 0.50 times 80 plus 0.20 times 20 equals 45 plus 40 plus 4 equals 89 lives. On average, Option B saves about 89 newborn lives -- roughly 30 percent more than Option A. The midwife training reaches more facilities and is less dependent on a single point of failure.

## Slide: Comparing the Two Options Side by Side
Look at the comparison. *(pause)* Option A: 68 expected lives, range of 10 to 120, depends heavily on maintenance capacity. Option B: 89 expected lives, range of 20 to 150, depends heavily on midwife retention. *(pause)* Option B wins on expected value. But notice the green callout on the slide. This assumes we know the probabilities correctly. What if we got them wrong? What if retention turns out to be much worse than we think? That question leads us directly to the value of information.

## Slide: Decision Trees -- A Different View
A decision tree is just a decision map drawn sideways, as a branching diagram. *(pause)* How to read it: start at the left with your choice -- the rectangle. Follow each branch to the uncertain events -- the ovals. At the end of each branch, find the outcome. Then work backwards: multiply outcomes by probabilities, compare the choices. This working backwards approach is called "folding back" the tree. *(pause)* A decision tree and a decision map contain the same information. Decision trees are good for sequential problems where one choice leads to another. Decision maps are better for seeing the whole causal structure at once.

## Slide: The Umbrella Analogy
Here is the key distinction for this chapter, and I want you to really get this. *(pause)* Watching: you look outside and see people carrying umbrellas. You conclude it is probably raining. The umbrella is a signal. It tells you about the weather. Doing: you hand out umbrellas to everyone on the street. Does it start raining? Of course not. Giving someone an umbrella does not change the weather. *(pause)* Seeing an umbrella is not the same as giving an umbrella. This seems obvious with umbrellas, but it is one of the most common mistakes in policy and program design.

Here is another way to think about it. Watching is about correlation -- things that go together. Doing is about causation -- one thing actually making another happen. You already know from Chapter 1 that correlation is not causation. The umbrella analogy makes that abstract idea viscerally concrete. Carry this analogy with you. Every time someone shows you a correlation and says "let us do more of X," ask yourself: are they handing out umbrellas?

## Slide: Watching vs. Doing in Kenya's Health System
Let me make this concrete. *(pause)* Watching: you look at data from Kenya's 47 counties and notice that counties where facilities have CPAP machines tend to have 30 percent lower neonatal mortality. But those counties also tend to have more health workers, better supply chains, stronger management teams, higher budgets. The CPAP machine is a signal of a well-resourced county. It is the umbrella. *(pause)* Doing: you give a CPAP machine to a facility in an under-resourced county, changing nothing else. The true causal effect might be only a 10 percent reduction. Still valuable, but much less than 30 percent. When you watch, you see the effect of CPAP plus everything else that comes with it. When you do, you see only the effect of CPAP itself.

## Slide: Why Does This Happen?
The problem is confounders -- exactly what we learned in Chapter 6. *(pause)* Look at the DAG on the slide. County Resources sits at the top -- the hidden common cause. Rich counties buy CPAP and have lower mortality for lots of reasons. When you just watch, you see the combined effect of resources plus CPAP. When you do -- when you give CPAP to a resource-poor county -- you only get the direct CPAP effect.

This is Simpson's Paradox applied to decision-making. If you use observational correlations to choose your intervention, you will systematically favor whatever intervention happens to cluster in well-resourced counties. That is not a recipe for good decisions -- it is a recipe for reinforcing existing inequalities.

## Slide: The Lesson for Decision-Making
Before you use data to make decisions, always ask: am I looking at the result of watching or doing? *(pause)* Watching data includes confounders. Doing data isolates the causal effect. If you use watching data as if it were doing data, you will overestimate the benefit of your intervention and misallocate resources. *(pause)* The numbers you use for expected value calculations must come from "doing" estimates, not "watching" estimates. Otherwise your decision map will point you in the wrong direction.

## Slide: Graph Surgery -- The Big Idea
Here is how we formalize the watching-versus-doing distinction. *(pause)* When you intervene on a variable -- when you set it to a specific value by deliberate action -- you cut all the arrows pointing into it in your causal diagram. The variable no longer depends on its usual causes; it depends only on your choice. Why? Because when you decide to give a facility a CPAP machine, that decision does not depend on whether the county is rich or poor. You are making it happen. So the arrow from County Resources to CPAP no longer applies.

The name "graph surgery" is dramatic, and it should be, because this is a big idea. You are literally taking scissors to the diagram. The arrows you cut are the ones that normally determine the variable's value. But when you intervene, you override those causes. The variable is now set by you, the decision-maker, not by the system.

## Slide: Before and After Surgery
Look at the two diagrams side by side. *(pause)* Before surgery -- the watching version. County Resources has arrows going to both CPAP and NMR. CPAP also has an arrow to NMR. Everything is connected through the confounder and through the direct causal path. After surgery -- the doing version. The arrow from Resources to CPAP is cut. Now the only path from CPAP to NMR is the direct causal one. The confounder is blocked. *(pause)* County Resources still affects NMR directly -- richer counties still have lower mortality for other reasons. But it no longer confuses our estimate of what CPAP itself does.

## Slide: Graph Surgery Applied to Our Kenya Decision
Look at the full decision diagram. *(pause)* The director's choice on the left. It flows through intervention delivery to neonatal outcomes to lives saved. Below, maintenance capacity and midwife retention feed into the uncertain variables. The director controls her choice. She does not control maintenance capacity or retention. Graph surgery cuts all arrows into the decision node, making it clear that the only thing connecting her choice to lives saved is the causal path.

## Slide: The Pilot Question
Our county health director has picked Option B based on expected value. But she is uncertain about midwife retention. *(pause)* What if she could find out the retention rate before committing her entire budget? What if she spent KES 1.5 million -- 10 percent of the budget -- to pilot the training in 5 facilities first and measure retention over 6 months? *(pause)* This is the value of information question. Before committing resources to all facilities, what is it worth to learn something first? If the pilot changes her decision, it has value. If it does not change her decision -- she would pick training regardless -- it has no value.

## Slide: When Information Has Value
Information is valuable when you are uncertain about a key variable, different answers would lead to different decisions, and the cost of being wrong is high. *(pause)* It is not valuable when you would make the same decision regardless, when the cost of gathering information is too high, or when the information arrives too late to act on. *(pause)* In our case: if the pilot reveals high turnover, the director switches to CPAP. That switch saves resources that would have been wasted. If the pilot just confirms what she already believed, it did not change anything.

## Slide: Calculating the Value of a Pilot
Let me put numbers on this. *(pause)* The pilot can reveal one of three things. Retention is high -- 30 percent chance. Best decision: training, saving 150 lives. Retention is moderate -- 50 percent chance. Best decision: still training, saving 80 lives. Retention is low -- 20 percent chance. Best decision: switch to CPAP, saving 68 lives. *(pause)* Expected value with the pilot: 0.30 times 150 plus 0.50 times 80 plus 0.20 times 68 equals 45 plus 40 plus 13.6 equals 98.6 lives. Expected value without the pilot: 89 lives. *(pause)* Value of the pilot: 98.6 minus 89 equals 9.6 additional lives saved. The pilot is worth running if its cost -- in terms of lives delayed -- is less than 9.6 lives. That is the value of information.

Now notice where the value comes from. In two out of three pilot outcomes -- high and moderate retention -- the director would have chosen training anyway. The pilot only changes her decision 20 percent of the time, when retention turns out to be low. But that 20 percent matters enough to justify the pilot because the cost of choosing wrong -- training with high turnover -- would waste a large chunk of the budget.

## Slide: Applying This to Kenya's 47 Counties
Scaling the idea. *(pause)* Kenya has 47 counties with significant variation in health system capacity. Before rolling out a single strategy nationwide, the national government could pilot in 5 diverse counties -- urban, rural, arid, high-burden, low-burden. Measure the key uncertain variables. Update the decision map with real data. Then customize by county -- maybe CPAP is better for some, training for others. *(pause)* This is a sequential decision: pilot first, then decide. The value of the pilot depends on county-level variation.

## Slide: Kenya's Maternal and Newborn Health Context
Some key facts. *(pause)* Kenya has 47 counties with devolved health governance since 2013. About 89 percent facility delivery rate nationally, but wide county variation. Maternal mortality around 342 per 100,000. Significant county-level variation in neonatal mortality -- from 15 to 40-plus per 1,000. County governments control health budgets, staffing, and procurement. Each county health director faces her own version of the CPAP versus training decision. *(pause)* Why Kenya is a perfect case study: the devolved system means 47 different decision-makers are independently making resource allocation choices.

## Slide: The Full Decision Problem
Here is the scenario for a high-burden county. *(pause)* NMR about 38 per 1,000, 65 percent facility delivery, limited equipment. Option A: CPAP for 10 facilities, reaches 20 technicians, best case 120 lives, worst case 10, expected value 68. Option B: EmONC training for 50 midwives across 25 facilities, best case 150 lives, worst case 20, expected value 89. Same cost, different reach, different risks.

Look at the reach difference. CPAP touches 10 facilities and 20 technicians. Training touches 25 facilities and 50 midwives. That is two-and-a-half times the coverage. In a setting where the bottleneck is human capacity, broader reach can be a significant advantage.

## Slide: How the Decision Changes Across County Types
Not every county is the same. *(pause)* Look at the table. In high-burden counties with weak systems, training wins decisively -- expected value of 95 versus 55 for CPAP. In high-burden counties with moderate systems, training still wins but by a smaller margin. In moderate-burden counties, it is a toss-up. And in low-burden counties with strong systems? CPAP actually wins -- 80 versus 55. *(pause)* The answer is not the same everywhere. In counties with weak health systems, training addresses the most binding constraint -- workforce capacity. In well-resourced counties, CPAP fills a different gap. Context determines the optimal choice.

## Slide: The "Watching vs. Doing" Trap in County Data
Here is a common mistake in practice. *(pause)* A policymaker looks at data from all 47 counties and sees: counties that invested in CPAP last year had 25 percent lower neonatal mortality than counties that invested in training. She concludes: tell all counties to buy CPAP. *(pause)* This is the watching-versus-doing mistake. Counties that bought CPAP were already better-resourced. The 25 percent difference is mostly about county resources, not about CPAP itself. After graph surgery, the true causal effect of CPAP might be only 10 percent, while the true causal effect of training might be 15 percent. The naive data pointed in the wrong direction.

## Slide: R -- Setting Up the Decision Problem
Let us move to R. *(pause)* We define the two options with their scenarios, probabilities, and lives saved. Then we compute expected value for each. The code is straightforward -- group by option, sum probability times lives saved. Option B comes out at 89, Option A at 68. Training wins.

## Slide: R -- Visualizing the Two Options
A horizontal bar chart comparing expected values. *(pause)* Two bars. Training on top at 89 lives, CPAP below at 68 lives. Clean and clear. This is the kind of visual you would use to brief a county health director.

## Slide: R -- Sensitivity Analysis
Now we ask: how robust is our answer? *(pause)* We vary the probability of high retention for the training option from 0 to 0.70 and plot how expected value changes. The training line slopes upward. The CPAP line stays flat at 68. The lines cross at a very low retention probability -- around 8 percent. *(pause)* The training option is surprisingly robust. It beats CPAP unless the probability of high retention drops to near zero. Even if our retention estimate is somewhat wrong, the decision probably does not change.

This is sensitivity analysis, and it is one of the most important things you can do after computing an expected value. The expected value itself is one number. The sensitivity plot tells you how much that number can move before your decision flips. If the answer is "it barely moves," you can be confident. If the answer is "any small change flips the decision," you need to think a lot harder -- or run a pilot.

## Slide: R -- Value of Information Calculation
Here we compute the value of the pilot in R. *(pause)* Without the pilot, best decision is training at 89 lives. With the pilot, we learn retention before committing and can switch to CPAP if retention is low. Expected value with pilot: 98.6 lives. Value of information: 9.6 lives. The pilot is worth running if its cost in delayed lives is less than 9.6.

## Slide: R -- County-Type Comparison
Finally, we visualize how the optimal strategy varies by county type. *(pause)* A grouped bar chart with four county types on the x-axis and CPAP versus training bars for each. In weak-system counties, training towers over CPAP. In strong-system counties, CPAP towers over training. In the middle, they are about even. No single intervention is best everywhere.

This is a key result. If someone asks you "should we invest in equipment or training?" the correct answer is not one or the other. The correct answer is "it depends on the county." The decision map plus expected value plus county-type analysis gives you the tools to make that case with numbers.

## Slide: Key Takeaways
Four essential lessons. *(pause)* First, decision maps add your choices and goals to causal diagrams, turning understanding into action. Second, expected value -- "play it 100 times" -- gives you a principled way to compare options under uncertainty. The county health director should fund midwife training -- it saves about 30 percent more lives on average. *(pause)* Third, watching is not the same as doing. Use graph surgery to isolate the true causal effect before plugging numbers into your decision map. Fourth, information has measurable value. Before committing to all 47 counties, a pilot in 5 diverse counties could save an additional 9 to 10 lives per county -- if it changes the decision.

## Slide: Looking Ahead
Next chapter, we scale up. *(pause)* Instead of one county director's choice, we zoom out to the national level. Allocating a fixed budget across Kenya's 47 counties. Sequential decisions -- pilot in some counties, then scale based on results. County government co-financing uncertainty. And the cost of waiting versus the cost of being wrong -- when is it better to act now with imperfect information? The single-agent framework we built today becomes the workhorse for multi-country resource allocation. See you next time.
