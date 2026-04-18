# Speaker Notes -- Chapter 5: Situational Analysis

## Overview
Welcome to Chapter 5. This is where we start running the model backwards -- like a detective working from the crime scene. In Chapter 4 we built a Bayesian network that goes forward, from causes to effects. Today we flip it around. We observe an outcome -- like high neonatal mortality in an Ethiopian region -- and ask: what is most likely going wrong? And the star of today's session is something called "explaining away." It is the most counterintuitive and practically important result in causal reasoning, and I promise it will change how you think about diagnosis.

## Slide: Learning Objectives
Five things I want you to walk away with. *(pause)* First, explaining belief updating in plain language -- "updating your best guess when you learn something new." Second, computing marginal probabilities by averaging across possibilities you have not yet observed. Third, tracing how evidence flows through chains, forks, and colliders -- and knowing when the flow stops. Fourth, the explaining away phenomenon -- the crown jewel of causal inference. And fifth, using a Bayesian network to diagnose why an Ethiopian region has high neonatal mortality.

## Slide: Chapter Overview -- Running the Model Backwards
Look at the five-step flow on the slide. *(pause)* The detective's question, averaging across possibilities, updating your best guess, how evidence flows, explaining away, and finally the Ethiopian region diagnosis. And look at the big idea at the bottom. In Chapter 4 we built the model forward -- starting from causes and predicting outcomes. Now we run it backwards. We see the outcome and ask: what caused this? This is how managers, doctors, and detectives actually think.

## Slide: The Wet Sidewalk
Here is a scenario everyone can relate to. *(pause)* You walk outside and the sidewalk is wet. What happened? There are two possibilities. Maybe it rained. Or maybe the neighbor's sprinklers went off at 5 AM. You were asleep, so you did not see either one happen. *(pause)* This is the detective's question. You see the result -- wet sidewalk. You did not see the cause. You have to reason backwards, from effect to cause, using what you know about how the world works. That is exactly what we are going to do with health data today.

Notice something: you are not randomly guessing. You bring knowledge to the problem. You know it is the rainy season, so rain is plausible. You know your neighbor has sprinklers on a timer. You weigh those possibilities against each other. That weighing is belief updating, and it is exactly what the Bayesian network does -- just with numbers instead of gut feelings.

## Slide: The Same Logic, Applied to Health
Now here is the detective question for a health program manager. *(pause)* An Ethiopian region reports a neonatal mortality rate of 35 per 1,000 live births -- well above the national average of about 28 per 1,000. The program director asks: "What is most likely going wrong? Is it staffing? Equipment? The referral system? All three?" You cannot visit every facility. But you have a model. You can run it backwards. *(pause)* This chapter teaches you the mechanics of running the model backwards. There are exactly three skills: averaging across possibilities, updating your best guess, and understanding how evidence flows through different structures.

## Slide: From Forward to Backward
Look at the two boxes on the slide. *(pause)* On the left, Chapter 4's forward reasoning: "If staffing is low and equipment is unavailable, what is the probability of high mortality?" That is prediction. On the right, Chapter 5's backward reasoning: "We observe high mortality in a region. What does this tell us about staffing and equipment?" That is diagnosis. *(pause)* Both directions use the same model. The math is the same. The difference is what you know and what you want to find out.

Here is why this matters so much in practice. Prediction is useful for planning -- you can estimate what will happen if conditions are a certain way. But diagnosis is what managers actually need most of the time. They already see the outcome. The question is: what caused it, and where do I intervene?

## Slide: When You Do Not Know
Suppose you want to predict mortality in a region, but you have no idea whether staffing is adequate or low. *(pause)* You know two things from your model. If staffing is adequate, probability of high mortality is 20 percent. If staffing is low, probability of high mortality is 55 percent. And you know from national data that about 40 percent of Ethiopian health facilities have adequate staffing. *(pause)* So what is your overall best guess? You average across the two possibilities, weighted by how likely each one is. Overall P(High Mortality) = 0.40 times 0.20 plus 0.60 times 0.55 = 0.08 plus 0.33 = 0.41. A 41 percent chance of high mortality. That is a weighted average. The fancy name for this is "marginal probability," but "weighted average across possibilities" is all it really is.

