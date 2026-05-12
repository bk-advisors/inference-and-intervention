# CLAUDE.md — Causal Analysis in Public Health Management

## Project Overview

"Causal Analysis in Public Health Management" is a 10-chapter Quarto reveal.js course based on *Inference and Intervention: Causal Models for Business Analysis* (Ryall & Bramson, 2014), adapted for Maternal & Newborn Health (MNH). Each chapter has a main lecture (textbook-structured, v2 style) plus a tutorial / breakout-session deck (Made-to-Stick / SUCCES style). Includes a companion course website, pre-class essays, whiteboard diagrams, and speaker notes.

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
  chapters/                 # Chapter companion pages (website) — embed both lecture + tutorial decks
  course-intro/             # Course intro slide deck (Made-to-Stick style)
  # Main lecture decks (textbook v2 style) — one per chapter
  ch01-intro/
  ch02-qualitative-models/
  ch03-interview-case/
  ch04-quantitative-models/
  ch05-situational-analysis/
  ch06-business-financials/
  ch07-single-agent/
  ch08-resource-allocation/
  ch09-multi-agent/
  ch10-data-driven/
  # Tutorial / breakout session decks (Made-to-Stick style) — one per chapter
  ch01-intro-tutorial/
  ch02-qualitative-models-tutorial/
  ch03-interview-case-tutorial/
  ch04-quantitative-models-tutorial/
  ch05-situational-analysis-tutorial/
  ch06-simpsons-paradox-tutorial/
  ch07-decision-analysis-tutorial/
  ch08-resource-allocation-tutorial/
  ch09-game-theory-tutorial/
  ch10-structure-learning-tutorial/
  reflections on course videos/  # Video transcript review workflow (gitignored — private)
    input/                     #   YouTube transcripts (.docx), reference examples, photo, CV
    output/                    #   Revised scripts (.docx) and slide decks (Quarto revealjs)
  country-plans/            # Source .docx files (reference only — use public data from these)
  context/                  # Reference PDFs (do not modify)
  _archive/                 # Archived versions: v1-graduate-level/, v2-mnh-high-school/ (v2 = source of current lecture decks)
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

### Deploy gotcha (important)

Project-level `quarto render` **only builds the website pages** listed in `_quarto.yml` — it does *not* re-render the standalone reveal.js decks in `ch*/`. After changing shared SCSS or any deck content, you must:

1. Re-render each deck individually: `quarto render ch02-qualitative-models/index.qmd` (loop over all `ch*/` and `course-intro/`).
2. Sync the refreshed deck HTMLs into `_site/` (GitHub Pages serves from `_site/`, not the repo root): `cp ch*/index.html _site/ch*/index.html` equivalent.
3. Commit and push. Pages redeploys in 1–3 minutes; use a cache-bust query (`?v=...`) to bypass the Fastly CDN when verifying.

## See Also

- `skills.md` — Full operational manual with CSS classes, slide patterns, speaker note conventions
