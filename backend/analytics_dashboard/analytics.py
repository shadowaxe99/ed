```python
import psycopg2
from psycopg2 import sql
from flask import Flask, jsonify

app = Flask(__name__)

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="influencer_db",
        user="admin",
        password="password"
    )
    return conn

@app.route('/analytics/', methods=['GET'])
def get_analytics():
    conn = connect_db()
    cur = conn.cursor()

    query = sql.SQL("SELECT * FROM analytics")
    cur.execute(query)

    rows = cur.fetchall()

    analytics_data = []
    for row in rows:
        analytics_data.append({
            'analytics_id': row[0],
            'user_id': row[1],
            'brand_id': row[2],
            'partnership_id': row[3],
            'email_id': row[4],
            'event': row[5],
            'timestamp': row[6]
        })

    return jsonify(analytics_data)

if __name__ == '__main__':
    app.run(debug=True)
```