# Speaker Notes — Chapter 2: Qualitative Causal Models

## Overview
Welcome back. Today is our grammar lesson for causal thinking. Last time we learned *why* causal models matter — the correlation traps, the confounding, the danger of acting on misleading data. Now we're going to learn *how* to actually build one. The payoff is three simple patterns — chain, fork, and collider — that control how information flows through any causal diagram, no matter how big. Memorize those three patterns and you can reason about anything. We'll finish by building a complete model of Rwanda's health system together.

## Slide: Learning Objectives
Five objectives today, and they build like a staircase. *(pause)* First, we learn the three main types of nodes — the building blocks. Then we learn how to connect them with signed links — plus and minus. Then we get to the heart of it: the three fundamental triplet structures. From there, we learn the formal rule called d-separation — when does information flow, and when does it stop? And finally, we put it all together and build a complete DAG for Rwanda's maternal and newborn health system. *(pause)* Each piece is simple on its own. The power comes from combining them.

## Slide: Chapter Overview
Look at the five-step flow across the top. We go from mental models to formal DAGs, then node types and links, then the three triplets, then information flow rules, and finally the Rwanda application. *(pause)* Here's where we are in the course: Chapter 1 showed us *why* causal thinking matters. Now we learn *how* to draw a causal model. By the end of today, you'll have a complete diagram of Rwanda's health system on paper and in R.

## Slide: From Intuition to Structure
Let's talk about why writing down your causal beliefs changes everything.

## Slide: Everyone Has a Mental Model
You already carry causal beliefs around in your head. *(pause)* "If we train more community health workers, outcomes will improve." "Insurance coverage drives facility delivery rates." "Better equipment leads to better care." Those are all causal claims. The problem? They live in your head, where nobody can challenge them.

Think about it — everyone has a mental model. The question is whether yours is written down where others can see it, poke holes in it, and help you improve it.

## Slide: Implicit vs. Explicit Models
Look at the two columns. *(pause)* On the left — implicit models, the ones stuck in your head. They're vague and shifting. Assumptions are hidden. Two people can disagree without even knowing *why* they disagree. You can't test them against data.

On the right — explicit models on paper. Precise and shareable. Assumptions are out in the open. Disagreements become *productive* because you can point to the exact arrow you disagree about. And they generate testable predictions. *(pause)* A qualitative causal model is just a disciplined way of writing down what you believe about how things connect — before you add any numbers. That's all it is. Let's learn how.

## Slide: The Model-Building Process
Five steps, every time. *(pause)* List your variables. Classify your node types. Draw your arrows. Assign your signs. Check the structure.

Here's an everyday example to make it click. A school principal says: "I think class size affects teacher attention, and teacher attention affects test scores." That one sentence *is* a causal model: Class Size, arrow with a minus sign to Teacher Attention, arrow with a plus sign to Test Scores. We just gave it structure. *(pause)* The rest of this chapter teaches you the formal rules for each step.

## Slide: Three Node Types
The building blocks of every causal diagram.

## Slide: Probabilistic Nodes (Ovals)
Probabilistic nodes are the things the world throws at you — variables whose values are uncertain. You observe them, but you don't directly control them. Drawn as ovals. *(pause)* Everyday examples: tomorrow's weather, a student's exam score, traffic on your drive to school. In our health context: Quality of Care — is it good or poor? Care-Seeking Behavior — high or low? Workforce Competency — competent or still developing?

These are the variables where you have to deal with uncertainty. Nature decides, not you.

## Slide: Decision Nodes (Rectangles)
Decision nodes are the levers you can pull — variables you *choose*. Drawn as rectangles. *(pause)* Everyday: which university to apply to, how much to spend on advertising, whether to study tonight or watch TV. In our health context: how much to invest in community health worker training, whether to buy more equipment, whether to expand Rwanda's Mutuelle insurance program.

These are the handles you can grab. The choices are yours.

## Slide: Objective Nodes (Hexagons)
Objective nodes are the scoreboard — what you're ultimately trying to achieve. Drawn as hexagons. Arrows flow *into* objective nodes but never *out*. *(pause)* Everyday: your final GPA, a company's annual profit, a team's win-loss record. In our context: Neonatal Mortality and Maternal Mortality.

Nobody "controls" the objective directly. It's the result of everything upstream. It just sits at the end and collects the effects of all your decisions and all the uncertainty.

