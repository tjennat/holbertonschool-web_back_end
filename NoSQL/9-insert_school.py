#!/usr/bin/env python3
"""Function insert_school"""


def insert_school(mongo_collection, **kwargs):
    """function that's honna inserts a new doc in a db based on kwargs"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
