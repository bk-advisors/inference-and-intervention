# Speaker Notes — Chapter 3: The MNH Diagnostic Case Study

## Overview
Welcome to Chapter 3. This is where we roll up our sleeves and actually *do* this. In Chapter 1 we learned why causal thinking matters. In Chapter 2 we learned the grammar — nodes, arrows, triplets, d-separation. Now we're going to use all of that to solve a real mystery. We'll build a causal model of Kenya's health system from scratch, expanding it through three rounds of interviews with people who work in the system. By the end, the model will basically write our recommendations for us.

## Slide: Learning Objectives
Five objectives today, and notice — every one is about *doing* something, not just understanding a concept. *(pause)* You'll practice the iterative cycle: form a hypothesis, interview someone, revise your model, repeat. You'll learn to tell apart root nodes — the highest-leverage places to intervene — from intermediate nodes that just pass effects along. You'll see why fixing the supply side alone isn't enough without tackling demand-side barriers. And by the end, you'll see how the structure of a well-built model basically does the prioritization for you.

## Slide: Chapter Overview
Look at the flow across the bottom. *(pause)* Five steps: case setup, then three rounds of interviews, then final model and recommendations. This is how real consulting work happens. You don't show up on day one with the answer. You show up with a simple model, go talk to people, and let each conversation tell you what you were missing.

And here's the detective metaphor I want you to keep in mind throughout today. Building a causal model from interviews is like solving a mystery. Each conversation reveals new suspects, new motives, new connections. You don't build a 20-node diagram on day one. You start simple and let the evidence guide you.

## Slide: The Diagnostic Mindset
How do consultants and analysts actually build causal models from real conversations?

## Slide: The Iterative Process
This is the methodological heart of everything we're doing today. *(pause)* Diagnostic causal modeling is an iterative cycle: start with a hypothesis, interview a stakeholder, revise the model, generate sharper questions, and repeat.

The key principle is "start simple." Begin with the most stripped-down model you can draw — maybe three or four nodes. Then talk to someone. Listen for causes, mechanisms, and surprises. Come back and add the new variables their story reveals. The updated model tells you exactly what to ask next. Each round deepens the model and narrows your uncertainty.

Why not just build the big model from the start? *(pause)* Because you don't know what you don't know. The first interview *always* reveals variables you never considered. If you lock in a complex model too early, you'll miss the real story.

## Slide: Key Principles
Four principles for good diagnostic work. *(pause)* First — focus on significant drivers. Not every variable matters equally. Model what matters, leave out the noise. Second — seek common causes. When one variable drives multiple problems simultaneously, that's a gold mine. That's your highest-leverage intervention point. Third — let the model guide your questions. Vague interviews get vague answers. Use your current diagram to generate *specific* hypotheses for the next conversation. Fourth — supply and demand both matter. A health system has two sides. Improving facility quality is wasted if mothers can't reach the facility.

## Slide: The Case Setup
Alright, let's set the stage.

## Slide: The Brief: Why Is Maternal Mortality Still So High?
Here's our case. *(pause)* Kenya — 47 counties with a devolved health system since 2013. Despite a facility delivery rate of roughly 89 percent, the maternal mortality ratio remains around 342 per 100,000, and neonatal mortality sits at about 21 per 1,000.

Look at the numbers in the table. 89 percent of women are delivering in health facilities. That's impressive. But mortality is still high. *(pause)* So here's the central question, and I want you to sit with how strange it is: women are reaching facilities, but outcomes aren't improving fast enough. Why? Something is broken between "getting to the facility" and "surviving."

## Slide: County-Level Variation
One of Kenya's most striking features is how much outcomes vary across its 47 counties. *(pause)* Some counties are doing great — mortality well below the national average, more midwives, functional referral networks. Others — Bungoma, Kakamega, Kilifi — report much higher mortality despite having health facilities in place.

This variation is a clue. *(pause)* If the problem were purely about whether facilities *exist*, every county with facilities would do well. The variation tells us that what happens *inside* the facility — and whether women can reach it *in time* — matters more than whether the building is there.

## Slide: The Initial (Simple) Model
Before we talk to anyone, let's draw the simplest model we can. *(pause)* Four nodes in a chain: Facility Access, plus arrow to Facility Births, plus arrow to Quality of Care, minus arrow to Maternal Mortality.

Round 0: 4 nodes, 3 links. The logic seems reasonable, right? More access leads to more facility births, which means better care, which reduces deaths.

But look at the problems. *(pause)* This treats Quality of Care as a black box — what drives it? It assumes getting women to facilities is enough — but Kenya already has 89 percent facility delivery. And there's no detail on the supply side — no staffing, no equipment, no training. We need to go talk to people who actually work in the system.

