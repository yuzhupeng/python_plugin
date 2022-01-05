# 挂载FastAPI应用程序

## 一、目的
如果需要两个独立的FastAPI应用程序，以及他们各自拥有独立的文档，则可以拥有一个主应用程序并`装载`多个子应用程序。

## 二、创建主应用程序

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/app")
def read_main():
    return {"msg":"This is main app"}
```

## 三、创建子应用程序
```python
subapp = FastAPI()

@subapp.get("/sub")
def read_sub():
    return {"msg":"This is sub app"}
```

## 四、把子应用挂载到主应用上
- 主应用程序的对象`app`, 使用`mount`方法进行装载子应用
- 第一个参数为api路径
- 第二个参数为子应用程序对象`subapp` 
```python
app.mount("/subapi", subapp)
```

## 五、独立文档
- 主应用文档地址 `http://127.0.0.1:8000/docs`
- 子应用文档地址 `http://127.0.0.1:8000/subapi/docs`