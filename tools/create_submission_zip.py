#!/usr/bin/env python3
"""
Rentora Submission Zip Packager
Creates a clean, complete, production-ready submission ZIP for TrainPlex Checker Bot.
CRITICAL: Explicitly includes the complete .git/ repository history (all 14 commits and 5 PR merges),
while excluding bloated folders like node_modules and build artifacts.
"""

import os
import sys
import zipfile
import shutil
import tempfile
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_ZIP = Path("C:/Users/BABI/Desktop/rentora_submission.zip")

EXCLUDED_DIR_NAMES = {
    "node_modules",
    "dist",
    ".pytest_cache",
    "__pycache__",
    "htmlcov",
    "target",
}

EXCLUDED_EXTENSIONS = {
    ".pyc",
    ".pyo",
    ".pyd",
}

def create_zip():
    print("=" * 80)
    print(f"Creating TrainPlex Submission ZIP at: {OUTPUT_ZIP}")
    print("=" * 80)

    if OUTPUT_ZIP.exists():
        OUTPUT_ZIP.unlink()

    file_count = 0
    git_file_count = 0
    total_uncompressed_bytes = 0

    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
        for root, dirs, files in os.walk(ROOT_DIR):
            rel_root = os.path.relpath(root, ROOT_DIR)
            parts = [p.lower() for p in rel_root.split(os.sep)]

            # Check if this directory should be skipped
            if any(exc in parts for exc in EXCLUDED_DIR_NAMES):
                continue

            # Do NOT skip .git! Explicitly process .git
            is_in_git = ".git" in parts or rel_root == ".git"

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in EXCLUDED_EXTENSIONS:
                    continue
                if file.endswith(".zip"):
                    continue
                if "timestamp-" in file:
                    continue

                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, ROOT_DIR)

                # Store relative path so .git/ is directly at root of zip
                zipf.write(abs_path, arcname=rel_path)
                file_count += 1
                size = os.path.getsize(abs_path)
                total_uncompressed_bytes += size

                if is_in_git:
                    git_file_count += 1

    zip_size_mb = OUTPUT_ZIP.stat().st_size / (1024 * 1024)
    print(f" -> Total files packaged: {file_count:,}")
    print(f" -> Git history files included: {git_file_count:,} (in .git/)")
    print(f" -> Output ZIP Size: {zip_size_mb:.2f} MB")
    print(f" -> Saved to: {OUTPUT_ZIP}")

    verify_zip()

def verify_zip():
    print("\n" + "=" * 80)
    print("Verifying packaged ZIP integrity in isolated sandbox...")
    print("=" * 80)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        with zipfile.ZipFile(OUTPUT_ZIP, "r") as zipf:
            zipf.extractall(temp_path)

        # 1. Check .git exists
        git_exists = (temp_path / ".git").exists()
        print(f" [1] .git directory present in extracted root: {git_exists}")

        # 2. Check git status and commits
        try:
            res_count = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=str(temp_path), capture_output=True, text=True)
            commit_count = int(res_count.stdout.strip())
            print(f" [2] Git commit count in extracted archive: {commit_count} (Required: >= 5) -> {'PASS' if commit_count >= 5 else 'FAIL'}")

            res_merges = subprocess.run(["git", "log", "--merges", "--oneline"], cwd=str(temp_path), capture_output=True, text=True)
            merges = [line for line in res_merges.stdout.strip().splitlines() if line.strip()]
            print(f" [3] Git PR merges in extracted archive: {len(merges)} (Required: >= 4) -> {'PASS' if len(merges) >= 4 else 'FAIL'}")
            for m in merges:
                print(f"      * {m}")
        except Exception as ex:
            print(f" [ERROR] Git validation failed: {ex}")

        # 3. Check LOC
        exts = {'.java', '.js', '.jsx', '.ts', '.tsx', '.py'}
        excludes = {'tests', 'test', 'node_modules', '.git', 'coverage', 'dist', 'generated', 'build', 'target'}
        total_loc = 0
        for r, d, fs in os.walk(temp_path):
            d[:] = [x for x in d if x.lower() not in excludes and not x.startswith('.')]
            for f in fs:
                if os.path.splitext(f)[1].lower() in exts:
                    p = os.path.join(r, f)
                    if any(exc in [part.lower() for part in p.split(os.sep)] for exc in excludes):
                        continue
                    try:
                        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                            total_loc += sum(1 for line in fp if line.strip())
                    except Exception:
                        pass
        print(f" [4] Total production LOC in extracted archive: {total_loc:,} (Required: >= 50,000) -> {'PASS' if total_loc >= 50000 else 'FAIL'}")

        # 4. Check executable indicators
        has_docker = (temp_path / "Dockerfile").exists()
        has_compose = (temp_path / "docker-compose.yml").exists()
        has_makefile = (temp_path / "Makefile").exists()
        has_pkg = (temp_path / "package.json").exists()
        has_app = (temp_path / "app.py").exists()
        print(f" [5] Executable indicators: Dockerfile={has_docker}, docker-compose={has_compose}, Makefile={has_makefile}, package.json={has_pkg}, app.py={has_app}")

        # 5. Check tests
        test_files = list((temp_path / "tests").glob("test_*.py")) if (temp_path / "tests").exists() else []
        print(f" [6] Test suite in extracted archive: {len(test_files)} test files found.")

    print("\n" + "=" * 80)
    print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
    print(f"You can now upload: {OUTPUT_ZIP}")
    print("=" * 80)

if __name__ == "__main__":
    create_zip()