## Slide: Interview Round 1: County Health Director
Time for our first interview — the supply-side view.

## Slide: The County Health Director's Perspective
We sit down with a County Health Director from one of Kenya's high-burden counties. *(pause)*

First quote: "We have 14 health facilities that handle deliveries. But only 4 of them have enough midwives for round-the-clock coverage. The rest rely on general nurses who haven't had emergency obstetric training. When a woman comes in with a hemorrhage at 2 AM, sometimes there's nobody on shift who knows how to manage it." *(pause)* That's a staffing problem.

Second quote: "We received the equipment. But we have one midwife for every 15 deliveries per shift. She's exhausted. She can't monitor a CPAP machine, manage a complicated delivery, and attend to three other women at the same time. The equipment sits there." *(pause)* So equipment without enough staff is useless.

Third quote: "We ran a training last year — 60 health workers attended. But the training was two weeks long and follow-up was weak. I'd estimate maybe a third of them are actually applying what they learned." *(pause)* Training happened, but it didn't translate into practice.

## Slide: What We Learned: Round 1
The Director revealed three new variables hiding inside our "Quality of Care" black box. *(pause)* Staffing Levels — the ratio of midwives to deliveries is dangerously low. Equipment Availability — it's physically present but not being used effectively because of staffing constraints. Training Effectiveness — workshops were delivered but only a fraction of workers are actually applying new skills.

Each quote mapped to a new node in our model.

## Slide: Updating the Model: Round 1
New variables: Staffing, Equipment, Training. *(pause)* Now the County Health Budget flows into three channels — Staffing Levels, Equipment Available, and Training Delivered — and all three feed into Quality of Care, which reduces Maternal Mortality.

Round 1: 7 nodes, 6 links. The black box has been cracked open. *(pause)* And here's the key insight: the Director's testimony suggests staffing is the binding constraint. Equipment without staff to operate it is a wasted investment. Training without enough staff to apply it evaporates. Everything keeps pointing back to staffing.

## Slide: What Questions to Ask Next?
Look at what the model tells us to ask. *(pause)* Why is staffing so low — is it a hiring problem, a retention problem, or a deployment problem? Why doesn't training translate into competency — is the training poorly designed, or do trained staff leave? Is the equipment actually functional — the Director said "we have it," but does it work?

Without the model, we'd ask vague questions like "What's going wrong?" With the model, we can ask: "Of the 60 health workers you trained last year, how many are still in your county?" That's a much sharper question. The model guides the next interview.

## Slide: Interview Round 2: Midwife at District Hospital
Round two — let's go see the front-line reality.

## Slide: The Midwife's Reality
We visit a district hospital and interview a senior midwife who's worked there for eight years. *(pause)*

First quote: "When I started, we had six midwives in the maternity ward. Now we're three. Two transferred to Nairobi — better pay, better housing. One went to work for an NGO. We were promised replacements, but the county government hasn't hired anyone in two years." *(pause)* Staff retention is wiping out the workforce.

Second quote: "We received two CPAP machines. One broke after three months — the humidifier cracked. There's no biomedical technician in this county. We submitted a repair request, but spare parts have to come from Nairobi. It's been three months and we're still waiting." *(pause)* Equipment breaks and stays broken because there's nobody to fix it.

Third quote: "We're supposed to refer complicated cases to the county hospital. But the ambulance is shared with four facilities. Sometimes we call and it's already out. Last month a woman waited four hours for transport. She didn't survive." *(pause)* Let that sink in. Four hours.

## Slide: Here's What Surprised Us
The midwife revealed something our Round 1 model completely missed: the transmission problem. *(pause)*

The money went in at the top, but it leaked out — or got stuck. Training was delivered, but trained staff *left* — that's a retention failure. Equipment was procured, but it *broke* and nobody could fix it — that's a maintenance failure. Referral systems were designed, but ambulances weren't available when needed — that's a referral failure.

Three new variables: Staff Retention, Equipment Maintenance, and Referral System. These are the transmission mechanisms between "money spent" and "lives saved," and they're all broken.

## Slide: Updating the Model: Round 2
Round 2: 9 nodes, 10 links. *(pause)* Staff Retention now sits between staffing levels and actual competency on the ground. Equipment Maintenance sits between equipment procured and equipment actually working. The Referral System is an independent pathway to mortality.

The model is getting richer, and a critical pattern is emerging.

## Slide: Spotting the Common Causes
Here's the discovery that changes everything. *(pause)* Staff Retention is a fork — a common cause. When trained midwives leave, *both* clinical competency drops *and* equipment goes unused because nobody remaining knows how to operate it. Two symptoms, one root cause.

