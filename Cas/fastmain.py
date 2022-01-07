# coding: utf-8
# fun1
 

from fastapi import FastAPI
import uvicorn

app = FastAPI()
import baiduapi 

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/address/{start}/{end}")
def read_item(start: str, end:str):
    result=baiduapi.get_driving_direction(start,end)
    return result


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}



if __name__ == '__main__':
    uvicorn.run(app='fastmain:app', host="127.0.0.1", port=8900, reload=True, debug=True)