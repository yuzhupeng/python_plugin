# APScheduler 定时任务

## 一、APScheduler

`APScheduler`全称`Advanced Python Scheduler` 作用为在指定的时间规则执行指定的作业。

- 指定时间规则的方式可以是间隔多久执行，可以是指定日期时间的执行，也可以类似Linux系统中Crontab中的方式执行任务。
- 指定的任务就是一个Python函数。

## 二、安装

```bash
pip install apscheduler
```

## 三、创建定时任务

- 创建一个任务 `func`
    - 一个任务就是一个函数，或者异步函数
- 创建调度器 `BlockingScheduler`
    - `BlockingScheduler`是最基本的调度器，阻塞型的调度器
- 把任务添加到调度器中 `add_job`
    - 参数一：任务名
    - 参数二：触发器，使用的是`interval`间隔触发器
    - `seconds`：间隔时间，单位秒，没个几秒执行一次
    - `args`：所添加的任务的传入参数
- 启动定时任务 `start`
```python
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def func(name):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + f" Hello world, {name}")


scheduler = BlockingScheduler()
scheduler.add_job(func, 'interval', seconds=3, args=["desire"])
scheduler.start()
```

**执行结果：**

```bash
2021-05-25 15:04:36 Hello world, desire
2021-05-25 15:04:39 Hello world, desire
2021-05-25 15:04:42 Hello world, desire
2021-05-25 15:04:45 Hello world, desire
```



## 四、调度器（schedulers）

### `BlockingScheduler`
- 阻塞型调度器，最基本的调度器，调用`start`函数会阻塞当前线程，不能立即返回
- 适用于调度程序时进程中唯一运行的进程
- `from apscheduler.schedulers.blocking import BlockingScheduler`

### `BackgroundScheduler`
- 后台运行调度器，调用`start`后主线程不会阻塞
- 适用于调度程序在应用程序的后台运行
- `from apscheduler.schedulers.background import BackgroundScheduler`

### `AsyncIOScheduler`
- 适用于使用了`asyncio`模块的应用程序
- `from apscheduler.schedulers.asyncio import AsyncIOScheduler`

### `GeventScheduler`
- 适用于使用`gevent`模块的应用程序
- `from apscheduler.schedulers.gevent import GeventScheduler`

### `TwistedScheduler`
- 适用于构建`Twisted`的应用程序
- `from apscheduler.schedulers.twisted import TwistedScheduler`

### `QtScheduler`：
- 适用于构建`Qt`的应用程序
- `from apscheduler.schedulers.qt import QtScheduler`

### `TornadoScheduler`
- 适用于构建`Tornado`的应用程序
- `from apscheduler.schedulers.tornado import TornadoScheduler`

## 五、触发器（triggers）



### 1、date触发器

- 在某个日期时间只触发一次事件
- `run_date`：参数为指定触发事件的日期

```python
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def func(name):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + f" Hello world, {name}")


scheduler = BlockingScheduler()
# 指定在2021/05/25 15:43 进行执行任务
scheduler.add_job(func, 'date', run_date=datetime(2021, 5, 25, 15, 43), args=["desire"])
scheduler.start()
```

**运行结果：**

```bash
2021-05-25 15:43:00 Hello world, desire
```

### 2、interval触发器

#### 在固定的时间间隔触发事件
#### `interval`触发器可以设置的触发参数：
- `weeks`：周，int
- `days`：一个月中的天，int
- `hours`：小时，int
- `minutes`：分钟，int
- `seconds`：秒，int
- `start_date`：间隔触发的起始时间
- `end_date`：间隔触发的结束时间
- `jitter`：触发的时间误差

```python
# 三秒执行一次
scheduler.add_job(func, 'interval', seconds=3, args=["desire"])
```



### 3、cron触发器

#### 在某个确切的时间周期性的触发时间
#### 参数：
- `year`：4位数的年份
- `month`：1-12月份
- `day`：1-31日
- `week`：1-53周
- `day_of_week`：一个礼拜中的第几天
    - 0-6
    - mon、tue、wed、thu、fri、sat、sun
