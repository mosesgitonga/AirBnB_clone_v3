#!/usr/bin/python3
"""
create a route /status on the object app_views that returns a JSON
"""
from api.v1.views import app_views
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', strict_slashes=False)
def  ok_status():
    status = {
                "status": "ok"
              }
    return jsonify(status)
    
