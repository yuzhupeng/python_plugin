# docker笔记

## 安装Docker(CentOS 8)

### 1、安装yum-utils命令包（yum-config-manager命令需要）
```bash
sudo yum -y install yum-utils
```
### 2、添加软件源信息(国内源, 速度更快, 推荐)
```bash
sudo yum-config-manager \
    --add-repo \
    https://mirrors.ustc.edu.cn/docker-ce/linux/centos/docker-ce.repo
```
### 3、更新Docker-CE 
```bash
yum makecache fast(可能会报错，报错的话，用下面的)
yum makecache (CentOS8没有fast参数，可以去掉)
```
### 4、安装Docker Engine
```bash
yum install docker-ce docker-ce-cli containerd.io
```
### 5、开启docker
```bash
systemctl enable docker(设置开机自启动)
systemctl start docker
```
### 6、验证是否安装成功
```bash
docker run hello-world
```
**如果出现“Hello from Docker!”，则代表运行成功**

### 7、docker 版本信息
```bash
docker version
```

## docker
### 一、docker基本操作
#### 1、docker image(镜像)
- 列出镜像
```bash
# 列出所有镜像
docker images

# 仅列出镜像的ID
docker images -q
```
- 搜索镜像
```bash
docker search mysql
```
- 下载镜像
```bash
docker pull nginx
```
- 删除镜像
```bash
docker rmi ImageID
```

- 查看镜像详细信息
```bash
docker inspect jenkins
```

#### 2、docker container(容器)
- 运行容器
```bash
docker run image

docker run centos
# 启动容器并打开容器bash终端
docker run -it centos /bin/bash

docker run --name web -d -p 8080:80 -v $PWD:/usr/share/nginx/html nginx

参数：-i -t --name -d -p -P -v --net

docker exec -it mysql /bin/bash
```
> - -i 已交互模式运行容器，通常与-t同时使用
> - -t 为容器重新分配一个伪输入终端，通常与-i同时使用
> - --name 为容器指定一个名称
> - -d 后台运行容器，并返回容器ID
> - -p 代表端口映射，格式为 宿主机映射端口:容器运行端口
> - -P 随机端口映射，容器内部端口随机映射到主机的端口
> - -v 映射目录，将容器内的配置与数据文件夹，映射到宿主机目录
> - -e 代表添加环境变量
> - --net指定容器的网络连接类型，支持bridge/host/none/container四种类型
> - --volume 绑定一个卷
> - -h 指定容器的hostname

- 列出容器
```bash
# 列出当前运行的容器
docker ps

# 列出系统中所有的容器
docker ps -a

# 列出容器上运行的所有历史命令
sudo docker history centos
```
- 查看容器的进程和资源利用情况
```bash
# 查看容器的进程
docker top ContainerID

# 查看容器的资源利用情况
docker stats ContainerID
```
- 停止/开启容器
```bash
# 停止容器
docker stop ContainerID

# 开启容器
docker restart ContainerID
```
- 暂停/启动容器
```bash
# 暂停容器
docker pause web

# 启动容器
docker unpause web
```
- 删除容器
```bash
# 删除一个未运行的容器
docker rm web

# 删除一个正在运行的容器
docker rm -f web
```


### 二、docker网络
#### 1、docker0
- 默认容器与宿主机之间的桥梁

#### 2、网络类型
- bridge
    - nat网络模型
    - 虚拟交换机
- host
    - 与宿主机共享网络
    - --net=host
- none
    - 不配置网络
        - --net=none
- overlay
    - 不同网络进行通信
- 与一个容器共享网络
    - --net=container:ContainerName

#### 3、相关操作
##### 1）查看
```bash
docker network ls

docker network inspect networkname
```
##### 2）创建
```bash
docker network create --driver drivername name

docker network create -d bridge --subnet 172.16.100.0/24 one_network
```


### 三、volume 数据卷
#### 1、介绍
- 使用数据卷实现数据持久化
- 数据备份/数据共享

