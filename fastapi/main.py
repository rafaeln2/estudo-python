from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#check universal http responses for the stat codes
app = FastAPI()

class Item(BaseModel):
    text: str #retirar o valor base ativa not null no campo
    is_done: bool = False

@app.get("/")
def root():
    return {"message": "Hello World"}

items = []

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]
    raise HTTPException(status_code=404, detail="Item not found")
#{"error": "Item not found"}

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")
#{"error": "Item not found"}

def root():
    return {"message": "Hello World"}
