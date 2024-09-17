#!/usr/bin/env python3
"""
    Module for the Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class to handle API authentication process
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Just returns false
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns none. Request arg is Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Returns none. Request arg is Flask request object
        """
        return None
