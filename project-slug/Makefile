.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry run pre-commit install

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry check --lock
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a

.PHONY: build
build: clean-build ## Build the lambda zip
	@echo "🚀 Building the lambda deployable package"
	@pip install -t dist/lambda .
	@cd dist/lambda
	@zip -x '*.pyc' -r dist/lambda.zip .

.PHONY: clean
clean: clean-test clean-build clean-venv ## clean entire package

.PHONY: clean-venv
clean-venv: ## clean venv
	@rm -rf .venv

.PHONY: clean-test
clean-test: ## clean test artifacts
	@rm -f .coverage
	@rm -f coverage.xml
	@rm -rf .pytest_cache

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml
