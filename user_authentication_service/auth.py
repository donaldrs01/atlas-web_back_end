#!/usr/bin/env python3
"""
Module containig authentication logic
"""
from db import DB
from user import Base, User
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Function that hashes password and returns in
    byte representation
    """
    byte_password = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())
    return hashed_password
