SHELL := /bin/bash
PY = ./.venv/bin/python

help: ## List available commands
		@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

create: ## Ask the user for a todo details, and save it to the database
		${PY} scripts/create_todo.py

json: ## Export all todos from the database to "./export/todos.json"
		${PY} scripts/export.py

list: ## Display all todos on a table
		${PY} scripts/todos_list.py

remaining: ## Display remaining todos on a table
		${PY} scripts/todos_remaining.py

piechart: ## Display a pie chart that shows todos status
		${PY} scripts/todos_piechart.py

finish: ## Set the state of a choosen todo as 'done' 
		${PY} scripts/finish_todo.py