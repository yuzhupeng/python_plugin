## HTTPRunner

### 一、简介
2.x版本集成了

3.x版本集成了pytest

### 二、安装
```bash
pip install httprunner==2.3.0
```

### 三、创建httprunner工程
```bash
hrun --startproject ./hrdemo
```
### 四、目录结构
```bash
|-hrdemo
|--api：主要存放接口的最小执行单位（正向用例）
|--reports：用于存放测试报告
|--testcases：用于处理接口的负责执行逻辑，实现接口间的依赖
|--testsuites：用于添加多条测试用例，批量执行，处理数据驱动测试（参数化）
|--.env：用于自定义全局环境变量，可以在整个项目的测试脚本中调用
|--.gitignore
|--debugtalk.py：用于处理动态参数，也可以处理参数化动态数据
```
### 五、简单使用
#### 1）yml用例
```yml
name: get demo
request:
  method: GET
  url: https://httpbin.org/get
validate:
  - eq: ["status_code",200]
```

#### 2）运行yml用例
```bash
hrun api/get_demo.yml --report-dir reports
OR
httprunner api/get_demo.yml --report-dir reports
```

### 六、特殊用法

#### 1）局部变量
在yml文件中，在variables节点下定义的参数为局部变量，作用域只在当前yml下
```yml
name: get params
variables:
  value1: value1
  value2: value2
```
**使用：**

固定语法：`$变量名`
```yml
name: get params
variables:
  value1: value1
  value2: value2
request:
  method: GET
  url: 'https://httpbin.org/get'
  params:
    value1: $value1
    value2: $value2
validate:
  - eq: ['status_code', 200]
```
#### 2）base_url
在yml文件中，添加一个新的节点base_url(名字为固定写法)
```yml
base_url: 'https://httpbin.org'
```
#### 3）环境变量`.env`文件
在`.env`中定义的变量为环境变量
```
USERNAME=leolee
PASSWORD=123456
BASE_URL=https://httpbin.org
```
**使用：**

固定语法：`${ENV(定义的环境变量名)}`
```yml
name: get params
variables:
  value1: value1
  value2: value2
base_url: ${ENV(BASE_URL)}
request:
  method: GET
  url: /get
  params:
    value1: $value1
    value2: $value2
validate:
  - eq: ['status_code', 200]
```
#### 4）使用自定义函数-`debugtalk.py`
在`debugtalk.py`中定义函数
```python
import random

def get_agent():
    agents = ["Mozilla/5.0 Desire", "Mozilla/5.0 Tommy",
              "Mozilla/5.0 Ronin", "Mozilla/5.0 DD"]
    return random.choice(agents)
```
**使用：**

固定语法：`${函数调用}`
```yml
name: get params
variables:
  value1: value1
  value2: value2
base_url: ${ENV(BASE_URL)}
request:
  method: GET
  url: /get
  params:
    value1: $value1
    value2: $value2
  headers:
    User-Agent: ${get_agent()}
validate:
  - eq: ['status_code', 200]
```
#### 5）前置（setup_hooks） OR 后置（teardown_hooks）hook(不可用于testsuite中)
```yml

name: login api
variables:
    username: desire
    password: 123456
    n_secs: 1

base_url: ${ENV(BASE_URL)}
request:
    url: /user/login/
    method: POST
    headers:
        Content-Type: "application/json"
    json:
        username: $username
        password: $password
# 前置条件
setup_hooks:
    # 调用自定义的前置函数，修改请求信息headers中的User-Agent为Desire
    - ${setup_hook_add_kwargs($request)}
# 后置条件
teardown_hooks:
    # 调用自定义的后置函数，如果响应成功则休眠5秒，响应非200则休眠n_secs
    - ${teardown_hook_sleep_N_secs($response, $n_secs)}
validate:
    - eq: ["status_code", 200]
```
**debugtalk.py自定义函数**
```python
import time

def setup_hook_add_kwargs(request):
    request["headers"]["User-Agent"] = "Desire"


def teardown_hook_sleep_N_secs(response, n_secs):
    """ sleep n seconds after request
    """
    if response.status_code == 200:
        time.sleep(5)
    else:
        time.sleep(n_secs)
```

