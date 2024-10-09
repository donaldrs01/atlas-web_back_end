#!/usr/bin/env python3
"""
Module containing function logic for listing all documents in MongoDB collection
"""
from pymongo import MongoClient

instance = MongoClient()

def list_all(mongo_collection):
    """
    Returns a list of all documents in the mongo_collection
    """
    return list(mongo_collection.find({}))