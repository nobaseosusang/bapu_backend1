from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from enum import Enum as PyEnum
from pydantic import BaseModel
from typing import List
from datetime import datetime

Base = declarative_base()

class MealType(PyEnum):
    BREAKFAST = "BREAKFAST"
    LAUNCH = "LAUNCH"
    DINNER = "DINNER"

class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=func.now(), nullable=False)
    meal_type = Column(Enum(MealType), nullable=False)
    rest_name = Column(String, index=True, nullable=False)
    menu_name = Column(String, index=True, nullable=False)

class SetBapRequest(BaseModel):
    date: datetime
    meal_type: MealType
    rest_name: str
    menus: List[str]

class Meal(BaseModel):
    date: datetime
    meal_type: MealType
    rest_name: str
    menus: List[str]

class MenuResponse(BaseModel):
    results: List[Meal]
