第二节课笔记
1 运算符
1.1 算术运算符
| 运算符 |  描述  |                             实例                             |
|   +    |  加号  |               就是两个数值相加：a + b；输出和                |
|   -    |  减号  |               就是两个数值减号：a - b；输出差                |
|   *    |  乘号  |  两个数值相乘或者重复的次数：a * b ；输出积或者重复后的次数  |
|   /    |  除号  |                 两个数值相除：a / b ; 输出商                 |
|   //   | 取整除 | 两个数值相除，然后输出整数商： a = 3，b = 2；a // b的输出结果为1 |
|   %    |  取余  | 两个数值相除，然后输出相除的余数：a = 5，b = 3； a % b的结果为2 |
|   **   |  指数  | 第一个数值相乘，乘的次数为第二数值，然后输出积：a = 2，b =3； a ** b的结果为8 |

1.2 类型转换
所有类型是可以转换的但是需要满足一定的要求
转换为int类型：int()
转为float类型：float()
转为bool类型：bool()
str类型转换为int类型一定是纯数字，其他都报错
str类型转换为number类型，需要符number类型的形式

1.2.1 int 转换为 float 变成小数  整数--小数
a = 1
print(type(a))
a= float(a)
print(a)
print(type(a))
结果：
<class 'int'>
1.0
<class 'float'>

1.2.2 float 转换为 int 直接变成整数  小数--整数
b = 1.6
print(type(b))
b = int(b)
print(b)
print(type(b))
结果：
<class 'float'>
1
<class 'int'>

1.2.3 str满足number条件就可以转换为int类型   字符串--整数
c = "1230"
print(type(c))
c = int(c)
print(c)
print(type(c))
结果：
<class 'str'>
1230
<class 'int'>

错误示范：
c = "12.30"
print(type(c))
c = int(c)
print(c)
print(type(c))
结果：
invalid literal for int() with base 10: '12.30'
<class 'str'>


1.2.4 str 转换为 float类型  字符串--小数
d = "123.0"
print(type(d))
d = float(d)
print(d)
print(type(d))
结果：
<class 'str'>
123.0
<class 'float'>

1.2.5 bool 转换为 int 类型  布尔--整数
e = True
e = int(e)
print(e)
结果：
1

1.2.6 bool 转换为 float 类型  布尔--小数
f = True
f = float(f)
print(f)
结果：
1.0

2. 赋值运算符
| 运算符  | 描述 |                             实例                     |
|   =    | 赋值 | 就是右边的值赋值给到左边的变量：a = 1 ；变量a就已经存储了数值1 |
3. 复合运算符
| 运算符  |       描述     |           实例           |
|   +=   |  加法赋值运算符  |  a += b相当于a = a + b   |
|   -=   |  减法赋值运算符  |  a -= b相当于a = a - b   |
|   *=   |  乘法赋值运算符  |  a *= b相当于a = a * b   |
|   /=   |  除法赋值运算符  |  a /= b相当于a = a / b   |
|  //=   | 取整除赋值运算符 | a //= b相当于a = a // b  |
|   %=   |  取余赋值运算符  |  a %= b相当于a = a % b   |
|  **=   |  指数赋值运算符  | a ** = b相当于a = a ** b |

4. str字符串类型

4.1字符串的含义与作用
字符串其实就是文本信息，记录文本信息和文字信息(如果数值是字母或者汉字，或者文字数字组合都是输入字符串，bool值除外)
字符串的格式（单双三）
变量名 = 'xxx'
变量名 = "xxx"
变量名 = """ xxx """

name 是变量名
name = 'kk'
print(name)
结果：
kk

和多行注释类似的地方:多行注释如果有赋值的动作就会变成字符串
a = """
kk
"""
print(a)
结果：

kk



4.2 字符串的引号嵌套使用
输出： 我说: "明天我上班不上课"
a = '我说: "明天我上班不上课" '
print(a)

a = """ 我说: "明天我上班不上课" """
print(a)


4.3 字符串的转义字符
4.3.1 转义字符:
\' 转义单引号， 就是输出单引号的意思
\" 转义双引号， 就是输出双引号的意思
\n 转义换行， 就是换行输出
\t 转义制表，可以理解 输出四个空格或者一个tab键（table键）

4.3.2 取消转义：
全部取消 ： r'' : r+字符串：里面的转义全部取消
部分取消 ：\\

输出 ： 我今天学习了字符串符号： ''  " "  """ """
a = ' 我今天学习了字符串符号： \'\'  \" \"  \""" \"""  '
print(a)
结果：
我今天学习了字符串符号： ''  " "  """ """

b = "kk说：\n 加油"
print(b)
结果：
kk说：
 加油

c = "kk说：\t 加油"
print(c)
结果：
kk说：	 加油


输出网址：www.切片实例.com\nxxx\txxx\ax\bx
a = r"www.i.com\nxxx\txxx\ax\bx"
print(a)
结果：
www.切片实例.com\nxxx\txxx\ax\bx

输出网址：
www.切片实例.com\nxxx\txxx\ax\bx
www.baidu.com

b = "www.i.com\\nxxx\\txxx\\ax\\bx \n www.baidu.com"
print(b)
结果：
www.切片实例.com\nxxx\txxx\ax\bx
 www.baidu.com


5. 有序序列
序列：就是可以储存多个数值或者多种数值的集合体
有序序列：有顺序的序列，可以理解为有index(下标值)

5.1 下标
下标：就是索引（目录）, 但是下标值看不到，只存在内存里面
作用：和目录一样，标明某个数值的位置，定位作用
下标的顺序：
从左往右开始
从右往左开始
下标的排列：
从左往右：0,1,2,3,4,5,6......[0,正无穷] 从0开始递增
从右往左，....-5,-4,-3,-2,-1 [负无穷，-1] 从-1递减

5.3 数值的获取
格式：序列名[下标值]

5.3.1 获取2这个字符
字符：  1  2  3  4
下标值： 0  1  2  3
       -4 -3 -2 -1
a = "1234"
print(a[1])
print(a[-3])
结果：
2
2

5.3.2 取一个高字
朋友又高又帅
朋   友  又  高  又  帅
0   1   2   3  4   5
-6  -5  -4  -3  -2 -1
b = "朋友又高又帅"
print(b[3])
print(b[-3])

5.4 切片（取多个数值）
就是根据下标值设置起点和终点进行截取
格式：序列名[起点下标值:终点下标值]
终点一定是大于起点，起点不能大于终点
所有切片的方向首先看步长，步长决定方向，起点和终点是根据步长去自动调整
如果步长是正数，所有的起点和终点同步转向全部对应的正数切片


5.4.1取值的时候注意终点数值是取不到的
编程转换为数学表达式:
编程的格式[起点:终点]
数学表达式： [起点，终点)
[1:2] => [1,2) => 1
就是终点为开区间
公式化：序列名[起点下标值: 终点下标值+1]

5.4.2 123456789   获取4-8
1  2  3  4  5  6  7  8  9
0  1  2  3  4  5  6  7  8
序列名[起点下标值: 终点下标值+1]
a = "123456789"
print(a[3:7+1])
print(a[3:8])
结果：
45678

 获取2-5
print(a[1:4+1])
print(a[1:5])
结果：2345


5.5 步长（向量）
步长：切片的距离，默认数值为1，如果不写就是1
格式：序列名[起点下标值:终点下标值:步长]
公式：序列名[起点下标值: 终点下标值+1:步长] (n+1) - (n-1) 意思就是后一个下标值-前一个下标值（任意相邻的两个下标值）

123456789  输出偶数：
1  2  3  4  5  6  7  8  9
0  1  2  3  4  5  6  7  8
序列名：[起点下标值: 终点下标值+1:步长]
公式：(n+1) - (n-1) 意思就是后一个下标值-前一个下标值（任意相邻的两个下标值）
步长的公式运用：3-1,5-3，7-5
a = "123456789"
print(a[1:7+1: 3-1])
print(a[1:8:2])
结果：
2468
输出奇数：
print(a[0:9:2])
结果：
13579

输出：8642
1  2  3  4  5  6  7  8  9
-9 -8 -7 -6 -5 -4 -3 -2 -1
序列名[起点下标值: 终点下标值+1:步长]
步长： -2 - (-4)或者-4 -（-6） ：步长是2，但是方向时从右往左是为-号
+从左往右是+，-是从右往左切
print(a[-(2):-(8+1):-(2)])
print(a[-2:-9:-2])
结果：8642


5.6 逆向输出  （序列都可以逆向输出）
默认最前面的或者最后面的可以不写
a = "123456789"
print(a[::-1])
结果：
987654321


5.7 序列长度：用len()测出序列的长度（测出多少个数值）
a = "pwoeuroiweruewilkfnd"
print(len(a))
结果：20


6. 作业
1.使用运算符代码计算一下式子：
214 + 265   341-125   264 × 356   214 ÷ 42  74² ÷ 23
算出5421÷564的整数商和余数
2.创建字符串为      小明说：“ 天气真热，去买西瓜吃！"，按照下面进行输出：
小明说："天气真热，去买西瓜吃！"
3.创建字符串为     小明说：\n“ 天气真热，\t去买西瓜吃！"，输出结果：
小明说：\n“ 天气真热，\t去买西瓜吃！"  注意：\n和\t要输出
4.字符串：a = “sdfsdfs”, 按照下面提示输出
请输出dfsd
请输出sdf
请输出dfs
请输出sfds
请输出dsf
请输出dd
请输出sfdsfds
请输出字符串a的字符串长度