Equipment Maintenance is also a fork. When there's no biomedical technician, *all* equipment degrades — not just one machine. A single maintenance failure ripples through multiple care pathways.

Why does this matter? *(pause)* Common causes are the highest-leverage intervention points in any system. Fixing retention alone could improve both competency *and* utilization at the same time. That's two results for one intervention.

## Slide: Interview Round 3: Community Health Worker
Round three opens up an entirely new dimension.

## Slide: We'd Been Looking at Half the Picture
Two rounds of interviews focused entirely on the supply side — what happens inside health facilities. A community health worker based in a rural sub-county opens our eyes to a completely different set of barriers. *(pause)*

First quote: "The nearest facility that handles deliveries is 18 kilometers away. There's no paved road. During the rainy season, a motorcycle ride takes two hours — if you can find a motorcycle. Some women start walking when labor begins, but labor doesn't wait for the road to improve." *(pause)* Geographic access.

Second quote: "The delivery is free, yes. But the motorcycle costs 500 shillings. You need to bring your own basin, your own razor blade, your own cotton wool. For a family earning 200 shillings a day, that's a week's income. Some women just stay home." *(pause)* Financial barriers, even when the service itself is free.

Third quote: "Some older women in the community tell young mothers that hospitals are dangerous. And some women say they were shouted at by nurses during their last delivery. They'd rather deliver at home with a traditional birth attendant who treats them with respect." *(pause)* Trust and past experience shape whether women choose facility care at all.

## Slide: The Demand-Side Revelation
We'd been looking at half the picture. *(pause)* Kenya's 89 percent facility delivery rate is a national average. In rural sub-counties of high-burden counties, it drops to 50 or 60 percent. And even women who do reach a facility may arrive too late because of transport delays.

Three new demand-side variables: Geographic Access — can she physically get there? Financial Barriers — can her family afford the trip? Health-Seeking Behavior — does she trust the facility enough to go?

## Slide: Updating the Model: Round 3
The model now has two distinct halves that converge on the outcome. *(pause)* On the supply side from Rounds 1 and 2: Budget flows through staffing, equipment, and training, but gets undermined by retention failures and equipment breakdowns at the transmission layer. On the demand side from Round 3: geographic access, financial barriers, and health-seeking behavior determine whether women reach facilities at all.

Here's the structural insight: Quality of Care and Facility Births are both parents of Maternal Mortality. Improving quality without improving access doesn't help the women who never arrive. Improving access without improving quality sends more women into facilities that can't save them. *(pause)* Both halves must move together.

## Slide: The Complete Causal Model
Round 3: 12 nodes. *(pause)* Look at it. Supply side on the left, demand side on the right, and they converge on Maternal Mortality at the bottom. Every single arrow tells a part of the story. This is the complete diagnostic picture, built one interview at a time.

## Slide: Model Evolution Summary
Let's see how our understanding grew round by round.

## Slide: Evolution of the Model
Look at the table. *(pause)* Round 0 — nobody talked to, 4 nodes, just the basic chain. Round 1 — County Health Director, 7 nodes, added staffing, equipment, training. Round 2 — Senior Midwife, 9 nodes, added retention, maintenance, referral system. Round 3 — Community Health Worker, 12 nodes, added geographic access, financial barriers, health-seeking behavior.

Each round roughly doubled the model's explanatory power. *(pause)* And notice who taught us what. The Director saw the system from the top. The midwife saw it from the front line. The community health worker saw it from the community. Each perspective revealed variables the others couldn't see. This is why you need multiple stakeholders. No single person has the full picture.

## Slide: Prioritizing Recommendations
Now here's the payoff. The model doesn't just diagnose problems — it tells you where to fix them first.

## Slide: Using Model Structure to Prioritize
How do we decide where to intervene? We could go with gut instinct, but the model gives us a more disciplined answer. *(pause)*

A root node is a node with no parents — nothing in the diagram causes it. Root nodes are the ultimate causes. Intervening on them has the broadest downstream effects because every pathway flows *from* them. The principle: count the downstream paths from each node to the outcome. Nodes with more paths are higher-leverage.

## Slide: The Priority Ranking
Highest priority — root causes with multiple downstream effects. *(pause)*

Number one: Staff Retention. Root cause affecting *both* competency and equipment utilization. Every midwife who leaves takes her training, her experience, and her equipment skills with her. Invest in housing allowances, career development, rural service incentives.

Number two: Equipment Maintenance. Root cause affecting all equipment pathways. Deploy county-level biomedical technicians and establish spare parts supply chains. Equipment without maintenance is a wasted investment — it breaks, and it stays broken. *(pause)*

