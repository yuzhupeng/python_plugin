# FastAPI简单使用

## 1、安装

```bash
pip install fastapi
pip install uvicorn
```

## 2、简单的demo

> main.py

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## 3、运行

```bash
uvicorn main:app --port 8888 --reload
```

> 命令含义如下:

- main：main.py 文件（一个 Python「模块」）。
- app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
- --port：执行端口号
- --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。

## 4、 访问

http://127.0.0.1:8888 # 访问接口

http://127.0.0.1:8888/docs # 交互式API文档（Swagger UI）

http://127.0.0.1:8888/redoc # 可选的API文档

