# shell笔记

## 一、常用命令

### 1.head
**默认获取文件前10行**

-n 获取指定的行数
```bash
head -n 3 /etc/passwd
head -3 /etc/passwd
```
-c 获取前n个字符
```bash
head -c 3 /etc/passwd
```
### 2.tail
默认获取文件后10行

- -n 获取指定的行数
```bash
tail -n 3 /etc/passwd
tail -3 /etc/passwd
```
- -c 获取后n个字符
```bash
tail -c 3 /etc/passwd
```
### 3.cut
取出文件制定的列

默认以空格或者tab键进行分割（不支持不规则的空格）
- -d 指定分割符
- -f 指定获取的列号(获取第二和第四列：-f2,4)


### 4.uniq
去除重复的内容
- -d 仅打印有重复的元素（duplicate）
- -c 打印元素重复的个数

### 5.sort
对文本的内容进行排序
默认以字符的ASCII码数值从小到大排序
- -n 以数值大小排序
- -r 倒序

### 6.wc
计算文本数量
- wc -l 打印行数
- wc -w 打印单词数
- wc -c 打印字节数
- wc -L 打印最长行的字节数


## 二、变量
### 1、定义变量（定义的变量默认为本地变量）
##### 方式一：
	变量名=变量值
	变量值必须是一个整体，中间没有特殊字符
	等号两侧不能有空格

##### 方式二：
	变量名='变量值'
	看到的内容，就输出什么内容
##### 方式三：
	变量名="变量值"
##### 方式四：
	变量名=$(linux命令)
	变量名=`linux命令`
	常用方法

#### 定义变量的时候，单引号和双引号的区别：
- 1. 如果变量值中有空格要用放到引号中
- 2. 单引号中的变量如果有引用别的变量，那么打印出来的值不会进行解析
- 3. 双引号中的变量如果有引用别的变量，那么打印的时候会进行解析
```bash
	name='aa bb'
	echo $name # aa bb
	var='$name'
	echo $var # $name
	var="$name"
	echo $var # aa bb
```
### 2、全局变量
可以通过命令(env)查看环境变量（只显示全局变量）

#### 定义全局变量
##### 方式一：
	变量=值
	export 变量
##### 方式二（最常用）：
	export 变量=值

### 3、定义永久变量
- 可以在 ~/.bashrc中进行定义全局变量
- 也可以在 ~/.bash_profile中定义

### 4、查看变量
#### 方式一：
	echo $变量名
#### 方式二：
	echo "$变量名"

#### 输出进行转义
    echo -e "one\ntwo\tthress"
#### 输出不换行
    echo -n "one two"; echo -n "333"
#### 输出带颜色的字符
    echo -e "\e[031mYES\e[0m" # 红色
    032 # 绿色
    034 # 蓝色

### 5、内置变量

- $0 获取当前执行的shell脚本文件名，包括脚本路径
- $n 获取当前执行的shell脚本的第n个参数值，n=1...9，如果n大于9就要用大括号括起来${10}
- $# 获取当前shell命令行中参数的总个数
- $? 获取执行上一个指令的返回值(0为成功，非0为失败)
- $* $@

### 6、数值运算
- \+ \- \* / %
- < <= > >=
- = !=

#### 方式一：
	$((算数表达式))
	变量可以不加$
#### 方式二：
	expr 算数表达式
	如果遇到 < > 需要进行转义 /< />
#### 方式三：
	bc
	scale=3 表示保留3位小数
	echo "scale=3; 10/3" | bc

### 7、条件表达式
#### 格式：
	test 
	[ 条件表达式 ]
#### 1. 返回值
	条件成立，返回0
	条件不成立，返回1

#### 2. 文件表达式
	-f 判断输入的内容是否是一个文件
	-d 判断输入内容是否是一个目录
	-x 判断输入内容是否可执行
	-e 判断文件是否存在
	-r 
	-w 

#### 3. 数值操作符
	n1 -eq n2  相等
	n1 -gt n2 大于
	n1 -lt n2 小于
	n1 -ne n2 不等于

