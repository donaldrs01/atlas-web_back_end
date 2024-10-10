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

    document_count = db.nginx.count_documents({})
    print(f"{document_count} logs")