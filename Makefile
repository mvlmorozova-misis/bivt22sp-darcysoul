# Makefile

PYTHON = python3
LINTER = flake8

lint:
	$(LINTER) .

run:
	$(PYTHON) -m bin.brain_games

clean:
	find . -name "__pycache__" -exec rm -r {} +

# По умолчанию запустить линтер и игру "Brain Games"
run_lint: lint run
