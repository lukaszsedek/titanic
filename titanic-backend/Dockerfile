FROM python:3.9-alpine3.13

WORKDIR /app

EXPOSE 8081

COPY titanic-backend/ .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]