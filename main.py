from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model untuk data
class Item(BaseModel):
    id: int
    name: str
    description: str

# Tempat penyimpanan data sementara (in-memory)
items: List[Item] = []

# Endpoint untuk menambahkan item
@app.post("/items/", response_model=Item)
def add_item(item: Item):
    items.append(item)
    return item

# Endpoint untuk menampilkan semua item
@app.get("/items/", response_model=List[Item])
def get_items():
    return items

