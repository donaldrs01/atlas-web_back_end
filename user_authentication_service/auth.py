#!/usr/bin/env python3
"""
Module containig authentication logic
"""
from db import DB
from user import Base, User
import bcrypt
from sqlalchemy.orm.exc import NoResultFound


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
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user



    def _hash_password(self, password: str) -> bytes:
        """
        Function that hashes password and returns in
        byte representation
        """
        byte_password = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())
        return hashed_password
    
