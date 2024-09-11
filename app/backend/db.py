from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine("sqlite:///taskmanager.db", echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    from app.models import user, task
    Base.metadata.create_all(bind=engine)