Number three: Geographic Access and Referral System. Independent pathway to mortality. Women who can't reach a facility in time die regardless of facility quality. Ambulance networks, maternity waiting homes.

Number four: Demand-side barriers. Financial barriers and health-seeking behavior. Transport subsidies, respectful care training, community health worker engagement.

Notice how the prioritization follows directly from the DAG structure. We didn't guess. The model told us: intervene where the most downstream paths originate.

## Slide: Why Root Nodes Are Highest-Leverage
Let me show you why root nodes matter so much. *(pause)* Staff Retention is a root node — nothing in our model causes it. But it has at least three downstream effects: Retention affects Competency, which affects Quality, which affects Mortality. Retention affects Equipment Utilization, which affects Quality, which affects Mortality. Retention affects staffing ratios, which affects Quality, which affects Mortality.

Fix retention, and you improve three pathways at once. Fix training alone — a non-root node — and trained staff still leave, so the effect evaporates. *(pause)* The model does the prioritization for you. Count the downstream paths. The variables with the most connections to the outcome are the ones to invest in first.

## Slide: MNH Application: The Full Kenya DAG
The completed diagnostic model.

## Slide: The Full Kenya MNH Causal Model
Look at the summary table. *(pause)* Inputs — budget, staffing, equipment, training — are funded and delivered. Check. But the transmission layer — retention, maintenance, referral system — is broken. The demand side — geographic access, financial barriers, health-seeking behavior — was underestimated and missed until Round 3. Outcomes — quality, facility births, maternal mortality — are below target.

The program invested in the right inputs. But it missed the transmission mechanisms and the demand-side barriers. *(pause)* Redirecting even a modest portion of the budget toward these neglected nodes could unblock the entire system. The money went in at the top, but it leaked out before it could reach the people it was meant to help.

## Slide: R Workshop: Building the DAG Iteratively
Let's move to R and formalize each interview round.

## Slide: R: Round 1 — The Simple Supply-Side Model
Here we build the 7-node model from Round 1 in dagitty. *(pause)* Budget flows into Staffing, Equipment, and Training. Those feed into Quality, and Quality drives Mortality. Run this code and you'll get a clean picture of the supply-side model the County Health Director helped us build.

## Slide: R: Round 2 — Adding Transmission Failures
Now we expand to capture what the midwife revealed. *(pause)* Retention feeds into both Competency and Utilization — that's the fork structure, the common cause. Maintenance feeds into Utilization. Referral feeds into Quality. The common-cause structures are now formally encoded in the DAG. Trace the paths and you'll see how retention failures ripple through multiple channels.

## Slide: R: Round 3 — The Complete Model
Here's the full model with all the demand-side variables from Round 3. *(pause)* Geographic Access, Financial Barriers, and Health-Seeking Behavior all flow into Facility Births. Quality and Facility Births both flow into Mortality. This is the complete diagnostic framework. Take a moment to trace paths from Budget all the way to Mortality — there are multiple routes, and each one tells a different part of the story.

## Slide: R: Analyzing the Complete Model
Three powerful functions. *(pause)* adjustmentSets tells us which variables we *must* measure to evaluate the program's causal effect. impliedConditionalIndependencies generates testable predictions — when data arrives, we can check each one, and if the data disagrees, our model needs revision. And paths shows every route from Budget to Mortality.

The d-separation test at the bottom — is Retention independent of Maintenance? — checks whether we might be missing a hidden common cause. If the data says they're related and our model says they should be independent, we know where to look for what we missed.

## Slide: Key Takeaways
Four things to take away. *(pause)* Build models iteratively. Start with 3 or 4 nodes and let stakeholder interviews reveal what's missing. You can't build the right model from a desk — you have to talk to people.

Root nodes are leverage points. Staff Retention and Equipment Maintenance emerged as the critical bottlenecks that initial investment plans overlooked. They have the most downstream effects.

Supply and demand both matter. Kenya's 89 percent facility delivery rate masks huge variation. Demand-side barriers are invisible from the supply side.

The model does the prioritization. You don't need to guess which interventions matter most. The structure of the diagram tells you: intervene where the most downstream paths originate.

## Slide: Looking Ahead
Next chapter, we add numbers to these models. *(pause)* Conditional probability tables replace the plus and minus signs with actual probabilities. Bayes' rule lets us update our beliefs when new evidence arrives. We'll compute the probability that mortality is high given specific combinations of supply and demand conditions. The qualitative model tells you *what* affects what. The quantitative model tells you *by how much*. And that's what we need to make real budget allocation decisions. See you in Chapter 4.
