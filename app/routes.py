from fastapi import APIRouter, HTTPException
from pymongo import MongoClient, ASCENDING, DESCENDING, UpdateOne
from app.models import Course, Chapter
from app.connections import get_courses_collection
from app.utils import serialize_doc
course_router = APIRouter()


# Connect to MongoDB
def get_collection():
    return get_courses_collection()


courses_collection = get_collection()


# Endpoint to get a list of all available courses
@course_router.get("/courses")
def get_courses(sort_by: str = "name", domain: str = None):

    query = {}
    if domain:
        query['domain'] = domain

    if sort_by == "name":
        sort_field = "name"
        order = ASCENDING
    elif sort_by == "date":
        sort_field = "date"
        order = DESCENDING
    elif sort_by == "rating":
        sort_field = "rating"
        order = DESCENDING
    else:
        raise HTTPException(status_code=400, detail="Invalid sort parameter")

    courses = list(courses_collection.find(query).sort(sort_field, order))
    serialized_courses = [serialize_doc(course) for course in courses]

    return serialized_courses


# Endpoint to get the course overview
@course_router.get("/courses/{course_id}")
def get_course_overview(course_id: str):
    course = courses_collection.find_one({"_id": course_id})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


# Endpoint to get specific chapter information
@course_router.get("/courses/{course_id}/chapters/{chapter_id}")
def get_chapter_info(course_id: str, chapter_id: int):
    course = courses_collection.find_one({"_id": course_id})
    if not course or chapter_id >= len(course['chapters']):
        raise HTTPException(status_code=404, detail="Chapter not found")
    return course['chapters'][chapter_id]


# Endpoint to rate a chapter
@course_router.post("/courses/{course_id}/chapters/{chapter_id}/rate")
def rate_chapter(course_id: str, chapter_id: int, rating: str):
    if rating not in ["positive", "negative"]:
        raise HTTPException(status_code=400, detail="Invalid rating value")

    # Find the course and validate the chapter
    course = courses_collection.find_one({"_id": course_id})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    if chapter_id < 0 or chapter_id >= len(course['chapters']):
        raise HTTPException(status_code=404, detail="Chapter not found")

    # Update the rating of the specific chapter
    chapter_key = f"chapters.{chapter_id}.ratings.{rating}"
    course_key = f"total_rating.{rating}"

    update_operations = [
        UpdateOne(
            {"_id": course_id},
            {"$inc": {chapter_key: 1, course_key: 1}}
        )
    ]

    courses_collection.bulk_write(update_operations)

    return {"message": "Rating submitted successfully"}