## Slide: The Weighted Average in Pictures
Look at the table on the slide. *(pause)* Each row is one scenario. Staffing adequate has a 40 percent weight and contributes 0.08 to the total. Staffing low has a 60 percent weight and contributes 0.33. Add them up: 0.41. That is our starting point before we learn anything about this specific region. Everything that follows is about how this number changes when evidence comes in.

## Slide: Averaging with Two Unknown Parents
Now suppose you also do not know whether equipment is available. *(pause)* You average across all four combinations -- adequate staffing with available equipment, adequate with unavailable, low with available, low with unavailable. Each one is weighted by how likely that combination is. Look at the table -- the biggest contributor is the last row: low staffing plus unavailable equipment, with a weight of 0.39 and a high mortality probability of 0.60. That single combination contributes 0.234 to the total. *(pause)* Add them all up and you get P(High Mortality) = 41.7 percent. That is our "before" number -- our baseline expectation before any evidence arrives.

## Slide: Before and After
Here is the core idea of this chapter, in one sentence. *(pause)* When you learn something new, your estimates change. Your "before" beliefs are called the prior. Your "after" beliefs -- after incorporating evidence -- are called the posterior. The shift from prior to posterior is belief updating. Think of the wet sidewalk again. Before looking outside, you gave a 50 percent chance it rained. After seeing the wet sidewalk, that goes up to 75 percent. The wet sidewalk shifted your belief by 25 percentage points.

## Slide: Updating in the MNH Model
Now let us apply this to a real problem. *(pause)* Before we learn anything about this specific Ethiopian region, our priors come from national averages. P(Staffing = Low) = 60 percent. P(Equipment = Unavailable) = 65 percent. These are our defaults. *(pause)* Now we learn the region has high neonatal mortality. After updating: P(Staffing = Low given High NMR) = 73 percent. P(Equipment = Unavailable given High NMR) = 74 percent. Both bad explanations became more likely. What just happened? High mortality is more consistent with low staffing than with adequate staffing. So observing high mortality shifts our belief toward the "low staffing" explanation. Same logic for equipment.

## Slide: How Much Does Evidence Shift Your Beliefs?
Look at the table -- this is where the diagnostic payoff shows up. *(pause)* Staffing shifts the most, 13 percentage points. Equipment shifts by 9 points. Referral by 8 points. So if you are the program analyst and you can only investigate one thing first, where do you look? Staffing. It is the variable with the strongest signal. *(pause)* This is the power of running the model backwards -- it tells you where to look first.

## Slide: The Updating Rule in Plain English
Let me give you the recipe in four steps, no formula needed. *(pause)* One: start with your best guess about a cause -- that is the prior. Two: ask how likely the evidence is under each possible state of the cause. Three: the state that makes the evidence more likely gets a boost; the other state gets downgraded. Four: normalize so your beliefs still add up to 100 percent. That is all Bayes' rule does. You have already seen the formal math in Chapter 4. Here we focus on the logic.

## Slide: The Three Structures, Revisited
In Chapter 2 you learned three patterns that every causal diagram is built from. Now we ask a new question: how does evidence travel through each one? *(pause)* Look at the table on the slide. Chains: evidence flows along the chain, unless the middle node is known. Forks: evidence flows through the common cause, unless the common cause is known. Colliders: evidence is blocked by default, unless the middle node is known. *(pause)* Chains and forks behave the same way -- conditioning on the middle node blocks the flow. Colliders are the rebel. Conditioning on the middle node opens the flow.

