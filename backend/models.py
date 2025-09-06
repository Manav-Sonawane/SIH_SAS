# models.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Student(BaseModel):
    id: Optional[int] = None
    name: str
    image_path: Optional[str] = None


class Attendance(BaseModel):
    id: Optional[int] = None
    student_id: int
    name: str
    timestamp: datetime
    status: str = "Present"
