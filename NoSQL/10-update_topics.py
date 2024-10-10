#!/usr/bin/env python3
"""
Module for function that changes topic
"""
from pymongo import MongoClient

client = MongoClient()

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )