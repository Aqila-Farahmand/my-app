from flask import Flask, g
from pymongo import MongoClient
import os

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db_client = MongoClient(
            host=os.environ.get('DB_HOST', 'db'),
            port=int(os.environ.get('DB_PORT', 27017))
        )
        g.db = g.db_client[os.environ.get('DB_NAME', 'users')]
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db_client = g.pop('db_client', None)
    if db_client is not None:
        db_client.close()

@app.route('/')
def hello_world():
    db = get_db()
    user_data = db.user_data.find_one()
    user_name = user_data['name'] if user_data else 'Unknown'
    return f'Hello world, {user_name}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)