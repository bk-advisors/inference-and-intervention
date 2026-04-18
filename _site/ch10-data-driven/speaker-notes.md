# Speaker Notes — Chapter 10: Structure Learning

## Overview
This is the final chapter -- and it brings us full circle. For nine chapters, we have been drawing the arrows ourselves. Experts told us what causes what, and we built models from that knowledge. Today we flip the question: can a computer figure out the arrows just from data? The short answer is "sort of." And the nuances of that "sort of" are what make this chapter so interesting. By the end, you will see why the best approach combines human expertise with data -- and why neither one alone is enough.

## Slide: Learning Objectives
Five objectives for today. *(pause)* First, why data alone cannot always determine the direction of a causal arrow -- that is a deeper issue than you might expect. Second, what structure-learning algorithms can do and what they cannot. Third, how to combine expert knowledge with algorithmic output to build stronger causal models. Fourth, the feedback loop between data and models -- each one makes the other better. And fifth, hands-on practice using the `bnlearn` package in R to learn a DAG from simulated data and compare it to the truth.

## Slide: Chapter Overview
Here is our roadmap. Five stops. *(pause)* Can data find causes? Same pattern, different arrows. What algorithms can do. Expert plus algorithm. And the feedback loop. Look at that callout at the bottom -- it frames the central question. Throughout Chapters 1 through 9, we drew the arrows ourselves based on expert knowledge. This chapter asks: can a computer figure out the arrows just from data? The answer is nuanced, and that nuance is the most important lesson in the course.

## Slide: Can the Computer Draw the Arrows?
Look at these two columns. *(pause)* On the left, what we have been doing for nine chapters. An expert draws the DAG from domain knowledge. We assign numbers from data or expert judgment. We use the DAG for inference, decisions, and resource allocation. The DAG came from human expertise.

On the right, the new question. We have a dataset with many variables. Can a computer algorithm figure out which arrows to draw? Can it tell us what causes what, just from patterns in the data? *(pause)* Spoiler alert: the answer is partly yes and partly no. Data can narrow down the possibilities dramatically, but it cannot always determine the direction of every arrow. That is why you still matter.

## Slide: Three Simple DAGs
Let me make this concrete. Consider three variables -- Staffing, Training, and Mortality -- and three ways the arrows could go. *(pause)* DAG 1, the chain: Staffing causes Training, which causes Mortality. DAG 2, the fork: Training causes both Staffing and Mortality. DAG 3, the reverse chain: Mortality causes Training, which causes Staffing. Three completely different causal stories.

Now here is the surprising fact. All three DAGs produce the same statistical pattern in the data. If you know Training, then Staffing and Mortality become independent. No amount of data can tell you which of these three is correct. *(pause)* Let that sink in. You could collect a million data points and never distinguish these three causal stories from each other.

## Slide: The Collider Is the Exception
Now look at a fourth arrangement. *(pause)* Both Staffing and Mortality independently cause Training. This is called a collider -- two arrows pointing into the same node.

This one is different. In the collider, Staffing and Mortality are independent when you do not know Training. But they become dependent when you do know Training. That is the opposite pattern from the chain and the fork. *(pause)* Why does this matter? Because colliders create a unique data fingerprint. If the algorithm detects this pattern -- marginal independence turning into conditional dependence -- it can determine the arrow direction. Colliders are the one structure that data can identify on its own.

## Slide: The Core Problem -- A Summary
Let me summarize what we just learned. *(pause)* When you see that Staffing and Mortality are independent given Training, three different DAGs are compatible -- you cannot tell them apart. When you see that Staffing and Mortality are independent without conditioning but become dependent when you condition on Training, only one DAG is compatible -- the collider. Data can decide.

The definition box formalizes this. When two different DAGs produce the same data pattern, they are called Markov equivalent. No statistical test, no matter how large the sample, can distinguish between them. Only expert knowledge or experimental data can break the tie.

## Slide: From Millions of Options to a Handful
Okay, so what can algorithms actually do? *(pause)* Without an algorithm, with just 5 variables, there are over 29,000 possible DAGs. With 10 variables, the number exceeds 4 trillion. You could never check them all by hand.

With an algorithm, you test which variables are connected and which are independent, and you eliminate the vast majority. You end up with a small set -- often just a handful -- consistent with the data. *(pause)* Think of it like a detective. The algorithm cannot always name the one culprit. But it can narrow the suspect list from thousands down to three or four. That is enormously helpful.

## Slide: How the Algorithm Works
You do not need to know the math. Here is the basic idea behind score-based structure learning. *(pause)* Step 1: start with no arrows. Step 2: try adding an arrow. Step 3: does the DAG fit the data better? Step 4: keep it if yes, discard if no. Step 5: repeat until no more improvements.

