# Resume Doctor

A resume diagnosis and optimization tool designed for software developers.

## Features

- **5-Step Analysis** — Overall score, highlight identification, red flag warnings, optimization suggestions, ATS keywords
- **Resume Optimization** — Generate high-quality resumes based on analysis
- **Interview Prediction** — Technical fundamentals + Project deep-dive + System design

## Supported Positions

Frontend / Backend / Algorithm / Data / DevOps

## Input

Minimum required: job position, years of experience, work experience, project details (at least 1)

Methods: paste text, upload file (.pdf/.docx/.txt/.md), describe experience

## Output Example

### 1. Overall Score (10-point scale)

| Score | Standard                                                                   |
| ----- | -------------------------------------------------------------------------- |
| 9-10  | Complete info, quantified data, almost no red flags                        |
| 7-8   | High quality, minor room for improvement                                   |
| 5-6   | Obvious issues (no quantification, vague tech stack, generic descriptions) |
| 3-4   | Multiple high-risk red flags                                               |

### 2. Highlight Identification

Identify technical highlights based on position (performance optimization, high concurrency, architecture design, etc.)

### 3. Red Flag Warnings

Detect vague descriptions ("responsible for/participated in"), lack of quantified data, unclear tech stack, etc.

### 4. Optimization Suggestions

Provide specific modification examples for each red flag

### 5. ATS Keyword Analysis

Output position match analysis and recommended keywords

## Language

- Chinese resume → Chinese output
- English resume → English output

## Quick Start

Install the skill in Claude Code:

```
git clone https://github.com/chenchen112/resume-doctor.git ~/.claude/skills/resume-doctor
```

Then describe your resume or upload a file to get started.

## How to Use

Describe your resume or upload a file in Claude Code to get analysis

## File Structure

```
├── SKILL.md         # Skill definition
├── CLAUDE.md        # Claude Code guidance
├── evals/evals.json # Test cases
└── README*.md       # Bilingual documentation
```
