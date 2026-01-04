from sqlalchemy import Column, DateTime, Integer, String, Boolean, func
from app.db.session import Base

class NotificationORM(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(String(50), nullable=False)
    message = Column(String(255), nullable=False)
    type = Column(String(50), default="info")
    read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
