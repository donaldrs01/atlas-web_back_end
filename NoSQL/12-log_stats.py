#!/usr/bin/env python3
"""
Module for function that displays log stats
"""
from pymongo import MongoClient

instance = MongoClient()

def log_stats():
    """
    Function that performs various operations and displays Nginx logs
    """
    db = instance.logs
    collection = db.nginx

    document_count = collection.count_documents({})
    print(f"{document_count} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:

