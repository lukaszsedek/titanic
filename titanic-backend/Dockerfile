FROM python:3.9-alpine3.13

WORKDIR /app

EXPOSE 8081

COPY . .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]