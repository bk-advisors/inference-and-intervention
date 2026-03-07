# Speaker Notes -- Chapter 4: Quantitative Causal Models

## Overview
Alright, welcome to Chapter 4. This is the chapter where we put numbers on the arrows. Up until now, we have been drawing diagrams that say "this causes that" and labeling arrows with plus and minus signs. That is valuable -- it tells us the shape of the story. But today we go further. We are going to learn how to make those diagrams actually *compute* things. And I promise -- no scary formulas. We are going to start with plain counting, the way you already think about uncertainty, and build up from there.

## Slide: Learning Objectives
Five things I want you to walk away with today. *(pause)* First, turning real-world counts into probabilities -- nothing fancier than "55 out of 100." Second, reading and building lookup tables that capture how parent variables shape a child. Third, using Bayes' rule to think backwards -- "we see a bad outcome; what probably caused it?" Fourth, understanding the key rule that makes the whole thing practical: each node only depends on its direct parents. And fifth, building and querying an actual Bayesian network in R. Each piece builds on the one before it, so we will take them in order.

## Slide: Chapter Overview -- From Arrows to Numbers
Take a look at the flow up on the slide. *(pause)* We start with the qualitative DAG from Chapters 2 and 3 -- that is the arrows. We add lookup tables -- those are the numbers. And what we get is a Bayesian network -- a smart diagram that does math for you. Think of it this way: a qualitative model is like a road map that shows which towns are connected. A quantitative model adds the distances between towns. Now you can actually plan a trip.

## Slide: Start with Counts
The most natural way to think about uncertainty is to count things. That is where we start. *(pause)* Look at the Tanzania example on the slide. Tanzania has roughly 8,000 health facilities across 26 regions. The country faces a workforce shortage of about 55 percent -- that number comes from WHO and the Lancet. So out of 100 health facilities in rural Tanzania, about 55 have a severe workforce shortage. The other 45 have staffing closer to what is needed. *(pause)* That is a fact you can picture. Line up 100 facilities, and more than half are short-staffed. These counts -- "55 out of 100" -- are called natural frequencies. They are easier to reason with than abstract decimals, so we will use them as our starting point throughout this chapter. Why are natural frequencies easier? Because your brain was built to process counts. When someone says "0.55 probability," your eyes glaze over. When someone says "55 out of 100," you can picture the room.

## Slide: From Counts to Probability
Probability is just shorthand for natural frequencies. *(pause)* Look at the table. "55 out of 100 facilities are short-staffed" becomes P(Staffing = Low) = 0.55. "20 out of 1,000 newborns do not survive the first month" becomes P(Neonatal Death) = 0.020. That is literally all probability is -- a fraction. And there are only two ground rules. Every probability is between 0 and 1. And the probabilities of all possible states add up to 1. So if P(Low) = 0.55, then P(Adequate) = 1 minus 0.55 = 0.45. Simple as that.

## Slide: Where Do These Numbers Come From?
Good question, and there are two answers. *(pause)* On the left, from data. Tanzania's DHIS2 system and periodic facility surveys give us real counts. When data exists, use it. On the right, from expert judgment. Sometimes the data is incomplete. In those cases, experienced health workers or district officers give their best estimates. "I would say about 3 in 10 facilities in this region have functioning CPAP." *(pause)* In practice, we use both. The numbers in this chapter are illustrative, but they are grounded in publicly available data on Tanzania's health system.

## Slide: The Key Question
Now we get to the sharp version of the probability question. *(pause)* Plain probability asks: "What fraction of all facilities have high neonatal mortality?" Conditional probability asks something sharper: "Given that a facility has low staffing, what fraction have high neonatal mortality?" That word "given" changes everything. We are no longer looking at all 100 facilities. We are zooming in on just the 55 that are short-staffed and asking: among those, how many have high mortality?