#第一题：
a = 214;b =265
print(a+b)
c = 214;c+=265
print(c)
结果：
479
479

e = 341;f = 125
print(e-f)
g = 341;g -= 125
print(g)
结果：
216
216

h = 264;i = 356
print(h*i)
j = 264;j *= 356
print(j)
结果：
93984
93984
k = 214;l = 42
print(k/l)
m = 214;m /= 42
print(m)
结果：
5.095238095238095
5.095238095238095

n = 74**2;o = 23
print(n/o)
p =74**2;p /= 23
print(p)
结果：
238.08695652173913
238.08695652173913

q = 5421;q //= 564
print(q)
r = 5421;r %= 564
print(r)
结果：
9
345

#第二题
a = r'小明说："天气真热，去买西瓜吃！"'
print(a)
结果：
小明说："天气真热，去买西瓜吃！"
#第三题
b = '小明说：\\n“ 天气真热，\\t去买西瓜吃！"'
print(b)
结果：
小明说：\n“ 天气真热，\t去买西瓜吃！"
#第四题
a = "sdfsdfs"
#dfsd
print(a[1:5])
print(a[-6:-2])
# sdf
print(a[:3])
print(a[3:6])
print(a[-4:-1])
print(a[-7:-4])
#dfs
print(a[1:4])
print(a[4:7])
print(a[-6:-3])
print(a[-3:])
print(a[-3:-8:-2])
#sfds
print(a[:7:2])
print(a[:2:-1])
#dsf
print(a[1:6:2])
print(a[-3:-6:-1])
#dd
print(a[1:5:3])
print(a[-3:-7:-3])
#sfdsfds
print(a[::-1])
#len
print(len(a))


作业讲解：
创建字符串为【小明说：\n“ 天气真热，\t去买西瓜吃！" ，输出结果：小明说：\n“ 天气真热，\t去买西瓜吃！"

a = r'小明说：\n“ 天气真热，\t去买西瓜吃！"'
print(a)
# 4.字符串：i = “sdfsdfs”, 按照下面提示输出
a  = "sdfsdfs"


 请输出dfsd
     s  d  f  s  d  f  s
下左 0  1  2  3  4  5  6
下右 -7 -6 -5 -4 -3 -2 -1

 公式：序列名[起点: 终点+1: 步长]
 起点:1 终点：4 步长：后下标值-前下标值：4-3=1
 a[1:4+1:1] => a[1:5:1]

 方向看步长，
print(a[1:5:1])
print(a[1:-2])
print(a[-6:-2])


# 请输出sdf
# 起点是多少，终点是多少，步长是多少 -3 -(-1)=-2
print(a[0:3:1])
print(a[-1:-6:-2])



#请输出dfs
print(a[4:7:1])
print(a[1:4:1])


#请输出sfds
#     s  d  f  s  d  f  s
# 下左 0  1  2  3  4  5  6
# 下右 -7 -6 -5 -4 -3 -2 -1
print(a[-4::-1])
print(a[0::2])
print(a[-1:-5:-1])

#请输出dsf
#     s  d  f  s  d  f  s
# 下左 0  1  2  3  4  5  6
# 下右 -7 -6 -5 -4 -3 -2 -1
# 公式：序列名[起点: 终点+1: 步长]
# 起点：1,终点：5+1 步长：5-3=2
# 1 6 2
# 起点：-3 终点：-5 +（-1），步长：-5 -（-4）=-1
# -3 -6 -1
print(a[-3:-6:-1])
print(a[1:6:2])


# 请输出dd
#     s  d  f  s  d  f  s
# 下左 0  1  2  3  4  5  6
# 下右 -7 -6 -5 -4 -3 -2 -1
# 公式：序列名[起点: 终点+1: 步长]
print(a[1:5:3])
print(a[1:7:3])
print(a[-3:-7:-3])

#   i=sdfsdfs
#请输出sfdsfds
print(a[::-1])

#请输出字符串a的字符串长度
print(len(a))


    s  d  f  s  d  f  s
下左 0  1  2  3  4  5  6
下右 -7 -6 -5 -4 -3 -2 -1
公式：序列名[起点: 终点+1: 步长]
a[-3:-7]=>a[4:0]=>无解集
print(a[-3:-7])
a[-3:4]=>a[4:4],没有距离4-4=0和步长相悖一样是无解集
print(a[-3:4])