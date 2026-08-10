pip install black pylint pre-commit mypy
black --help
black myfile.py
pylint my_file.py  #Gives a score. Can say code quality must be x or higher. Can define own custom rules. Notice it didn't actually fix anything.
pylint --help
mypy my_file.py  #Checks types.

pre-commit #Creates a .pre-commit-config.yaml file.
#Pre-commit hooks are a way to prevent bad code from ever entering your code by running pre-commit hooks. Hooks can include formatters, linters, etc. Can do pre-push hooks.