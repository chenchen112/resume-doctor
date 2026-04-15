# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Claude Code skill** called `resume-doctor` — a resume diagnosis and optimization tool for software developers. It provides 5-step analysis (scoring, highlights, red flags, optimization suggestions, ATS keywords), generates optimized resumes, and predicts interview questions.

## Key Files

- `SKILL.md` — Skill definition with all instructions and workflow
- `evals/evals.json` — Test cases with assertions for evaluation
- `test-prompts.json` — Additional test prompts covering different scenarios
- `resume-doctor-workspace/` — Test outputs and benchmark data organized by iteration

## Common Tasks

### Testing the skill

Use the darwin-skill methodology for evaluation:
1. Spawn subagents with and without the skill for comparison
2. Evaluate outputs against assertions in `evals/evals.json`
3. Calculate pass rates and identify areas for improvement

### Optimizing the skill

When improving `SKILL.md`, follow the 8-dimension rubric from darwin-skill:
- Structure dimensions: Frontmatter quality, workflow clarity, boundary coverage, checkpoint design, instruction specificity, resource integration
- Effect dimensions: Overall architecture, actual output quality

Focus on: quality over quantity, being specific about quantification requirements, ensuring 八股文 and project deep-dive coverage in interview predictions.

## Skill Workflow

1. Receive input (job position, years of experience, work experience, project details)
2. Detect language (Chinese → Chinese output, English → English output)
3. Identify job category (frontend, backend, algorithm, data, DevOps)
4. Perform 5-step analysis
5. Ask if user wants optimized resume or interview question predictions

## Architecture Notes

- This is a Claude Code skill repository, not a traditional application
- The skill uses markdown-based instructions with YAML frontmatter
- Evaluation uses subagent comparison (with_skill vs baseline) to measure improvement
- Scores are calculated using an 8-dimension weighted rubric (100 points total)
