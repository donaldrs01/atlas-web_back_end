#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
from typing import TypeVar
from models.user import User
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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        Extracts user email / password from the decoded Base64 string

        Returns:
        - None, None if decoded auth header is None
        - None, None if decoded auth header is not a string
        - None, None is decoded auth header doesn't contain ':'
        - On success, returns the user's email address and password
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None
        # use split command to split input string at first colon
        email, password = decoded_base64_authorization_header.split(":", 1)

        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar("User"):
        """
        Based on inputted email and password, returns the appropriate 'User'
        instance

        Returns:
        - None if user_email is None or not a string
        - None if user_pwd is None or not a string
        - None if DB doesn't contain matching User instance
        - None if user_pwd does not match the password of the User
        - On success, return correct User instance
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
            if not users or len(users) == 0:
                return None
            # loop through users to check for password match
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
                return None  # return None if no matching user identified
        except Exception as e:
            return None
    
    def current_user(self, request=None) -> TypeVar("User"):
        """
        After receiving auth request, retrieves the appropriate User instance
        """
        # Retrieve authorization header from request
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        # Extract Base64 section of auth_header
        base64_part = self.extract_base64_authorization_header(auth_header)
        if base64_part is None:
            return None
        # Decode the Base64 section
        decoded_auth_header = self.decode_base64_authorization_header(base64_part)
        if decoded_auth_header is None:
            return None
        # Extract email and password from decoded auth header
        user_email, user_password = self.extract_user_credentials(decoded_auth_header)
        if user_email is None or user_password is None:
            return None
        # Retrieve user instance based on pw/email match
        return self.user_object_from_credentials(user_email, user_password)

