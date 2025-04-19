from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Postgres connection details from environment
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)
conn.autocommit = True
cur = conn.cursor()

@app.route('/messages', methods=['POST'])
def write_message():
    data = request.get_json()
    text = data.get('text')
    cur.execute("INSERT INTO messages (text) VALUES (%s)", (text,))
    return jsonify({'status': 'OK', 'message': text}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)