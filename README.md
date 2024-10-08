# FastAPI Course API

This repository contains a back-end API for serving course information using FastAPI and MongoDB. The API handles requests from the front-end application, retrieves course information from a MongoDB database, and returns the relevant data in a standardized format.

## Features

- Retrieve a list of all available courses with sorting options (alphabetical, date, total course rating).
- Get an overview of a specific course.
- Get specific chapter information from a course.
- Rate each chapter (positive/negative), with aggregated ratings for each course.

## Project Structure
course_api/ │ ├── app/ │ ├── init.py │ ├── main.py │ ├── models.py │ ├── routes.py │ └── utils.py │ ├── data/ │ └── courses.json │ ├── scripts/ │ └── load_courses.py │ ├── Dockerfile ├── docker-compose.yml ├── requirements.txt └── tests/ ├── init.py └── test_app.py

## Getting Started

### Prerequisites

- Python 3.7+
- MongoDB (locally or via Docker)
- Docker and Docker Compose (if you prefer running the application in Docker)
- `pip` (Python package installer)



### Installation

1. **Clone the repository:**

   ```bash
   https://github.com/SonuCodeCrafter/courses-mangement.git
   cd course-api
2. **Install dependencies:**

    ```bash
   pip install -r requirements.txt
   
3. **Load initial course data into MongoDB:**
4. **Running the Application**
    ```bash
   docker-compose up --build
