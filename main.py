from fastapi import FastAPI,HTTPException
import sqlite3
from service import getitemsbyid,additems,updateitems,deleteitem,getitemsbytype,getallitems
from pydantic import BaseModel
from typing import Optional


class Additems(BaseModel):
    id : int
    name : str
    price : int
    quantity : int
    type : str


class Updateitens(BaseModel):
    price : Optional[int] = None
    quantity : Optional[int] = None


app=FastAPI()

@app.get('/items/{id}')
def getitem(id:int):
    try :
        items=getitemsbyid(id)
        if not items :
            raise HTTPException(status_code=404,detail="Item Not Found")
        return items
    except HTTPException:
        raise
    except Exception :
        raise HTTPException(status_code=500,detail="Internal Server Error")

@app.get('/items')
def getitems(type:Optional[str]=None):
    try:
        if type:
            items=getitemsbytype(type)
        else:
            items=getallitems()
        if not items:
            raise HTTPException(status_code=404,detail="Item Not Found")
        return items
    except HTTPException:
        raise
    except Exception :
        raise HTTPException(status_code=500,detail="Internal Server Error")
     


@app.post('/items')
def add_item(data:Additems):
    try:
        result=additems(data)
        return result
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400,detail="Item Already Exists") 
    except Exception:
        raise HTTPException(status_code=500,detail="Internal Server Error")

@app.put('/items/{id}')
def update_item(id:int,data:Updateitens):
    try:
        result = updateitems(id,data)
        if result == None:
            raise HTTPException(status_code=404,detail="Item Not Found") 
        return result 
    except HTTPException :
        raise
    except Exception:
        raise HTTPException(status_code=500,detail="Internal Server Error") 

@app.delete('/items/{id}')
def delete_item(id:int):
    try:
        result = deleteitem(id)
        if result == None:
            raise HTTPException(status_code=404,detail="Item Not Found") 
        return result 
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500,detail="Internal Server Error") 