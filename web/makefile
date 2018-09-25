.PHONY : build nc run runlocal rm
build:
	docker build -t ech6:latest .
nc:
	docker build --no-cache -t ech6:latest .

run: rm
	docker run --name ech -d -p 80:5000 ech6:latest

rm:
	@docker kill ech >/dev/null 2>/dev/null || true 
	@docker rm ech >/dev/null 2>/dev/null || true 

runlocal:
	sh run_app.sh
