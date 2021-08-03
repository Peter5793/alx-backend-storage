#!/usr/bin/env python3
""" list all documents in a collections"""
import pymongo


def list_all(mongo_collection) -> list:
    """ function that list all the documents
    """
    documents: list = []

    for i in mongo_collection.find():
        documents.append(i)

    return i
