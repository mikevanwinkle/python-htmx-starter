dev:
	uvicorn main:app --port 8082 --reload
test:
	./bin/python -m pytest ./test
