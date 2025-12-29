from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base

class NotificationORM(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    message = Column(String)
    type = Column(String, default="info")
    read = Column(Boolean, default=False)
