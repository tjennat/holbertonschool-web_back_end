#!/usr/bin/env python3
"""Function update_topics"""


def update_topics(mongo_collection, name, topics):
    """func that's gonna changes all topics of a school doc based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
