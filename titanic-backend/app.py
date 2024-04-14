from flask import Flask
import os
import psycopg2
import json

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'postgres'),
        user=os.getenv('DB_USERNAME', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'password'))
    return conn

# conn.close()

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/status')
def app_status():
    results = {}
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    if cur.fetchone()[0] == 1: results['db_connection_status']="healthy"
    cur.close()
    return json.dumps(results)

@app.route('/passangersAll', methods=['GET'])
def get_all_passangers():
    results = {}
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT passengerid::integer as id, survived::integer, pclass::integer, name, sex FROM titanic;")
    results = cur.fetchall()
    cur.close()
    return json.dumps(results)


@app.route('/passanger/<id>', methods=['GET'])
def get_passenger(id):
    results = {}
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT passengerid::integer as id, survived::integer, pclass::integer, name, sex FROM titanic WHERE passengerid=" + id +";")
    results = cur.fetchall()
    cur.close()
    return json.dumps(results)