The scoring function balances two things -- how well the DAG explains the data versus how many arrows it uses. The algorithm finds the sweet spot between fit and simplicity. This approach is called hill climbing, and it is what the `bnlearn::hc()` function does.

## Slide: Three Limitations
Three things algorithms cannot do. *(pause)* First, arrow direction. Usually. When two variables are correlated, the algorithm often cannot tell whether A causes B or B causes A. The chain and the reverse chain look identical.

Second, hidden variables. If a confounder is not in your dataset, the algorithm cannot find it. It might draw a direct arrow between two variables that are actually both caused by something unmeasured. *(pause)* Third, the "why." The algorithm tells you that Staffing and NMR are connected. It does not tell you why -- whether it is because better-staffed facilities provide better emergency care, or because staffing is a proxy for overall quality.

A learned DAG is a hypothesis, not a proof. It tells you what the data is consistent with, not what is true.

## Slide: When Direction Is Ambiguous
Imagine the algorithm finds that Training and Quality of Care are strongly associated. It says they are connected. But which arrow is correct? *(pause)* Option A: Training causes Quality. You invest in training because you believe it improves care. Option B: Quality causes Training. High-quality facilities attract more training opportunities -- they have the reputation and infrastructure that training programs seek out.

How do you break the tie? You ask someone who knows the health system. A clinician would tell you: training came first. The facilities received training, and then quality improved. Expert knowledge resolves the ambiguity that data alone cannot.

## Slide: The Partnership
Now here is the key insight of the whole chapter. *(pause)* Look at the comparison table. Expert only: understands mechanisms, temporal order, and context, but may miss unexpected connections and is biased by prior beliefs. Algorithm only: checks every possible connection and finds surprises, but cannot determine all arrow directions and is blind to unmeasured variables.

Expert plus algorithm: the human draws the DAG, the computer checks the data, and disagreements trigger investigation. The winning strategy is to draw the DAG from what you know, let the computer check if the data agrees, and where they disagree, investigate. This is how science actually works -- theory and evidence in conversation.

## Slide: The Three-Step Workflow
Three steps. *(pause)* Step 1: the expert draws a DAG from domain knowledge. Step 2: the algorithm learns a DAG from data. Step 3: you compare. Where do they agree? Where do they disagree?

Where they agree, you have high confidence. Both theory and data point the same way. Trust the arrow. Where they disagree -- that is where the most interesting discoveries happen. Maybe the expert was wrong. Maybe the data is misleading. Maybe there is a hidden variable. *(pause)* Either way, the disagreement points you exactly where to look next.

## Slide: The Virtuous Cycle
Here is the big-picture conclusion of the entire course. *(pause)* Expert knowledge feeds into a causal model. The causal model generates testable predictions. You collect data to check those predictions. The data either confirms your model or surprises you. Either way, you revise your understanding and start the cycle again.

The cycle never truly ends. Each pass makes your understanding sharper and your decisions better. This is the scientific method applied to causal modeling -- not a one-time exercise, but a living process that improves with every iteration.

## Slide: What Each Step Does
Let me walk through the cycle. *(pause)* Step 1: expert knowledge becomes a causal model -- that is Chapters 1 through 3. Step 2: the causal model implies statistical patterns -- "if my DAG is right, X and Y should be independent given Z" -- that is Chapters 4 through 6. Step 3: you know exactly what to measure and look for -- Chapters 7 and 8. Step 4: data confirms your predictions, which is great, or surprises you, which is even better because you learn something new. Step 5: update your DAG and start the next cycle stronger.

This is the scientific method. It is not a one-time exercise.

## Slide: Tanzania's Digital Health Infrastructure
Now let us ground this in a real country. *(pause)* Tanzania has serious digital health infrastructure. DHIS2 -- the District Health Information System -- covers routine health data at approximately 80 percent of health facilities. GoTHOMIS handles individual-level clinical records. Together, they capture staffing, equipment, service delivery, and outcomes.

What this means for us: Tanzania has the data infrastructure to test causal models against real facility-level records. When we draw a DAG predicting that staffing affects delivery outcomes, we can check -- does the DHIS2 data agree? This is the feedback loop in action.

## Slide: Testing Predictions with Facility Data
Here is a concrete example. *(pause)* The expert prediction: adequate staffing reduces neonatal mortality, partly through improved emergency response capability. The DAG says: Staffing leads to Emergency Response, which leads to NMR. This implies that if you know Emergency Response, the correlation between Staffing and NMR should weaken.

The data test: using DHIS2 facility records, check whether the correlation between staffing and neonatal outcomes weakens after controlling for emergency C-section rates. If the data agrees, confidence in the DAG goes up. If it disagrees, maybe staffing also has a direct effect through other pathways. Revise the DAG.

