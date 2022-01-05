# FastAPI集成APScheduler

## 前言
`APScheduler`定时任务[传送门](https://xd825.github.io/Other/003%20APScheduler%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1/)

## 在FastAPI中集成aAPScheduler
- 使用FastAPI启动前后处理程序进行启动任务


### 1. 定时任务配置
- 使用`AsyncIOScheduler`调度器
- 使用`Redis`存储器
- 使用`ThreadPoolExecutor`执行器
```python
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

REDIS_DB = {
    "db": 1,
    "host": "127.0.0.1"
}


def func(name):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + f" Hello world, {name}")

interval_task = {
    # 配置存储器
    "jobstores": {
        # 使用Redis进行存储
        'default': RedisJobStore(**REDIS_DB)
    },
    # 配置执行器
    "executors": {
        # 使用进程池进行调度，最大线程数是20个
        'default': ThreadPoolExecutor(20)
    },
    # 创建job时的默认参数
    "job_defaults": {
        'coalesce': False,  # 是否合并执行
        'max_instances': 3,  # 最大实例数
    }

}
scheduler = AsyncIOScheduler(**interval_task)
# 添加一个定时任务
scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="desire_job", replace_existing=True)
```

### 2. 启动FastAPI之前启动定时任务
```python
from fastapi import FastAPI

# 导入定时任务配置
from scheduler import scheduler

app = FastAPI()

@app.on_event("startup")
async def start_event():
    scheduler.start()
    print("定时任务启动成功")

@app.get("/list")
async def jobs():
    jobs = scheduler.get_jobs()

    return [job.id for job in jobs]

```

### 3. 挂载到app上
#### 1）创建注册定时器的方法
```python
def register_scheduler(app: FastAPI):
    @app.on_event("startup")
    async def start_event():
        scheduler.start()
        print("定时任务启动成功")
```
#### 2）挂载到app上
```python
from fastapi import FastAPI

app = FastAPI()
# 进行挂载
register_scheduler(app)
```