- `hour`：0-23小时
- `minute`：0-59分钟
- `second`：0-59秒
- `start_date`：datetime类型或字符串类型，起始时间
- `end_date`：datetime类型或字符串类型，结束时间
- `timezone`：时区
- `jitter`：任务触发的误差时间
#### 也可以使用表达式类型
- `*`		任何		在每个值都触发
- `*/a`		任何		每隔`a`触发一次
- `a-b`		任何		在`a-b`区间内任何一个时间触发(a<b)
- `a-b/c`		任何		在`a-b`区间内每隔`c`触发一次
- `xth y`		day		第`x`个星期`y`触发
- `last y`		day		最后一个星期`x`触发
- `last`		day		一个月中的最后一天触发
- `x,y,z`		任何		可以把上面的表达式进行组合

```python
# 在每个50秒的时候触发
scheduler.add_job(func, 'cron', second=50, args=["desire"])

# 在第4个星期日触发
scheduler.add_job(func, 'cron', day="4th sun", args=["desire"])
```

## 六、任务存储器（job stores）

### `MemoryJobStore`
- 没有序列化，任务存储在内存中，增删改查都在内存中完成
- `from apscheduler.jobstores.memory import MemoryJobStore`

### `SQLAlchemyJobStore`
- 使用`SQLAlchemy`这个ORM框架作为存储方式
- `from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore`

### `MongoDBJobStore`
- 使用`mongodb`作为存储器
- `from apscheduler.jobstores.mongodb import MongoDBJobStore`

### `RedisJobStore`
- 使用`redis`作为存储器
- `from apscheduler.jobstores.redis import RedisJobStore`

## 七、执行器（executors）

### `ThreadPoolExecutor`
- 默认执行器
- 线程池执行器
- `from apscheduler.executors.pool import ThreadPoolExecutor`

### `ProcessPoolExecutor`
- 进程池执行器
- 适用于涉及到一些CPU密集计算的操作
- `from apscheduler.executors.pool import ProcessPoolExecutor`

### `GeventExecutor`
- `Gevent`程序执行器
- `from apscheduler.executors.gevent import GeventExecutor`

### `TornadoExecutor`
- `Tornado`程序执行器
- `from apscheduler.executors.tornado import TornadoExecutor`

### `TwistedExecutor`
- `Twisted`程序执行器
- `from apscheduler.executors.twisted import TwistedExecutor`

### `AsyncIOExecutor`
- `asyncio`程序执行器
- `from apscheduler.executors.asyncio import AsyncIOExecutor`


## 八、定时任务调度配置

### `jobstores` 用来配置存储器
- 使用SQLAlchemy进行存储
- 使用sqlite数据库，会自动创建数据库，并创建apscheduler_jobs表
### `executors` 用来配置执行器
- 使用线程池进行执行
- 设置最大线程数为20个
### `job_defaults` 创建job时的默认参数
- `coalesce` 是否合并执行
    - 比如由于某个原因导致某个任务积攒了很多次没有执行（比如有一个任务是1分钟跑一次，但是系统原因断了5分钟）
    - 如果 coalesce=True，那么下次恢复运行的时候，会只执行一次，
    - 而如果设置 coalesce=False，那么就不会合并，会5次全部执行。
- `max_instances` 最大实例数, 同一个任务同一时间最多只能有n个实例在运行。
    - 比如一个耗时10分钟的job，被指定每分钟运行1次，如果我 max_instance值5，那么在第6~10分钟上，新的运行实例不会被执行，因为已经有5个实例在跑了。

```python
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

interval_task = {
    # 配置存储器
    "jobstores": {
        # 使用SQLAlchemy进行存储,会自动创建数据库，并创建apscheduler_jobs表
        'default': SQLAlchemyJobStore(url="sqlite:///jobs.db")
    },
    # 配置执行器
    "executors": {
        # 使用线程池进行执行，最大线程数是20个
        'default': ThreadPoolExecutor(20)
    },
    # 创建job时的默认参数
    "job_defaults": {
        'coalesce': False,  # 是否合并执行
        'max_instances': 3  # 最大实例数
    }

}
scheduler = BlockingScheduler(**interval_task)
```



## 九、任务操作

### 1、添加job

- 1）调用`add_job()`方法
    - 最常用的方式
    - 返回一个`apscheduler.job.Job`实例，可以用它在之后修改或移除job
    - 如果调度的job在一个持久化的存储器里，当初始化应用程序时，必须要为job定义一个显示的ID并使用` replace_existing=True`, 否则每次应用程序重启时都会得到那个job的一个新副本
- 2）在任务中使用`scheduled_job()`装饰器
    - 通过声明job而不修改应用程序运行时是最为方便的

```python
# 最常用的方式
scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="desire_job", replace_existing=True)
# 使用装饰器
@scheduler.scheduled_job("interval", seconds=5, id="job2222222")
def test_task():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + f" Hello world, 使用装饰器")
```

### 2、移除job

- 1）通过job的ID来调用`remove_job`方法
- 2）通过在`add_job()`中得到的job实例调用`remove()`方法
- 如果一个job完成了调度（例如他的触发器不会再被触发）, 它会自动被移除

```python
# remove
job = scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="job_remove")
job.remove()

# remove_job
scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="job_remove")
scheduler.remove_job(job_id="job_remove")
```

### 3、暂停和恢复job

- 通过job实例或者schedule本身可以轻易地暂停和恢复job
- 当一个job被暂停，他的下一次运行时间将会被清空，同时不再计算之后的运行时间，直到这个job被恢复

```python
# 暂停一个job
# 方式一：
job = scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="job_remove")
job.pause()
# 方式二：
scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="job_remove")
scheduler.pause_job(job_id="job_remove")

# 恢复一个job
# 方式一：
job = scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="job_remove")
job.resume()
# 方式二：
scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="job_remove")
scheduler.resume_job(job_id="job_remove")
```

### 4、获取作业调度列表

- `get_jobs`获取机器上可处理的作业调度列表
    - 返回一个Job实例列表
    - 如果只对特定的存储器中的job感兴趣，可以将存储器的别名作为第二个参数
- `print_jobs` 格式化输出作业列表以及他们的触发器和下一次的运行时间

### 5、修改job

- `modify()`通过job实例进行修改属性
- `modify_job` 通过job的ID进行修改属性

```python
job = scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="job_modify")
# modify
job.modify(name="job222")
# modify_job
scheduler.modify_job(job_id="job_modify", name="job2222")
```

- `reschedule` 通过job实例重新调度job
- `reschedule_job`通过job的ID进行重新调度job

```python
job = scheduler.add_job(func, 'interval', seconds=3, args=["desire"], id="job_modify")
# reschedule
job.reschedule(trigger='cron', minute='*/5')
# reschedule_job
scheduler.reschedule_job(job_id="job_modify", trigger='cron', minute='*/5')
```

## 十、调度器操作

### 1、终止调度器

- `shutdown()`
    - 默认情况，会终止任务存储器以及执行器，然后等待所有目前执行的job完成后（自动终止）
    - `wait=False` 此参数不会等待任何运行中的任务完成，直接终止

```python
scheduler.shutdown()

scheduler.shutdown(wait=False)
```

### 2、暂停/恢复 job 的运行

- `scheduler.pause()` 暂停被调度的job的运行
- `scheduler.resume()` 恢复job的运行，会导致调度器在被恢复之前一致处于休眠状态
- `scheduler.start(paused=True)` 如果没有进行过唤醒，也可以对处于暂停状态的调度器执行`start`操作
    - 可以有机会在不想要的job运行之前将它们排除掉

## 十一、调度器事件操作

- `add_listener` 通过此方法对调度器绑定事件监听器

```python
def my_listener(event):
    if event.exception:
        print("任务出错了！！！！！！！！！")
    else:
        print("任务正常运行。。。。。")
# 绑定事件监听器，当出现异常或者错误的时，进行监听
scheduler.add_listener(my_listener, mask=EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
```

