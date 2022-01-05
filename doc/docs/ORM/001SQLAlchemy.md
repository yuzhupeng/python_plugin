# SQLAlchemy ORM 框架

## 一、安装
```bash
pip install sqlalchemy==1.4.7
pip install pymysql # 连接mysql数据库所需库
```

## 二、连接数据库
```python
from sqlalchemy import create_engine

engine = create_engine(f"mysql+pymysql://{数据库账号}:{密码}@{数据库地址}:3306/{数据库}", echo=True)
print(engine)

------打印结果------
Engine(mysql+pymysql://root:***@127.0.0.1:3306/scrapy)
```

## 三、创建会话通道
```python
from sqlalchemy.orm import sessionmaker

maker = sessionmaker(bind=engine)
session = maker()
print(session)

------打印结果----------------
<sqlalchemy.orm.session.Session object at 0x03BB4400>
```

## 四、关闭会话通道
```python
session.close_all()
```

## 五、创建数据表模型
- 创建models模块，存放模型对象
- 创建表的模型对象，要继承`declarative_base`对象
- `__tablename__`：数据库中表的名称
- 字段要与数据库中字段对应

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    fullname = Column(String(32))
    password = Column(String(32))

    def __repr__(self): # 当查询的时候，返回模型结果数据时调用
        return f"<User(name='{self.name}', fullname='{self.fullname}', password='{self.password}')>"
```

## 六、自动生成数据表（在没有表的情况下）
```python
Base.metadata.create_all(engine, checkfirst=True)
```


## 七、数据库操作

### 1、添加
#### 1）add: 单条添加

```python
# 实例化模型类
ed_user = User(name="desire", fullname="asdfasdf", password="123123")
# 添加
session.add(ed_user)
# 提交
session.commit()
```
====> sql

```sql
INSERT INTO users (name, fullname, password) VALUES (%(name)s, %(fullname)s, %(password)s)
[generated in 0.00054s] {'name': 'desire', 'fullname': 'asdfasdf', 'password': '123123'}
```
#### 2）add_all: 批量添加（内部还是使用的add）
```python
# 列表每个元素为模型类实例
session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='windy'),
        User(name='mary', fullname='Mary Contrary', password='mary'),
        User(name='fred', fullname='Fred Flintstone', password='freddy')])
    session.commit()
```
==> sql
```sql
INSERT INTO users (name, fullname, password) VALUES (%(name)s, %(fullname)s, %(password)s)
[cached since 0.005862s ago] {'name': 'wendy', 'fullname': 'Wendy Williams', 'password': 'windy'}

INSERT INTO users (name, fullname, password) VALUES (%(name)s, %(fullname)s, %(password)s)
[cached since 0.01483s ago] {'name': 'mary', 'fullname': 'Mary Contrary', 'password': 'mary'}

INSERT INTO users (name, fullname, password) VALUES (%(name)s, %(fullname)s, %(password)s)
[cached since 0.01808s ago] {'name': 'fred', 'fullname': 'Fred Flintstone', 'password': 'freddy'}
```
### 2、修改

#### 1）方式一

- 根据ID查询出来数据实体类
- 然后直接修改数据实体类中的数据
- 进行commit提交，

```python
user = session.get(User, 8)
user.password = "123456"
session.commit()
```

==> sql

```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.id = %(pk_1)s
-- [generated in 0.00105s] {'pk_1': 8}
UPDATE users SET password=%(password)s WHERE users.id = %(users_id)s
-- [generated in 0.00042s] {'password': '123456', 'users_id': 8}
```

#### 2）方式二

- 通过链式调用进行更新操作
- update参数为字典形式，字典的key要跟列名对应
- 更新成功返回1，更新失败返回0

```python
session.query(User).filter(User.id==8).update({"password":"654321"})
session.commit()
```

==> sql

```sql
UPDATE users SET password=%(password)s WHERE users.id = %(id_1)s
-- [generated in 0.00195s] {'password': '654321', 'id_1': 8}
```





### 3、查询

#### 1）查询所有数据

- 通过query进行查询，使用all()查询所有数据，返回数据为列表嵌套模型类
- 可以通过循环遍历获取
- 可以通过【类名.属性名】获取指定的数据

```python
users = session.query(User).all()
for user in users:
    print(user, user.name)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
```
==> 打印结果
```bash
<User(name='desire', fullname='asdfasdf', password='123123')> desire
<User(name='wendy', fullname='Wendy Williams', password='windy')> wendy
<User(name='mary', fullname='Mary Contrary', password='mary')> mary
<User(name='fred', fullname='Fred Flintstone', password='freddy')> fred
```

#### 2）查询第一条数据

- 使用first查询第一条数据
- 返回的是模型类，可以通过【类名.属性名】获取指定的数据

```python
user = session.query(User).first()
print(user, user.name)
```

==>  sql

```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
 LIMIT %(param_1)s
