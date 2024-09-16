#!/usr/bin/env python3
"""
Module that contains hash_password function
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function that hashes a password (passed as str)
    using bcrypt

    Args:
        password (str) : the password to be hashed

    Returns:
        bytes: password that has been salted and hashed
    """
    # convert password to bytes
    bytes_pw = password.encode("utf-8")
    # hash the password with randomnly-generated salt
    hashed_pw = bcrypt.hashpw(bytes_pw, bcrypt.gensalt())

    return hashed_pw


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Function that verifies that hashed pw matches original pw

    Args:
        hashed_password (bytes) : the hashed version of the pw
        password (str) : original password in plain text

    Returns:
        bool: True if match, False otherwise
    """
    # convert password to hashed version
    bytes_pw = password.encode("utf-8")
    # bcrypt validation that returns bool value
    return bcrypt.checkpw(bytes_pw, hashed_password)