## Slide: A 2x2 Table of 100 Facilities
Let me walk you through this table. *(pause)* Imagine we survey 100 facilities in rural Tanzania. We count how many fall into each combination of staffing and neonatal mortality. Look at the numbers. Of the 55 short-staffed facilities, 33 have high NMR and 22 have low NMR. Of the 45 adequately staffed facilities, only 9 have high NMR and 36 have low NMR. *(pause)* These are illustrative counts, but they reflect real estimates of Tanzania's workforce shortage and neonatal mortality rate.

## Slide: Reading the Table
Now we can answer both the plain and conditional questions. *(pause)* Plain probability: P(NMR = High) = 42 out of 100 = 0.42. Overall, 42 percent of facilities have high neonatal mortality. Conditional probability: P(NMR = High given Staffing = Low) = 33 out of 55 = 0.60. Among the short-staffed facilities, 60 percent have high mortality. *(pause)* And compare that with adequately staffed facilities: only 9 out of 45 = 0.20. The gap between 60 percent and 20 percent is enormous -- 40 percentage points. Staffing matters.

Here is a question for you. If someone told you "42 percent of facilities have high mortality" and also "55 percent of facilities have low staffing," could you compute the conditional probability from those two facts alone? *(pause)* No. You need the joint counts -- the inside of the table. The margins are not enough. That is exactly why lookup tables give us the joint information we need.

## Slide: Conditional Probability: The Idea
Here is the crucial warning I need you to burn into your memory. *(pause)* P(NMR = High given Staffing = Low) and P(Staffing = Low given NMR = High) are NOT the same thing. The first one is 33 out of 55 = 0.60 -- "of the short-staffed, 60 percent have high mortality." The second is 33 out of 42 = 0.79 -- "of the high-mortality facilities, 79 percent are short-staffed." Mixing these up is one of the most common mistakes in health data analysis. Bayes' rule, which we are about to learn, is the tool that connects them correctly.

## Slide: What Is a Lookup Table?
In Chapter 2 we drew an arrow from Staffing to Quality of Care. That arrow says staffing affects quality. But how much? A lookup table -- formally called a Conditional Probability Table, or CPT -- gives us the answer. *(pause)* Think of it as your cheat sheet. You look up the row that matches what you know about the parent variables, and the table tells you the probability of each outcome for the child variable. Every row adds up to 1.

## Slide: CPT for Quality of Care
Look at this table. *(pause)* Quality of Care depends on two parents: Staffing and Essential Medicines. Four rows, one for each combination. When a facility has adequate staffing AND available medicines, there is an 85 percent chance of good quality care. When a facility has adequate staffing but medicines are unavailable, it drops to 50-50. Low staffing but medicines available? Only 45 percent chance of good quality. And when both are lacking? Just 15 percent. *(pause)* That is the quantitative version of what we already knew qualitatively. Now we can see exactly how much each input matters.

## Slide: CPT for Neonatal Mortality
The second link in the chain. *(pause)* Good quality care gives an 82 percent chance of low NMR. Poor quality care? Only a 35 percent chance of low NMR. Nearly two in three facilities with poor care have high neonatal mortality. *(pause)* And notice the structure -- NMR depends only on Quality of Care in this table, not directly on Staffing or Medicines. Those upstream variables affect NMR, but only through Quality. The lookup table respects the arrows in our DAG.

Why does this matter practically? Because it means a district officer does not need to know every detail about staffing and medicines at a specific facility to estimate that facility's mortality risk. If she can assess quality of care -- maybe through a quick checklist -- that one variable captures everything upstream. The lookup table tells her: good quality? About 18 percent chance of high NMR. Poor quality? About 65 percent. That is a usable estimate from a single observation.

## Slide: Root Nodes Get Simple Tables
Nodes with no parents just need a single probability. No conditioning required. *(pause)* Staffing: 45 percent adequate, 55 percent low. Essential Medicines: 40 percent available, 60 percent unavailable. These reflect Tanzania's reality -- about 55 percent of facilities face staffing shortages, and essential medicine availability is low in many rural areas. *(pause)* And here is the key takeaway. A lookup table for every node equals a complete quantitative model. Root nodes get a simple one-row table. Every other node gets a table conditioned on its parents. Put them all together, and the model can compute any probability you ask it.