## Slide: Node Types: Quick Reference
Here's the cheat sheet. *(pause)* Probabilistic — ovals — uncertain things nature determines. Decision — rectangles — choices you make. Objective — hexagons — goals you're trying to achieve. There's also a fourth type — function nodes — for variables that are calculated exactly from their parents, like "Total Spending equals Training plus Equipment plus Systems." We won't focus on those, but just know they exist for accounting-type formulas.

## Slide: Signed Links
Arrows that tell you which direction things move.

## Slide: How Links Work
An arrow from A to B means changing A can change B. The sign tells you the direction. *(pause)* Plus means more A leads to more B — "A pushes B up." Minus means more A leads to less B — "A pushes B down."

Look at the diagram. CHW Training Investment, plus arrow to Workforce Competency, minus arrow to Neonatal Mortality. Read it out loud: "Training investment *increases* workforce competency, and higher competency *decreases* neonatal mortality." *(pause)* Two arrows and two signs, and we've already captured a meaningful causal story.

## Slide: Sign Multiplication Along Paths
Here's a trick that makes everything easier. When you follow a path through multiple arrows, you multiply the signs — just like multiplying positive and negative numbers. *(pause)* Plus times plus equals plus. Minus times minus equals plus. Plus times minus equals minus.

Look at the examples. Training to Competency to Mortality: plus times minus equals minus overall. Training reduces mortality. Makes sense, right? And the everyday example: Rain increases wet roads — that's plus. Wet roads increase accidents — that's plus. Overall: plus times plus equals plus. Rain increases accidents. *(pause)* Simple rule, but incredibly useful when you're tracing effects through a big diagram.

## Slide: The Three Triplets
Every causal diagram is built from just three patterns. This is the most important part of the whole chapter. Learn these three and you understand every DAG.

## Slide: Why Three Triplets Matter
Look at the table. *(pause)* Number one: the Chain — A causes B, B causes C. B is a mediator, passing information along. Number two: the Fork — B causes both A and C. B is a common cause. Number three: the Collider — A and C both cause B. B is a collision point.

Each one has its own rule about when information flows and when it stops. Get these rules wrong and your entire analysis falls apart. *(pause)* So let's go through them one at a time. Pay close attention. I'm going to ask you to burn this into your memory.

## Slide: Triplet 1: The Chain
A causes B, B causes C. B sits in the middle, passing information from A to C. *(pause)* The everyday example: Rain causes Wet Roads, Wet Roads cause Car Accidents. If you already know the roads are wet, does learning it rained tell you anything *new* about accident risk? No. The road condition already captured everything rain had to say.

Here's the rule: information flows from A to C through B. But if you hold B fixed — if you already know B's value — the flow stops. Think of it like a water pipe. Water flows from the faucet through the pipe to the bucket. Close the valve in the middle? Nothing gets through.

## Slide: Chain: MNH Example
Look at the health example. *(pause)* CHW Training Investment, plus arrow to Workforce Competency, minus arrow to Neonatal Mortality.

Left side, the green box — we're *not* holding competency fixed. Training and mortality are connected. Knowing a district invested in training, you'd predict lower mortality. Information flows through the chain.

Right side, the orange box — we *are* holding competency fixed. If we already know a health worker is competent, it doesn't matter *how* she became competent — training, years of experience, natural talent. The training information is blocked by the competency information. *(pause)* For Rwanda, this means training's value is entirely mediated through competency. Competency is what actually matters at the end of the day.

## Slide: Triplet 2: The Fork
A gets an arrow from B, and C gets an arrow from B. B is in the middle, causing both A and C. *(pause)* Here's our old friend the ice cream example. Ice Cream Sales and Drowning Deaths are both caused by Summer Heat. They look correlated, but neither one causes the other. Summer heat is the common cause hiding in the background.

The rule works just like the chain: A and C look associated, but only because of B. Hold B fixed — control for temperature — and the link between ice cream and drowning vanishes.

## Slide: Fork: MNH Example
Now the health version. *(pause)* CHW Deployment and Neonatal Mortality are both driven by Disease Burden. The naive observation says districts with more CHWs have higher mortality — health workers cause harm? Of course not. Disease burden is the common cause. High-burden districts get more workers *and* have higher mortality.

Control for disease burden, and the spurious link disappears. *(pause)* For Rwanda, across its 30 districts, the Ministry of Health deploys more CHWs to higher-burden areas. Any comparison of CHW numbers versus mortality *must* control for baseline disease burden, or you'll get the wrong answer.

## Slide: Triplet 3: The Collider
Okay, here's where it gets counterintuitive. Pay very close attention, because this one behaves *opposite* to everything we just learned. *(pause)*

A causes B, and C also causes B. Two arrows collide at B. That's why it's called a collider.