## Slide: What We Can Discover
With large-scale DHIS2 data from Tanzanian facilities, a structure-learning algorithm might discover several things. *(pause)* Expected connections: staffing and outcomes are linked -- the algorithm confirms what experts believe. Surprising connections: drug stockouts are more strongly linked to mortality than equipment availability -- suggesting supply chain might matter more than capital investment. Missing connections: training completion does not directly predict outcomes -- maybe the link works only through on-the-job practice.

Each surprise is a gift. The algorithm did not prove the expert wrong. It pointed to exactly where the expert should look more carefully.

## Slide: R Block 1 -- Simulate Health Facility Data
Time for code. *(pause)* We create a simulated dataset mimicking DHIS2 data -- a thousand facilities with six variables: Training, Drug Availability, Equipment, Staffing, Referral, and NMR. We know the true DAG because we built it ourselves, so later we can see how well the algorithm does.

Look at how the variables are generated. Training is binary. Drug availability is binary. Staffing depends on Training. Referral depends on Staffing and Equipment. NMR depends on Staffing and Drug Availability. Five arrows, six variables. The algorithm does not know any of this -- it only sees the data.

## Slide: R Block 2 -- Learn the DAG and Compare
Now we feed the data to the hill climbing algorithm -- no peeking at the true DAG. *(pause)* The `hc()` function from bnlearn runs the algorithm. Then we compare: which arrows did the algorithm get right? We count true arrows, learned arrows, correct matches, missed arrows, and false positives.

This is where it gets real. Run it and see -- some arrows get recovered perfectly, others get missed or reversed. That is the reality of structure learning.

## Slide: R Block 3 -- Visualize the Comparison
Side-by-side plots. *(pause)* True DAG on the left, learned DAG on the right. NMR highlighted in red so you can trace the causal paths to the outcome. Typical result with a thousand observations: the algorithm gets four out of five arrows correct. It finds all the right connections but may reverse one arrow direction. That reversed arrow is exactly where expert knowledge steps in.

## Slide: Interpreting the Results
So what do we typically find? *(pause)* The algorithm gets the connections right -- which nodes are linked. It gets collider structures right -- where two arrows point in. Strong effects with large sample sizes are well-recovered. But arrow direction in chains is harder -- it may flip an arrow. And weak effects may be missed entirely.

The practical strategy: use the learned skeleton as your starting point. Layer in expert knowledge to orient ambiguous arrows. Use temporal order -- things that happened earlier cannot be caused by things that happened later. That combination gives you the best final model. *(pause)* This is the expert-plus-algorithm partnership. The algorithm found the connection. The expert determined the direction. Together, they are stronger than either alone.

## Slide: The Four Pillars of the Course
Let us step back and see the full picture. *(pause)* Think causally -- Chapters 1 through 3. Add numbers -- Chapters 4 through 6. Make decisions -- Chapters 7 through 9. Discover from data -- Chapter 10. That is the complete arc. From drawing arrows, to filling in probabilities, to choosing interventions, to checking your work against evidence.

## Slide: The Complete Toolkit
Here is what you can now do. *(pause)* Draw a causal model from expert knowledge. Add probabilities from data or estimates. Avoid reasoning traps like confounding and selection bias. Calculate the value of different interventions. Allocate resources optimally across competing options. Anticipate strategic responses from other actors. And check your model against data and refine it.

The analyst's workflow ties it all together: interview experts and draw the DAG, populate it with data, identify the best intervention targets, allocate resources across countries, design incentive-compatible contracts, collect new data, check predictions, and refine. This is not a one-time analysis. It is a continuous cycle of learning and improving.

## Slide: Key Takeaways
Four core lessons from today. *(pause)* First, data alone cannot always determine causation. Different causal structures can produce the same data pattern. Only colliders create a unique fingerprint that data can identify.

Second, algorithms narrow down the possibilities dramatically. From trillions of possible DAGs, the algorithm finds the handful consistent with the data. That is powerful, even if it cannot pick the single right one.

Third, expert knowledge plus algorithm equals the best answer. The algorithm finds connections; the expert determines direction. This partnership is stronger than either approach alone.

And fourth -- the feedback loop is the course's central insight. Data refines your causal model. The model tells you what data to collect next. Each cycle makes your understanding, and your decisions, better.

## Slide: Congratulations
You have completed Inference and Intervention. *(pause)* The central message of the course: causal models are not just academic diagrams. They are practical tools for answering the questions that matter most. Where should we invest? What will happen if we do? How do we know we are right?

The combination of qualitative modeling, quantitative analysis, decision theory, and data-driven discovery provides a complete framework for making better decisions under uncertainty. *(pause)* The most important thing you take away is not any single technique. It is a way of thinking: always ask what causes what, draw it out, check it against evidence, and be willing to revise when the evidence says you were wrong. That is what separates good analysis from great analysis. And great analysis saves lives.
