from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from models import Menu, MealType

def create_menu(db: Session, rest_name: str, meal_type: MealType, menu_name: str, date: datetime):
    menu = Menu(rest_name=rest_name, meal_type=meal_type, menu_name=menu_name, date=date)
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu

def getmenu(db: Session, start_date: datetime, end_date: datetime):
    return db.query(Menu).filter(Menu.date >= start_date, Menu.date <= end_date).all()
