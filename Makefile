run:
	docker compose up -d --build

run_prod:
	docker compose -f docker-compose.prod.yml up -d --build

bash:
	docker compose exec -it api bash

bash_prod:
	docker compose -f docker-compose.prod.yml exec -it api bash
