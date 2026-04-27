---
name: submission-readiness-checker
description: Checks whether a project repository is ready for assignment submission by validating required files, skill folder structure, SKILL.md metadata, script presence, README content, and video link requirements. Use this when the user asks to review, audit, or confirm whether a coding or AI skill homework repo is submission-ready.
---

# Submission Readiness Checker

## When to use this skill

Use this skill when the user wants to check whether a project repository is ready to submit for a coding, AI workflow, or agent skill assignment.

This skill is especially useful when the assignment requires a specific folder structure, a README file, a script, a video link, and a clear explanation of the project.

## When not to use this skill

Do not use this skill to grade the quality of the user's writing or judge whether the idea is creative enough.

Do not use this skill when the user only wants general advice and does not have a project folder or repository to inspect.

Do not use this skill for non-code assignments such as essays, discussion posts, or reflection papers.

## Expected inputs

The user should provide one of the following:

1. A local repository path
2. A project folder
3. A GitHub repository that has been cloned locally
4. A README and skill folder structure to inspect

## What the script does

The Python script checks the repository structure in a deterministic way. It verifies whether:

- README.md exists
- a skill folder exists under `.agents/skills/`
- SKILL.md exists
- SKILL.md contains required frontmatter fields: `name` and `description`
- a `scripts/` folder exists
- at least one Python script exists inside `scripts/`
- README.md contains a video link
- README.md explains what the skill does, how to use it, and its limitations

This script is load-bearing because file existence, folder structure, and required text checks are better handled by code than by prose alone.

## Step-by-step instructions

1. Identify the root directory of the user's project.
2. Run the Python script from the skill folder.
3. Read the generated checklist report.
4. Explain the most important PASS, WARNING, and FAIL items to the user.
5. Recommend only the minimum changes needed to make the repository submission-ready.

## Expected output format

Return a short submission readiness report using this format:

Submission Readiness Report

Overall status: Ready / Almost ready / Not ready

Passed checks:
- ...

Warnings:
- ...

Required fixes:
- ...

Recommended next step:
- ...

## Limitations

This skill checks structure and required submission elements. It does not guarantee a perfect grade.

This skill does not replace the instructor's rubric.

This skill cannot confirm that a video link is publicly accessible unless the link is manually opened and reviewed.
