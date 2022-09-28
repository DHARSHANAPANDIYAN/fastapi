from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get('/item')
def index(limit=10, published:bool = True, sort : Optional[str]= None):
    if published:
        return {'data' : f'{limit} published items form db'}

    else:
        return {'data':f'{limit} items from db'}


@app.get('/item/{id}')
def show(id):
    return {'data': id }
    published : Optional[bool]


@app.get('/item/{id}/comment')
def comment(id):
    return {'data' : {'1','2'}}


class Item(BaseModel):
    title :str
    body:str


@app.post('/item')
def create_item(request : Item):
    return request
    return{'data' : f" Item is created with title as{item.title}"}