from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random

from pydantic import BaseModel, Field

from app.api import notification
from app.db.session import Base, engine
from app.models.notification import Notification

app = FastAPI(title="Notification Service")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )

@app.get("/")
def root():
    return {"message": "Notification service running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Create tables on startup 
Base.metadata.create_all(bind=engine)
app.include_router(notification.router)
# items_db = []

# class Item(BaseModel):
#     name: str = Field(
#         min_length = 1,
#         max_length = 100,
#         description = "Item Name"
#     )
# @app.get("/")
# def home():
#     return {"message": "Welcome to the Randomizer API"}


# @app.get("/random/{max_value}")
# def get_random_number(max_value: int):
#     return {"max": max_value, "random_number": random.randint(1, max_value)}


# @app.post("/items")
# def add_item(item: Item):
#     if item.name in items_db:
#         raise HTTPException(status_code=400, detail="Item already exists")

#     items_db.append(item.name)
#     return {
#         "message": "Item added successfully",
#         "item": item.name
#     }


# @app.put("/items/{update_item_name}")
# def update_item(update_item_name: str, item: Item):
#     if update_item_name not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")

#     if item.name in items_db:
#         raise HTTPException(
#             status_code=409, detail="An item with that name already exists"
#         )

#     index = items_db.index(update_item_name)
#     items_db[index] = item.name

#     return {
#         "message": "Item updated successfully",
#         "old_item": update_item_name,
#         "new_item": item.name,
#     }

# @app.delete("/items/{item}")
# def delete_item(item: str):
#     if item not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")

#     items_db.remove(item)

#     return {
#         "message": "Item deleted successfully",
#         "deleted_item": item,
#         "remaining_items_count": len(items_db),
#     }
