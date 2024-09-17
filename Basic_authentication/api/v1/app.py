#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
# Import Auth and BasicAuth classes
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Check for authentication type depending on AUTH_TYPE
auth = None  # create auth instance
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == "basic_auth":
    auth = BasicAuth()
else:
    auth = Auth()

# Error handler for forbidden access (403) error
@app.errorhandler(403)
def forbidden_access(error) -> str:
    """
    Forbidden handler for 403 error
    """
    return jsonify({"error": "Forbidden"}), 403


# Error handler for 401 user errors
@app.errorhandler(401)
def unauthorized_user(error) -> str:
    """
    Not found handler for 401 error
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
