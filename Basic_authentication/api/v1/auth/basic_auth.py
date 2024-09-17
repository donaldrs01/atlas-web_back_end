#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth class
    """
    pass

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Function that extracts Base64 part of auth header

        Returns:
        - None if auth_header is None
        - None if auth_header is not a string
        - None if auth_header doesn't start with "basic"
        - The Base64 part of "basic" otherwise
        """
        if authorization_header is None:
            return None
        
        # check that authorization_header is string
        if not isinstance(authorization_header, str):
            return None
        
        # use 'startswith' to check beginning of string
        if not authorization_header.startswith("Basic "):
            return None
        
        # return the part after "Basic "
        # extracts substring from after the space 
        return authorization_header[len("Basic "):]
