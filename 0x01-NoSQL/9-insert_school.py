#!/usr/bin/env python3
"""insert a new document in a collection"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """  args: mongo _collection
    return: id
    """
    new_school = mongo_collection.insert_one(kwargs)

    return (new_school.inserted_id)