#### 2、相关操作
##### 1）创建
```bash
# 手动创建
docker volume create nginx11

# 运行容器的时候，如果不存在则自动创建
docker run --name nginx33 -d -v nginx22:/usr/share/nginx/html -p 8888:80 nginx:alpine

```
##### 2）查看
```bash
# 列出所有的volume卷
docker volume ls

# 查询指定的volume卷的详细信息
docker volume inspect nginx22
```
##### 3）挂载
```bash
docker run -v 宿主机目录:容器目录

docker run --name nginx33 -d -v nginx22:/usr/share/nginx/html -p 8888:80 nginx:alpine

```
##### 4）删除
```bash
docker volume rm nginx11
```
### 四、Dockerfile
- 可以使用#号指定注释信息
- 文件名一般为Dockerfile
- 可以使用Dockerfile文件来自定义镜像
- 指定base image，基本镜像
- FROM一般为第一行，FROM基本镜像名称:tag版本编号
- 如果本地没有，会自动从docker hub 远程仓库下载，否则直接使用本地仓库提供的

#### 1、FROM
- FROM一般为第一行，FROM基本镜像名称:tag版本编号
```bash
FROM python:alpine
```

#### 2、LABEL
- 使用LABEL指定镜像的元数据信息（提示说明作用）
- LABEL key=value
- 如果value中有空格，需要使用引号括起来或者使用\进行转义

#### 3、COPY
- 用于将宿主机中的资源复制粘贴至容器中
- COPY 宿主机路径 容器中的路径
- 如果容器中指定的路径不存在，会自动创建
- 如果将一个文件复制到容器中，指定的容器路径，建议添加/
```bash
COPY . /app
```

#### 4、ADD
- ADD与COPY类似，用于将宿主机中的资源复制到容器中
- ADD 可以将远程文件下载之后，复制到容器中：ADD 远程文件链接 容器目录
- 也可以将本地的压缩文件解压之后，复制到容器中：ADD 本地压缩文件 容器目录
```bash
ADD https://github.com/docker-library/python/raw/master/update.sh .
```

#### 5、WORKDIR
- 相当于cd命令，用于容器进入到某个目录中
- 如果指定的路径不存在，会自动创建
```bash
WORKDIR /app
```
#### 6、RUN
- 用于在容器中执行linux命令
- 每一个RUN指令会独自占一层
- 为了优化镜像的大小，如果有多条命令，可以使用一个RUN指令，多条命令之间&&或者;使用\进行换行
```bash
RUN pip install -r requirements.txt
```

#### 7、ENV
```bash
ENV username=Desire\
    password=123456
```
#### 8、VOLUME
- 指定容器中哪些目录可以与宿主机进行共享

```bash
LABEL maintaier="Desire <desireyang.qq.com>"
LABEL description="define Dockerfile Demo"
```
#### 9、EXPOSE
- 指定容器中可以暴露的端口
```bash
EXPOSE 8000
```
#### 10、CMD
- 指定容器运行（docker run ）时，默认会执行的命令
- 如果在运行容器时，指定了其他命令，那么CMD命令会被覆盖
- 如果有多个CMD命令，只有最后一个会被执行
- 有两种格式，shell格式、exec格式
- exec格式(常用)：["命令的绝对路径","参数1","参数2"]
- shell格式：命令的绝对路径 参数1 参数2
```bash
CMD ["python", "fun.py"]
# CMD ["/bin/ls","/","/etc"]
# CMD python fun.py
```
#### 11、ENTRYPOINT
- 与CMD类似，当运行容器时，如果指定了其他命令，那么ENTRYPOINT不会被覆盖
- 如果有多个ENTRYPOINT，那么只有最后一个ENTRYPOINT会被执行
- 可以与CMD一起用，放在ENTRYPOINT后面，作为ENTRYPOINT默认参数
```bash
ENTRYPOINT ["python", "fun.py"]
ENTRYPOINT ["cat", "fun.py"]
CMD ["etc/passwd"]
# 可以指定shell脚本
ENTRYPOINT ["/bin/sh","docker-entrypoint.sh"]
```
#### 12、ARG
- 构建参数
- 和ENV的效果一样，都是设置环境变量
- ARG所设置的构建环境的环境变量，在将来容器运行时是不会存在这些环境变量的
- 不要因此使用ARG保存密码之类的信息，`docker history`是可以看到所有值的
- 定义的值可以在`docker build`中用`--build-arg <参数名>=<值>`进行覆盖
- 生效范围
    - 如果是在`FROM`指令之前指定，那么只能用于`FROM`指令中
