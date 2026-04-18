# Speaker Notes — Chapter 1: Introduction to Causal Analysis

## Overview
Welcome, everyone. Today I'm going to show you a puzzle that should genuinely bother you — and then we're going to learn the thinking tools to solve it. The big idea is simple: if you want to make smart decisions about where to put scarce resources, you need to know what actually *causes* what, not just what happens to show up alongside what. By the end of this session, you'll never look at a graph or a statistic the same way again.

## Slide: Learning Objectives
Here are five things I want you to walk away with today. *(pause)* First, we'll learn to tell apart two jobs every decision-maker has — figuring out what's going on, and deciding what to do about it. Then we'll work through real examples from Ethiopia that show why "correlation is not causation" isn't just a bumper sticker — getting it wrong can lead to exactly the wrong decision. We'll name the three classic traps that fool people, introduce the basic pieces of a causal model — nodes, arrows, and DAGs — and by the end you'll see why all of this matters when real lives are on the line.

## Slide: Chapter Overview
Think of this as today's roadmap. We're going from "What does a manager actually do?" all the way to "Here's a diagram that can keep you from making a terrible mistake." *(pause)* See the five steps up there? Assessment, Intervention, Correlation traps, Causal framework, and then a real application in Ethiopia. And look at the big idea at the bottom — when resources are scarce, and they always are, you need to know what causes what before you decide what to do. That's the thread running through everything today.

## Slide: Situational Assessment
Alright, let's jump in with the first big idea.

## Slide: Here's the Puzzle
Here's a puzzle that should make you uncomfortable. *(pause)* Ethiopia has one of the biggest community health worker programs in Africa — over 40,000 Health Extension Workers spread across the country. That's amazing. But here's the strange part: the regions where the *most* health workers are deployed tend to have the *highest* mortality rates. *(pause)* So... does deploying health workers cause deaths? Obviously not. But if you just looked at the numbers — workers deployed versus mortality rates — that's exactly what the data would seem to say. *(pause)* This is the kind of puzzle that causal thinking solves. The data isn't lying. But it's not telling the whole story, either. Stick with me, and by the end of this chapter you'll be able to explain exactly what's going on here.

## Slide: The Manager's Two Questions
This is the foundation of the whole course. Every decision-maker faces exactly two questions. *(pause)* Look at the two boxes. On the left: "What is happening?" That's what we call situational assessment — it's detective work. On the right: "What should I do about it?" That's intervention — choosing which levers to pull.

Here's the key insight, and I want you to really let this sink in: you cannot answer Question 2 well until you've answered Question 1 well. Acting without understanding causes is like a doctor prescribing medicine without a diagnosis. You might get lucky, or you might make things worse.

## Slide: What Is Situational Assessment?
So what does this detective work actually look like? *(pause)* Think about a doctor examining a patient — what symptoms are there, and what do they point to? Or a mechanic diagnosing a car — the engine's overheating, but is it the coolant, the fan, or a cracked gasket? Same thing with a health program manager in Ethiopia asking, "Why isn't neonatal mortality falling in this region — is it a staffing problem, a supply chain problem, or something else entirely?"

In every case, the person is trying to figure out what's causing what before deciding how to act. Causal models give us a systematic way to do that, instead of just guessing.

## Slide: Ethiopia's Health Challenge: The Numbers
Let me show you the situation Ethiopia faces. *(pause)* Look at these numbers. Maternal mortality is about 267 per 100,000 live births. Neonatal mortality is about 28 per 1,000. They've got over 40,000 Health Extension Workers deployed. About 74 percent of pregnant women get at least one check-up visit.

Now, here's the thing — Ethiopia has made *enormous* progress. Maternal mortality used to be over 1,000 per 100,000 back in the 1990s. So they've come a really long way. But there's still far to go, and figuring out where to invest next depends on understanding what's *causing* the remaining deaths.

## Slide: Managerial Intervention
Okay, let's move to the second big question — what should I actually do?

