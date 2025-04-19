from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

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
cur = conn.cursor()

@app.route('/messages', methods=['GET'])
def get_messages():
    cur.execute("SELECT id, text FROM messages ORDER BY id DESC LIMIT 10")
    rows = cur.fetchall()
    return jsonify([{'id': r[0], 'text': r[1]} for r in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)