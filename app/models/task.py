from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)  # Исправлено на 'users.id'
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="tasks")

if __name__ == "__main__":
    from sqlalchemy.schema import CreateTable
    from app.models.user import User
    print(CreateTable(Task.__table__))
