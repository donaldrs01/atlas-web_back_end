#!/usr/bin/env python3
"""
Module for function logic to return list with given topic attribute
"""
from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """
    Function that returns list of schools having a specific topic
    """
    school_list = []
    for school in mongo_collection.find({"topics": topic}):
        school_list.append(school)
    
    return school_list
