# coding: utf-8
# fun1
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/address/{start}/{end}")
def read_item(start: str, end:str):
    return {"item_id": start, "end": end}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app='fastapidemo:app', host="localhost", port=8098, reload=True, debug=True)