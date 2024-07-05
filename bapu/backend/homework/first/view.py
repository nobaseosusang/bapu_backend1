from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models import SetBapRequest, MenuResponse, Meal
import controller

router = APIRouter()

@router.post("/api/set/bap", response_model=MenuResponse)
async def set_bap(request: SetBapRequest, db: Session = Depends(get_db)):
    for menu_name in request.menus:
        controller.create_menu(db=db, rest_name=request.rest_name, meal_type=request.meal_type, menu_name=menu_name, date=request.date)
    return {"results": request}

@router.get("/api/get/bap/{start_time}/{end_time}", response_model=MenuResponse)
async def get_bap(start_time: datetime, end_time: datetime, db: Session = Depends(get_db)):
    menus = controller.getmenu(db=db, start_date=start_time, end_date=end_time)
    if not menus:
        raise HTTPException(status_code=404, detail="밥없어유")
    result = {}
    for menu in menus:
        if (menu.date, menu.meal_type, menu.rest_name) not in result:
            result[(menu.date, menu.meal_type, menu.rest_name)] = []
        result[(menu.date, menu.meal_type, menu.rest_name)].append(menu.menu_name)
    
    meals = [Meal(date=i[0], meal_type=i[1], rest_name=i[2], menus=j) for i, j in result.items()]
    return {"results": meals}