#### 4. 字符串比较
	str1 == str2 str1和str2字符串内容一致
	str1 != str2 str1和str2字符串内容不一致，!表示相反的意思

#### 5. 逻辑表达式
	&& 和 ||
	-a 与
	-o 或

### read用户输入
- read如果不添加任何参数，用户输入的内容会自动存放到$REPLY内置变量中
- read如果添加参数那么会自动复制
- -p 提示用户输入 read -p "请输入内容："
- -n 个数，指定接受用户输入的个数
- -s 指定不显示用户输入的内容
- -e 如果有退格键不会显示^H

## 三、shell脚本格式
### 1. 格式要求
##### 1）在文件首行指定执行shell的程序以及相关说明
	# !/bin/bash
	# Author: Desire
	# Date: 2021-03-29
##### 2）shell脚本文件后缀，.sh
##### 3）脚本执行失败时，使用exit返回非零值，来退出程序
##### 4）默认缩进4个空格
##### 5）shell脚本命名简单，有意义，见名知意

### 2. 执行脚本
##### 1）给shell脚本增加执行权限
	chmod u+x one.sh 给当前用户指定执行权限
	chmod +x one.sh 给所有用户指定执行权限

##### 2）执行shell脚本
	bash one.sh
	sh one.sh
	source one.sh
	# 设置权限后才可以使用
	./one.sh
##### 3）调试模式执行
	bash -x one.sh

### 3. 注释
##### 单行注释
	#
##### 多行注释
	:<<!
	注释内容
	!

## 四、函数
### 1. 格式
##### 格式一：
	函数名()
	{
		命令1
		命令2
	}
##### 格式二：
	function 函数名
	{
		命令1
		命令2
	}

### 2. 函数传参
```sh
is_online()
{
    ping -c1 $1 &> /dev/null
    if [ $? -eq 0 ];then
        echo "$1主机在线"
    else
        echo "$1主机不在线"
    fi

}
is_online www.baidu.com
```
### 3. shell脚本命令传递参数
```sh
------defind_func.sh--------
is_online()
{
    ping -c1 $1 &> /dev/null
    if [ $? -eq 0 ];then
        echo "$1主机在线"
    else
        echo "$1主机不在线"
    fi

}
is_online $1

------命令行执行shell脚本-----
bash defind_func.sh www.baidu.com
```

## 五、流程控制(break和continue在循环中也是可以用的)
### 1、if
##### 方式一：
    if [ 条件1 ]
    then
        指令1
    elif [ 条件2 ]
    then
        指令2
    else
        指令3
    fi
##### 方式二:
    if [ 条件1 ]; then
        指令1
    elif [ 条件2 ]; then
        指令2
    else
        指令3
    fi

### 2、for
##### 格式一：
    for 值 in 列表
    do
        执行语句
    done
##### 格式二：
    for ((i=1,i<10;i++))
    do
        echo "$i"
    done

### 3、while
##### 只要条件满足，就一直循环
    while 条件
    do
        执行语句
    done

### 4、until
##### 只要条件不满足，就一直循环
    until 条件
    do
        执行语句
    done

### 5、case
    case 变量名 in
        值1)
            指令1
            ;;
        值2)
            指令2
            ;;
        值3)
            指令3
            ;;
        *)
            指令4
            ;;
    esac

## 六、数组
### 1、数组的定义
**一对括号表示是数组，数组元素用“空格”符号分割开，引用个数组时从序号0开始**
##### 方式一：
```bash
array=(10 20 30 40)
```
##### 方式二：
```bash
array[0]=10
array[1]=20
array[2]=30
array[3]=40
```
##### 方式三：
```bash
var="10 20 30 40"; array=($var)
```
### 2、数组操作
#### 1）显示数组中第n项
**数组的序号是从0开始计算，超出索引不会报错**
```bash
echo ${array[n]}
```
#### 2）显示数组中的所有元素
```bash
echo ${array[@]}
OR
echo ${array[*]}
```
#### 3）显示数组长度
```bash
echo ${#array[@]}
OR
echo ${#array[*]}
```
#### 4）删除数组中第n项元素
**unset仅仅只清楚array[n]的值，并没有将array[n]删除掉**
```bash
unset array[1]
```
#### 5）删除整个数组
```bash
unset array
```
#### 6）输出数组的从第一项开始长度为3的数组
###### ${数组名[@ or *]:起始位置:长度}
```bash
echo ${array[@]:0:3}
```
#### 7）将数组中的0替换成1
###### ${数组名[@ or /*]/查找字符/替换字符}
```bash
echo ${array[@]/0/1}
```
#### 8）在数组追加新的元素
```bash
array[${#array[@]}]=1234; echo ${array[@]}
```