## Slide: Chain -- Evidence Flows Along the Path
Training goes to Competency goes to Mortality. *(pause)* If competency is unknown and you learn that mortality is high, that is bad news about competency, which is bad news about training. Evidence flows the whole way along the chain. "High mortality? Probably low competency. Probably inadequate training." *(pause)* But if you already know competency is low? Now learning that mortality is high tells you nothing new about training -- competency already explained everything. The chain is blocked.

## Slide: Fork -- Evidence Flows Through the Common Cause
PPH Detection and Newborn Resuscitation are both driven by Workforce Quality. *(pause)* If quality is unknown and a region is bad at PPH detection, that suggests low workforce quality, which suggests they are probably also bad at newborn resuscitation. Evidence flows through the common cause. *(pause)* But if you already know workforce quality is good? Learning about PPH detection tells you nothing new about resuscitation. The fork is blocked.

## Slide: Collider -- Evidence is BLOCKED by Default
Staffing and Equipment both feed into Neonatal Outcome. *(pause)* Here is what is different from everything we have seen so far. Staffing and equipment are independent decisions. Knowing one tells you nothing about the other. The collider blocks the flow. *(pause)* But if you learn the newborn survived? Now staffing and equipment are connected -- they compete to explain the good outcome. The collider is opened. This is explaining away.

## Slide: Summary -- The Three Rules
Burn these three rules into your memory. *(pause)* Chain: evidence flows unless the middle is known, then it stops. Fork: evidence flows unless the middle is known, then it stops. Collider: evidence is blocked unless the middle is known, then it flows. Chains and forks -- conditioning blocks. Colliders -- conditioning opens. The collider is the rebel.

If you only remember one thing from this section, make it the collider rule. The chain and fork rules feel natural -- most people get them intuitively. But the collider rule is genuinely surprising. The idea that knowing the outcome of two independent causes suddenly creates a connection between them -- that is the engine behind explaining away, which is where we are heading next.

## Slide: The Setup -- A Newborn Survives Against the Odds
Here is the scenario that will stick with you. *(pause)* A health facility in a remote Ethiopian region -- where outcomes are usually poor -- reports that a newborn with respiratory distress survived. This is great news, but surprising. Two things could explain it: amazing staff who performed skilled resuscitation, or great equipment -- a functioning CPAP machine was available. Or maybe both. *(pause)* Look at the diagram. Staffing Quality and Equipment Quality both feed into Newborn Outcome. This is a collider.

## Slide: The Twist
Now the twist. You investigate further and learn that the CPAP machine was broken that day. The equipment was NOT available. *(pause)* Think about what happens to your belief about the staff. Before learning about equipment: "The baby survived. Could be good staff, could be good equipment, could be both." After learning equipment was broken: "The baby survived without equipment?! The staff must have been incredible." *(pause)* This is explaining away. When you rule out one cause of a good outcome, you become even more convinced the other cause must be present. One explanation crowds out the other.

## Slide: Why This Matters So Much
Explaining away is not just a curiosity. It changes how you diagnose problems. *(pause)* Consider the reverse direction. A region has high neonatal mortality. You learn that staffing is actually adequate. What happens to your belief about equipment? It gets worse. If staffing is fine but outcomes are still bad, then equipment must be the problem. Good staffing "explains away" the possibility that staffing caused the bad outcome, leaving equipment as the prime suspect. *(pause)* The management insight: every time you confirm that one potential cause is in good shape, the spotlight shifts more intensely to the remaining causes. Explaining away focuses your attention.

## Slide: Explaining Away -- The Numbers
Let me make it concrete with numbers. *(pause)* Prior beliefs: P(Staff = Skilled) = 40 percent, P(Equipment = Available) = 35 percent. Now we observe the newborn survived. Both estimates go up modestly -- 52 and 47 percent. But now suppose we learn the equipment was broken. P(Staff = Skilled) jumps to 71 percent. *(pause)* Look at the jumps in the table on the slide. Knowing the baby survived raises both estimates modestly. But ruling out one cause makes the remaining cause shoot up dramatically. That is explaining away -- the most powerful diagnostic tool in your toolkit.