The everyday example: High Grades and Athletic Talent both help you get into a selective university. Among the general population, grades and athletic ability are unrelated. But among *admitted students* — if you know someone got in and they're not a great athlete — they must be an academic star. One cause "explains away" the other.

## Slide: Collider: MNH Example
Staffing Level and Equipment Availability both contribute to Quality of Care. Quality is the collider. *(pause)*

Left side, the green box — not looking at quality. Staffing and equipment are independent — separate decisions, no connection.

Right side, the red box — among facilities with *good* quality. If staffing is low at a good-quality facility, equipment must be excellent. The two causes "explain away" each other. *(pause)* This creates a fake negative relationship between staffing and equipment that doesn't actually exist. That's collider bias, and it trips up even experienced researchers.

## Slide: Information Flow Rules
d-Separation: when does information flow, and when does it stop?

## Slide: The Three Rules
Burn this into your memory. I'm serious. This is the single most important table in the entire course. *(pause)*

Chain: A to B to C. Default? Information flows. Condition on the middle? Blocked. Fork: A from B, C from B. Default? Flows. Condition on the middle? Blocked. Collider: A to B, C to B. Default? Blocked. Condition on the middle? Flows.

*(pause)* See the pattern? Chains and forks behave the same — conditioning on the middle blocks the flow. The collider is the rebel — conditioning on the middle *opens* the flow. The collider flips the rule. Everything else is the same; the collider is the odd one out.

The fancy name for these rules is d-separation — the "d" stands for directional. If every path between two variables is blocked, they're d-separated, and knowing one tells you nothing about the other.

## Slide: Applying d-Separation
In real diagrams, two variables might be connected by multiple paths. You have to check every path. *(pause)* The rule is: walk along each path. At each node, ask — is this a chain or fork middle, or a collider? Chain or fork middle that you're conditioning on? Blocked. Collider that you're *not* conditioning on? Blocked. One blocked node is enough to block the whole path.

If *all* paths between two variables are blocked, they're independent. Even one open path means information can still flow.

## Slide: d-Separation: Worked Example
Let's work through this together. *(pause)* Look at the diagram. Training flows to Quality, Quality flows to Mortality. Equipment also flows into Quality from below.

First question: is Training independent of Mortality given Quality? The path is Training to Quality to Mortality. That's a chain, and Quality is in our conditioning set. Chain with the middle conditioned on — blocked. Yes, d-separated.

Second question: is Training independent of Equipment given Quality? The path goes Training to Quality and Equipment to Quality. Quality is a collider here — two arrows point into it. And it's in our conditioning set. Collider conditioned on — opened! So no, Training and Equipment are *not* independent given Quality. *(pause)* Conditioning on quality created a spurious link between training and equipment. That's collider bias, right here in our own model.

## Slide: MNH Application: Rwanda
Now let's build a real model for a real country.

## Slide: Rwanda at a Glance
Here are the numbers. *(pause)* Neonatal mortality: about 16 per 1,000. Maternal mortality: about 248 per 100,000. Facility delivery rate: over 94 percent — that's really high. Health insurance through Mutuelle de Sante: about 85 percent coverage. They've got roughly 58,000 community health workers across 30 districts. But nurses per population is only about 1.3 per 1,000, way below the WHO target of 4.45.

Rwanda's CHW program and Mutuelle insurance are widely studied success stories. But the workforce is stretched thin, and neonatal mortality has been harder to crack than under-5 mortality.

## Slide: Choosing Our Variables
We want a diagram rich enough to capture the key dynamics but small enough to reason about. Seven nodes. *(pause)* Three decision nodes — rectangles, the levers we pull: CHW Training Investment, Equipment Procurement, and Insurance Policy. Three probabilistic nodes in the middle: Workforce Competency, Equipment Availability, and Care-Seeking Behavior. One more probabilistic node that acts as the bottleneck: Quality of Care. And one objective node — the hexagon, the scoreboard: Neonatal Mortality.

## Slide: The Rwanda MNH DAG
Look at the diagram. Read it left to right. *(pause)* Decisions on the left — what we control. Mediators in the middle — how they work. Quality of Care is the bottleneck where everything converges. And Neonatal Mortality on the right — what we want to reduce.

Each of the three decisions flows through its own channel. Training builds competency. Procurement gets equipment into facilities. Insurance drives care-seeking. All three channels pour into Quality, and Quality reduces mortality.

