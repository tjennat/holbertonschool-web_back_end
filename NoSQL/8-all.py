#!/usr/bin/env python3
""" func that's gonna list_all"""


def list_all(mango_collection):
    """Return a list of all documents in a collection"""
    return list(mango_collection.find())
    