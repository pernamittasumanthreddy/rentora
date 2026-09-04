# ==============================================================================
# Rentora Platform Automation Makefile
# ==============================================================================

.PHONY: all build run test lint clean docker-up docker-down help

PYTHON ?= python
NPM ?= npm
MVN ?= mvn

all: build

help:
	@echo "Rentora Build & Operations Commands:"
	@echo "  make build       - Build frontend bundle and backend JAR"
	@echo "  make run         - Run the Rentora platform via unified runner"
	@echo "  make test        - Run test suite with pytest and junit"
	@echo "  make lint        - Run linting across frontend and backend"
	@echo "  make clean       - Remove build artifacts and temporary files"
	@echo "  make docker-up   - Launch multi-service stack with Docker Compose"
	@echo "  make docker-down - Stop Docker Compose stack"

build:
	@echo "--> Building Frontend..."
	cd frontend && $(NPM) run build
	@echo "--> Building Backend..."
	cd backend && $(MVN) clean package -DskipTests
	@echo "--> Build Complete."

run:
	$(PYTHON) app.py

test:
	$(PYTHON) -m pytest tests/ -v --cov=services --cov=backend

lint:
	cd frontend && $(NPM) run lint --if-present

clean:
	rm -rf frontend/dist backend/target .pytest_cache htmlcov .coverage
	@echo "--> Cleaned successfully."

docker-up:
	docker-compose up -d --build

docker-down:
	docker-compose down -v