-- [generated in 0.00076s] {'param_1': 1}
```

==> 打印结果

```bash
<User(name='desire', fullname='asdfasdf', password='123123')> desire
```



#### 3）查询指定列数据

- 在query中添加多个参数，参数可以为模型类，也可以为列名，返回的数据为列表嵌套元组
- 通过循环遍历获取
- 同样可以使用【类名.属性名】获取指定的数据

```python
users = session.query(User.name, User.fullname).all()
for user in users:
    print(user, user.name,user.fullname)
```
==> sql
```sql
SELECT users.name AS users_name, users.fullname AS users_fullname
FROM users
```
==> 打印结果
```bash
('desire', 'asdfasdf') desire asdfasdf
('wendy', 'Wendy Williams') wendy Wendy Williams
('mary', 'Mary Contrary') mary Mary Contrary
('fred', 'Fred Flintstone') fred Fred Flintstone
```

#### 4）条件查询

##### 1. filter条件查询

- 使用filter进行条件查询，查询条件为【User.fullname==Wendy Williams】
- 使用filter指定列为条件时，需要使用【类名.属性名】当做条件
```python
users = session.query(User).filter(User.fullname == "Wendy Williams").all()
    for user in users:
        print(user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.fullname = %(fullname_1)s
-- [generated in 0.00043s] {'fullname_1': 'Wendy Williams'}
```
==> 打印结果
```bash
<User(name='wendy', fullname='Wendy Williams', password='windy')>
```

##### 2. filter_by条件查询
- 使用filter_by进行条件查询，可以把模型类属性当做filter_by参数进行条件查询【fullname="Wendy Williams"】
- 可以简化代码复杂度
```python
users = session.query(User).filter_by(fullname="Wendy Williams").all()
for user in users:
    print(user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.fullname = %(fullname_1)s
-- [generated in 0.00053s] {'fullname_1': 'Wendy Williams'}
```
==> 打印结果
```bash
<User(name='wendy', fullname='Wendy Williams', password='windy')>
```

##### 3.多条件查询

- 可以使用链式调用，添加多个`filter`/`filter_by`
- 也可以在`filter`/`filter_by`添加多个参数进行多条件查询

```python
users = session.query(User).filter_by(fullname="Wendy Williams", name="wendy").all()
# users = session.query(User).filter_by(fullname="Wendy Williams").filter_by(name="wendy").all()
# users = session.query(User).filter(User.fullname=="Wendy Williams", User.name=="wendy").all()
for user in users:
    print(user)
```

==> sql

```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.fullname = %(fullname_1)s AND users.name = %(name_1)s
-- [generated in 0.00053s] {'fullname_1': 'Wendy Williams', 'name_1': 'wendy'}
```

==> 打印结果

```bash
<User(name='wendy', fullname='Wendy Williams', password='windy')>
```



#### 5）模糊查询

- `like`模糊查询，不区分大小写，但是在其他后端区分大小写（暂时没遇到过）
- `ilike`模糊查询，对于保证不区分大小写的比较，推荐使用这个

```python
users = session.query(User).filter(User.fullname.like('%F%')).all()
# users = session.query(User).filter(User.fullname.ilike('%F%')).all()
for user in users:
    print(user)
```

==> sql

```sql
-- like>>
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.fullname LIKE %(fullname_1)s
-- [generated in 0.00051s] {'fullname_1': '%F%'}

-- ilike>>
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE lower(users.fullname) LIKE lower(%(fullname_1)s)
-- [generated in 0.00061s] {'fullname_1': '%F%'}
```

==> 打印结果

```bash
<User(name='desire', fullname='asdfasdf', password='123123')>
<User(name='fred', fullname='Fred Flintstone', password='freddy')>
```



#### 6）IN查询

##### 1. IN查询

- 查询多个id的数据时，可以使用IN查询
- 可以使用【类名.属性名.in_()】进行IN查询
- IN查询参数为列表
- 返回值为列表

```python
users = session.query(User).filter(User.id.in_([1,2,3])).all()
for user in users:
    print(user)
```

>  sql

```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.id IN (%(id_1_1)s, %(id_1_2)s, %(id_1_3)s)
-- [generated in 0.00055s] {'id_1_1': 1, 'id_1_2': 2, 'id_1_3': 3}
```

==> 打印结果

```bash
<User(name='desire', fullname='asdfasdf', password='123123')>
<User(name='wendy', fullname='Wendy Williams', password='windy')>
<User(name='mary', fullname='Mary Contrary', password='mary')>
```

##### 2. not IN查询

- 只需在IN查询的基础上添加`~`
- 【~类名.属性名.in_()】进行not IN查询

```python
users = session.query(User).filter(~User.id.in_([1,2,3])).all()
for user in users:
    print(user)
```

==> sql

```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.id NOT IN (%(id_1_1)s, %(id_1_2)s, %(id_1_3)s)
-- [generated in 0.00086s] {'id_1_1': 1, 'id_1_2': 2, 'id_1_3': 3}
```

==> 打印结果

```bash
<User(name='fred', fullname='Fred Flintstone', password='freddy')>
```



#### 7）and查询

- 可以直接使用`filter`进行`and`多条件查询
- 也可以使用`and_`进行多条件查询

```python
from sqlalchemy import and_

users = session.query(User).filter(and_(User.name == "wendy",User.fullname == "Wendy Williams")).all()
# users = session.query(User).filter(User.name == "wendy",User.fullname == "Wendy Williams").all()
for user in users:
    print(user)
```

==> sql

```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.name = %(name_1)s AND users.fullname = %(fullname_1)s
-- [generated in 0.00065s] {'name_1': 'wendy', 'fullname_1': 'Wendy Williams'}
```

==> 打印结果

```bash
<User(name='wendy', fullname='Wendy Williams', password='windy')>
```



#### 8）or查询

- 再进行过滤的时候，可以通过`or_`进行多个条件满足其一即可查询出来

```python
from sqlalchemy import or_

users = session.query(User).filter(or_(User.name == "wendy1",User.fullname == "Wendy Williams")).all()
for user in users:
    print(user)
```

==> sql

```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.name = %(name_1)s OR users.fullname = %(fullname_1)s
-- [generated in 0.00045s] {'name_1': 'wendy1', 'fullname_1': 'Wendy Williams'}
```

==> 打印结果

```bash
<User(name='wendy', fullname='Wendy Williams', password='windy')>
```

#### 9）主键查询
- 可以使用`get`进行主键查询
- 直接使用`session.get`
    - 第一个参数为模型类
    - 第二个参数为id值
- 使用链式调用`session.query(User).get(1)`
```python
user = session.get(User, 1)
# user = session.query(User).get(1)
print(user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.id = %(pk_1)s
-- [generated in 0.00083s] {'pk_1': 1}
```
==> 打印结果
```bash
<User(name='desire', fullname='asdfasdf', password='123123')>
```

#### 10）范围查询

##### 1. `BETWEEN ... AND ...`
- `between` 范围查询
- 查询确定范围的值，这些值可以是数字，文本或日期
- 范围包含开始和结束值
```python
q = session.query(User).filter(User.id.between(2,4)).all()
for user in q:
    print(user.id, user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.id BETWEEN %(id_1)s AND %(id_2)s
-- [generated in 0.00053s] {'id_1': 2, 'id_2': 4}
```
==> 打印结果
```bash
2 <User(name='wendy', fullname='Wendy Williams', password='windy')>
3 <User(name='mary', fullname='Mary Contrary', password='mary')>
4 <User(name='fred', fullname='Fred Flintstone', password='freddy')>
```
##### 2. `NOT BETWEEN ... AND ...`
- 只需在`between`查询的基础上添加`~`
```python
q = session.query(User).filter(~User.id.between(2,4)).all()
for user in q:
    print(user.id,user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE users.id NOT BETWEEN %(id_1)s AND %(id_2)s
-- [generated in 0.00042s] {'id_1': 2, 'id_2': 4}
```
==> 打印结果
```bash
1 <User(name='desire', fullname='asdfasdf', password='123123')>
7 <User(name='mary', fullname='Mary Contrary', password='mary')>
8 <User(name='fred', fullname='Fred Flintstone', password='654321')>
```


#### 11）分组查询
##### `group_by` 分组查询
```python
q = session.query(User).group_by(User.name).all()
for user in q:
    print(user.id,user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users GROUP BY users.name
-- [generated in 0.00048s] {}
```
==> 打印结果
```bash
1 <User(name='desire', fullname='asdfasdf', password='123123')>
2 <User(name='wendy', fullname='Wendy Williams', password='windy')>
3 <User(name='mary', fullname='Mary Contrary', password='mary')>
4 <User(name='fred', fullname='Fred Flintstone', password='freddy')>
```
##### `having` 聚合操作（使用聚合操作 需要导入 `func` 库）
```python
from sqlalchemy.sql import func
q = session.query(User).group_by(User.name).having(func.min(User.id)>3).all()
for user in q:
    print(user.id,user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users GROUP BY users.name
HAVING min(users.id) > %(min_1)s
-- [generated in 0.00083s] {'min_1': 3}
```
==> 打印结果
```bash
4 <User(name='fred', fullname='Fred Flintstone', password='freddy')>
```
##### 统计分组后的数据量
```python
from sqlalchemy.sql import func
q = session.query(User.name, func.count(User.name)) \
    .group_by(User.name).all()
print(q)
```
==> sql
```sql
SELECT users.name AS users_name, count(users.name) AS count_1
FROM users GROUP BY users.name
-- [generated in 0.00184s] {}
```
==> 打印结果
```bash
[('desire', 1), ('wendy', 1), ('mary', 2), ('fred', 2)]
```



### 4、删除
- `delete` 删除操作
- 删除操作后，要进行提交`commit`
- 返回：删除成功 1，删除失败 0
```python
result = session.query(User).filter_by(id=5).delete()
print(result)
session.commit()
```
==> sql
```sql
DELETE FROM users WHERE users.id = %(id_1)s
-- [generated in 0.00052s] {'id_1': 5}
```
==> 打印结果
```bash
1
```

### 5、使用文本SQL

- 可以使用`text()`进行文本SQL执行

```python
from sqlalchemy import text

users = session.query(User).filter(text("id < 3")).all()
for user in users:
    print(user)
```

==> sql

```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
WHERE id < 3
```

==> 打印结果

```bash
<User(name='desire', fullname='asdfasdf', password='123123')>
<User(name='wendy', fullname='Wendy Williams', password='windy')>
```

### 6、统计
- `count` 统计结果数
```python
num = session.query(User).count()
print(num)
```
==> sql
```sql
SELECT count(*) AS count_1
FROM (SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users) AS anon_1
```
==> 打印结果
```bash
4
```

### 7、去重
- `distinct` 去重
```python
users = session.query(User).distinct().all()
print(users)
```
==> sql
```sql
SELECT DISTINCT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users
```
==> 打印结果
```bash
[
    <User(name='desire', fullname='asdfasdf', password='123123')>, 
    <User(name='wendy', fullname='Wendy Williams', password='windy')>, 
    <User(name='mary', fullname='Mary Contrary', password='mary')>, 
    <User(name='fred', fullname='Fred Flintstone', password='freddy')>
]
```

### 8、排序
- `order_by` 排序
#### 1. 默认排序，升序
```python
users = session.query(User).order_by(User.id).all()
for user in users:
    print(user.id, user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users ORDER BY users.id
```
==> 打印结果
```bash
1 <User(name='desire', fullname='asdfasdf', password='123123')>
2 <User(name='wendy', fullname='Wendy Williams', password='windy')>
3 <User(name='mary', fullname='Mary Contrary', password='mary')>
4 <User(name='fred', fullname='Fred Flintstone', password='freddy')>
```

#### 2. 降序
```python
users = session.query(User).order_by(User.id.desc())
for user in users:
    print(user.id, user)
```
==> sql
```sql
SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
FROM users ORDER BY users.id DESC
```
==> 打印结果
```bash
4 <User(name='fred', fullname='Fred Flintstone', password='freddy')>
3 <User(name='mary', fullname='Mary Contrary', password='mary')>
2 <User(name='wendy', fullname='Wendy Williams', password='windy')>
1 <User(name='desire', fullname='asdfasdf', password='123123')>
```

### 9、别名

#### 1. 为实体类指定别名
- 使用`aliased`对实体类指定别名
    - 第一个参数为：实体类名
    - 第二个参数为：别名
- 添加列时，要使用【别名.属性】
```python
user_alias = aliased(User, name='user_alias')
users = session.query(user_alias, user_alias.name).all()
for instance in users:
    print(instance.user_alias, instance.name)
```
==> sql
```sql
SELECT user_alias.id AS user_alias_id, user_alias.name AS user_alias_name, user_alias.fullname AS user_alias_fullname, user_alias.password AS user_alias_password
FROM users AS user_alias
```
==> 打印结果
```bash
<User(name='desire', fullname='asdfasdf', password='123123')> desire
<User(name='wendy', fullname='Wendy Williams', password='windy')> wendy
<User(name='mary', fullname='Mary Contrary', password='mary')> mary
<User(name='fred', fullname='Fred Flintstone', password='freddy')> fred
```

#### 2. 为列指定别名
- `label` 为列指定别名
- 获取值得时候，要使用别名进行获取，否则会报错
```python
users = session.query(User.name.label('name_label')).all()
for user in users:
    print(user.name_label)
```
==> sql
```sql
SELECT users.name AS name_label
FROM users
```
==> 打印结果
```bash
desire
wendy
mary
fred
```

