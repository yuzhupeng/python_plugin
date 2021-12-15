from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.put("/testfastapi/{args}")
def checkfastpai(args:str):
    results=[]
    for item in args:
         results.append(item)
    return{results} 

if __name__ == '__main__':
    uvicorn.run(app='apidemo:app', host="localhost", port=8008, reload=True, debug=True)