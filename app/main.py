from fastapi import FastAPI, Request
from app.routers import user, task


app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)



#python -m uvicorn main:app  uvicorn app.main:app --reload