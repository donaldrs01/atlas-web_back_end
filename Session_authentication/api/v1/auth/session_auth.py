#!/usr/bin/env python3
"""
Module for SessionAuth class
"""
from api.v1.auth.auth import Auth
from models.user import User
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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Instance method that returns user_id based on inputted session ID

        Args:
        -session_id (str) : the session ID of the user

        Returns:
        - The user_id of the user corresponding to that session
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        # use .get() to retrieve user_id associated with given session id
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Return user based on session ID retrieved from cookie
        """
        if request is None:
            return None
        
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        
        try:
            user = User.get(user_id)
            if user is None:
                return None
            return user
        except Exception:
            return None