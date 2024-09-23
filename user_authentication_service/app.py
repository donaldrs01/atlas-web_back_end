#!/usr/bin/env python3
"""
Basic Flask application
"""
from flask import Flask, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    """
    GET route that returns JSON response
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> str:
    """
    Handles user registration
    """
    email = request.forn.get("email")
    password = request.form.get("password")
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email: f"{email}, "message" "user created"})
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
