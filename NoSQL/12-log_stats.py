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
    document_count = logs.nginx.count_()
    print(f"{document_count} logs")