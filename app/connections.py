from pymongo import MongoClient
from fastapi import Depends

# Initialize MongoDB client
client = None


def get_mongo_client():
    global client
    if not client:
        client = MongoClient('mongodb://mongodb:27017/')
    return client


def get_courses_collection():
    client = get_mongo_client()
    db = client['course_database']
    return db['courses']


def close_mongo_connection():
    global client
    if client:
        client.close()
        client = None
