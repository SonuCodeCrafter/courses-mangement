from fastapi import FastAPI
from app.routes import course_router

app = FastAPI()

# Include the course router
app.include_router(course_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