## Slide: Everyday Explaining Away
Here are examples you already know. *(pause)* A student got into a top university. Was it grades or athletics? If you learn the student has average grades, you become very confident they are a star athlete. A restaurant is packed. Is the food amazing, or is it the only option nearby? If you learn there are ten other restaurants on the same block, you become more convinced the food must be exceptional. Your internet is slow. Router or provider? You restart the router and it is still slow. Now you are much more sure the problem is the provider. *(pause)* Explaining away happens every time two independent causes compete to explain the same result. It is everywhere once you start looking for it.

## Slide: Ethiopia -- The Context
Let us look at the numbers for Ethiopia. *(pause)* NMR around 28 per 1,000. MMR around 267 per 100,000. About 74 percent antenatal care coverage. Over 38,000 Health Extension Workers across 8-plus regions. But facility delivery is only about 50 percent nationally, with wide regional variation. And skilled birth attendance is about 28 percent, with huge regional gaps. *(pause)* Ethiopia has made remarkable progress through its Health Extension Worker program, but regional variation is enormous -- some regions perform far better than others.

## Slide: The Diagnostic Scenario
Here is the situation. *(pause)* A region in rural Ethiopia reports NMR of 35 per 1,000 -- well above the national average. Despite receiving program resources, mortality has not improved. The program director asks: "What is going wrong?" We will use our Bayesian network to diagnose the problem one piece of evidence at a time. *(pause)* The model has five nodes: HEW Staffing, Equipment, and Referral System as root nodes feeding into Quality of Care, which feeds into NMR.

## Slide: Step 1 -- Start with Priors
Before learning anything about this specific region, our best guesses come from national data. *(pause)* 40 percent of facilities have adequate HEW staffing. 35 percent have functioning essential equipment. Only 30 percent have reliable referral pathways. These priors reflect typical conditions across Ethiopian regions. These numbers come from publicly available HMIS and survey data.

Notice that all three start in rough shape. Most facilities are short-staffed, most lack functioning equipment, and most have weak referral systems. That is the baseline reality in much of rural Ethiopia. The question is not whether things are bad -- we already know that. The question is which specific thing is most likely causing the problem in this particular region.

## Slide: Step 2 -- First Evidence: NMR is High
We observe NMR is high. *(pause)* Using the model, we update all three root causes. Staffing shifts from 60 to 72 percent -- a 12-point jump. Equipment shifts from 65 to 74 percent -- 9 points. Referral shifts from 70 to 78 percent -- 8 points. *(pause)* All three causes shifted toward their bad states. But staffing shifted the most, suggesting it is the strongest suspect. If you can only investigate one thing, start there.

## Slide: Step 3 -- Second Evidence: Equipment is Adequate
A field visit reveals that equipment is actually in decent shape -- CPAP machines are available, essential drugs are stocked. *(pause)* Now we update again, adding this evidence. P(Staffing = Low) jumps from 72 to 81 percent -- another 9-point increase. P(Referral = Weak) jumps from 78 to 84 percent. *(pause)* This is explaining away in action. We ruled out equipment as the problem. But mortality is still high. So our belief that staffing and referrals are causing the problem intensified. Equipment being adequate makes the other causes more suspect, not less.

## Slide: Step 4 -- Third Evidence: Referral System is Functional
Deeper investigation shows the referral system actually works. *(pause)* Now P(Staffing = Low) jumps to 91 percent. We have ruled out equipment and referrals. The model now says there is a 91 percent probability that staffing is the root cause. Each piece of evidence that ruled out an alternative cause made staffing more likely -- classic explaining away. *(pause)* Recommendation: prioritize an HEW staffing review for this region.

