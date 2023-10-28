#!/usr/bin/python3
"""
create a route /status on the object app_views that returns a JSON
"""
from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def  ok_status():
    """
    ok status
    """
    status = {
                "status": "OK"
              }
    return jsonify(status)
    
