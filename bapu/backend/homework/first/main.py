from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

class SetBapRequest(BaseModel):
    rest_name: str
    menus: List[str]

class MenuResponse(BaseModel):
    menus: List[str]


@app.post("/api/set/bap")
async def set_bap(request: SetBapRequest, db: Session = Depends(get_db)):
    for menu_name in request.menus:
        menu = models.Menu(rest_name=request.rest_name, menu_name=menu_name)
        db.add(menu)
    db.commit()

@app.get("/api/get/bap/{rest_name}", response_model=MenuResponse)
async def get_bap(rest_name: str, db: Session = Depends(get_db)):
    menus = db.query(models.Menu).filter(models.Menu.rest_name == rest_name).all()
    if not menus:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    menu_names = [menu.menu_name for menu in menus]
    return MenuResponse(menus=menu_names)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)