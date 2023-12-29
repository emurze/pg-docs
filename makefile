
clean:
	docker compose down -v

run: 
	docker compose up --build -d

restart: clean run

in:
	docker exec -it db /bin/bash
