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

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def count():
    """
    count num of obj
    """
    from models import storage
    return jsonify({
                  "amenities": storage.count('Amenity'), 
                  "cities": storage.count('City'), 
                  "places": storage.count('Place'), 
                  "reviews": storage.count('Review'), 
                  "states": storage.count('State'), 
                  "users": storage.count('User')
                    })    
