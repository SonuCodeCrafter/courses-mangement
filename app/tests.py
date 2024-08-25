import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rate_chapter_positive():
    response = client.post("/courses/1/chapters/0/rate", json={"rating": "positive"})  # Replace with a valid course_id and chapter_id
    assert response.status_code == 200 or response.status_code == 404
    if response.status_code == 200:
        assert response.json() == {"message": "Rating submitted successfully"}

def test_rate_chapter_invalid_rating():
    response = client.post("/courses/1/chapters/0/rate", json={"rating": "invalid"})  # Replace with a valid course_id and chapter_id
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid rating value"}

def test_rate_chapter_invalid_course():
    response = client.post("/courses/invalid_course_id/chapters/0/rate", json={"rating": "positive"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Course not found"}

def test_rate_chapter_invalid_chapter():
    response = client.post("/courses/1/chapters/999/rate", json={"rating": "positive"})  # Assuming chapter_id 999 does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Chapter not found"}
