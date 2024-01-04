# Run | Clean | In

clean:
	docker compose down -v

run: 
	docker compose up --build -d

restart: clean run

in:
	docker exec -it api /bin/bash

# Test

black:
	poetry run black -l 79 .

lint:
	poetry run flake8 --config setup.cfg tests src;

types:
	poetry run mypy tests src

unittests:
	poetry run pytest -s tests

coverage:
	poetry run coverage run src/main.py && poetry run coverage report

test: black lint types unittests coverage

# Migrations

migrations:
	docker exec -it api poetry run alembic revision --autogenerate -m "Database creation"

upgrade:
	docker exec -it api poetry run alembic upgrade ${rev}

downgrade:
	docker exec -it api poetry run alembic downgrade ${rev}

permissions:
	chmod 777 src/migrations/versions/*.py