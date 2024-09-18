#!/usr/bin/env python3
"""
Module for SessionAuth class
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session authentication class who has parent Auth
    """
    # Class attribute that maps session IDs to user_ids
    user_id_by_session_id = {}


    def create_session(self, user_id: str = None) -> str:
        """
        Instance method that creates a session ID for each user_id

        Args:
        - user_id (str) : the user's ID

        Returns:
        - The session ID or None
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        # store session ID mapped to the user_ID in dictionary
        self.user_id_by_session_id.update({session_id: user_id})
    
        return session_id


