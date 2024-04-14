FROM python:3.9-alpine3.13

WORKDIR /app

EXPOSE 8081

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]