## Slide: The Backwards Question
So far we have been thinking forwards: given the causes, what outcome do we expect? But in real life, managers often face the backwards question. *(pause)* A district in Tanzania has high neonatal mortality. Before checking, you thought there was a 55 percent chance that any given facility is short-staffed. Now that you know mortality is high -- what is the updated chance that staffing is the problem? This is the kind of question Bayes' rule answers. Let us walk through it with natural frequencies -- no formulas first, just counting.

## Slide: Step 1 -- Start with 100 Facilities
Imagine 100 facilities. We know that about 55 are short-staffed and 45 have adequate staffing. *(pause)* That is our starting belief -- before seeing any mortality data. Look at the tree on the slide. One hundred facilities split into two branches: 55 low staffing, 45 adequate.

## Slide: Step 2 -- How Many Have High NMR?
Now we apply what we know from our lookup table. *(pause)* Of the 55 short-staffed facilities, 60 percent have high NMR. That is 33 facilities. Of the 45 adequately staffed facilities, 20 percent have high NMR. That is 9 facilities. Total with high NMR: 33 plus 9 equals 42 facilities.

## Slide: Step 3 -- Among High-NMR Facilities, How Many Are Short-Staffed?
Now comes the key move. We have 42 facilities with high NMR. We zoom in on just those 42 and ask: how many are short-staffed? *(pause)* Answer: 33 out of 42, which equals 0.79 -- that is 79 percent. Before seeing the mortality data, we had a 55 percent belief that a facility is short-staffed. After learning NMR is high, that jumped to 79 percent. A 24 percentage-point shift. *(pause)* That is Bayes' rule in action. Seeing high mortality is strong evidence of a staffing problem. No formulas needed, just careful counting.

## Slide: The Tree Diagram
Here is the same logic drawn as a tree. *(pause)* Start at the top with your total. Branch by the cause you are interested in. Then branch again by the evidence you observed. Count the relevant leaves. Divide. This is the same thing as the Bayes' formula, but you never have to memorize a formula. You just draw the tree and count. *(pause)* Let me say that again because it is important. The tree diagram approach and the formula approach always give the same answer. The tree is just friendlier for humans. If you ever get stuck on a Bayes' rule problem, draw the tree. Every time.

## Slide: Why Does This Matter?
Let me connect this to a real decision. *(pause)* A district health officer in one of Tanzania's 26 regions sees that a cluster of facilities has high neonatal mortality. Before any investigation, the officer knows that staffing shortages affect about 55 percent of facilities nationally. But after seeing the mortality data, Bayes' rule tells them: there is now a 79 percent chance the problem is staffing. That updated belief can guide where to send the audit team first -- and that matters when audit resources are scarce. *(pause)* This is the logic behind mortality audits. Deaths are diagnostic signals. Bayes' rule turns outcome data into actionable intelligence about what went wrong.

## Slide: Bayes' Rule -- The General Pattern
For those who want to see the formula, here it is. *(pause)* P(Cause given Evidence) = P(Evidence given Cause) times P(Cause) divided by P(Evidence). In our example: 0.60 times 0.55 divided by 0.42 equals 0.79. But you do not need to memorize this formula. If you can draw the tree and count, you get the same answer. The formula is just the shortcut.

## Slide: What Is a Bayesian Network?
Now let us put the pieces together. *(pause)* A Bayesian network is a DAG -- the arrows from Chapters 2 and 3 -- plus a lookup table for every node. Together, they form a model that can answer probability questions automatically. The DAG is the skeleton -- it shows the shape. The lookup tables are the muscle -- they give the model the numbers it needs. Put them together and you have a smart diagram that can answer "what if" questions.

