# docker安装集合
## Docker安装RabbitMQ

### 下载Docker镜像

```bash
# 下载自带管理的镜像
docker pull rabbitmq:management
```

### 启动rabbitmq容器

```bash
docker run -d --hostname desire-rabbit --name desire-rabbit -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password -p 15672:15672 -p 5672:5672 rabbitmq:management
```

- `RABBITMQ_DEFAULT_USER` 设置登录用户
- `RABBITMQ_DEFAULT_PASS` 设置登录密码
- `-p 15672:15672` 映射15672端口，用来访问管理后台
- `-p 5672:5672` 映射5672端口，用来连接操作rabbit

### 访问管理后台

```bash
http://ip:15672
```

## Docker安装mysql

### 1、查看mysql-docker镜像
```bash
docker search mysql
```
### 2、pull mysql镜像
```bah
docker pull mysql
```
### 3、运行容器
#### 1）创建映射文件
```bash
mkdir -p /home/docker/mysql/conf.d
mkdir -p /home/docker/mysql/data
```
#### 2）运行容器，添加映射
```bash
docker run -di -p 3306:3306 -v /home/docker/mysql/conf.d:/etc/mysql/conf.d -v /home/docker/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name mysql mysql
```
- -v 映射目录，将容器内的配置与数据文件夹，映射到宿主机目录
- -p 代表端口映射，格式为 宿主机映射端口:容器运行端口
- -e 代表添加环境变量  MYSQL_ROOT_PASSWORD是root用户的登陆密码
