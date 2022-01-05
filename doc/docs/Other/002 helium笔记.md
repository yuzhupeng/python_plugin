# helium(selenium-python-helium)笔记

## 一、前言

### 1. 资料
- Github：https://github.com/mherrmann/selenium-python-helium
- Docs：https://selenium-python-helium.readthedocs.io/en/latest/

### 2. 优点
- 简化了Selenium操作，对Selenium进行封装，提供了简单的API
- 可以和Selenium进行混用
- 去除了驱动的下载安装，自动配置驱动
- 支持Chrome和Firefox

## 二、安装helium
```bash
pip install helium
```

## 三、浏览器常用操作
### 1. 导包
```python
import helium
```
### 2. 启动浏览器
> `helium.start_chrome(url=None, headless=None, options=None)`

> `helium.start_firefox(url=None, headless=None, options=None)`

- 参数
    - url: 默认为空，打开浏览器并打开网址
    - headless: 默认为False，是否使用无头模式打开浏览器
    - options: 默认为空，启动浏览器的高级配置

```python
# 1、只打开浏览器
helium.start_chrome()

# 2、打开浏览器并打开网址
helium.start_chrome("https://www.baidu.com/")

# 3、无头模式操作(部署到服务器上时，需要进行设置)
helium.start_chrome("https://www.baidu.com/",headless=True)

# 4、高级配置
from selenium import webdriver

options = webdriver.ChromeOptions()
# 配置触屏方式
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
# 部署到浏览器的时候需要添加这个配置，否则会报错
options.add_argument('--no-sandbox') # 彻底停用沙箱
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
# 无头模式运行，跟 headless=True 一样
options.add_argument('--headless')
# 以最大化打开浏览器窗口
options.add_argument('--start-maximized')

helium.start_chrome("https://www.baidu.com/",options=options)
```

### 3. 打开网址

> `helium.go_to(url)`

- 参数
    - url: 要打开的网址
```python
helium.go_to("https://www.baidu.com/")
```

### 4. driver操作

> `helium.set_driver(driver)` 设置driver对象

> `helium.get_driver()` 获取driver对象

```python
helium.start_chrome()
driver= helium.get_driver()
print(driver) 
# <selenium.webdriver.chrome.webdriver.WebDriver (session="7d684039be5714229ef2921f14dec310")>
```

### 5. 输入

> `helium.write(text, into=None)`

- 参数
    - text: 写入的内容
    - into: 默认为空，可以输入的类型为：`HTMLElement`/`selenium.webdriver.remote.webelement.WebElement`/`Alert`

```python
# 使用into默认值，
helium.write("Python")

# 使用WebElement类型into参数
driver = helium.get_driver()
busin_name = driver.find_element_by_xpath("元素定位")
helium.write("Python", into=busin_name)

# 使用Alert类型into参数
helium.write("Michael", into=Alert("Please enter your name"))
```

### 6. 使用键盘按键

> `helium.press(key)`

- 参数
    - key: 要按下的按键或按键组合

```python
helium.start_chrome("https://www.baidu.com/")
helium.press("Python") # 按下 Python 按键
helium.press('a') # 按下 a 按键
helium.press('A') # 按下 A 按键
helium.press(helium.ENTER) # 按下 回车 按键
helium.press(helium.CONTROL + 'a') # 按下 Ctrl+a 全选 按键
```

### 7. 点击

> `helium.click(element)`

- 参数
    - element: 类型可为：`str`/`HTMLElement`/`selenium.webdriver.remote.webelement.WebElement`/`Point`
```python

helium.start_chrome("https://www.baidu.com/")
helium.press("Python")
helium.click("百度一下") # 点击按钮 方式一(str)
# helium.click(helium.Button("百度一下")) # 点击按钮 方式二(HTMLElement)
# helium.click(driver.find_element_by_xpath("xpath元素定位")) # 点击按钮 方式三(WebElement)
# helium.click(helium.Point(200,300)) # 点击按钮 方式四(Point)
helium.click("Welcome to Python.org") # 点击链接

```
### 8. 双击

> `helium.doubleclick(element)`

- 参数
    - element: 类型可为：`str`/`HTMLElement`/`selenium.webdriver.remote.webelement.WebElement`/`Point`

```python
helium.doubleclick("Double click here")
helium.doubleclick(helium.Image("Directories"))
helium.doubleclick(helium.Point(200, 300))
helium.doubleclick(helium.TextField("Username").top_left - (0, 20))
```

### 9. 拖动

> `helium.drag(element, to)`

- 参数
    - element：要拖动的元素，类型可为：`str`/`HTMLElement`/`selenium.webdriver.remote.webelement.WebElement`/`Point`
    - to: 要拖动到的元素，类型可为：`str`/`HTMLElement`/`selenium.webdriver.remote.webelement.WebElement`/`Point`

```python
helium.drag("Drag me!", to="Drop here.")
```

### 10. Alert弹窗处理

> `helium.Alert(search_text=None)`

- 参数
    - text: Alert弹窗内容
- 方法
    - accept(): 确定
    - dismiss(): 取消

```python
alert = helium.Alert()
alert.accept() # 确定
alert.dismiss() # 取消
```

### 11. 窗口切换

> `helium.switch_to(window)`

### 12. 滚动

> `helium.scroll_down(num_pixels=100)` 向下滚动

> `helium.scroll_up(num_pixels=100)` 向上滚动

> `helium.scroll_right(num_pixels=100)` 向右滚动

> `helium.scroll_left(num_pixels=100)` 向左滚动

### 13. 悬停

> `helium.hover(element)`

### 14. 刷新

> `helium.refresh()`

### 15. 等待元素出現

> `helium.wait_until(condition_fn, timeout_secs=10, interval_secs=0.5)`

- 参数
    - condition_fn: 元素表达式，元素是否存在
    - timeout_secs：超时时间
    - interval_secs：轮训时间
```python
helium.start_chrome("https://www.baidu.com/")

helium.write("Python")
try:
  # 通过显示等待，查询元素是否存在 
  helium.wait_until(helium.S('//input[@id="s22"]').exists)
  # 如果存在就进行点击
  helium.click(helium.S('//input[@id="s22"]'))
except:
  # 当查询元素不存在时，会抛出异常 
  print('元素未找到')
```

### 16. 关闭浏览器

> `helium.kill_browser()`

### 17. S表达式

> `helium.S(selector, below=None, to_right_of=None, above=None, to_left_of=None)`

- 参数
    - selector: jQuery样式选择器（ID、NAME、CSS、XPATH）
```python
helium.start_chrome("https://www.baidu.com/")

helium.write("Python")
helium.click(helium.S('//input[@id="su"]'))
```

### 18. 查找所有符合的标签

> `helium.find_all(predicate)`

```python
helium.start_chrome("https://www.baidu.com/")
eles = helium.find_all(helium.S('//input[@id="su"]'))
print(eles)
# [<input type="submit" id="su" value="百度一下" class="bg s_btn">]
```