## Slide: Signs and Path Analysis
Let's assign signs. *(pause)* Training to Competency — plus. Procurement to Availability — plus. Insurance to Care-Seeking — plus. Competency to Quality — plus. Availability to Quality — plus. Care-Seeking to Quality — plus. Quality to Mortality — minus.

Now follow any path from a decision to mortality. Training to Competency to Quality to Mortality: plus times plus times minus equals minus overall. Training reduces mortality. Same for all three channels — every one carries an overall minus sign. All three reduce mortality. *(pause)* The question is: which one has the *strongest* effect? That's what we'll need actual numbers for in Chapter 4.

## Slide: Spotting Triplets in the Rwanda DAG
Time for pattern recognition. *(pause)* Look at the green box — chains. Training to Competency to Quality. Insurance to Care-Seeking to Quality. Procurement to Availability to Quality to Mortality. Conditioning on the mediator blocks each of these paths.

Now the red box — colliders. Competency and Availability both flow into Quality. Competency and Care-Seeking both flow into Quality. Quality is a collider for all of these pairs. *(pause)* That means if you condition on Quality — say, you only study high-quality facilities — you create a fake link between staffing and equipment. With Rwanda's nurse shortage of 1.3 per 1,000, if you only look at high-performing facilities, staffing and equipment will appear negatively related. That's a statistical illusion from collider bias. Be careful what you condition on.

## Slide: R Workshop
Let's build Rwanda's DAG in R with dagitty and ggdag.

## Slide: Setting Up
Same three packages as last time — dagitty, ggdag, and ggplot2. *(pause)* If they're already installed, just load them. If not, uncomment the install line and run it first.

## Slide: Step 1: Define Rwanda's DAG
Here we define the full seven-node model in code. *(pause)* Look at the dagitty syntax. Three decision nodes on the left: CHW_Training, Equipment_Procure, Insurance_Policy. Three mediators in the middle: Competency, Equip_Avail, Care_Seeking, plus Quality. And Neonatal_Mortality on the right. Seven arrows connecting them. Then we check isAcyclic — it should return TRUE, confirming we haven't accidentally created any loops. That's our sanity check.

## Slide: Step 2: Visualize the DAG
Now let's see it. *(pause)* The first call, ggdag, gives us the basic picture. The second call, ggdag_status, color-codes the exposure and outcome — so we can see the path from CHW Training to Neonatal Mortality highlighted. Run both and see how the structure pops visually.

## Slide: Step 3: Test d-Separation
Here's where we check our understanding against the computer. Three tests. *(pause)* Test 1: Is Training independent of Mortality given Quality? That's a chain — we expect TRUE, blocked. Test 2: Is Competency independent of Equipment Availability unconditionally? No connecting path — we expect TRUE. Test 3: Is Competency independent of Equipment Availability given Quality? That's a collider — we expect FALSE, opened!

Run the code. If your predictions match, you've got the triplet rules down. If any surprise you, go back and trace the path by hand. *(pause)* TRUE means independent, path blocked. FALSE means information flows. Test 3 is the collider effect in action.

## Slide: Step 4: Paths and Adjustment Sets
Two more powerful tools. *(pause)* The paths function lists every route from CHW_Training to Neonatal_Mortality. The impliedConditionalIndependencies function generates every testable prediction our model makes — if data violates any of these, our model needs fixing. And adjustmentSets tells us what we need to control for.

Notice it returns the empty set for CHW_Training. Why? Because Training has no parents in this DAG — it's a root node. No backdoor paths to close. The causal effect can be estimated without any adjustment, *if* the DAG is correct. That's a big "if," and it's why getting the diagram right matters so much.

## Slide: Key Takeaways
Three things to take away. *(pause)* First, a qualitative causal model makes your assumptions visible, shareable, and testable. It gets beliefs out of your head and onto paper.

Second, every DAG is built from three triplets — chains, forks, and colliders — each with its own information flow rule. Chains and forks: conditioning on the middle blocks the flow. Colliders: conditioning on the middle opens the flow. Get this backwards and you introduce bias instead of removing it.

Third, for Rwanda: three investment decisions flow through three mediators into Quality of Care, then Neonatal Mortality. The diagram tells us *where* to look — the numbers will tell us *how much*.

## Slide: Looking Ahead
Next session we put these tools to work on a real consulting case. *(pause)* We'll build a DAG from stakeholder interviews in Kenya — talking to a County Health Director, a midwife, and a community health worker. Each conversation reveals new variables our model was missing. It's detective work, and it's where the theory becomes practice.

Then in Chapter 4, we replace the plus and minus signs with actual probabilities — answering not just *what* affects what, but *how much*. See you next time.
