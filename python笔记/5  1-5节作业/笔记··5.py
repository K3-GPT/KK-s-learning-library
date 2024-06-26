#第一节
print()
input()

#第二节
1.使用IDLE创建demo.py文件，保存到桌面

2.使用**变量**储存我们的个人信息（姓名，身高，年龄，身份证号码等）,
而且要使用**单行注释**标注各个变量的含义，使用**多行注释**标注代码文件demo的功能作用、编写日期、开发人
```
# 如何理解作业做法
"""
开发人：xxxx
编写日期：xxxx
"""
a = "xxx"
b = 11
```

3.在demo.py文件编写，使用使用**驼峰法**（小驼峰或者大驼峰）**命名**变量名储存商品信息（商品名，商品价格，商品数量，以及日期是否过期）
要求【这里特指是数值，等于号的右边：商品名的数值是**字符串类型** ，商品价格的数值是**float类型**（浮点类型），
商品数量的数值是**int类型**（整型类型），日期是否(自己写)过期是**bool类型**（真是不过期。假是过期）】自己直接给一个True或者False

```
# 要驼峰法起名字
shopName = "宜家"
money = 18.0
# 日期是否过期
date = True # 不过期
```

4.选择题，把答案发给老师就行：
```
补充：分号同一行的意思
1.在程序中，小明在交互模式输入if = 1 结果输出为（）          D

A. 1   B. 0   C. False  D. 程序报错

2.在程序中，小明在交互模式中输入
_=False
print(_)
结果输出为（）

A. 1   B. 0   C. False  D. 程序报错

3.在程序中，在交互模式中输入# while = 1 ; print(while)结果输出为（）

A. 1   B. 没有显示   C. False  D.程序报错

4.在程序中，交互模式中输入
false = 1
print(false)
结果输出为（）

A. 1   B. 没有显示   C. False  D.程序报错
5. 在程序中，交互模式输入
a1 = 1
b1 = 1.0
sum = a1 + b1
print(sum)
结果输出为（）
A. 2.0  B. 0   C. False  D. 程序报错
```

第三节
1.使用运算符代码计算一下式子：
```
214 + 265   341-125   264 × 356   214 ÷ 42  74² ÷ 23
算出5421÷564的整数商和余数
```

2.创建字符串为      小明说：“ 天气真热，去买西瓜吃！"   ，按照下面进行输出：
```
小明说："天气真热，去买西瓜吃！"
```

3.创建字符串为     小明说：\n“ 天气真热，\t去买西瓜吃！"     ，输出结果：
```
小明说：\n“ 天气真热，\t去买西瓜吃！"  注意：\n和\t要输出
```

4.字符串：a = “sdfsdfs”, 按照下面提示输出
# 请输出dfsd
# 请输出sdf
#请输出dfs
#请输出sfds
#请输出dsf
#请输出dd
#请输出sfdsfds
#请输出字符串a的字符串长度



第四节
1.创建一个空列表li，在里面添加姓名，年龄，身高

2.在列表li中，身高前面插入出生日期，在身高后面插入家庭地址

3.查询列表li是否有包含出生日期

4.把列表li中的出生日期和家庭地址删除

5.清空列表li的数值，清空后删除列表


第五节
1. 下面字母输出全小写、全大写
(1) hello word
(2)	HELLO WORD

2. 按照要求进行输出
（1）"asw2ewwsdf":把所有里面的【w】改为【a】输出
（2）"123456789":以【5】字符为切割点，进行切分为2段
（3）"我好饿啊!!!!":把后面的【!】清除掉并查找里面的【饿】的字符

3.请把下面的字符串安装特定的格式化要求输出
（1）创建变量a，b。分别赋值"高"，"帅"。然后进行放到字符串里面进行输出：字符串输出例如[我又高又帅]
（2）使用format把Name和Age放到字符串进行输出。例如：【我今年26岁，我是梓良老师】
（3）创建heigh（身高）变量，赋值178.67123，分别用%s,%d,%.2f进行输出

4.记忆
切片公式：序列名[起点下标值:终点下标值]         ==》序列名[起点下标值:终点下标值+1]
步长公式：序列名[起点下标值: 终点下标值:步长]    ==》序列名[起点下标值: 终点下标值+1:步长] (n+1) - (n-1)


第六节（复习）
1.执行下列语句后显示的结果是什么？>>>world="world">>>print("hello",world)
()
# 变量名不需要双引号
A、helloworld
B、“hello”world
C、hello world
D、语法错误

2.下列哪个语句在python中是违法的？
# x,y = 1,2
A、x=y=z=1
B、x=(y=z+1)
C、x,y=y,x
D、x+=y

3.在python中，数学表达式的写法错误的是()
A．5*a+b
B. 5a+b
C. 切片实例 + b / 3
D. 切片实例 * 5 + b % 3

4.python中，下列程序输出结果为( )
# append 追加，添加到末尾的意思
a=['爱国','坚强','勇敢']
a.append('加油')
print('武汉',a[3])
A. 武汉 '加油'
B. 武汉 加油
C. 武汉 '勇敢'
D. 武汉 勇敢

5.列表就是一组用( )括起来的数据。
A. ( )
B. [ ]
C. { }
D. “”

6.下面小程序的运行结果是()
x = 1
x +=2
print(x)
A. 2
B. 3
C. 5
D. 6

7.请参考以下字符串处理程序，执行结果正确的是：( )
s=‘My☆home☆is☆in☆Weihai’
print(s[3:7])
# 切片是左闭右开
A . ☆hom
B .home
C .ome☆
D. ☆home☆

8.下面语句中，能够给变量 a 赋值为字符串类型的是()。
# input 默认值就是字符串
A. 切片实例=float(input("第一条边的长度："))
B. 切片实例=int(input("第一条边的长度："))
C. 切片实例= input("第一条边的长度：")
D. 切片实例=float(input("请输入文字"))

9.以下变量命名不符合规则的是：(  )
# 1. 只能下划线，大小字母为首字符
# 2. 只能由下划线，大小字母和数字组成
# 3. 不能为关键字，（行业内 内置函数也是不行的）

A. price
B. a3
C. first_name
D. 3a


编程题：
1.小明今年15岁。考虑一下，怎么输出小明的个人信息：格式如下：姓名：小明，年龄：15岁

2.已知一个字符串为 “hello_world_yoyo”，如何得到一个队列 [“hello”,”world”,”yoyo”] ？

3.把字符串 s 中的每个空格替换成”%20”，输入：s = “We are happy.”，输出：“We%20are%20happy.”
