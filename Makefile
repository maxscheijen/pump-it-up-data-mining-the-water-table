all: data

lint:
	flake8 src/

raw_data:
	@echo Make raw dataset...
	@python3 src/data/make_dataset.py
 