## Slide: What Can a Bayesian Network Do?
Once you have a Bayesian network, you can ask it three types of questions. *(pause)* Forward: "If we improve staffing to adequate levels across the district, what happens to expected neonatal mortality?" Backward: "We observe high mortality. What is the most likely cause -- staffing, medicines, or both?" And what-if: "If essential medicines suddenly become available but staffing stays low, how much does mortality improve?" The network computes the answers using the lookup tables and the arrows. You do not have to do the math by hand -- software like R's bnlearn package handles it.

Think about how powerful that is. A district officer with four variables and three connections can now run dozens of scenarios instantly. What if we fix staffing but not medicines? What if we fix medicines but not staffing? What if a new supply chain improves medicine availability from 40 percent to 70 percent? Each scenario is just a query to the same network.

## Slide: The Rule That Simplifies Everything
Here is the single most important idea that makes Bayesian networks practical. *(pause)* Each node only depends on its direct parents. Once you know the parents of a node, nothing else in the network gives you additional information about that node. Consider the chain: Staffing goes to Quality of Care goes to NMR. If you already know that Quality of Care is poor, does it matter why it is poor? Whether it was caused by low staffing, missing medicines, or both -- the probability of high NMR is the same. Quality "screens off" everything upstream from NMR. That is why the NMR lookup table only has a Quality column, not a Staffing column.

## Slide: Why This Rule Matters -- Fewer Numbers to Specify
Without this rule, we would need a giant table. *(pause)* Four variables with 2 states each means 16 rows. Ten variables means 1,024 rows. Twenty variables means over a million rows. But with the rule, each node only needs its parents in its table. Typical nodes have 1 to 3 parents, so each table has 2 to 8 rows. Twenty variables with up to 3 parents each? About 160 rows total. The DAG structure tells us which probabilities we can skip. The causal structure does the work of simplifying the numbers.

## Slide: The Tanzania MNH Bayesian Network
Now let us put the whole thing together with Tanzania's data. *(pause)* Four nodes. Staffing and Essential Medicines are root nodes at the top. Quality of Care sits in the middle, depending on both Staffing and Medicines. And NMR is the outcome, depending only on Quality. Four nodes, three connections, and the lookup tables we already built. It is small enough to work through by hand, but rich enough to illustrate every concept we have covered today.

## Slide: Full Lookup Tables
Here are all the numbers. *(pause)* Root nodes: P(Adequate Staffing) = 0.45, P(Medicines Available) = 0.40. The Quality CPT has four rows. When both parents are favorable, 85 percent chance of good quality. When both are unfavorable, only 15 percent. The NMR CPT: good quality maps to 18 percent chance of high NMR, poor quality maps to 65 percent. These tables are the complete specification of the model. From these numbers alone, we can answer any probability question about these four variables.

## Slide: Querying the Model -- Best vs. Worst Case
Let us compute the extremes. *(pause)* Best case: adequate staffing and available medicines. That gives 85 percent chance of good quality, and when we work through the NMR probabilities, we get P(NMR = High) of about 25 percent. Worst case: low staffing, no medicines. Only a 15 percent chance of good quality, and P(NMR = High) jumps to about 58 percent. *(pause)* The gap is 33 percentage points. Moving from worst case to best case cuts the probability of high NMR from 58 percent to 25 percent. That is the combined payoff of adequate staffing and available medicines.

## Slide: Which Parent Matters More?
This is the analysis that actually helps with resource decisions. *(pause)* Fix staffing alone -- go from low to adequate while keeping medicines unavailable -- and P(NMR = High) drops by 21 percentage points. Fix medicines alone? A 14 percentage-point drop. Fix both? A 33 percentage-point drop. *(pause)* Staffing has the larger individual effect. But fixing both is better than the sum of fixing each alone. The combined improvement shows that staffing and medicines reinforce each other. A trained midwife with the right medicines can do far more than either resource alone. In a resource-constrained setting, this tells you: invest in workforce first, but do not neglect the tools they need.