## Slide: Managers Manage Scarce Resources
Here's a point that sounds obvious but has huge consequences. *(pause)* Resources are always limited. Money, time, people, equipment — you never have enough of everything. That means every investment involves trade-offs. Every dollar you spend on training midwives is a dollar you didn't spend on buying equipment. Every month you spend building a data system is a month you're not spending on direct care.

So which investments will actually *cause* the biggest drop in mortality? If you don't know the answer to that causal question, you're basically guessing.

## Slide: The Trade-Off
Look at these three options. *(pause)* Option A: invest in People — train 5,000 more midwives. Option B: invest in Products — buy CPAP machines and emergency kits for every district hospital. Option C: invest in Systems — build a real-time data dashboard and a referral transport network.

All three sound reasonable, right? But you can't do all three equally well. So which one will *cause* the greatest reduction in mortality? *(pause)* That's a causal question, and you can't answer it just by looking at a spreadsheet full of correlations.

## Slide: Why You Need Causal Thinking to Decide
Here's what happens when you skip the causal reasoning and just look at the data. *(pause)* You might see that regions with the most equipment have the lowest mortality. So you say, "Buy more equipment!" But wait — those regions are also the wealthiest and most urban. They'd have had lower mortality anyway. The equipment isn't causing the low mortality. Wealth is causing both.

That's huge. Let that sink in. *(pause)* Without causal thinking, data can lead you to exactly the wrong decision.

## Slide: Correlation ≠ Causation
Now let's dig into *why* correlations mislead us. There are three specific traps, and we're going to name each one.

## Slide: The Ice Cream Problem
Before we get back to health data, here's a classic example everyone can relate to. *(pause)* On days when ice cream sales are high, drowning deaths are also high. So... does ice cream cause drowning? *(pause)* Of course not. Hot weather causes both. People eat more ice cream in summer, and people swim more in summer. Summer heat is the hidden third variable connecting both.

This hidden-third-variable problem has a name: confounding. And it's just one of three traps that make people confuse correlation with causation.

## Slide: Trap 1: Confounding
Confounding happens when a third variable influences both the supposed cause and the supposed effect. *(pause)* Remember our Ethiopia puzzle? Regions with more Health Extension Workers have higher mortality. Does that mean health workers cause deaths? No — more workers get deployed to the sickest regions. Disease burden is the confounder. It drives both where workers go *and* where mortality is high.

Look at the diagram. See how Disease Burden sends arrows to both Health Worker Deployment and Neonatal Mortality? That shared cause creates a correlation between workers and mortality, even though workers actually *help*. Same data, totally misleading conclusion — unless you think causally.

## Slide: Trap 2: Reverse Causation
Second trap. *(pause)* Countries that receive more international health funding tend to have higher mortality rates. So does foreign aid increase mortality? *(pause)* No. High mortality *attracts* funding. Donors send money to the countries with the worst outcomes. The causal arrow runs from mortality to funding, not the other way around.

Think of it this way: seeing more firefighters at bigger fires doesn't mean firefighters cause fires. They're *responding* to them. Same logic.

## Slide: Trap 3: Selection Bias
Third trap, and this one is sneaky. *(pause)* Imagine you look at data from hospitals that report to Ethiopia's health information system. Among those hospitals, CPAP machines don't seem related to survival. So equipment doesn't matter, right?

Not so fast. Only well-resourced hospitals report data consistently. The hospitals where CPAP machines would make the *biggest* difference — small, under-resourced facilities — are missing from the data entirely. You're drawing conclusions from a biased sample. The danger? You might conclude equipment doesn't matter, when actually it matters enormously for the facilities you can't see.

## Slide: Three Traps: Summary
Let's pull it together. Look at the summary table. *(pause)* Confounding — a hidden third variable. Reverse causation — the arrow points the wrong way. Selection bias — your data sample isn't representative. All three create patterns that look like real causal effects but aren't.

The antidote? Explicit causal modeling — drawing a picture of what causes what *before* you analyze the data. And that's exactly what we're building next.

## Slide: The Causal Model Framework
Alright, now here's where it gets really interesting.

## Slide: What Is a Causal Model?
Think of a causal model as just a diagram that shows what causes what. *(pause)* It has three simple ingredients. Nodes — the things you care about, drawn as shapes. Arrows — causal links from one thing to another. And signs — plus or minus — telling you which direction the effect goes.

