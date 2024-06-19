#!/usr/bin/env python3
'''
Defines a schools_by_topic function
'''


def schools_by_topic(mongo_collection, topic):
    "Returns the list of school associating with specific topic"""
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
