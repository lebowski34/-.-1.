from .db import SessionLocal
from typing import AsyncIterator
from fastapi import Depends

async def get_db() -> AsyncIterator[SessionLocal]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
