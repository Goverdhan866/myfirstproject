#!/usr/bin/env python3
import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (make sure MongoDB is running on the same network or container)
client = MongoClient("mongo:27017")

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except Exception as e:
        return f"Server not available: {str(e)}"
    return "Hello from the MongoDB client!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("FLASK_SERVER_PORT", 9090)), debug=True)