### 七、断言 `validate`
#### 1）断言方式
| 断言方法         | 源码（httprunner/built_in.py）                               | 说明                               |
| ---------------- | ------------------------------------------------------------ | ---------------------------------- |
| **eq**           | **def equals(*check_value*, *expect_value*):**               | **是否相等**                       |
| **lt**           | **def less_than(*check_value*, *expect_value*):**            | **小于**                           |
| **le**           | **def less_than_or_equals(*check_value*, *expect_value*):**  | **小于等于**                       |
| **gt**           | **def greater_than(*check_value*, *expect_value*):**         | **大于**                           |
| **ge**           | **def greater_than_or_equals(*check_value*, *expect_value*):** | **大于等于**                       |
| **ne**           | **def not_equals(*check_value*, *expect_value*):**           | **不等于**                         |
| **str_eq**       | **def string_equals(*check_value*, *expect_value*):**        | **字符串等于**                     |
| **len_eq**       | **def length_equals(*check_value*, *expect_value*):**        | **长度等于**                       |
| **len_gt**       | **def length_greater_than(*check_value*, *expect_value*):**  | **长度大于**                       |
| **len_ge**       | **def length_greater_than_or_equals(*check_value*, *expect_value*):** | **长度大于等于**                   |
| **len_lt**       | **def length_less_than(*check_value*, *expect_value*):**     | **长度小于**                       |
| **len_le**       | **def length_less_than_or_equals(*check_value*, *expect_value*):** | **长度小于等于**                   |
| **contains**     | **def contains(*check_value*, *expect_value*):**             | **预期结果是否被包含在预期结果中** |
| **contained_by** | **def contained_by(*check_value*, *expect_value*):**         | **实际结果是否被包含在预期结果中** |
| **type_match**   | **def type_match(*check_value*, *expect_value*):**           | **类型是否匹配**                   |
| **regex_match**  | **def regex_match(*check_value*, *expect_value*):**          | **正则表达式是否匹配**             |
| **startswith**   | **def startswith(*check_value*, *expect_value*):**           | **字符串是否以什么开头**           |
| **endswith**     | **def endswith(*check_value*, *expect_value*):**             | **字符串是否以什么结尾**           |
|                  |                                                              |                                    |

#### 2）断言内容-`check_value`
- status_code：响应状态码
- encoding：字符集
- ok：是否OK
- reason：
- url：请求地址
- headers：请求头
  - headers.content-type
- cookies：cookie信息
- content：响应体
  - content.person.name.first_name
- text：响应体文本格式
- json：响应体json格式


### 八、提取数据 `extract`

```yml

config:
    name: "demo testcase"
    variables:
        device_sn: "ABC"
        # username: ${ENV(USERNAME)}
        # password: ${ENV(PASSWORD)}
    base_url: ${ENV(BASE_URL)}

teststeps:
-
    name: $title
    api: api\login.yml
    variables:
        user_agent: 'iOS/10.3'
        device_sn: $device_sn
    # 提取用例执行的结果，并给赋值给token
    extract:
        - token: content.token
    validate:
        - eq: ["status_code", $status_code]
        - contains: ["content", $msg]
```

### 九、整个HttpRunner项目目录文件解析

