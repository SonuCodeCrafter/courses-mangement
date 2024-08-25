import json
import os
from pymongo import MongoClient, ASCENDING, DESCENDING


def load_courses_to_mongo():
    """
    Load Courses to mongo DB
    """

    with open('courses.json', 'r') as file:
        courses_data = json.load(file)

    # 2. Connect to MongoDB and create the database and collection
    client = MongoClient('mongodb://localhost:27017/')
    db = client['course_database']
    courses_collection = db['courses']

    breakpoint()

    # 3. Create indices for efficient retrieval
    courses_collection.create_index([('name', ASCENDING)])  # For alphabetical sorting
    courses_collection.create_index([('date', DESCENDING)])  # For date sorting
    courses_collection.create_index([('rating', DESCENDING)])  # For rating sorting

    # 4. Insert the course data into the collection
    courses_collection.insert_many(courses_data)

    print("Courses data has been loaded into MongoDB successfully.")


if __name__ == "__main__":
    load_courses_to_mongo()
