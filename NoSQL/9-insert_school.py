#!/usr/bin/env python3
"""
Module for function logic to insert new document into mongo_collection
"""
from pymongo import MongoClient

instance = MongoClient()

def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a document into mogno_collection
    and returns the new doc ID
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id

