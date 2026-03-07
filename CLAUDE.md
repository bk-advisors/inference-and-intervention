# CLAUDE.md — Inference and Intervention

## Project Overview

A 10-chapter Quarto reveal.js lecture series based on *Inference and Intervention: Causal Models for Business Analysis* (Ryall & Bramson, 2014), adapted for Maternal & Newborn Health (MNH). Includes a companion course website, pre-class essays, whiteboard diagrams, and speaker notes.

## Audience

**High school level learners.** Content must be understandable by a motivated high school student with no statistics or programming background. Use conversational but smart language — no dumbing down, but no jargon without explanation.

## Tone

Conversational, engaging, story-driven. Short sentences, active voice. Everyday analogies before technical concepts. "Try It" prompts instead of formal exercises.

## Content Rules

### Country Names — Use Real Names
Use **Ethiopia, Rwanda, Kenya, Tanzania** directly. No anonymization of country names (the old Country A–J mapping is retired).

### Data — Public Sources Only
All MNH data must come from **publicly available sources**: WHO, UNICEF, DHS (Demographic and Health Surveys), Lancet, government health ministry reports. Cite the source when using specific numbers.

### Banned Terms (Confidential — must NEVER appear)

| Category | Banned Terms |
|----------|-------------|
| Organization names | Beginnings Fund, Meridian Health Alliance, the Alliance |
| Donor names | CIFF, Delta Philanthropies, ELMA, Gates Foundation, Mohamed bin Zayed |
| Governance | Investment Committee |
| Budget amounts | Any specific dollar amounts tied to the program ($525M, $90M, $35M, $76M, $75M, etc.) |
| Lives-saved targets | 322,000; 322,847; 86,124; 14,585; or any program-specific target |
| Co-financing details | Government co-financing amounts, probabilities, or agreements from internal documents |
| Internal strategies | Phase structures, cohort details, internal implementation timelines |
| Partner orgs | HaHCo, Fund Two |

**Generic replacements:** "a large-scale MNH initiative", "donor-funded health programs", "health program leadership"

### No Textbook Examples
Do not use examples directly from Ryall & Bramson: no Feather Touch/TruSmartz, Robert Maxwell, Slimtree Publishing, Hubris Health, the Rideshare Case. Teach the same concepts with new MNH examples drawn from public data.

## Simplification Principles

1. **No formulas without a story.** Narrative first; formula (if any) second.
2. **Natural frequencies over probabilities.** "55 out of 100" not "P(X)=0.55"
3. **Everyday analogies first.** Rain/umbrella, ice cream/drowning, university admissions — then MNH.
4. **Active voice, short sentences.** "The model tells us X" not "It can be derived from the model that X."
5. **"Try It" boxes** replace formal exercises.
6. **R code with guard rails.** Plain-English paragraph before every code block. Inline comments on every non-obvious line.
7. **Real names, real numbers** from public sources.

## File Structure

```
inference-and-intervention/
  _quarto.yml               # Website project configuration
  CLAUDE.md                  # This file
  skills.md                  # Detailed operational manual
  index.qmd                 # Website home page
  schedule.qmd              # Course syllabus
  r-setup.qmd               # R setup guide
  references.qmd            # Bibliography
  styles.scss               # Website SCSS theme
  chapters/                 # Chapter companion pages (website)
  ch01-intro/               # Ch 1 slide deck (standalone)
  ch02-qualitative-models/  # Ch 2 slide deck
  ch03-interview-case/      # Ch 3 slide deck
  ch04-quantitative-models/ # Ch 4 slide deck
  ch05-situational-analysis/# Ch 5 slide deck
  ch06-business-financials/ # Ch 6 slide deck
  ch07-single-agent/        # Ch 7 slide deck
  ch08-resource-allocation/ # Ch 8 slide deck
  ch09-multi-agent/         # Ch 9 slide deck
  ch10-data-driven/         # Ch 10 slide deck
  country-plans/            # Source .docx files (reference only — use public data from these)
  context/                  # Reference PDFs (do not modify)
  _archive/                 # Archived v1 graduate-level content
```

## Build Commands

```bash
# Render a single slide deck
quarto render ch01-intro/index.qmd

# Render the full website
quarto render

# Live preview
quarto preview
```

## See Also

- `skills.md` — Full operational manual with CSS classes, slide patterns, speaker note conventions
