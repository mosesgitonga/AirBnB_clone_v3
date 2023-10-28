#!/usr/bin/python3
"""
register blueprint
"""

from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify

app = Flask(__name__)
#make json printing beautiful
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(err):
    """
    teardown
    """
    storage.close()


@app.errorhandler(404)
def handle_404(error):
    """
    handle 404 errors(page not found)
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    import os 
    host = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    port = os.getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=int(port), threaded=True)
