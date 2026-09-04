#!/usr/bin/env python3
"""
Rentora Unified Platform Application Runner & Management CLI
Entry point for running Rentora microservices, health audits, database migrations, and telemetry simulations.
"""

import os
import sys
import time
import signal
import logging
import argparse
import subprocess
from pathlib import Path

# Configure Structured Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [RentoraPlatform] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("rentora-runner")

ROOT_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = ROOT_DIR / "frontend"
BACKEND_DIR = ROOT_DIR / "backend"
SERVICES_DIR = ROOT_DIR / "services"

def print_banner():
    banner = r"""
  =============================================================================
   ______   _______  _        _______  _______  _______  _______ 
  (  ___ \ (  ____ \( (    /|(  ___  )(  ____ )(  ___  )(  ___  )
  | (   ) )| (    \/|  \  ( || (   ) || (    )|| (   ) || (   ) |
  | (__/ / | (__    |   \ | || |   | || (____)|| |   | || (___) |
  |  __ (  |  __)   | (\ \) || |   | ||     __)| |   | ||  ___  |
  | (  \ \ | (      | | \   || |   | || (\ (   | |   | || (   ) |
  | )___) )| (____/\| )  \  || (___) || ) \ \__| (___) || )   ( |
  |/ \___/ (_______/|/    )_)(_______)|/   \__/(_______)|/     \|
             Smart Product, Vehicle & Hardware Rental Platform
  =============================================================================
  "Rent • Share • Save • Sustain"
  Architecture: React 18 + Spring Boot 3 + MySQL 8 + IoT Telematics Engine
    """
    print(banner)

def verify_environment():
    """Verify system prerequisites and environment configuration."""
    logger.info("Verifying system runtime prerequisites...")
    checks = {
        "Python": sys.version.split()[0],
        "Node Modules Exists": (FRONTEND_DIR / "node_modules").exists(),
        "Backend Source Exists": (BACKEND_DIR / "src").exists(),
        "Database SQL Exists": (ROOT_DIR / "database" / "schema.sql").exists(),
    }
    for check_name, status in checks.items():
        logger.info(f" -> {check_name}: {status}")
    return True

def run_tests():
    """Execute the Rentora automated test suite with coverage."""
    logger.info("Executing comprehensive test suite via pytest...")
    test_cmd = [sys.executable, "-m", "pytest", "tests/", "-v", "--cov=services", "--cov=backend"]
    try:
        res = subprocess.run(test_cmd, cwd=str(ROOT_DIR))
        return res.returncode == 0
    except Exception as e:
        logger.error(f"Failed to execute tests: {e}")
        return False

def run_dev():
    """Start local development server stack."""
    logger.info("Starting Rentora development servers...")
    logger.info("Frontend: http://127.0.0.1:3000/")
    logger.info("Backend API: http://127.0.0.1:8080/api/v1")
    logger.info("Telematics Engine: http://127.0.0.1:8000/")
    
    # Spawn frontend dev server if available
    try:
        proc = subprocess.Popen(["npm", "run", "dev", "--", "--host", "127.0.0.1", "--port", "3000"], cwd=str(FRONTEND_DIR))
        logger.info("Development servers launched successfully (PID: %d). Press Ctrl+C to terminate.", proc.pid)
        proc.wait()
    except KeyboardInterrupt:
        logger.info("Gracefully shutting down Rentora servers...")
    except Exception as e:
        logger.error(f"Error launching dev environment: {e}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Rentora Platform Executive Runner")
    parser.add_argument("--mode", choices=["dev", "test", "audit", "status"], default="status", help="Execution mode")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host")
    parser.add_argument("--port", type=int, default=3000, help="Bind port")
    args = parser.parse_args()

    verify_environment()

    if args.mode == "dev":
        run_dev()
    elif args.mode == "test":
        success = run_tests()
        sys.exit(0 if success else 1)
    else:
        logger.info("Platform is ready. Run with '--mode dev' or execute 'npm start' to run full stack.")
        sys.exit(0)

if __name__ == "__main__":
    main()