## 七、文本处理三剑客
- grep
- sed
- awk
### 1、grep
#### 查找文件里符合条件的字符串
```bash
grep [option] pattern [file1,file2,...]
come command | grep [option] pattern
```
- -i 忽略大小写
- -c 只输出匹配行的数量
- -n 显示行号
- -r 递归搜索
- -E 支持拓展正则表达式
- -w 匹配整个单词
- -l 只列出匹配的文件名
- -F 不支持正则，按字符串字面意思进行匹配

### 2、sed
#### 流编辑器，对文件逐行进行处理
```bash
sed [option] "pattern command" file
some command | sed [option] "pattern command"
```
- -n 只打印模式匹配的行
- -f 加载存放动作的文件
- -r 支持拓展正则
- -i 支持修改文件

#### pattern模式
- 5 只处理第5行
- 5,10 只处理第5行到第10行
- /pattern1/ 只处理能匹配pattern1的行
- /pattern1/,/pattern2/ 只处理从匹配pattern1的行到匹配pattern2的行

#### command命令
- 查询
    - p 打印
- 新增
    - a 在匹配行后新增
    - i 在匹配行前新增
    - r 外部文件读入，行后新增
    - w 匹配行写入外部文件
- 删除
    - d
- 替换
    - s/old/new/ 只修改匹配行中第一个old
    - s/old/new/g 修改匹配行中所有的old
    - s/old/new/ig 忽略大小写

#### 例子
```bash
# 查询
sed "p" passwd # 打印源行信息和模式匹配的行（行打印信息会有重复的）
sed -n "p" passwd # 只打印模式匹配到的行数据
sed -n "5 p" passwd # 打印第5行匹配到的行数据
sed -n "5,10 p" passwd # 打印第5行到第10行匹配到的数据（包含第5行和第10行）
cat -n passwd | sed -n "12 p" # 从前面的命令执行结果中，打印第12行匹配到的行数据
sed -n "/root/ p" passwd # 打印匹配到root的行数据
sed -n "/^root/ p" passwd # 打印匹配到以root开头的行数据
sed -n "/\/sbin\/nologin/ p" passwd # 打印匹配到`/sbin/nologin`的行数据`/`需要进行转义
sed -n "/www/ p" passwd # 打印匹配到`www`的行数据
sed -nr "/w{3} p" passwd # 使用扩展正则打印匹配到`www`的行数据

# 新增
sed -n "/halt/ a 新增文本内容" passwd # 在匹配行后新增`新增文本内容`（这条命令并没有真正的新增,可以当做验证命令是否正确）
sed -i "/halt/ a 新增文本内容" passwd # 使用 `-i`才可以真正的修改文件
sed -i "/halt/ w test.txt" passwd # 把匹配到的行数据，写入到test.txt外部文件中
# sed_file.sed内容为`/bash/ a 存放动作的文件` 
sed -i -f sed_file.sed passed # 加载存放动作命令的文件进行匹配行数据

# 删除
sed -i "/#/ d" sshd_config # 删除匹配到的`#`注释
sed -i "/^$/ d" sshd_config # 删除匹配到的空行

