from unicodedata import decimal
import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/v1/cart/session")
def get_session_id():
    return JSONResponse(content=[{'session_id':str(uuid.uuid4())}])

@app.get("/v1/cart/items/{session_id}")
def get_items(session_id:str):
    return JSONResponse(content=[{'item_id':21215,'item_name':'simple product','quantity':2, 'price': 223.14},{'item_id':21210,'item_name':'other product','quantity':1, 'price': 2501.99}])

@app.get("/v1/cart/items/count/{session_id}")
def get_items_count(session_id:str):
    return JSONResponse(content=[{'items':3,'unique_items':2}])

@app.get("/v1/cart/sum/{session_id}")
def get_sum(session_id:str):
    return JSONResponse(content=[{'sum':3540}])


class Item(BaseModel):
    item_id: int
    item_name: str
    quantity: int
    price: float

class Items(BaseModel):
    items: List[Item]
    session_id: str

@app.post("/v1/cart/items/add")
def add_items(items: Items, session_id: str = 0):
    return JSONResponse(content=[{'result':'ok'}])

@app.delete("/v1/cart/removeall")
def remove_all(session_id: str):
    return JSONResponse(content=[{'result':'ok'}])


class DeleteItem(BaseModel):
    item_id: int

class DeleteItems(BaseModel):
    items: List[DeleteItem]
    session_id: str

@app.delete("/v1/cart/items/delete")
def delete_items(delete_items: DeleteItems, session_id: str):
    return JSONResponse(content=[{'result':'ok','items':2,'unique_items':1,'sum':2345, 'cart':[{'item_id':21215,'item_name':'simple product','quantity':2, 'price': 223.14},{'item_id':21210,'item_name':'other product','quantity':1, 'price': 2501.99}]}])

@app.patch("/v1/cart/item/increment")
def increment_item(item_id: int, session_id: str, increment: int =1):
    return JSONResponse(content=[{'result':'ok','items':2,'unique_items':1,'sum':2345, 'cart':[{'item_id':21215,'item_name':'simple product','quantity':2, 'price': 223.14},{'item_id':21210,'item_name':'other product','quantity':1, 'price': 2501.99}]}])

@app.patch("/v1/cart/item/decrement")
def decrement_item(item_id: int, session_id: str, decrement: int =1):
    return JSONResponse(content=[{'result':'ok','items':3,'unique_items':3,'sum':6745, 'cart':[{'item_id':21215,'item_name':'simple product','quantity':2, 'price': 223.14},{'item_id':21210,'item_name':'other product','quantity':1, 'price': 2501.99}]}])





