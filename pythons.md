<div id="topics">
        <div class="post">

#

[
<span>人生苦短我用 Python，本文助你快速入门</span>

](https://www.cnblogs.com/lbhym/p/14269528.html)<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

<div class="toc"><div class="toc-container-header">目录</div>

- [前言](#前言)
- [Python 基础](#python基础)

  [注释](#注释)

  - [变量](#变量)
  - [数据类型](#数据类型)
    [浮点型](#浮点型)

    - [复数类型](#复数类型)
    - [字符串](#字符串)
    - [布尔类型](#布尔类型)

  - [类型转换](#类型转换)
  - [输入与输出](#输入与输出)
  - [运算符](#运算符)
    [算术运算符](#算术运算符)

    - [比较运算符](#比较运算符)
    - [赋值运算符](#赋值运算符)
    - [逻辑运算符](#逻辑运算符)

  - [if、while、for](#ifwhilefor)

- [容器](#容器)

  [列表](#列表)

  - [元组](#元组)
  - [字典](#字典)
  - [集合](#集合)

- [函数](#函数)

  [函数的定义](#函数的定义)

  - [缺省参数](#缺省参数)
  - [命名参数](#命名参数)
  - [不定长参数](#不定长参数)
  - [匿名函数](#匿名函数)
  - [闭包和装饰器](#闭包和装饰器)

- [包和模块](#包和模块)

  [包](#包)

  - [模块](#模块)

- [面向对象](#面向对象)

  [类和对象](#类和对象)

  - [构造方法](#构造方法)
  - [访问权限](#访问权限)
  - [继承](#继承)

- [异常处理](#异常处理)

  [捕获异常](#捕获异常)

  - [抛出异常](#抛出异常)

- [文件操作](#文件操作)

  [读写文件](#读写文件)

  - [文件管理](#文件管理)
  - [操作 JSON](#操作json)

- [正则表达式](#正则表达式)

  [单字符匹配](#单字符匹配)
  [数量表示](#数量表示)
  [边界表示](#边界表示)
  [转义字符](#转义字符)
  [匹配分组](#匹配分组)
  [操作函数](#操作函数)</div>

  > 友情提示：本文针对的是非编程零基础的朋友，可以帮助我们快速了解 Python 语法，接着就可以快乐的投入到实战环节了。如果是零基础，还是老老实实看书最为稳妥。

## 前言<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

​ 偶然在知乎上看到了一些好玩的 Python 项目([学 Python 都用来干嘛的？](https://www.zhihu.com/question/34098079))，让我对 Python 产生了些许兴趣。距离北漂实习还有两个月时间，正好可以在这段空闲时间里学一学。如果能做出些小工具，说不定对工作还有帮助，何乐而不为呢？

​ 关于环境的安装和 IDE 就不多说了，网上有很多教程。这里贴出一篇博客，大家按里面的步骤安装就行：[VSCode 搭建 Python 开发环境](https://blog.csdn.net/qq429477872/article/details/101721869)。使用 VSCode 主要是因为免费，而且有大量插件可以下载，大家可以尽情的定制自己的 IDE。如果曾经没有使用过 VSCode，最好多了解下哪些必须的插件，优化自己的 Coding 体验。比如：[Python 插件推荐](https://blog.csdn.net/hnshhshjq/article/details/80140401)。

​ 环境搭建好后，就可以愉快地敲代码了。VSCode 需要自己创建 Python 文件，以.py 为后缀。Ctrl+F5 运行程序，F5 调试程序。

## Python 基础<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

### 注释<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

​ 单行注释：#

​ 多行注释：''' (三个英文单引号开头，三个英文单引号结尾)

    <span class="hljs-comment"># 这是单行注释</span>

    <span class="hljs-string">'''
    这是多行注释
    '''</span>
    `</pre>

    ### 变量<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	Python的变量定义不需要显式指明数据类型，直接【变量名=值】即可。注意变量名分大小写，如Name和name不是同一个变量。

    <pre highlighted="true">`name = <span class="hljs-string">"小王"</span>
    print(name) <span class="hljs-comment"># 输出 小王</span>
    `</pre>

    ### 数据类型<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	Python提供**6种基础的数据类型**：数字类型（number）、字符串类型（string）、列表（list）、元组（tuple）、字典（dictionary）、集合（set）。其中数字类型还包括三种数值类型：整型（int）、浮点型（float）、复数类型（complex）。

    ​	列表、元组那些我们留在容器那一节里面讲，先看看数字类型。

    #### 浮点型<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	浮点型表示小数，我们创建一个浮点型变量，再通过type函数看一看它的类型：

    <pre highlighted="true">`pi = <span class="hljs-number">3.1415926</span>
    print(<span class="hljs-built_in">type</span>(pi)) <span class="hljs-comment"># 输出&lt;class 'float'&gt;</span>
    `</pre>

    ​	**int整数型**就不说了，其为Integer的缩写。

    #### 复数类型<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	复数类型，所谓复数就是我们中学学的，实数+虚数，比如：

    <pre highlighted="true">`x = <span class="hljs-number">10</span>+<span class="hljs-number">1.2j</span> <span class="hljs-comment"># 虚数以j或J结尾</span>
    print(<span class="hljs-built_in">type</span>(x)) <span class="hljs-comment"># 输出&lt;class 'complex'&gt;</span>
    `</pre>

    ​	刚开始接触复数时，很纳闷为啥会有这种类型，到底有啥实际作用，遂百度了一番：

    > mzy0324：微电子方面的运算基本全部都是复数运算。

>     hilevel：至少复数用来计算向量的旋转要比矩阵方便多了。科学计算和物理应该会用得到吧。PS:我经常把Python当带编程功能的计算器用，用来调试纯粹的数学算法挺方便的。
>
>     morris88：Python 的一大应用领域，主要是科学计算，主要用于太空宇航、银行等。

    ​	联想到Python平时在算法、科学研究等领域应用颇多，所以也就明白了，只是自己没使用的需求而已。

    #### 字符串<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	字符串类型的变量定义用一对**双引号或者单引号**括起来。如：

    <pre highlighted="true">`x = <span class="hljs-string">"Hello Python"</span>
    y = <span class="hljs-string">'Hello Python'</span>
    print(x,y) <span class="hljs-comment"># 输出Hello Python Hello Python</span>
    `</pre>

    ​	字符串内置函数：

    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">函数</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">find(str[,start,end])</td>
    <td style="text-align: center">在字符串中查找子串str，可选参数start和end可以限定范围</td>
    </tr>
    <tr>
    <td style="text-align: center">count(str[,start,end])</td>
    <td style="text-align: center">在字符串中统计子串str的个数，可选参数start和end可以限定范围</td>
    </tr>
    <tr>
    <td style="text-align: center">replace(old,new[,count])</td>
    <td style="text-align: center">在字符串中用new子串替换old子串，可选参数count代表替换个数，默认全部替换</td>
    </tr>
    <tr>
    <td style="text-align: center">split(sep[,maxsplit])</td>
    <td style="text-align: center">用指定分隔符sep分割字符，返回一个列表，可选参数maxsplit代表分割几次，默认全部</td>
    </tr>
    <tr>
    <td style="text-align: center">upper()、lower()</td>
    <td style="text-align: center">转换大小写</td>
    </tr>
    <tr>
    <td style="text-align: center">join(序列)</td>
    <td style="text-align: center">把序列中的元素用指定字符隔开并生成一个字符串。</td>
    </tr>
    <tr>
    <td style="text-align: center">startwith(prefix[,start,end])</td>
    <td style="text-align: center">判断字符串中是否以prefix开头，返回bool类型。还有一个**endwith**，判断结尾的。</td>
    </tr>
    <tr>
    <td style="text-align: center">strip([,str])</td>
    <td style="text-align: center">去掉字符串开头和结尾的空白字符(包括\n、\t这些)，可选参数代表可以去掉指定字符</td>
    </tr>
    </tbody>
    </table></div>

    #### 布尔类型<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	顺便再说一下布尔类型，不过与Java不同的是，布尔类型的True和False，首字母必须大写：

    <pre highlighted="true">`x = <span class="hljs-literal">True</span>
    print(<span class="hljs-built_in">type</span>(x)) <span class="hljs-comment"># 输出&lt;class 'bool'&gt;</span>
    `</pre>

    ### 类型转换<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	说完几个基本的数据类型，不免要提到类型转换。Python内置一些类型转换的函数：

    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">函数名</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">int(x)</td>
    <td style="text-align: center">将x转换为整型（小数转整型会去掉小数部分）</td>
    </tr>
    <tr>
    <td style="text-align: center">float(x)</td>
    <td style="text-align: center">将x转换为浮点型</td>
    </tr>
    <tr>
    <td style="text-align: center">str(x)</td>
    <td style="text-align: center">将x转换为字符串</td>
    </tr>
    <tr>
    <td style="text-align: center">tuple(x)</td>
    <td style="text-align: center">将x转换为元组</td>
    </tr>
    <tr>
    <td style="text-align: center">list(x)</td>
    <td style="text-align: center">将x转换为列表</td>
    </tr>
    <tr>
    <td style="text-align: center">set(x)</td>
    <td style="text-align: center">将x转换为集合，并去重</td>
    </tr>
    </tbody>
    </table></div>

    ### 输入与输出<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	输入函数为**input**。input函数返回用户输入的信息为字符串类型。所以如果你输入的是数字类型，**记得类型转换**。

    <pre highlighted="true">`x = <span class="hljs-built_in">input</span>(<span class="hljs-string">"请输入数字"</span>)
    print(<span class="hljs-built_in">type</span>(x),x) <span class="hljs-comment"># 输出&lt;class 'str'&gt; 10</span>
    `</pre>

    ​	输出前面已经演示了很多次了，函数为**print**，可以直接输出变量与值。一次输出多个变量可以用**逗号隔开**，就想上面的演示一样，既要输出类型，也要输出值。**不换行**输出，可以在print函数里加上end=""这个参数，因为print默认end="\n"，\n就是换行的意思。如果想输出特殊字符，可能需要用到转义字符：\。

    <pre highlighted="true">`x = <span class="hljs-number">10</span>
    y = <span class="hljs-number">20</span>
    print(x,y,end=<span class="hljs-string">""</span>) <span class="hljs-comment"># 输出10 20 加上end="" 不换行</span>
    print(<span class="hljs-string">"Hello \\n Python"</span>) <span class="hljs-comment"># 输出 Hello \n Python</span>
    `</pre>

    ​	在输出时，还可以**格式化**输出内容：%s代表字符串格式、%d代表整型、%f代表浮点型

    <pre highlighted="true">`z = <span class="hljs-number">1.2</span>
    print(<span class="hljs-string">"%f"</span>%z) <span class="hljs-comment"># 输出 1.200000</span>
    `</pre>

    ​	除了格式化，%d等还可以当作占位符：

    <pre highlighted="true">`name = <span class="hljs-string">"小明"</span>
    age = <span class="hljs-number">18</span>
    print(<span class="hljs-string">"姓名：%s,年龄：%d"</span>%(name,age)) <span class="hljs-comment"># 姓名：小明,年龄：18</span>
    `</pre>

    ​	如果你闲这个占位符麻烦，还可以使用format函数，占位符只用写一对{}：

    <pre highlighted="true">`print(<span class="hljs-string">"姓名：{},年龄：{}"</span>.<span class="hljs-built_in">format</span>(name,age)) <span class="hljs-comment"># 姓名：小明,年龄：18</span>
    `</pre>

    ### 运算符<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    #### 算术运算符<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	除了加减乘除，还有幂（**）、取模（%）、取整（//）

    <pre highlighted="true">`x = <span class="hljs-number">3</span> ** <span class="hljs-number">2</span> <span class="hljs-comment"># x=9 即3的2次方 </span>
    y = <span class="hljs-number">5</span> % <span class="hljs-number">3</span> <span class="hljs-comment"># y=2 即5除以3余2</span>
    z = <span class="hljs-number">5</span> // <span class="hljs-number">2</span> <span class="hljs-comment"># z=2 即5除以2,整数部分为2</span>
    `</pre>

    #### 比较运算符<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	和其他常用编程语言基本一模一样，不等于（!=）、大于等于（&gt;=）、等于（==）。

    #### 赋值运算符<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	Python也支持+=、*=等形式的赋值运算。除此之外，当然也支持前面说到的幂、取模等算术运算符，如取整并赋值（//=）、取模并赋值（%=）。

    <pre highlighted="true">`x = <span class="hljs-number">10</span>
    x %= <span class="hljs-number">3</span>
    print(x) <span class="hljs-comment"># 输出1 ,x%=3 意为 x = x%3</span>
    `</pre>

    #### 逻辑运算符<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	非（not）、与（and）、或（or）

    <pre highlighted="true">`x = <span class="hljs-literal">True</span>
    print(<span class="hljs-keyword">not</span> x) <span class="hljs-comment"># 输出 False</span>
    `</pre>

    ### if、while、for<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	这三个和其他编程语言基本没差，就是写法上有点区别。首先没了大括号，条件语句后以**冒号**开头；代码快有**严格的缩进要求**，因为没了大括号，缩进就是条件语句判断自己代码快范围的依据。其他的基本一样，比如continue跳过当次循环，break跳出整个循环体。下面看三个简单的例子就明白了：

    <pre highlighted="true">`a = <span class="hljs-number">10</span>
    <span class="hljs-comment"># if或else后面是冒号，代码块还需要缩进</span>
    <span class="hljs-keyword">if</span> a &gt;= <span class="hljs-number">10</span>:
        print(<span class="hljs-string">"你好啊老大"</span>)
    <span class="hljs-keyword">else</span>:
        print(<span class="hljs-string">"滚蛋"</span>)

    <span class="hljs-comment"># 同样的while后面也需要冒号，代码块必须缩进。（Python没有num++，得写成num+=1）</span>
    <span class="hljs-comment"># print想不换行打印，最后得加个end="",因为默认有一个end="\n"</span>
    <span class="hljs-comment"># " "*(j-i),代表j-i个空格</span>
    i = <span class="hljs-number">1</span>
    j = <span class="hljs-number">4</span>
    <span class="hljs-keyword">while</span> i &lt;= j:
        print(<span class="hljs-string">" "</span>*(j-i), end=<span class="hljs-string">""</span>)
        n = <span class="hljs-number">1</span>
        <span class="hljs-keyword">while</span> n &lt;= <span class="hljs-number">2</span>*i<span class="hljs-number">-1</span>:
            print(<span class="hljs-string">"*"</span>, end=<span class="hljs-string">""</span>)
            n += <span class="hljs-number">1</span>
        print(<span class="hljs-string">""</span>)
        i += <span class="hljs-number">1</span>

    <span class="hljs-comment"># 语法：for 变量 in 序列 ,还没讲序列，暂时用range表示，代表1-21的序列</span>
    <span class="hljs-comment"># continue略过当次循环，break跳出整个循环</span>
    <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> <span class="hljs-built_in">range</span>(<span class="hljs-number">1</span>, <span class="hljs-number">21</span>):
        <span class="hljs-keyword">if</span> i % <span class="hljs-number">2</span> == <span class="hljs-number">0</span>:
            <span class="hljs-keyword">if</span>(i % <span class="hljs-number">10</span> == <span class="hljs-number">0</span>):
                <span class="hljs-keyword">continue</span>
            <span class="hljs-keyword">if</span>(i &gt;= <span class="hljs-number">15</span>):
                <span class="hljs-keyword">break</span>
            print(i)
    `</pre>

    ## 容器<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ### 列表<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	列表使用一对[]定义，每个元素用逗号隔开，元素类型不强求相同，通过索引获取列表元素。具体的我们看下面的代码：

    <pre highlighted="true">`info_list = [<span class="hljs-string">"小红"</span>, <span class="hljs-number">18</span>, <span class="hljs-string">"男"</span>] <span class="hljs-comment">#可以不是同一类型</span>
    info_list[<span class="hljs-number">2</span>] = <span class="hljs-string">"女"</span> <span class="hljs-comment"># 修改指定索引位置的元素</span>
    <span class="hljs-keyword">del</span> info_list[<span class="hljs-number">1</span>] <span class="hljs-comment"># 删除指定索引位置的元素</span>
    info_list.remove(<span class="hljs-string">"女"</span>) <span class="hljs-comment"># 删除列表中指定的值</span>
    <span class="hljs-keyword">for</span> att <span class="hljs-keyword">in</span> info_list:   <span class="hljs-comment"># 遍历元素</span>
        print(att)
    `</pre>

    ​	上面的示例代码演示了部分列表的用法，下面再列出一些其他的常用函数或语法：

    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">函数或语法</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">list.append(element)</td>
    <td style="text-align: center">向列表list结尾添加元素（这个元素也可以是个列表）</td>
    </tr>
    <tr>
    <td style="text-align: center">list.insert(index,element)</td>
    <td style="text-align: center">向列表指定位置添加元素</td>
    </tr>
    <tr>
    <td style="text-align: center">list.extend(new_list)</td>
    <td style="text-align: center">向列表list添加new_list的所有元素</td>
    </tr>
    <tr>
    <td style="text-align: center">list.pop([,index])</td>
    <td style="text-align: center">弹出最后一个元素，可选参数index，弹出指定位置元素</td>
    </tr>
    <tr>
    <td style="text-align: center">list.sort([,reverse=True])</td>
    <td style="text-align: center">对列表排序，可选参数reverse=True表示降序</td>
    </tr>
    <tr>
    <td style="text-align: center">list[start:end]</td>
    <td style="text-align: center">对列表分片，start和end代表起始结束索引</td>
    </tr>
    <tr>
    <td style="text-align: center">list1+list2</td>
    <td style="text-align: center">拼接两个列表</td>
    </tr>
    </tbody>
    </table></div>

    ### 元组<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	元组用一对（）定义。元组也是有序的，它和列表的区别就是，列表可以修改元素，元组不行。正是因为这个特点，元组占用的内存也比列表小。

    <pre highlighted="true">`name_list=(<span class="hljs-string">"小红"</span>,<span class="hljs-string">"小王"</span>)
    `</pre>

    ### 字典<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	字典使用一对{}定义，元素是键值对。用法示例如下：

    <pre highlighted="true">`user_info_dict = {<span class="hljs-string">"name"</span>: <span class="hljs-string">"小王"</span>, <span class="hljs-string">"age"</span>: <span class="hljs-string">"18"</span>, <span class="hljs-string">"gender"</span>: <span class="hljs-string">"男"</span>}
    name = user_info_dict[<span class="hljs-string">"name"</span>] <span class="hljs-comment"># 直接用key获取value</span>
    age = user_info_dict.get(<span class="hljs-string">"age"</span>) <span class="hljs-comment"># 也可以用get(key)获取value</span>
    user_info_dict[<span class="hljs-string">"tel"</span>] = <span class="hljs-string">"13866663333"</span> <span class="hljs-comment"># 当key不存在，就是往字典添加键值对，如果存在就是修改value</span>
    <span class="hljs-keyword">del</span> user_info_dict[<span class="hljs-string">"tel"</span>] <span class="hljs-comment"># 删除指定键值对</span>
    `</pre>

    ​	以上就是常用语法和函数。字典也可以遍历，只是遍历时，需要指定遍历的是key还是value，比如：

    <pre highlighted="true">`<span class="hljs-keyword">for</span> k <span class="hljs-keyword">in</span> <span class="hljs-built_in">dict</span>.keys(): <span class="hljs-comment"># 遍历所有key</span>
    <span class="hljs-keyword">for</span> v <span class="hljs-keyword">in</span> <span class="hljs-built_in">dict</span>.values(): <span class="hljs-comment"># 遍历所有value</span>
    <span class="hljs-keyword">for</span> item <span class="hljs-keyword">in</span> <span class="hljs-built_in">dict</span>.items(): <span class="hljs-comment"># 也可以直接遍历键值对</span>
    `</pre>

    ### 集合<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	集合是无序的，也用一对{}定义，但不是键值对了，是单独且不重复的元素。部分用法如下：

    <pre highlighted="true">`user_id_set = {<span class="hljs-string">"1111"</span>,<span class="hljs-string">"22222"</span>,<span class="hljs-string">"3333"</span>} <span class="hljs-comment"># 元素不重复</span>
    print(<span class="hljs-built_in">type</span>(user_id_set)) <span class="hljs-comment"># 输出&lt;class 'set'&gt;</span>
    <span class="hljs-comment"># 除了直接用{}定义，还可以用set函数传入一个序列，其会为list去重，并返回一个集合（如果是字符串，字符串会被拆成字符）</span>
    new_user_id_set = <span class="hljs-built_in">set</span>(<span class="hljs-built_in">list</span>)
    `</pre>

    ​	上面演示了部分用法，下面我们用一个表格展示一些常用的函数或语法：

    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">函数或语法</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">element in set</td>
    <td style="text-align: center">判断元素是否在集合中，返回布尔类型</td>
    </tr>
    <tr>
    <td style="text-align: center">element not in set</td>
    <td style="text-align: center">判断元素是否不在集合中</td>
    </tr>
    <tr>
    <td style="text-align: center">set.add(element)</td>
    <td style="text-align: center">向集合添加元素</td>
    </tr>
    <tr>
    <td style="text-align: center">set.update(list,.....)</td>
    <td style="text-align: center">将序列中的每个元素去重并添加到集合中，如果有多个序列，用逗号隔开</td>
    </tr>
    <tr>
    <td style="text-align: center">set.remove(element)</td>
    <td style="text-align: center">删除指定元素，如果元素不存在就会报错</td>
    </tr>
    <tr>
    <td style="text-align: center">set.discard(element)</td>
    <td style="text-align: center">删除指定元素，如果元素不存在也不会报错</td>
    </tr>
    <tr>
    <td style="text-align: center">set.pop()</td>
    <td style="text-align: center">随机删除集合中的元素，并返回被删除的元素</td>
    </tr>
    <tr>
    <td style="text-align: center">set1 &amp; set2 或set1 intersection set2</td>
    <td style="text-align: center">求两个集合的交集，两种用法结果一样</td>
    </tr>
    <tr>
    <td style="text-align: center">set1 | set2 或set1 union set2</td>
    <td style="text-align: center">求两个集合的并集</td>
    </tr>
    <tr>
    <td style="text-align: center">set1 - set2 或set1.difference(set2)</td>
    <td style="text-align: center">求两个集合的差集，注意顺序。set1-set2代表set1有set2没有的元素</td>
    </tr>
    </tbody>
    </table></div>

    ## 函数<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ### 函数的定义<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	Python中函数用**def**定义，格式为：

    <pre highlighted="true">`<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">function_name</span>(<span class="hljs-params">参数列表</span>):</span> <span class="hljs-comment"># 参数可为空，多个参数用逗号隔开</span>
    	函数体
    	<span class="hljs-keyword">return</span> 返回值 <span class="hljs-comment">#可选</span>

    <span class="hljs-comment"># 函数的调用</span>
    function_name(参数列表)
    `</pre>

    ### 缺省参数<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	和循环体一样的，因为没有了大括号，所以**缩进是严格要求的**。除了上面那种比较常见的格式，Python函数的参数中，还有一种缺省参数，即**带有默认值的参数**。调用带有缺省参数的函数时，可以不用传入缺省参数的值，如果传入了缺省参数的值，则会使用传入的值。

    <pre highlighted="true">`<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">num_add</span>(<span class="hljs-params">x,y=<span class="hljs-number">10</span></span>):</span> <span class="hljs-comment"># y为缺省函数，如果调用这个函数只传入了x的值，那么y默认为10</span>
    `</pre>

    ### 命名参数<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	一般情况下，调用函数传入实参时，都会遵循参数列表的顺序。而命名参数的意思就是，调用函数时，通过参数名传入实参，这样可以不用按照参数定义的顺序传入实参。

    <pre highlighted="true">`<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">num_add</span>(<span class="hljs-params">x, y</span>):</span>
        print(<span class="hljs-string">"x:{},y:{}"</span>.<span class="hljs-built_in">format</span>(x, y))
        <span class="hljs-keyword">return</span> x+y
    <span class="hljs-comment"># 输出：</span>
    <span class="hljs-comment"># x:10,y:5</span>
    <span class="hljs-comment"># 15</span>
    print(num_add(y=<span class="hljs-number">5</span>, x=<span class="hljs-number">10</span>))
    `</pre>

    ### 不定长参数<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	不定长参数可以接收任意多个参数，Python中有两种方法接收：1.在参数前加一个*，传入的参数会放到元组里；2.在参数前加两个**，代表接收的是键值对形式的参数。

    <pre highlighted="true">`<span class="hljs-comment"># 一个*</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">eachNum</span>(<span class="hljs-params">*args</span>):</span>
        print(<span class="hljs-built_in">type</span>(args))
        <span class="hljs-keyword">for</span> num <span class="hljs-keyword">in</span> args:
            print(num)
    <span class="hljs-comment"># 输出：</span>
    <span class="hljs-comment"># &lt;class 'tuple'&gt;‘</span>
    <span class="hljs-comment"># (1, 2, 3, 4, 5)</span>
    eachNum(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>)

    <span class="hljs-comment">## 两个**。这个other是想告诉你，在使用不定长参数时，也可以搭配普通的参数</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">user_info</span>(<span class="hljs-params">other,**info</span>):</span>
        print(<span class="hljs-built_in">type</span>(info))
        print(<span class="hljs-string">"其他信息：{}"</span>.<span class="hljs-built_in">format</span>(other))
        <span class="hljs-keyword">for</span> key <span class="hljs-keyword">in</span> info.keys():
            print(<span class="hljs-string">"{} : {}"</span>.<span class="hljs-built_in">format</span>(key,info[key]))
    <span class="hljs-comment"># 传入参数时，不用像定义字典一样，加个大括号再添加键值对，直接当命名参数传入即可</span>
    <span class="hljs-comment"># 输出：</span>
    <span class="hljs-comment"># &lt;class 'dict'&gt;</span>
    <span class="hljs-comment"># 其他信息：管理员</span>
    <span class="hljs-comment"># 略...</span>
    user_info(<span class="hljs-string">"管理员"</span>,name=<span class="hljs-string">"赵四"</span>,age=<span class="hljs-number">18</span>,gender=<span class="hljs-string">"男"</span>)
    `</pre>

    ​	上面示例代码中的注释说到了，当使用不定长参数时，不用像字典或者元组的定义那样，直接传入参数即可。但有时候，可能会遇到想把字典、元组等容器中的元素传入到不定长参数的函数中，这个时候就需要用到**拆包**了。

    ​	所谓拆包，其实就是在传入参数时，在容器前面加上一个或两个*。还是以上面的user_info函数为例：

    <pre highlighted="true">`user_info_dict={<span class="hljs-string">"name"</span>:<span class="hljs-string">"赵四"</span>,<span class="hljs-string">"age"</span>:<span class="hljs-number">18</span>,<span class="hljs-string">"gender"</span>:<span class="hljs-string">"男"</span>}
    user_info(<span class="hljs-string">"管理员"</span>,**user_info_dict) <span class="hljs-comment"># 效果和上面一样</span>
    `</pre>

    ​	注意，如果接收方的不定长参数只用了一个 * 定义，那么传入实参时，也只能用一个  *。

    ### 匿名函数<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	匿名函数，即没有名字的函数。在定义匿名函数时，既不需要名称，也不需要def关键字。语法如下：

    <pre highlighted="true">`<span class="hljs-keyword">lambda</span> 参数列表: 表达式
    `</pre>

    ​	多个参数用逗号隔开，匿名函数会自动把表达式的结果return。在使用时，一般会用一个变量接收匿名函数，或者直接把匿名函数当参数传入。

    <pre highlighted="true">`<span class="hljs-built_in">sum</span> = <span class="hljs-keyword">lambda</span> x,y : x+y
    print(<span class="hljs-built_in">sum</span>(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)) <span class="hljs-comment"># 输出3</span>
    `</pre>

    ### 闭包和装饰器<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	在Python中，函数内还可以定义函数，外面这个函数我们就称为外部函数，里面的函数我们就称为内部函数。而外部函数的返回值是**内部函数的引用**，这种表达方式就是**闭包**。内部函数可以调用外部函数的变量，我们看一个示例：

    <pre highlighted="true">`<span class="hljs-comment"># 外部函数</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">sum_closure</span>(<span class="hljs-params">x</span>):</span>
        <span class="hljs-comment"># 内部函数</span>
        <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">sum_inner</span>(<span class="hljs-params">y</span>):</span>
            <span class="hljs-keyword">return</span> x+y
        <span class="hljs-keyword">return</span> sum_inner <span class="hljs-comment"># 返回内部函数</span>
    <span class="hljs-comment"># 获取了内部函数</span>
    var1 = sum_closure(<span class="hljs-number">1</span>)
    print(var1) <span class="hljs-comment"># 输出&lt;function sum_closure.&lt;locals&gt;.sum_inner at 0x000001D82900E0D0&gt;，是个函数类型</span>
    print(var1(<span class="hljs-number">2</span>)) <span class="hljs-comment"># 输出3</span>
    `</pre>

    ​	说完闭包的用法，接着了解一下**装饰器**。不知道大家了解过AOP没，即面向切面编程。说人话就是在目标函数前后加上一些公共函数，比如记录日志、权限判断等。Python中当然也提供了实现切面编程的方法，那就是装饰器。装饰器和闭包一起，可以很灵活的实现类似功能，下面看示例：

    <pre highlighted="true">`<span class="hljs-keyword">import</span> datetime <span class="hljs-comment">#如果没有这个包，在终端里输入pip3 install datetime</span>
    <span class="hljs-comment"># 外部函数，其参数是目标函数</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">log</span>(<span class="hljs-params">func</span>):</span>
        <span class="hljs-comment">#内部函数，参数得和目标函数一致。也可以使用不定长参数，进一步提升程序灵活性</span>
        <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">do</span>(<span class="hljs-params">x, y</span>):</span>
            <span class="hljs-comment"># 假装记录日志，执行切面函数。（第一次datetime是模块、第二个是类、now是方法。在下一节讲到模块）</span>
            print(<span class="hljs-string">"时间：{}"</span>.<span class="hljs-built_in">format</span>(datetime.datetime.now()))
            print(<span class="hljs-string">"记录日志"</span>)
            <span class="hljs-comment"># 执行目标函数</span>
            func(x, y)
        <span class="hljs-keyword">return</span> do

    <span class="hljs-comment"># @就是装饰器的语法糖，log外部函数</span>
    <span class="hljs-meta">@ log</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">something</span>(<span class="hljs-params">x, y</span>):</span>
        print(x+y)

    <span class="hljs-comment"># 调用目标函数</span>
    <span class="hljs-comment"># 输出：</span>
    <span class="hljs-comment"># 时间：2021-01-06 16:17:00.677198</span>
    <span class="hljs-comment"># 记录日志</span>
    <span class="hljs-comment"># 30</span>
    something(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>)
    `</pre>

    ​	函数相关的就说到这里了，其实还有一些知识没说到，比如变量的作用域、返回值等。这部分内容和其他语言几乎无异，一点区别无非就是返回值不用在乎类型了，毕竟定义函数时也没指定函数返回值类型，这一点各位老司机应该也会想到。

    ## 包和模块<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ### 包<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	Python中包与普通文件夹的区别就是，包内要创建一个__init__.py文件，来标识它是一个包。这个文件可以是空白的，也可以定义一些**初始化操作**。当其他包下的模块调用本包下的模块时，**会自动的执行__init__.py文件的内容**。

    ### 模块<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	一个Python文件就是一个模块，不同包下的模块可以重名，在使用的时候以“包名.模块名”区别。导入其他模块用import关键字，前面的示例代码中也演示过一次。导入多个模块可以用逗号隔开，也可以直接分开写。除了导入整个模块，还可以导入模块中指定的函数或类：

    <pre highlighted="true">`<span class="hljs-keyword">from</span> model_name <span class="hljs-keyword">import</span> func_name(<span class="hljs-keyword">or</span> class_name)
    `</pre>

    ​	导入函数或类后，就不要使用模块名了，**直接调用导入的类或函数即可**。

    ## 面向对象<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ### 类和对象<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	Python是一种面向对象的解释型编程语言。面向对象的关键就在于类和对象。Python中类的定义用class关键字，如下：

    <pre highlighted="true">`<span class="hljs-class"><span class="hljs-keyword">class</span> 类名:</span>
    	<span class="hljs-function"><span class="hljs-keyword">def</span> 方法名(<span class="hljs-params">self[,参数列表]</span>)
    	...
    </span>`</pre>

    ​	定义在类里面的函数叫做方法，只是与类外部的函数做个区分，不用在意叫法。类里面的方法，参数列表中会有一个默认的参数，表示当前对象，**你可以当作Java中的this**。因为一个类可以创建多个对象，有了self，Python就知道自己在操作哪个对象了。我们在调用这个方法时，**不需要手动传入self**。示例代码：

    <pre highlighted="true">`<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span>:</span>
        <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">do</span>(<span class="hljs-params">self</span>):</span>
            print(self)
    <span class="hljs-comment"># 创建两个Demmo类型的对象</span>
    demo1=Demo()
    demo1.do() <span class="hljs-comment"># 输出&lt;__main__.Demo object at 0x0000019C78106FA0&gt;</span>
    demo2=Demo()
    demo2.do() <span class="hljs-comment"># 输出&lt;__main__.Demo object at 0x0000019C77FE8640&gt;</span>
    print(<span class="hljs-built_in">type</span>(demo1)) <span class="hljs-comment"># &lt;class '__main__.Demo'&gt;</span>
    `</pre>

    ### 构造方法<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	构造方法的作用是在创建一个类的对象时，对对象进行初始化操作。Python中类的构造方法的名称是__init__（两边分别两个下划线）。在创建对象时，__init__方法自动执行。和普通方法一样的，如果你想自定义构造方法，也要接收self参数。示例代码：

    <pre highlighted="true">`<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span>:</span>
        <span class="hljs-comment"># 构造方法，还可以传入其他参数化</span>
        <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self,var1,var2</span>):</span>
            <span class="hljs-comment"># 把参数设置到当前对象上，即使类中没有属性也可以设置</span>
            self.var1=var1
            self.var2=var2
            print(<span class="hljs-string">"初始化完成"</span>)
        <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">do</span>(<span class="hljs-params">self</span>):</span>
            print(<span class="hljs-string">"Working..."</span>)
    <span class="hljs-comment"># 通过构造方法传入实参</span>
    demo1=Demo(<span class="hljs-number">66</span>,<span class="hljs-number">77</span>)
    demo1.do()
    <span class="hljs-comment"># 通过当前对象，获取刚刚设置的参数</span>
    print(demo1.var1)
    print(demo1.var2)
    `</pre>

    ### 访问权限<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	Java或C#中有好几种访问权限，在Python中，**属性和方法前添加两个下划线**即为私有，反之就是共公有。具有私有访问权限的属性和方法，**只能在类的内部方法**，外部无法访问。和其他语言一样，私有的目的是为了保证属性的准确性和安全性，示例代码如下：

    <pre highlighted="true">`<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span>:</span>
        <span class="hljs-comment"># 为了方便理解，我们显示的设置一个私有属性</span>
        __num = <span class="hljs-number">10</span>
        <span class="hljs-comment"># 公有的操作方法，里面加上判断，保证数据的准确性</span>
        <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">do</span>(<span class="hljs-params">self, temp</span>):</span>
            <span class="hljs-keyword">if</span> temp &gt; <span class="hljs-number">10</span>:
                self.__set(temp)
    	<span class="hljs-comment"># 私有的设置方法，不让外部直接设置属性</span>
        <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__set</span>(<span class="hljs-params">self, temp</span>):</span>
            self.__num = temp
    	<span class="hljs-comment"># 公有的get方法</span>
        <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">get</span>(<span class="hljs-params">self</span>):</span>
            print(self.__num)

    demo1 = Demo()
    demo1.do(<span class="hljs-number">11</span>)
    demo1.get() <span class="hljs-comment"># 输出 11</span>
    `</pre>

    ​	一堆self.刚开始看时还有点晕乎，把它当作this就好。

    ### 继承<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	继承是面向对象编程里另一大利器，好处之一就是代码重用。子类只能继承父类的**公有属性和方法**，Python的语法如下：

    <pre highlighted="true">`<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SonClass</span>(<span class="hljs-params">FatherClass</span>):</span>
    `</pre>

    ​	当我们创建一个SonClass对象时，直接可以用该对象调用FatherClass的公有方法。Python还支持多继承，如果是多继承就在小括号里把父类用逗号隔开。

    ​	如果想在子类里面调用父类的方法，一般有两种方式：1.父类名.方法名(self[,参数列表])。此时的self是子类的self，且需要显示传入；2.super().方法名()。第二种方式因为没有指定父类，所以在多继承的情况下，如果调用了这些父类中同名的方法，Python实际会执行小括号里写在前面的父类中的方法。

    ​	如果子类定义了与父类同名的方法，子类的方法就会覆盖父类的方法，这就是**重写**。

    ## 异常处理<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ### 捕获异常<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	捕获异常的语法如下：

    <pre highlighted="true">`<span class="hljs-keyword">try</span>:
        代码快 <span class="hljs-comment"># 可能发生异常的代码</span>
    <span class="hljs-keyword">except</span> (异常类型,...) <span class="hljs-keyword">as</span> err: <span class="hljs-comment"># 多个异常类型用逗号隔开，如果只有一个异常类型可以不要小括号。err是取的别名</span>
        异常处理
    <span class="hljs-keyword">finally</span>:
        代码快 <span class="hljs-comment"># 无论如何都会执行</span>
    `</pre>

    ​	在try代码块中，错误代码之后的代码是不会执行的，但**不会影响到try ... except之外的代码**。看个示例代码：

    <pre highlighted="true">`<span class="hljs-keyword">try</span>:
        <span class="hljs-built_in">open</span>(<span class="hljs-string">"123.txt"</span>) <span class="hljs-comment">#打开不存在的文件，发生异常</span>
        print(<span class="hljs-string">"hi"</span>) <span class="hljs-comment"># 这行代码不会执行</span>
    <span class="hljs-keyword">except</span> FileNotFoundError <span class="hljs-keyword">as</span> err:
        print(<span class="hljs-string">"发生异常：{}"</span>.<span class="hljs-built_in">format</span>(err)) <span class="hljs-comment"># 异常处理</span>

    print(<span class="hljs-string">"我是try except之外的代码"</span>) <span class="hljs-comment">#正常执行</span>
    `</pre>

    ​	虽然上面的内容和其他语言相差不大，但是刚刚接触Python鬼知道有哪些异常类型，有没有类似Java的Exception异常类型呢？肯定是有的。Python同样提供了**Exception**异常类型来捕获全部异常。

    ​	那如果发生异常的代码没有用try except捕获呢？这种情况要么直接报错，程序停止运行。要么会被外部的try except捕获到，也就是说**异常是可以传递的**。比如func1发生异常没有捕获，func2调用了func1并用了try except，那么func1的异常会被传递到func2这里。是不是和Java的throws差不多？

    ### 抛出异常<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	Python中抛出异常的关键字是**raise**，其作用和Java的throw new差不多。示例代码如下：

    <pre highlighted="true">`<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">do</span>(<span class="hljs-params">x</span>):</span>
        <span class="hljs-keyword">if</span>(x&gt;<span class="hljs-number">3</span>): <span class="hljs-comment"># 如果大于3就抛出异常</span>
            <span class="hljs-keyword">raise</span> Exception(<span class="hljs-string">"不能大于3"</span>) <span class="hljs-comment"># 抛出异常，如果你知道具体的异常最好，后面的小括号可以写上异常信息</span>
        <span class="hljs-keyword">else</span>:
            print(x)

    <span class="hljs-keyword">try</span>:
        do(<span class="hljs-number">4</span>)
    <span class="hljs-keyword">except</span> Exception <span class="hljs-keyword">as</span> err:
        print(<span class="hljs-string">"发生异常：{}"</span>.<span class="hljs-built_in">format</span>(err)) <span class="hljs-comment"># 输出 发生异常：不能大于3</span>
    `</pre>

    ## 文件操作<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ### 读写文件<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	想要操作一个文件，首先得打开它。Python中有个内置的函数：**open**。使用open打开文件可以有三种模式，分别为：只读（默认的模式，只能读取文件内容，r表示）、只写（会覆盖原文本内容，w表示）、追加（新内容追加到末尾，a表示）。示例如下：

    <pre highlighted="true">`f = <span class="hljs-built_in">open</span>(<span class="hljs-string">"text.txt"</span>,<span class="hljs-string">"a"</span>) <span class="hljs-comment"># 用追加的方式获取文件对象</span>
    `</pre>

    ​	因为text.txt和代码在同一目录所以只写了文件名，如果不在同一目录需要写好相对路径或绝对路径。

    ​	获取到文件对象后，接下来就可以操作了，反正就是些API，直接看示例：

    <pre highlighted="true">`f = <span class="hljs-built_in">open</span>(<span class="hljs-string">"text.txt"</span>,<span class="hljs-string">"a"</span>,encoding=<span class="hljs-string">"utf-8"</span>) <span class="hljs-comment"># 以追加的方式打开文件，并设置编码方式，因为接下来要写入中文</span>
    f.write(<span class="hljs-string">"234567\n"</span>) <span class="hljs-comment"># 写入数据，最后的\n是换行符，实现换行</span>
    f.writelines([<span class="hljs-string">"张三\n"</span>,<span class="hljs-string">"赵四\n"</span>,<span class="hljs-string">"王五\n"</span>]) <span class="hljs-comment"># write只能写一个字符串，writelines可以写入一列表的字符串</span>
    f.close() <span class="hljs-comment"># 操作完记得关闭</span>
    `</pre>

    ​	以上是写文件的两个方法。最后记得关闭文件，因为操作系统会把写入的内容缓存起来，万一系统崩溃，写入的数据就会丢失。虽然程序执行完文件会自动关闭，但是实际项目中，肯定不止这点代码。Python也很贴心，防止我们忘了close，提供了一种安全打开文件的方式，语法是 with open() as 别名：，示例如下

    <pre highlighted="true">`<span class="hljs-keyword">with</span> <span class="hljs-built_in">open</span>(<span class="hljs-string">"test.txt"</span>,<span class="hljs-string">"w"</span>) <span class="hljs-keyword">as</span> f: <span class="hljs-comment"># 安全打开文件，不需要close。</span>
        f.write(<span class="hljs-string">"123"</span>)
    `</pre>

    ​	写完了，该读一读了。示例如下：

    <pre highlighted="true">`f = <span class="hljs-built_in">open</span>(<span class="hljs-string">"text.txt"</span>,<span class="hljs-string">"r"</span>,encoding=<span class="hljs-string">"utf-8"</span>)
    data = f.read() <span class="hljs-comment"># read会一次性读出所有内容</span>
    print(data)
    f.close()
    `</pre>

    ​	除了一次性读取完，还可以按行的方式返回全部内容，并用一个列表装起来，这样我们就可以进行遍历了。方法是readlines，示例如下：

    <pre highlighted="true">`f = <span class="hljs-built_in">open</span>(<span class="hljs-string">"text.txt"</span>,<span class="hljs-string">"r"</span>,encoding=<span class="hljs-string">"utf-8"</span>)
    lines = f.readlines() <span class="hljs-comment"># lines是个列表</span>
    <span class="hljs-keyword">for</span> line <span class="hljs-keyword">in</span> lines:
        print(line)
    f.close()
    `</pre>

    ### 文件管理<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	在操作文件的时候，肯定不止读写这么简单，可能还会涉及文件的删除、重命名、创建等等。在用Python的函数操作文件之前，需要导入os模式：`import os` 。下面简单的演示一下重命名的函数，其他的函数我们以表格的形式展现。

    <pre highlighted="true">`<span class="hljs-keyword">import</span> os
    os.rename(<span class="hljs-string">"text.txt"</span>,<span class="hljs-string">"123.txt"</span>) <span class="hljs-comment"># 把text.txt改名为123.txt</span>
    `</pre>
    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">函数</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">os.remove(path)</td>
    <td style="text-align: center">删除指定文件</td>
    </tr>
    <tr>
    <td style="text-align: center">os.mkdir(path)</td>
    <td style="text-align: center">在指定路径下创建新文件</td>
    </tr>
    <tr>
    <td style="text-align: center">os.getcwd()</td>
    <td style="text-align: center">获取程序运行的绝对路径</td>
    </tr>
    <tr>
    <td style="text-align: center">os.listdir(path)</td>
    <td style="text-align: center">获取指定路径下的文件列表，包含文件和文件夹</td>
    </tr>
    <tr>
    <td style="text-align: center">os.redir(path)</td>
    <td style="text-align: center">删除指定路径下的空文件夹（如果不是空文件夹就会报错）</td>
    </tr>
    </tbody>
    </table></div>

    ### 操作JSON<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	学了前面的容器，会发现JSON的格式和Python的字典有点像，都是键值对形式的。虽然格式很像，但还是有点小区别，比如：Python的元组和列表在JSON中都是列表、Python的True和Flase会被转换成小写、空类型None会被转换成null。下面我们来看一些具体的函数把。

    ​	在Python中操作JSON格式的数据需要导入json模块。同样的，我这里只演示一个函数，其他常用的用表格列出来。

    <pre highlighted="true">`<span class="hljs-keyword">import</span> json
    user_info={<span class="hljs-string">"name"</span>:<span class="hljs-string">"张三"</span>,<span class="hljs-string">"age"</span>:<span class="hljs-number">18</span>,<span class="hljs-string">"gender"</span>:<span class="hljs-string">"男"</span>,<span class="hljs-string">"hobby"</span>:(<span class="hljs-string">"唱歌"</span>,<span class="hljs-string">"跳舞"</span>,<span class="hljs-string">"打篮球"</span>),<span class="hljs-string">"other"</span>:<span class="hljs-literal">None</span>} <span class="hljs-comment"># 创建一个字典</span>
    json_str=json.dumps(user_info,ensure_ascii=<span class="hljs-literal">False</span>) <span class="hljs-comment"># dumps函数会把字典转换为json字符串</span>
    <span class="hljs-comment"># 输出 {"name": "张三", "age": 18, "gender": "男", "hobby": ["唱歌", "跳舞", "打篮球"], "other": null}</span>
    print(json_str)
    `</pre>

    ​	需要注意如果数据存在中文，需要在dumps函数加上`ensure_ascii=False`。

    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">函数</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">json.loads(json_str)</td>
    <td style="text-align: center">把json字符串转换为Python数据结构</td>
    </tr>
    <tr>
    <td style="text-align: center">json.dump(user_info,file)</td>
    <td style="text-align: center">把Python数据写入到json文件，要先获取文件，那个file就是文件对象</td>
    </tr>
    <tr>
    <td style="text-align: center">json.load(file)</td>
    <td style="text-align: center">把json文件中的数据转为成Python数据结构，同样需要获取文件</td>
    </tr>
    </tbody>
    </table></div>

    ​	关于JSON的操作就说这些。通用的数据格式不止JSON一种，比如还有xml、csv等。为了节约篇幅，就不再赘述了，大家可以根据自己的需求查对应的API即可。

    ## 正则表达式<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	最后一节讲正则表达式，一是因为这也算个基础知识，在很多地方都有可能用到。二是因为后面的爬虫实战，肯定会用到正则表达式来解析各种数据。

    ​	Python中内置了re模块来处理正常表达式，有了这个模块我们就可以很方便的对字符串进行各种规则匹配检查。不过正则表达式真正难的是表达式的书写，函数主要就一个：`re.match(pattern,string)`，其中pattren就是正则表达式，stirng就是待匹配字符串。如果匹配成功就会返回一个Match对象，否则就返回None。**匹配是从左往右，如果不匹配就直接返回None，不会接着匹配下去**。示例如下：

    <pre highlighted="true">`<span class="hljs-keyword">import</span> re
    res=re.match(<span class="hljs-string">"asd"</span>,<span class="hljs-string">"asdabcqwe"</span>) <span class="hljs-comment"># 匹配字符串中是否有asd(如果asd不在开头就会返回None)</span>
    print(res) <span class="hljs-comment"># 输出 &lt;re.Match object; span=(0, 3), match='asd'&gt;</span>
    print(res.group()) <span class="hljs-comment"># 输出 asd 如果想获取匹配的子字符就用这个函数</span>
    `</pre>

    ​	秉着帮人帮到底的精神，下面就简单的介绍下正则表达式的一些规则。

    ### 单字符匹配<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	单字符匹配，顾名思义就是匹配一个字符。除了直接使用某个具体的字符，还可以使用以下符号来进行匹配：

    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">符号</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">.</td>
    <td style="text-align: center">匹配除”\n“以外的任意单个字符</td>
    </tr>
    <tr>
    <td style="text-align: center">\d</td>
    <td style="text-align: center">匹配0-9之间的一个数字，等价于[0-9]</td>
    </tr>
    <tr>
    <td style="text-align: center">\D</td>
    <td style="text-align: center">匹配一个非数字字符，等价于[^0-9]</td>
    </tr>
    <tr>
    <td style="text-align: center">\s</td>
    <td style="text-align: center">匹配任意空白字符，如空格、\t、\n等</td>
    </tr>
    <tr>
    <td style="text-align: center">\S</td>
    <td style="text-align: center">匹配任意非空白字符</td>
    </tr>
    <tr>
    <td style="text-align: center">\w</td>
    <td style="text-align: center">匹配单词字符，包括字母、数字、下划线</td>
    </tr>
    <tr>
    <td style="text-align: center">\W</td>
    <td style="text-align: center">匹配非单词字符</td>
    </tr>
    <tr>
    <td style="text-align: center">[]</td>
    <td style="text-align: center">匹配[]中列举的字符，比如[abc]，只要出现这三个字母中的一个即可匹配</td>
    </tr>
    </tbody>
    </table></div>

    ​	以防有的朋友从未接触过正则表达式，不知道怎么用，下面我来做个简答的演示。假如我想匹配三个字符：第一个是数字、第二个是空格、第三个是字母，一起来看看怎么写这个正则表达式吧：

    <pre highlighted="true">`<span class="hljs-keyword">import</span> re
    pattern = <span class="hljs-string">"\d\s\w"</span> <span class="hljs-comment"># \d匹配数字、\s匹配空格、\w匹配字母（切记是从左往右依次匹配的，只要有一个字符匹配不上就直接返回None）</span>
    string = <span class="hljs-string">"2 z你好"</span>
    res=re.match(pattern,string)
    print(res.group()) <span class="hljs-comment"># 输出:2 z</span>
    `</pre>

    ​	看到这你可能会想，非得一个个字符匹配，那多麻烦啊，有没有更灵活的规则？当然有了，接着看。

    ### 数量表示<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	如果我们只想匹配字母，但不限制有多少个，该怎么写呢？看下面的表格就知道了：

    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">符号</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">*</td>
    <td style="text-align: center">匹配一个字符出现0次或多次</td>
    </tr>
    <tr>
    <td style="text-align: center">+</td>
    <td style="text-align: center">匹配一个字符至少出现一次，等价于{,1}</td>
    </tr>
    <tr>
    <td style="text-align: center">?</td>
    <td style="text-align: center">匹配一个字符出现0次或1次，等价于{1,2}</td>
    </tr>
    <tr>
    <td style="text-align: center">{m}</td>
    <td style="text-align: center">匹配一个字符出现m次</td>
    </tr>
    <tr>
    <td style="text-align: center">{m,}</td>
    <td style="text-align: center">匹配一个字符至少出现m次</td>
    </tr>
    <tr>
    <td style="text-align: center">{m,n}</td>
    <td style="text-align: center">匹配一个字符出现m到n次</td>
    </tr>
    </tbody>
    </table></div>

    ​	数量匹配的符号后面如果加上`?`，**就会尽可能少的去匹配字符**，在Python里面叫非贪婪模式，反之默认的就是贪婪模式。比如`{m,}`会尽可能多的去匹配字符，而`{m,}?`在满足至少有m个的情况下尽可能少的去匹配字符。其他的同理。

    ​	来看一个例子，我想匹配开头是任意个小写字母，接着是1到5个2-6的数字，最后是至少一个空格：

    <pre highlighted="true">`<span class="hljs-keyword">import</span> re
    pat = <span class="hljs-string">r"[a-z]*[2-6]{1,5}\s+"</span>
    <span class="hljs-built_in">str</span> = <span class="hljs-string">"abc423  你好"</span>
    res=re.match(pat,<span class="hljs-built_in">str</span>)
    print(res) <span class="hljs-comment">#输出 abc423  </span>
    `</pre>

    ​	我们来解析下这个正则表达式，pat字符串开头的r是告诉Python这是个正则表达式，不要转义里面的\，建议写表达式时都加上。`[a-z]`代表任意小写字母，不用\w的原因是，\w还包括数字、下划线，没有严格符合我们的要求。加上个*就代表任意数量。这里强调一下**单字符匹配和数量表示之间的逻辑关系**，以`[a-z]*`为例，**其表达的是任意个`[a-z]`，而不是某个字母有任意个**。明白了这个逻辑后，其他的也好理解了。

    ​	前面的例子都是我随意编的，其实学了这些，已经可以写出一个有实际作用的表达式了，比如我们来匹配一个手机号。首先手机号只有11位，第一个数字必须是1，第二个是3、5、7、8中的一个。知道了这三个个规律，我们来写一下表达式：`1[3578]\d{9}`。看上去好像可以，但是仔细一想，前面不是说了正则表达式是从左往右匹配，只要符合了就会返回结果，也不会管字符串匹配完全没有。如果最后有10个数字，这个表达式也会匹配成功。关于这个问题我们接着看。

    ### 边界表示<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	边界表示符有两个：开头`^`和结尾`$`。使用起来也很简单，还是以上面的手机号为例，我们再来完善一下：`^1[3578]\d{9}$`。其中`^1`表示以1开头，`\d{9}$`表示以9个数字结尾。其实这个`^1`可有可无，毕竟是从左往右的，字符串不是1开头的话直接就会返回None，但是这个结尾符是必须的。

    ### 转义字符<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	假如我们想匹配的字符与正则表达式规定的这些字符一样该怎么办？比如我们想单纯的匹配`.`这个字符，但是这个字符在正则表达式中表示的是任意字符。这时候就要用到转义字符`\`了。其实这个转义字符在很多语言里都是一样的。那么前面的例子就可以写出`\.`。我们再演示个匹配邮箱的例子：

    <pre highlighted="true">`<span class="hljs-keyword">import</span> re
    pat = <span class="hljs-string">r"^\w{4,10}@qq\.com"</span> <span class="hljs-comment"># 如果.前面不加\，就代表任意字符了</span>
    <span class="hljs-built_in">str</span> = <span class="hljs-string">"1234@qq.com"</span>
    res=re.match(pat,<span class="hljs-built_in">str</span>)
    print(res)
    `</pre>

    ### 匹配分组<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

    ​	看到上面的匹配邮箱例子，是不是有个疑问，如果我想不止匹配QQ邮箱该怎么办呢。那就要用到分组了，其可以实现匹配多种情况。分组符号如下：

    <div class="table-wrapper"><table>
    <thead>
    <tr>
    <th style="text-align: center">符号</th>
    <th style="text-align: center">作用</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: center">()</td>
    <td style="text-align: center">将括号里的内容当作一个分组，每个分组会有一个编号，从1开始</td>
    </tr>
    <tr>
    <td style="text-align: center">|</td>
    <td style="text-align: center">连接多个表达式，表达式之间是“或”的关系，可与()一起使用</td>
    </tr>
    <tr>
    <td style="text-align: center">\num</td>
    <td style="text-align: center">引用分组，num代表分组编号</td>
    </tr>
    <tr>
    <td style="text-align: center">(?P<name>...)</name></td>
    <td style="text-align: center">给分组取别名，别名写在表达式前面，name不用打引号</td>
    </tr>
    <tr>
    <td style="text-align: center">(?P=name)</td>
    <td style="text-align: center">根据别名使用分组中的正则表达式</td>
    </tr>
    </tbody>
    </table></div>

    ​	那么我们把上面的例子稍微修改下：`^\w{4,10}@(qq|163|outlook|gmail)\.com`。这样就可以匹配多种邮箱了。

    ​	简单的演示了下`|`的用法，大家可能对其他的分组符号还有点疑惑，下面我们再来演示一下这些符号：

    <pre highlighted="true">`<span class="hljs-keyword">import</span> re
    pat = <span class="hljs-string">r"&lt;(.+)&gt;&lt;(.+)&gt;.*&lt;(/\2)&gt;&lt;(/\1)&gt;"</span>
    <span class="hljs-built_in">str</span> = <span class="hljs-string">"&lt;body&gt;&lt;div&gt;&lt;/div&gt;&lt;/body&gt;"</span>
    res=re.match(pat,<span class="hljs-built_in">str</span>)
    print(res)

​ 这个表达式匹配的是由两个标签组成的 html 字符串。第一眼看上去有点麻烦，实际很简单。再次强调一下，普通字符也可以当表达式来匹配的，比如上面的`&lt; &gt;`就是普通字符而已。

​ 我们来分析一下这个表达式，首先一对小括号表示一个分组，里面的`.+`表示只有一个非\n 字符。中间的`.*`用来匹配标签内的内容。`/\2`中，第一个斜杠与前面的 html 标签组成一对，/2 表示引用第二个分组的内容。这里为什么要使用分组呢？**因为我们还要保证 html 标签正确匹配**。如果后面也使用`.+`，大家可以试着把`/div`和`/body`交换位置，表达式依旧匹配成功，但这显然不符合 html 的语法。

### 操作函数<button class="cnblogs-toc-button" title="显示目录导航" aria-expanded="false"></button>

​ 正则表达式的一些规则符号终于讲完了，最后再列举几个 Python 中操作正则表达式的函数：（re 为导入的模块）

<div class="table-wrapper"><table>
<thead>
<tr>
<th style="text-align: center">函数</th>
<th style="text-align: center">作用</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center">re.compile(patt)</td>
<td style="text-align: center">封装正则表达式，并返回一个表达式对象</td>
</tr>
<tr>
<td style="text-align: center">re.search(patt,str)</td>
<td style="text-align: center">从左往右搜索第一个配正则表达式匹配的子字符串</td>
</tr>
<tr>
<td style="text-align: center">re.findall(patt,str)</td>
<td style="text-align: center">在字符串中查找正则表达式匹配到的所有子字符串，并返回一个列表</td>
</tr>
<tr>
<td style="text-align: center">re.finditer(patt,str)</td>
<td style="text-align: center">在字符串中查找正则表达式匹配到的所有子字符串，并返回一个Iterator对象</td>
</tr>
<tr>
<td style="text-align: center">re.sub(patt,newstr,str)</td>
<td style="text-align: center">将字符串中被正则表达式匹配到的子字符串替换成newstr，并返回新的字符串，原字符串不变</td>
</tr>
</tbody>
</table></div>

​ Python 的第一篇文章就到这里了。接下来会边学边写，做一些好玩的 Python 项目，再一起分享出来。如有错误，感谢指出！

> 参考资料：《Python 3 快速入门与实战》
