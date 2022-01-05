# FastAPI启动前后处理程序

## 前言
FastAPI可以定义在应用程序启动之前或应用程序关闭时需要执行的事件程序（函数）

## startup 事件
要添加在应用程序启动之前运行的功能时, 要使用事件声明(`on_event`)启动事件：`startup`
```python
# 在启动程序之前运行，启动定时任务
@app.on_event("startup")
async def start_event():
    # scheduler.start()
    print("定时任务启动成功")
```
## shutdown 事件
要添加在应用程序关闭时运行的功能时, 要使用事件声明(`on_event`)关闭事件：`shutdown`
```python
# 在关闭程序时运行，将内容写入到log.txt文件中
@app.on_event("shutdown")
async def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")
```