## Slide: Exercise -- Try It Yourself
Your turn. *(pause)* Using the lookup tables from the previous slides, answer three questions. One: what is the overall P(Quality = Good) across all 100 facilities? There are four types of facility -- weight each by how common it is, then add them up. Two: what is the overall P(NMR = High)? Use your answer from question one with the NMR lookup table. Three: using Bayes' rule or the tree approach, if a facility has high NMR, what is the probability it has low staffing? *(pause)* Take a few minutes. The hints are on the slide. We will check the answers in the R workshop.

## Slide: R Block 1 -- Define the Network Structure
Okay, let us move to R and build this thing for real. *(pause)* We are using bnlearn's model string syntax to define the DAG. The notation is compact -- square brackets for each node, and a vertical bar for conditioning. So [Quality|Staffing:Medicines] means Quality depends on both Staffing and Medicines. Once you run this, you can inspect the structure with nodes() and arcs() to confirm it matches our four-node diagram.

## Slide: R Block 2 -- Fill In the Lookup Tables
Now we add the numbers. *(pause)* We are creating CPT arrays for all four nodes. Root nodes are simple -- just the probabilities for each state. The Quality CPT is a multi-dimensional array that matches our four-row table. The trickiest part is getting the array dimensions right, but the pattern is the same every time. Once you have all four CPTs, custom.fit() combines them with the DAG structure into a complete Bayesian network. A tip: read the comments in the code carefully. Each row is labeled so you know which combination of parents it corresponds to. If you get a row out of order, your model will give wrong answers. Always double-check the dimnames against your lookup table.

## Slide: R Block 3 -- Query the Network
Now the fun part -- asking questions. *(pause)* The cpquery function uses simulation to estimate conditional probabilities. Overall P(NMR = High) should come out around 0.44 -- about 44 percent of facilities have high NMR. P(NMR = High given Staffing = Low) should be around 0.52. And P(NMR = High given both parents favorable) should be around 0.25, matching our best-case calculation. These are the exercise answers computed by the network.

## Slide: R Block 4 -- Bayes' Rule in Action
Here is the backwards question implemented in R. *(pause)* Given that we observe high NMR, what is the probability that staffing is low? The answer should come out around 0.68 to 0.70. Compare that to the prior of 0.55. The evidence shifted our belief upward. High mortality is a signal that staffing is likely the problem.

## Slide: R Block 5 -- Exact Inference and Scenario Comparison
For precise answers with no randomness, we convert to the gRain package and compare intervention scenarios. *(pause)* This is the payoff of the whole chapter. The mutilated function implements the do-operator -- it simulates an intervention by forcing a variable to a specific value. We can compare "do nothing" versus "fix staffing" versus "fix medicines" versus "fix both" and see exactly how much each intervention reduces the probability of high NMR.

Look at the output table when it prints. You will see four rows -- one for each scenario. The "do nothing" row is the baseline. The "fix both" row is the best case. And the two single-fix rows let you see exactly how much each intervention contributes on its own. This table is the quantitative answer to the question every district officer asks: "Where should I put my resources first?"

## Slide: Key Takeaways
Let me pull it all together. *(pause)* Bayesian network equals DAG plus lookup tables. Natural frequencies make probability intuitive. Conditional probability sharpens our questions. Lookup tables are your cheat sheets. Bayes' rule lets you think backwards -- use the tree diagram. The key rule keeps the model manageable. And R plus bnlearn lets you build, query, and compare intervention scenarios in a few lines of code. *(pause)* We built the engine. Next chapter, we learn to drive it.

## Slide: Looking Ahead
Next chapter, we run this model backwards. We will observe outcomes in Ethiopia and use Bayes' rule to figure out what is most likely going wrong upstream. We will learn about a phenomenon called "explaining away" -- and I promise it will surprise you. Think of it as detective work: you see the crime scene, and you work backwards to figure out who did it. See you next time.
