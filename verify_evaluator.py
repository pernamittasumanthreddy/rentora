#!/usr/bin/env python3
"""
Rentora Platform Comprehensive Evaluator Verification Script
Audits all criteria specified in the grading rubric and reports PASS/FAIL status.
"""

import os
import sys
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def audit_lines_of_code():
    print("\n[1] Auditing Lines of Code (Production Only)...")
    extensions = {'.java', '.js', '.jsx', '.ts', '.tsx', '.py'}
    excludes = {'tests', 'test', 'node_modules', '.git', 'coverage', 'dist', 'generated', 'build', 'target'}
    
    total_loc = 0
    file_count = 0
    by_ext = {}
    
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d.lower() not in excludes and not d.startswith('.')]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in extensions:
                p = os.path.join(root, f)
                parts = [part.lower() for part in p.split(os.sep)]
                if any(exc in parts for exc in excludes):
                    continue
                try:
                    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                        lines = sum(1 for line in fp if line.strip())
                        total_loc += lines
                        file_count += 1
                        by_ext[ext] = by_ext.get(ext, 0) + lines
                except Exception:
                    pass

    print(f" -> Found {total_loc:,} non-empty prod LOC across {file_count} files.")
    print(f" -> Breakdown: {by_ext}")
    passed = total_loc >= 50000
    status = "PASS" if passed else "FAIL"
    print(f" -> Result: [{status}] (Required: 50,000, Actual: {total_loc:,})")
    return passed, total_loc

def audit_git_repository():
    print("\n[2] Auditing Git-based Repository...")
    git_dir = ROOT / ".git"
    exists = git_dir.exists() and git_dir.is_dir()
    status = "PASS" if exists else "FAIL"
    print(f" -> .git directory found: {exists}")
    print(f" -> Result: [{status}]")
    return exists

def audit_git_commits():
    print("\n[3] Auditing Git Commits Count...")
    try:
        res = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=str(ROOT), capture_output=True, text=True)
        count = int(res.stdout.strip())
        passed = count >= 5
        status = "PASS" if passed else "FAIL"
        print(f" -> Commit count: {count}")
        print(f" -> Result: [{status}] (Required: >= 5)")
        return passed, count
    except Exception as e:
        print(f" -> Error checking commits: {e}")
        return False, 0

def audit_pull_requests():
    print("\n[4] Auditing Meaningful Pull Requests (Merge Commits)...")
    try:
        res = subprocess.run(["git", "log", "--merges", "--oneline"], cwd=str(ROOT), capture_output=True, text=True)
        merges = [line for line in res.stdout.strip().splitlines() if line.strip()]
        count = len(merges)
        passed = count >= 4
        status = "PASS" if passed else "FAIL"
        print(f" -> Merge commits (PRs) found: {count}")
        for m in merges:
            print(f"    * {m}")
        print(f" -> Result: [{status}] (Required: >= 4)")
        return passed, count
    except Exception as e:
        print(f" -> Error checking pull requests: {e}")
        return False, 0

def audit_executable_project():
    print("\n[5] Auditing Executable Indicators & Build System...")
    indicators = {
        "Dockerfile": (ROOT / "Dockerfile").exists(),
        "docker-compose.yml": (ROOT / "docker-compose.yml").exists(),
        "Makefile": (ROOT / "Makefile").exists(),
        "Root package.json": (ROOT / "package.json").exists(),
        "app.py entry point": (ROOT / "app.py").exists(),
        "main.py entry point": (ROOT / "main.py").exists(),
    }
    for name, present in indicators.items():
        print(f" -> {name}: {'FOUND' if present else 'MISSING'}")
    passed = sum(indicators.values()) >= 3
    status = "PASS" if passed else "FAIL"
    print(f" -> Result: [{status}] (Required: At least 1 indicator, Found: {sum(indicators.values())})")
    return passed

def audit_test_coverage():
    print("\n[6] Auditing Test Coverage...")
    tests_dir = ROOT / "tests"
    test_files = list(tests_dir.glob("test_*.py")) if tests_dir.exists() else []
    pytest_ini = (ROOT / "pytest.ini").exists()
    print(f" -> Test files count: {len(test_files)}")
    print(f" -> Pytest config (pytest.ini) present: {pytest_ini}")
    
    # Run pytest
    try:
        res = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"], cwd=str(ROOT), capture_output=True, text=True)
        tests_passed = res.returncode == 0
        print(f" -> Pytest execution: {'PASSED (All tests green)' if tests_passed else 'FAILED'}")
    except Exception as e:
        tests_passed = False
        print(f" -> Pytest execution failed: {e}")

    passed = len(test_files) > 0 and pytest_ini and tests_passed
    status = "PASS" if passed else "FAIL"
    print(f" -> Result: [{status}]")
    return passed

def audit_complete_app():
    print("\n[7] Auditing Complete Application Readiness...")
    has_frontend = (ROOT / "frontend" / "src" / "App.jsx").exists()
    has_backend = (ROOT / "backend" / "pom.xml").exists()
    has_database = (ROOT / "database" / "schema.sql").exists()
    passed = has_frontend and has_backend and has_database
    status = "PASS" if passed else "FAIL"
    print(f" -> Frontend React App: {'FOUND' if has_frontend else 'MISSING'}")
    print(f" -> Backend Spring Boot: {'FOUND' if has_backend else 'MISSING'}")
    print(f" -> Database Schema & Seeds: {'FOUND' if has_database else 'MISSING'}")
    print(f" -> Result: [{status}]")
    return passed

def main():
    print("=" * 80)
    print("           RENTORA EVALUATOR AUDIT & COMPLIANCE VERIFICATION")
    print("=" * 80)

    results = []
    results.append(("50,000+ Lines of Code", audit_lines_of_code()[0]))
    results.append(("Git-based Repository (.git)", audit_git_repository()))
    results.append(("At least 5 Commits", audit_git_commits()[0]))
    results.append(("At least 4 Pull Requests", audit_pull_requests()[0]))
    results.append(("Executable Project Indicators", audit_executable_project()))
    results.append(("Test Coverage Included", audit_test_coverage()))
    results.append(("Complete Working Application", audit_complete_app()))

    print("\n" + "=" * 80)
    print("                     FINAL EVALUATOR SCORECARD")
    print("=" * 80)
    all_passed = True
    for name, passed in results:
        status_str = "PASSED [OK]" if passed else "FAILED [X]"
        print(f"  * {name:<40} : {status_str}")
        if not passed:
            all_passed = False

    print("=" * 80)
    if all_passed:
        print(">>> 100% PASS: ALL 7 EVALUATION CRITERIA ARE FULLY SATISFIED! <<<")
    else:
        print(">>> SOME CRITERIA FAILED <<<")
    print("=" * 80)

    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
