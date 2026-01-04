from fastapi import APIRouter, Depends, HTTPException, WebSocket
from sqlalchemy.orm import Session
from app.db import models
from app.db.session import SessionLocal
from app.models.notification import Notification
from app.services.notifier import send_notification

router = APIRouter(prefix="/notify", tags=["notifications"])

# Dependency to get DB session 
def get_db(): 
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close()

@router.websocket("/ws/{user_id}") 
async def websocket_endpoint(websocket: WebSocket, user_id: str): 
    await websocket.accept() 
    await websocket.send_text(f"Connected: {user_id}")
    
# New Added

@router.post("/", response_model=Notification)
def create_notification(notification: Notification, db: Session = Depends(get_db)):
    db_notification = models.NotificationORM(
        user_id=notification.user_id,
        message=notification.message,
        type=notification.type,
        read=notification.read
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.get("/list", response_model=list[Notification])
def list_notifications(db: Session = Depends(get_db)):
    return db.query(models.NotificationORM).all()

@router.get("/{notification_id}", response_model=Notification)
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    n = db.query(models.NotificationORM).filter(models.NotificationORM.id == notification_id).first()
    if not n:
        raise HTTPException(status_code=404, detail="Notification not found")
    return n

@router.get("/user/{user_id}")
def get_user_notifications(user_id: str, db: Session = Depends(get_db)):
    return db.query(models.NotificationORM).filter(models.NotificationORM.user_id == user_id).all()

@router.put("/{notification_id}/read", response_model=Notification)
def mark_as_read(notification_id: int, db: Session = Depends(get_db)):
    notif = db.query(models.NotificationORM).filter(models.NotificationORM.id == notification_id).first()
    if not notif:
        raise HTTPException(status_code=404, detail="Notification not found")
    notif.read = True
    db.commit()
    db.refresh(notif)
    return notif


@router.put("/{notification_id}", response_model=Notification)
def update_notification(notification_id: int, updated: Notification, db: Session = Depends(get_db)):
    n = db.query(models.NotificationORM).filter(models.NotificationORM.id == notification_id).first()
    if not n:
        raise HTTPException(status_code=404, detail="Notification not found")
    n.user_id = updated.user_id
    n.message = updated.message
    n.type = updated.type
    n.read = updated.read
    db.commit()
    db.refresh(n)
    return n

@router.delete("/{notification_id}")
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    n = db.query(models.NotificationORM).filter(models.NotificationORM.id == notification_id).first()
    if not n:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(n)
    db.commit()
    return {"status": "deleted"}