Here's the one rule I want you to remember: an arrow from A to B means that *changing* A can change B. But changing B does not change A. Arrows have a direction, and the direction matters.

## Slide: What Is a DAG?
DAG stands for Directed Acyclic Graph. *(pause)* "Directed" means arrows have a direction. "Acyclic" means no loops — you can never follow the arrows from any node back to itself. "Graph" is just the math word for a diagram of connected things.

Look at the two examples. The valid DAG goes A to B to C — you can follow the arrows forward but never get back to where you started. The invalid one goes A to B to C and back to A — that's a loop, and it breaks the whole thing. *(pause)* Why does this matter? Because loops make it impossible to figure out what causes what — everything causes everything. DAGs force you to be clear about direction.

## Slide: A Simple 3-Node Chain
Here's the simplest useful causal model for a health program. *(pause)* Investment goes to Coverage, and Coverage goes to Mortality. More investment increases coverage — that's the plus sign. Higher coverage reduces mortality — that's the minus sign.

Notice that Investment doesn't directly reduce mortality. It works *through* coverage. That's what we call a chain. And it already tells us something useful: if investment goes up but coverage does *not* go up, the money is being wasted somewhere in between. The chain helps you find where things break down.

## Slide: But Wait — It Is Not That Simple
Obviously, three nodes is too simple. What about confounders like disease burden? What about multiple pathways — investment might improve training, equipment, *and* data systems, each affecting mortality differently? What about quality of care?

That's what the rest of the course is about. *(pause)* In Chapter 2, we'll learn the formal rules for building these diagrams. In later chapters, we'll add numbers and use the models to make actual decisions. For now, just make sure you've got the basic building blocks: nodes, arrows, and direction.

## Slide: Preview: A Richer Model
Here's a taste of where we're headed. *(pause)* Look at this diagram. Investment on the left flows through three channels — Workforce Training, Equipment Supply, and Data Systems. Those all feed into Quality of Care, which then drives Mortality Reduction.

Investment is a decision node — that's the rectangle, meaning we control it. What's missing? Confounders. We'll add those in Chapter 2. But even this preview shows you how much richer the picture gets when you think in terms of multiple pathways.

## Slide: MNH Application: Ethiopia
Now let's apply all of this to a real health system.

## Slide: Ethiopia's Three-Pillar Approach
Ethiopia's Health Extension Program has invested across three pillars. *(pause)* People — over 40,000 Health Extension Workers. Products — essential medicines, equipment, supplies. Systems — data tracking, referral networks, supervision.

Here's the causal question: how do these three pillars combine to produce better outcomes? Think of it this way: a trained midwife without emergency equipment can't stop a hemorrhage. Emergency equipment without a trained midwife is just a box on a shelf. And neither one helps if the mother can't get to the facility. People, Products, and Systems are complements — they multiply each other's effect.

## Slide: Ethiopia's Causal Chain
Look at the diagram. All three pillars flow into Quality of Care. Quality then reduces both Maternal Mortality and Neonatal Mortality. *(pause)* Notice that Quality is the bottleneck — the place where everything converges. If quality is poor, no amount of spending on any single pillar will fix the outcomes. Everything has to come together at that node.

## Slide: Why the Numbers Mislead
Now let's go back to our opening puzzle. *(pause)* If you looked at raw data across Ethiopia's regions, you'd see that regions with the most Health Extension Workers also have the highest mortality. A naive analyst might say, "These investments aren't working!"

But here's what the causal model reveals: the regions with the highest disease burden receive the most resources *because* they have the worst outcomes. Confounding by disease burden creates a positive correlation between resources and mortality, even when resources are saving lives. *(pause)* This is exactly Trap 1 in action. Same data, different conclusion — because we thought causally.

## Slide: ANC Coverage: A Closer Look
Ethiopia's antenatal care coverage shows how much progress has been made and how far there is to go. *(pause)* About 74 percent of pregnant women get at least one visit, but only about 43 percent complete the recommended four visits. Urban coverage is much higher than rural coverage — yet another confounder.

