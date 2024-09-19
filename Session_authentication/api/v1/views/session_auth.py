#!/usr/bin/env python3
"""
Module that contains Flask view for routes related to
Session authentication
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User

@app_views.route('/auth_session/login', methods=["POST"], strict_slashes=False)
def user_login():
    """
    Function that handles user login
    """
    # pull user email/password from session request
    email = request.form.get("email")
    password = request.form.get("password")

    # validate
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    # check for email and retrieve associated user
    user = User.search({"email": email})
    if not user or len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    # check to make sure password matches the user
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    

    