```bash
# 只在 FROM 中生效
ARG DOCKER_USERNAME=library

FROM ${DOCKER_USERNAME}/alpine

# 要想在 FROM 之后使用，必须再次指定
ARG DOCKER_USERNAME=library

RUN set -x ; echo ${DOCKER_USERNAME}
```
#### 13、USER
- 指定当前用户
- USER只是帮助切换到指定用户，并不会创建用户
```bash
USER root
```

#### 通过Dockerfile文件构建镜像
```bash
docker build -t 镜像名:tag -f 指定Dockerfile文件路径 .
```
- -t 指定构建的镜像名称和tag，如果不指定tag，默认使用latest，镜像名一般为用户名/镜像名称
- -f 指定Dockerfile文件路径，如果命名为Dockerfile，且在当前路径下，那么可以不用指定，否则必须指定
- . 代表将当前路径作为构建上下文

#### Dockerfile文件
```bash
FROM python:alpine

LABEL maintaier="Desire <desireyang.qq.com>"
LABEL description="define Dockerfile Demo"

COPY . /app

# ADD https://github.com/docker-library/python/raw/master/update.sh .

WORKDIR /app

RUN pip install -r requirements.txt

ENV username=Desire\
    password=123456

VOLUME /app

# EXPOSE 8000

CMD ["python", "fun.py"]
# CMD ["/bin/ls","/","/etc"]
# CMD python fun.py

# ENTRYPOINT ["python", "fun.py"]
# ENTRYPOINT ["cat", "fun.py"]
# CMD ["etc/passwd"]
# 可以指定shell脚本
# ENTRYPOINT ["/bin/sh","docker-entrypoint.sh"]
```

### 五、docker-compose
#### 1、安装
```bash
# 运行此命令下载当前的 Docker Compose 稳定版本
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# 对二进制文件应用可执行权限
sudo chmod +x /usr/local/bin/docker-compose
# 检查是否安装成功
docker-compose --version
```
#### 2、使用docker-compose部署应用
```bash
# 指定版本信息
version: '3'

# 定义服务（容器）
services:
   # 创建具体的服务（容器）
   db:
     # 指定需要使用的镜像名称
     # 镜像名:tag
     # 如果本地没有指定镜像，那么会从docker hub中下载，否则直接使用本地的镜像
     image: mariadb
     # 在运行容器时，指定需要执行的命令或者参数
     command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
     # 指定数据持久化映射
     volumes:
       # - 数据卷名称或者宿主机文件、路径:容器中的路径
       - mysql_db:/var/lib/mysql
     # 指定容器失败时（Existed），重启策略
     restart: always
     # 指定容器中的全局变量
     environment:
      # 变量名: 变量值
      MYSQL_ROOT_PASSWORD: "123456"
      MYSQL_DATABASE: my_django
     # 指定当前容器需要加入的网络
     networks:
      - django_app_net

   django_app:
     # 指定当前服务（容器）依赖的服务
     depends_on:
      - db
     # 指定通过Dockerfile去构建镜像（Dockerfile所在路径）
     build: ./django
     # 在build下方，指定构建的镜像名称:tag
     image: desireyang/django_app:v2
     restart: always
     volumes:
       - logs:/usr/src/app/logs/
       - django_code:/usr/src/app/web_test/
     networks:
      - django_app_net

   web:
     depends_on:
       - django_app
     build: ./nginx
     image: desireyang/web:v2
     restart: always
     # 将容器中监听的端口与宿主机端口镜像映射
     ports:
       - "8444:80"
       - "8440:8000"
     volumes:
       - logs:/var/log/nginx/
     networks:
      - django_app_net
      
# 指定需要使用的网络
networks:
  # 指定网络的名称，默认会创建bridge桥接网络
  django_app_net:

# 指定数据卷
volumes:
    mysql_db:
    django_code:
    logs:
```
#### 3、检查是否有错误
```bash
docker-compose config
```

#### 4、只构建不运行
```bash
docker-compose build
```
#### 5、运行
```bash
docker-compose up -d
# 如果docker-compose文件名不是docker-compose.yml，需要加上-f指定文件
docker-compose up -d -f docker-compose-django.yml
```