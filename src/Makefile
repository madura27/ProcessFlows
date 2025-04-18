.PHONY: test

default: test

run:
	PYTHONPATH=. python3 main.py

test:
	PYTHONPATH=. pytest -s

test-filter:
	PYTHONPATH=. pytest -s -k $(FILTER)

clean:
	rm -rf ../output_files/*
