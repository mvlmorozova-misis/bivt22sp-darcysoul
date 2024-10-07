# Makefile

PYTHON = python3
LINTER = flake8

lint:
	$(LINTER) .

run:
	$(PYTHON) -m src.brain-games

clean:
	find . -name "__pycache__" -exec rm -r {} +

# По умолчанию запустить линтер и игру "Brain Games"
run_lint: lint run