Here's the causal chain: ANC visits lead to early detection of complications, which leads to timely referral, which leads to skilled treatment, which leads to survival. Every link has to work. If *any* one link breaks — a missed visit, a failed referral, an absent midwife, a missing drug — the outcome can be death. *(pause)* That's why causal models matter for real decisions. A naive analysis might say "check-ups don't help" if coverage goes up but deaths stay constant. A causal model asks: where in the chain is it breaking?

## Slide: R Workshop: Your First Causal Diagrams
Alright, now let's get our hands on some code.

## Slide: Setting Up the R Environment
First things first — we need to load our tools. Three packages: dagitty for defining and analyzing causal diagrams, ggdag for drawing pictures of those diagrams, and ggplot2 which powers the visuals behind the scenes. *(pause)* If you haven't installed them yet, uncomment that first line and run it. These three packages are going to be our toolkit throughout the whole course, so make sure they're working.

## Slide: R: Drawing Our Simple 3-Node Chain
Let's build our first diagram in code. *(pause)* Look at the dagitty syntax — it's pretty straightforward. We define three nodes: Investment, Coverage, and Mortality. We set their positions so they lay out in a nice row. Then we draw the arrows: Investment causes Coverage, Coverage causes Mortality. That's our three-node chain from earlier, except now it's in R where we can actually analyze it. The ggdag call at the bottom turns it into a picture. Notice the arrows only go left to right — that direction matters.

## Slide: R: Adding a Confounder
Now let's add Disease Burden as a confounder. *(pause)* This is the hidden variable that was creating the misleading correlation between health workers and mortality. Look at the code — Disease Burden sits at the top and sends arrows down to *both* Health Workers and Mortality. That's the fork structure — the classic confounding pattern we talked about. We use color coding to make it pop: green for the thing we think is the cause, red for the outcome, amber for the confounder.

## Slide: R: What Do We Need to Control For?
Here's the powerful part. *(pause)* Once we've drawn the diagram, R can tell us *exactly* which variables we need to control for. We call adjustmentSets, and it returns: Disease Burden. That's it. Control for disease burden, and the confounding goes away.

In plain English? If you compare regions that have the *same* disease burden, the regions with more health workers will have *lower* mortality. *(pause)* This is the whole point of the course in one slide. Draw the diagram. Ask R what to control for. Analyze correctly. Make better decisions.

## Slide: R: Ethiopia's Three-Pillar Model
Now let's build the richer model with all three pillars — People, Products, and Systems — plus Disease Burden as a confounder. *(pause)* Look at how the code defines each node and each arrow. All three pillars flow into Quality. Quality reduces both NMR and MMR. Disease Burden affects outcomes directly. Run this code, look at the picture, and trace the pathways from any starting point to any outcome. This is how investment translates into results.

## Slide: R: Finding All the Paths
We can ask R to show us every causal pathway from a starting point to an endpoint. *(pause)* The paths function shows all the routes from People to NMR — every different way that a workforce investment could affect mortality. And adjustmentSets tells us what we'd need to control for to isolate that effect. Try modifying the code to look at paths from Systems to MMR instead. How many routes are there? What do you need to control for?

## Slide: Key Takeaways
Let's wrap up with the big ideas. *(pause)* Causal thinking starts with two questions: "What is happening?" and "What should I do?" You can't answer the second without the first. Correlation does not equal causation — confounding, reverse causation, and selection bias all create misleading patterns. A causal model makes your assumptions visible, testable, and actionable. It tells you what to control for, where the chain breaks, and which interventions will actually work.

And Ethiopia's 40,000 Health Extension Workers are not causing deaths. Disease burden is confounding the relationship. Causal models help us see through the numbers to the truth.

## Slide: Looking Ahead
Next time, we learn the formal grammar of causal diagrams. *(pause)* Three types of nodes, signed links, and the three fundamental structures — chains, forks, and colliders. Colliders are the most surprising one, and they trip up even experienced analysts. That's where we go from "causal thinking is important" to "here's exactly how to do it." See you in Chapter 2.
