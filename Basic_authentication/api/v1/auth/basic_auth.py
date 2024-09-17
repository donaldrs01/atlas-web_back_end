#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth class
    """
    pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """
        Decodes Base64 part of auth header

        Returns:
        - None if base64 auth header is None
        - None if base64 auth header is not a string
        - None if base64 auth header is not a valid Base64 string
        - On success, the decoded value as UTF-8 string
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode Base64 string
            decoded_string = base64.b64decode(base64_authorization_header)
            # Convert into UTF-8 string
            return decoded_string.decode('utf-8')
        except (UnicodeDecodeError):
            return None  # return None in case of decoding error
