clean-pycache:
	find ./ -type d -name '__pycache__' -exec rm -rf {} +

get-data:
	wget -O data/label.csv https://raw.githubusercontent.com/wayfair/WANDS/main/dataset/label.csv 
	wget -O data/product.csv https://raw.githubusercontent.com/wayfair/WANDS/main/dataset/product.csv 
	wget -O data/query.csv https://raw.githubusercontent.com/wayfair/WANDS/main/dataset/query.csv

lint:
	poetry run ruff check src/* --fix 

format:
	poetry run ruff format src/*

imports:
	poetry run ruff check src/* --select I --fix

pretty:
	$(MAKE) lint
	$(MAKE) format
	$(MAKE) imports