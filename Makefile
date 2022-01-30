SHELL := /bin/bash
PY = ./.venv/bin/python

help: ## List available commands
		@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

new-todo: ## Ask the user for a todo details, and save it to the database
		${PY} scripts/create_todo.py

export-todos: ## Export all todos from the database to "./export/todos.json"
		${PY} scripts/export.py

