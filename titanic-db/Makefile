all:
	docker build -t titanic-db .
	docker run -e POSTGRES_PASSWORD=password -e POSTGRES_HOST_AUTH_METHOD='trust' -p 5432:5432 -it -d --rm --name titanic-db titanic-db