#### 1）api\login.yml
```yml
# 用例的名称
name: login api
# 局部变量
variables:
    username: desire
    password: 123456
# base url 指定用法
base_url: ${ENV(BASE_URL)}
# 请求数据
request:
    # 请求url，如果有base_url会自动进行拼接url
    url: /user/login/
    # 请求方式
    method: POST
    # 请求头信息
    headers:
        Content-Type: "application/json"
    # 请求参数（data/json/params）
    json:
        username: $username
        password: $password
# 断言信息
validate:
    - eq: ["status_code", 200]
```
#### 2）api\projects.yml
```yml
name: projects api
variables:
    page: 1
    size: 3

base_url: ${ENV(BASE_URL)}
request:
    url: /projects/
    method: GET
    headers:
        Content-Type: "application/json"
    params:
        page: $page
        size: $size
    headers:
        # 此接口需要token鉴权，要添加此请求头，并且token是从登陆接口中获取的
        Authorization: "JWT $token"
validate:
    - eq: ["status_code", 200]
```
#### 3）testcases\login_testcase.yml
```yml
config:
    name: "demo testcase"
    # 局部变量，作用域在整个testcases中
    variables:
        device_sn: "ABC"
        title: 登录用例
        status_code: 200
        msg: token
    base_url: ${ENV(BASE_URL)}

teststeps:
-
    name: $title
    api: api\login.yml
    # 定义变量，作用域在本step下
    variables:
        user_agent: 'iOS/10.3'
        device_sn: $device_sn
    validate:
        - eq: ["status_code", $status_code]
        - contains: ["content", $msg]
```
#### 4）testcases\projects_testcase.yml
```yml
# 用例集配置信息
config:
    # 用例集名称
    name: "demo testcase"
    # 局部变量，作用域为整个用例集（yml）
    variables:
        title: 获取项目列表
        status_code: 200
    # url 使用全局配置文件变量（.env）
    base_url: ${ENV(BASE_URL)}

# 测试步骤
teststeps:
# 用例一
-
    # 用例名称
    name: 正常登录
    # 用例接口所在yml文件 or 用例接口
    api: api\login.yml
    # 提取返回值
    extract:
        # 提取返回值，中的token值，然后赋值给变量token
        # token的作用域是在整个testcases，用例二中的projects.yml是可以获取到的
        - token: content.token
    # 断言
    validate:
        - eq: ["status_code", 200]
# 用例二
-
    name: $title
    # 用例接口，
    api: api\projects.yml
    validate:
        - eq: ["status_code", $status_code]
```
#### 5）testsuites\testsuite.yml
```yml
config:
    # 套件名称
    name: "接口套件"
    # 套件全局变量定义
    # 如果在测试集或者接口用例中，跟这里的变量有一样的，这里的优先级最高，其次是测试集中，最后是接口用例
    variables:
         device_sn: "XYZ"
    # 这里的base_url优先级最高
    base_url: "http://127.0.0.1:5000"

testcases:
-
    name: 登录接口套件-$title
    # 测试用例集
    testcase: testcases\login_testcase.yml
    # 进行参数化，这里的变量优先级最高，作用域只在当前的用例集中
    parameters: 
        # 参数化使用规则：变量之间用-拼接，使用自定义函数进行参数化，见：debugtalk.py文件中的get_accounts方法
        - title-username-password-status_code-msg: ${get_accounts()}
-
    name: 项目接口套件-$title
    testcase: testcases\projects_testcase.yml
    parameters:
        # 参数化使用规则：变量之间用-拼接，然后每一个用例数据就是一个列表，列表中的元素跟定义的变量一一对应
        - title-page-size-status_code:
            - ["获取项目列表数据，每页2条，第一页", "1", "2", 200]
            - ["获取项目列表数据，每页3条，第2页", "2", "3", 200]
            - ["获取项目列表数据，不指定每页数量，第一页", "1", "", 200]
            - ["获取项目列表数据，每页2条，，不指定页数", "", "2", 404]
```

#### 6）debugtalk.py
```python
# 可以根据实际情况创建带参数的函数
def get_accounts():
    
    # 定义参数化用例数据（嵌套字典的列表），每一个用例为一个字典，没个字典的key对应到设置的参数化
    accounts = [
        {"title": "正常登录", "username": "desire", "password": "123456",
            "status_code": 200, "msg": "token"},
        {"title": "密码错误", "username": "desire", "password": "123457",
            "status_code": 400, "msg": "non_field_errors"},
        {"title": "账号错误", "username": "desire111", "password": "123456",
            "status_code": 400, "msg": "non_field_errors"},
        {"title": "用户名为空", "username": "", "password": "123456",
            "status_code": 400, "msg": "username"},
        {"title": "密码为空", "username": "desire", "password": "",
            "status_code": 400, "msg": "password"},
    ]
    # 把参数化数据返回
    return accounts
```
#### 7）.env
```
# 环境变量名，一般是以大写定义，=后面是变量值（固定写法）
BASE_URL=http://127.0.0.1:8000/
```
#### 7）run.py

```python
from httprunner.api import HttpRunner

hr = HttpRunner()

# 使用HttpRunner提供的run方法进行执行用例

# 指定执行单个用例
# hr.run(r"api\login.yml")

# 指定执行测试集（相同变量，测试集中的变量优先级最高）
# hr.run(r"testcases\projects_testcase.yml")

# 指定执行测试套件（相同变量，测试套件中的变量优先级最高）
hr.run(r"testsuites\testsuite.yml")

# 通过HttpRunner提供的summary方法可以获取到执行的结果信息
print(hr.summary)
```