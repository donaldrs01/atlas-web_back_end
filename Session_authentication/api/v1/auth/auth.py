#!/usr/bin/env python3
"""
    Module for the Auth class
"""
import os
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class to handle API authentication process
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if path arg requires user authentication
        - Returns True if path is None
        - Returns True if excluded_paths arg is None or empty
        - Returns False if path is on list of exclused_paths
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Slash tolerance
        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False
        # if none of these checks are met, require user auth
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns none. Request arg is Flask request object
        """
        if request is None:
            return None
        # Check for presence of auth header
        if "Authorization" not in request.headers:
            return None
        # Return authorization header value
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Returns none. Request arg is Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns value of session cookie from request

        Args:
        - request: the request object containing cookie information

        Returns:
        - The value of the session cookie
        """
        if request is None:
            return None
        # retrieve session name from the env variable
        session_name = os.getenv("SESSION_NAME", "my_session_id")
        # return value of session cookie
        return request.cookies.get(session_name)
