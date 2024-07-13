from fastapi import FastAPI
from database import engine
import models
import view

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(view.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)