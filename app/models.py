from typing import List
from pydantic import BaseModel


class Chapter(BaseModel):
    title: str
    contents: str


class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]
