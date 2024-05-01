#!/usr/bin/env python3
"""Function schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """func that's gonna returns the list of schools having a specific topic"""
    return mongo_collection.find({"topics": topic})