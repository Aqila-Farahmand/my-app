from flask import Flask
import redis
import os

app = Flask(__name__)

#establish connection to Redis

r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)

@app.route('/')
def hello_world():
    # Fetch the name from Redis
    name = r.get('name')
    if name is None:
        return "Name not found in the database."
    return f"Hello world, {name.decode('utf-8')}!"

if __name__ == '__main__':
    app.run()


