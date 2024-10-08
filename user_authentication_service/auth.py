#!/usr/bin/env python3
"""
Module containig authentication logic
"""
from db import DB
from user import Base, User
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Class method that registers a user based on
        email and pw input args
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Function checking for valid login credentials
        and returns boolean based on result
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode("utf-8"), user.hashed_password):
                return True
        except NoResultFound:
            return False
        # return False on any other exception or if password doesn't match
        return False

    def create_session(self, email: str) -> str:
        """
        Function that takes in user email and returns
        their session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            return user.session_id
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """
    Function that hashes password and returns in
    byte representation
    """
    byte_password = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())
    return hashed_password


def _generate_uuid() -> str:
    """
    Generates new UUID for user registration
    """
    return str(uuid.uuid4())
