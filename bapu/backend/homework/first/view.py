from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple

from database import get_db
from models import SetBapRequest, MenuResponse, Meal, MealType
import controller

router = APIRouter()

@router.post("/api/set/bap", response_model=MenuResponse)
async def set_bap(request: SetBapRequest, db: Session = Depends(get_db)):
    for menu_name in request.menus:
        controller.create_menu(db=db, rest_name=request.rest_name, meal_type=request.meal_type, menu_name=menu_name, date=request.date)
    return {"results": request}

@router.get("/api/get/bap/{start_time}/{end_time}", response_model=MenuResponse)
async def get_bap(start_time: datetime, end_time: datetime, db: Session = Depends(get_db)) -> MenuResponse:
    menus = controller.getmenu(db=db, start_date=start_time, end_date=end_time)
    if not menus:
        raise HTTPException(status_code=404, detail="No menus found")
    
    grouped_menus: Dict[Tuple[datetime, MealType, str], List[str]] = defaultdict(list)
    
    for menu in menus:
        key = (menu.date, menu.meal_type, menu.rest_name)
        grouped_menus[key].append(menu.menu_name) # type: ignore
    
    meals = [Meal(date=key[0], meal_type=key[1], rest_name=key[2], menus=value)
             for key, value in grouped_menus.items()]
    
    return MenuResponse(results=meals)
