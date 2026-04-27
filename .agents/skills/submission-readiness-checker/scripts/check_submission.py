import argparse
import re
from pathlib import Path


VIDEO_PATTERNS = [
    r"youtube\.com",
    r"youtu\.be",
    r"vimeo\.com",
    r"zoom\.us",
]


def check_readme(repo_root: Path, results: list):
    readme = repo_root / "README.md"

    if not readme.exists():
        results.append(("FAIL", "README.md is missing."))
        return

    results.append(("PASS", "README.md found."))

    text = readme.read_text(encoding="utf-8", errors="ignore").lower()

    required_sections = [
        "what the skill does",
        "why",
        "how to use",
        "script",
        "limitation",
    ]

    for section in required_sections:
        if section in text:
            results.append(("PASS", f"README mentions '{section}'."))
        else:
            results.append(("WARNING", f"README may be missing a section about '{section}'."))

    has_video = any(re.search(pattern, text) for pattern in VIDEO_PATTERNS)

    if has_video:
        results.append(("PASS", "README contains a video link."))
    else:
        results.append(("FAIL", "README does not contain a recognizable video link."))


def check_skill_folder(repo_root: Path, results: list):
    skills_root = repo_root / ".agents" / "skills"

    if not skills_root.exists():
        results.append(("FAIL", ".agents/skills/ folder is missing."))
        return

    skill_folders = [p for p in skills_root.iterdir() if p.is_dir()]

    if not skill_folders:
        results.append(("FAIL", "No skill folder found inside .agents/skills/."))
        return

    results.append(("PASS", f"Found {len(skill_folders)} skill folder(s)."))

    for skill_folder in skill_folders:
        check_single_skill(skill_folder, results)


def check_single_skill(skill_folder: Path, results: list):
    skill_name = skill_folder.name

    if skill_name.lower() != skill_name or "_" in skill_name:
        results.append(("WARNING", f"Skill folder name '{skill_name}' should be lowercase and hyphenated."))
    else:
        results.append(("PASS", f"Skill folder name '{skill_name}' looks valid."))

    skill_md = skill_folder / "SKILL.md"

    if not skill_md.exists():
        results.append(("FAIL", f"{skill_name}/SKILL.md is missing."))
        return

    results.append(("PASS", f"{skill_name}/SKILL.md found."))

    text = skill_md.read_text(encoding="utf-8", errors="ignore")

    if re.search(r"^---\s*\n", text):
        results.append(("PASS", "SKILL.md contains frontmatter."))
    else:
        results.append(("FAIL", "SKILL.md is missing frontmatter."))

    if re.search(r"name:\s*\S+", text):
        results.append(("PASS", "SKILL.md contains a name field."))
    else:
        results.append(("FAIL", "SKILL.md is missing a name field."))

    if re.search(r"description:\s*.+", text):
        results.append(("PASS", "SKILL.md contains a description field."))
    else:
        results.append(("FAIL", "SKILL.md is missing a description field."))

    scripts_folder = skill_folder / "scripts"

    if not scripts_folder.exists():
        results.append(("FAIL", f"{skill_name}/scripts/ folder is missing."))
        return

    python_scripts = list(scripts_folder.glob("*.py"))

    if python_scripts:
        results.append(("PASS", f"Found {len(python_scripts)} Python script(s) in scripts/."))
    else:
        results.append(("FAIL", "No Python script found inside scripts/."))


def print_report(results: list):
    fail_count = sum(1 for status, _ in results if status == "FAIL")
    warning_count = sum(1 for status, _ in results if status == "WARNING")

    if fail_count == 0 and warning_count == 0:
        overall = "Ready"
    elif fail_count == 0:
        overall = "Almost ready"
    else:
        overall = "Not ready"

    print("\nSubmission Readiness Report")
    print("=" * 30)
    print(f"Overall status: {overall}\n")

    for status, message in results:
        print(f"{status}: {message}")


def main():
    parser = argparse.ArgumentParser(
        description="Check whether a homework repository is ready for submission."
    )
    parser.add_argument(
        "repo_root",
        nargs="?",
        default=".",
        help="Path to the repository root. Default is current directory.",
    )

    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()

    results = []

    if not repo_root.exists():
        print(f"FAIL: Repository path does not exist: {repo_root}")
        return

    check_readme(repo_root, results)
    check_skill_folder(repo_root, results)
    print_report(results)


if __name__ == "__main__":
    main()