# 替换
sed -i "/\/sbin\/nologin/ s/bin/BIN/" passwd # 修改匹配到的`/sbin/nologin`行中，首个`bin`更改为`BIN`
sed -i "/\/sbin\/nologin/ s/bin/BIN/g" passwd # 修改匹配到的`/sbin/nologin`行中，所有`bin`更改为`BIN`
sed -i "s/^#Port 22/Port 2200/" sshd_config # 把匹配到的`Port 22`修改为`Prot 2200`
```

### 3、awk
#### 文本处理工具，处理数据并生成结果报告
```bash
awk 'BEGIN{} pattern {commands} END{}' file
some command | awk 'BEGIN{} pattern {commands} END{}'
```
#### 格式
- BEGIN{} 处理数据之前执行，只执行一次
- pattern 匹配模式
- {commands} 处理的命令
- END{} 处理数据之后执行，只执行一次

#### 内置变量
- $0 整行内容
- $1-$n 当前行的第1-n个字段
- NF(Number Field) 当前行字段数
- NR(Number Row) 当前行行号，从1开始
- FS(Field Separator) 输入字段分隔符，默认为空格或tab键
- RS(Row Separator) 输入行分隔符，默认为回车符
- OFS(Output Field Separator) 输出字段分割符，默认为空格
- ORS(Output Row Separator) 输出行分割符，默认为回车符

#### printf格式符

- %s 字符串
- %d 十进制数字
- %f 浮点数

#### 修饰符
- \+ 右对齐
- \- 左对齐

#### 匹配方式
- 正则表达式匹配
    - /正则表达式/
- 关系运算
    - < <= > >= == !=
- 算数运算
    - \+ \- \* / % ^ \*\*
    - ++i i--
#### 流程控制语句（与shell脚本语法不一样）
- if
```bash
if (条件)
    动作
else if (条件)
    动作
else
    动作
```
- for
```bash
for (i=0;i<=100,i++)
{
    动作
}

for (i in awk数组){
    echo $i
}
```
- while
```bash
while (条件)
{
    动作
}
```
#### 函数
##### 字符串函数
- length(str)
- tolower(str)
- toupper(str)

#### 例子
```bash
awk '{print $0}' stu.txt # 读取所有的内容
awk '{print $1}' stu.txt # 读取第一列数据
awk '{print NF}' stu.txt # 获取每一行的字段数
awk '{print NR}' stu.txt # 获取当前行号

awk -F":" '{print $1}' passwd # 指定以`:`为分割符的第一列数据
awk -F":" '/root/ {print $(NF-1)}' passwd # 指定以`:`为分割符的倒数第二列数据
awk -F":" '/^halt/,/^ftp/ {print $1}' passwd # 指定以`:`为分割符的以`halt`开头到以`ftp`开头行的第一列数据
awk 'BEGIN{FS=":"} /root/ {print $1}' passwd # 以`:`进行分割，获取包含root的行的第一列数据
awk -F":" 'NR == 5 {print}' passwd # 获取第5行数据
awk -F":" 'NR >= 5 && NR <=10 {print}' passwd # 获取第5-10行数据
awk -F":" 'NR == 5, NR ==10 {print}' passwd # 获取第5-10行数据
awk -F: '{count++} END{print count}' passwd # 获取文件总行数，count在awk中会自动进行定义变量（wc -l passwd 获取文件总行数 行数 文件）

awk -F= 'NR == 1 {print $2}' /etc/os-release | awk '{print $1}' |sed 's/\"//g' # 获取Linux发行版本

awk -F: 'BEGIN{printf "%-20s %-20s\n","BEGIN","END"} NR >1 {count++; printf "%-20s %-20s\n",$1,$(NF)} END{printf "%-20s %-20s\n","total",count}' /etc/passwd # 使用`BEGIN{}`给结果添加title,使用`count++`计算总数，使用`END{}`把总数添加到末尾(%-20s:表示字符串的指定长度为20，不满20字符，空格填充，-表示左边对齐)

awk -F: -f file.awk /etc/passwd # 跟上面是一样的，只不过，把复杂的指令放在了file.awk文件中
# file.awk:(在文件中可以使用if for while流程控制语句)
----------------------------------------------------
BEGIN{
    printf "%-20s %-20s\n","BEGIN","END"
}
{
    if (NR > 1)
    {
        count++; 
        printf "%-20s %-20s\n",$1,$(NF)
    }
}
END{
    printf "%-20s %-20s\n","total",count
}
----------------------------------------------------
```