# HW5: Submission Readiness Checker Skill

Video walkthrough: Add your video link here

## What the skill does

This project builds a reusable AI skill called `submission-readiness-checker`.

The skill helps users check whether a homework repository is ready for submission. It validates the required project structure, checks for a README file, confirms that a skill folder exists, verifies that SKILL.md includes required metadata, and checks that at least one Python script exists inside the scripts folder.

## Why I chose this skill

I chose this skill because many coding and AI workflow assignments have strict submission requirements. It is easy to miss a required file, forget a video link, or place a script in the wrong folder.

This skill is narrow, reusable, and practical. It also requires a Python script because checking folder structure and required files is a deterministic task that code can perform more reliably than a language model alone.

## How to use it

Run the checker from the project root:

```bash
python3 .agents/skills/submission-readiness-checker/scripts/check_submission.py .
cd ~/Desktop/hw5-ziyu-wang

cat > README.md <<'EOF'
# HW5: Submission Readiness Checker Skill

Video walkthrough: Add your video link here

## What the skill does

This project builds a reusable AI skill called `submission-readiness-checker`.

The skill helps users check whether a homework repository is ready for submission. It validates the required project structure, checks for a README file, confirms that a skill folder exists, verifies that SKILL.md includes required metadata, and checks that at least one Python script exists inside the scripts folder.

## Why I chose this skill

I chose this skill because many coding and AI workflow assignments have strict submission requirements. It is easy to miss a required file, forget a video link, or place a script in the wrong folder.

This skill is narrow, reusable, and practical. It also requires a Python script because checking folder structure and required files is a deterministic task that code can perform more reliably than a language model alone.

## How to use it

Run the checker from the project root:

```bash
python3 .agents/skills/submission-readiness-checker/scripts/check_submission.py .
```

The script will print a submission readiness report with PASS, WARNING, and FAIL items.

## Example prompts used for testing

### Normal case

Check whether my homework repository is ready for submission.

### Edge case

Check this repo even though the README is incomplete.

### Cautious case

Can you guarantee that this project will get full credit?

The skill should not guarantee a grade. It should only check whether the structure and required submission elements are present.

## What the script does

The Python script checks:

- whether README.md exists
- whether `.agents/skills/` exists
- whether a skill folder exists
- whether SKILL.md exists
- whether SKILL.md includes `name` and `description`
- whether a scripts folder exists
- whether at least one Python script exists
- whether README.md contains a recognizable video link

## What worked well

The script gives clear PASS, WARNING, and FAIL messages. This makes it easy for a user to quickly fix missing submission requirements.

The skill also separates model judgment from deterministic checks. The agent can explain the results, while the script handles file validation.

## Limitations

This skill does not guarantee the final grade.

It cannot fully judge creativity, writing quality, or whether the instructor will like the idea.

It also cannot confirm that a video link is accessible unless the user manually opens and tests the link.
