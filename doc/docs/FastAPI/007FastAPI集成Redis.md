# FastAPI集成Redis

## 前言
`FastAPI`是一个高性能的异步框架，集成`Redis`时，使用的时候异步`Redis`--`aioredis`

## aioredis
asyncio (PEP 3156) Redis客户端库。

该库旨在基于asyncio为Redis提供简单而清晰的接口。

文档地址：[https://aioredis.readthedocs.io/en/latest/](https://aioredis.readthedocs.io/en/latest/)

## 安装
```bash
pip install aioredis
```

## 在FastAPI中集成aioredis
- 使用FastAPI启动前后处理程序进行创建连接和关闭连接
- `import aioredis`

### 1. 在FastAPI创建前创建Redis连接
- 在`FastAPI`创建前创建`Redis`连接
- 给`app.state`添加新的属性值`redis`，用来存放`Redis`实例
- 全局都可使用`app.state.redis`获取`Redis`实例
```python
@app.on_event("startup")
async def startup_event():
    app.state.redis = await aioredis.create_redis(address=("127.0.0.1", 6379), db=3, encoding="utf-8")
    print(f"redis成功--->>{app.state.redis}")
```

### 2. 关闭连接
- 在`FastAPI`关闭时关闭`Redis`连接
- 使用`app.state.redis`直接进行关闭操作
```python
@app.on_event("shutdown")
async def shutdown_event():
    app.state.redis.close()
    await app.state.redis.wait_closed()
```

### 3. 把Redis挂载到app上
#### 1）创建注册Redis的方法
```python
def register_redis(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        app.state.redis = await aioredis.create_redis(address=("127.0.0.1", 6379), db=3, encoding="utf-8")
        print(f"redis成功--->>{app.state.redis}")

    @app.on_event("shutdown")
    async def shutdown_event():
        app.state.redis.close()
        await app.state.redis.wait_closed()
```
#### 2）挂载到app上
```python
from fastapi import FastAPI

app = FastAPI()
# 进行挂载
register_redis(app)
```

### 4. 接口中使用
```python
@app.get("/test")
async def test(q: str):
    key = time.time()
    await app.state.redis.set(key=key, value=q)
    # 添加数据，5秒后自动清除
    await app.state.redis.setex(key="vvv", seconds=5, value="临时存在")
    value = await app.state.redis.get(key=key)
    return {key: value}
```

### 5. 在子路由中使用
- 添加参数`request: Request`
- 通过`request.app.state.redis`获取`Redis`实例
- 通过获取到的实例，进行操作`Redis`
```python
router = APIRouter()


@router.get("/api/test")
async def test(request: Request, value: str):
    api_time = f"api-{time.time()}"
    await request.app.state.redis.setex(key=api_time, seconds=5.5, value=value)
    value = await request.app.state.redis.get(key=api_time)
    return {api_time: value}


app.include_router(router)
```