## Slide: The Diagnosis Pathway -- Summary
Look at the four-step flow on the slide. *(pause)* Prior: P(Staff Low) = 60 percent. After NMR is high: 72 percent. After equipment is OK: 81 percent. After referral is OK: 91 percent. Each time we ruled out a possible cause, the remaining causes became more suspect. This is explaining away applied sequentially -- a diagnostic workflow. The model did the hard reasoning for us. *(pause)* This is situational analysis. You observe outcomes, gather evidence, and use the model to progressively narrow down the root cause. It is exactly what a good doctor does -- and now you can do it for an entire health system.

## Slide: R Block 1 -- Build the Ethiopian MNH Model
Let us get into the R code. *(pause)* We define a five-node Bayesian network. Three root nodes: Staffing, Equipment, Referral. Quality depends on all three. NMR depends on Quality. The arcs function should show four directed edges. Walk through the model string carefully -- the notation is the same as in Chapter 4.

## Slide: R Block 2 -- Specify the CPTs
Now we attach the lookup tables. *(pause)* Root nodes are straightforward -- just the priors. The Quality CPT has 8 rows because it has three binary parents. The best case gives 92 percent good quality. The worst case gives just 12 percent. The NMR CPT maps quality to mortality: good quality gives 85 percent low NMR, poor quality gives 70 percent high NMR.

## Slide: R Block 3 -- Baseline Query
Our first query: what is the overall P(NMR = High) with no evidence? *(pause)* The cpquery function simulates a million hypothetical regions from the model, then counts how many have NMR = High. The answer should come out around 0.42 -- about a 42 percent chance of high NMR in a random region. That is our starting point before any evidence.

## Slide: R Block 4 -- Running the Model Backwards
Now the detective work. *(pause)* We observe NMR = High and ask: what does this tell us about staffing? The answer should be around 0.72 -- up from the prior of 0.60. We do the same for equipment and referral. Every root cause shifts toward its bad state, with staffing showing the biggest jump.

## Slide: R Block 5 -- Explaining Away in Action
Here is where it gets really good. *(pause)* Query 5: NMR is high AND equipment is OK. What happens to staffing? It jumps to about 0.81. Ruling out equipment made staffing more suspect. Query 6: NMR is high, equipment is OK, AND referral is OK. Staffing jumps to about 0.91. The more causes we rule out, the more certain we become about the remaining cause. This is explaining away -- the crown jewel.

## Slide: R Block 6 -- Comparing Two Regions
Now we compare a struggling region with a well-performing one. *(pause)* The compare_regions function computes posteriors for all root nodes given an NMR observation. For the high-NMR region, all causes shift toward their bad states. For the low-NMR region, all causes shift toward their good states. The shifts go in opposite directions. Same model doing both jobs -- diagnosing problems and identifying what is working well.

## Slide: R Block 7 -- Visualize the Belief Updating
Finally, we visualize the explaining away pathway. *(pause)* A bar chart showing P(Staffing = Low) at each step: prior 60 percent, after NMR high 72 percent, after equipment OK 81 percent, after referral OK 91 percent. When you see the bars climbing step by step, the pattern becomes unmistakable. This is the kind of visualization you would put in a report for a program director.

## Slide: Key Takeaways
Four things to take away. *(pause)* First, marginal probability equals your best guess before you learn anything -- a weighted average. Second, belief updating: new evidence shifts your beliefs, with Bayes' rule doing the heavy lifting. Third, chains and forks let evidence flow, but conditioning on the middle node blocks it. Colliders block evidence by default, but conditioning on the middle opens the flow. Fourth, explaining away is the most powerful diagnostic tool: ruling out one cause makes the remaining causes more likely. *(pause)* And in R, cpquery lets you ask any backward question with a single line of code.

## Slide: Looking Ahead
Next time we tackle a famous trap that will blow your mind. *(pause)* Simpson's Paradox -- where aggregated data literally reverses the true causal effect. An intervention that looks harmful overall but is beneficial in every country. Same data, opposite conclusions. We will see why this happens, how to avoid it, and what it means for comparing MNH programs across Ethiopia, Rwanda, Kenya, and Tanzania. See you next time.
