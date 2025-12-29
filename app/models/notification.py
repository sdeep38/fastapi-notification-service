from typing import Optional
from pydantic import BaseModel


class Notification(BaseModel):
    id: Optional[int] = None
    user_id: str
    message: str
    type: str = "info"
    read: bool = False

    class Config:
        from_attributes = True  # allows returning ORM objects directly
