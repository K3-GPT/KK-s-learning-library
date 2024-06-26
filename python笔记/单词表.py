#①
标识符，关键字
标识符：就是变量
1.首字符必须是大小写字母或者下划线
2.标识符必须是大小写字母，数字以及下划线组成
3.不能是有特殊符号$%&^*和关键字
不能以中文为变量名
不能以数字开头
常用规范命名方法： 下划线法、驼峰法

数据类型：
-int：整型，整数
-float：浮点类型(小数)
-bool：布尔类型 True，False
-number类型：数字类型
-str：string类型，字符串类型，所有的引号都是字符串类型
-type+变量名  ：知道该数值是什么类型：
转换为int类型：int()
转为float类型：float()
转为bool类型：bool()

关键词：
False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'

#②
运算符：
1.算术运算符
//  取整除：整数商
%   取余：除后取余
**  指数
2.复合运算符
//=   取整除赋值运算符  a //= b相当于a = a // b
%=    取余赋值运算符
**=   指数赋值运算符


字符串类型
字符串其实就是文本信息，记录文本信息和文字信息
变量名 = 'xxx'
字符串的转义字符:
\' 转义单引号， 就是输出单引号的意思
\" 转义上引号， 就是输出双引号的意思
\n 转义换行， 就是换行输出
\t 转义制表，可以理解输出四个空格或者一个tab键（table键）

序列   格式：序列名[下标值]
a = "1234"
print(a[1])
切片   格式：序列名[起点下标值:终点下标值+1]
步长   格式：序列名[起点下标值: 终点下标值+1:步长]  步长 (n+1) - (n-1)
逆向输出  [::-1]（序列都可以逆向输出）
序列长度：用len()测出序列的长度（测出多少个数值）



#③
列表  a=[25,4,8]
                                          增加：
.append(数值)：追加到末尾
.insert(下标，数值) ：按照填写的下标值插入特定的数值
.extend([6,7])：按照序列的顺序，从左往右依次添加到目标列表末尾

                                          删除：
.remove(数值)：移除特定值，如果有相同的数值，删除最左边的数值，如果没有该数值，会报错
.pop(下标值)：删除下标值的数值，填写默认最后一个，如果超过最大下标值会报错
del 序列名；物理删除，如果再次使用会直接报错
clear()清空列表数值

                                          修改：
列表名[下标值] = 数值

                                          查询：
index(数值)  查询下标值，如果遇到相同的数值，只查询最左边的下标值，没有数值报错

count(数值)  统计数值在列表的个数，如果没有数值，0
列表[下标值]

                                         元组
del + 元组名
元组和列表的互相转换: tuple()
列表用[下标值], 元组用()

列表嵌套与取值(*)       <剥花生>
例：
a = [[["123"],["456"]]]
# 取字符"2"
print(a[0])             #[["123"],["456"]]
print(a[0][0])          #["123"]
print(a[0][0][0])       #123
print(a[0][0][0][1])    #1
print(type(a[0][0][0][1]))

#④
replace( )代替方法使用：
格式：.replace("","")

strip( )方法使用     托马摒弃
格式：.strip("")
注：删除字符串左右指定连续数值，匹配时不按照字符顺序

rstrip( )/lstrip()使用：lift right
格式：lstrip：删除字符串左指定连续数值，匹配时不按照字符顺序
     rstrip：删除字符串右指定连续数值，匹配时不按照字符顺序


split( )分割方法使用：（输出的格式是列表，常用于爬虫）
格式：split(字符,number)   根据输入的字符作为一个分割点 number：分割的次数， 为-1(全部的意思)
注：没有从左往右切或者中间切



upper( )，lower( ) title( )方法使用       大小写切换
格式：upper() 字符串的字母全部改为大写
	 lower() 字符串的字母全部改小写
	 title() 字符串每一个单词(空格区分)的首字母大写，其他都是小写（类似大驼峰法

find(字符)： 查询字符串是否含有某个数值并输出该数值最左边的下标值（匹配不到的数值会输出-1）
格式：find(字符,起点,终点) 终点是开区间 ，和切片是一样的道理


endswith(字符)： 查询字符结尾是否是输入的字符串，输出bool值
运用：判断文件后缀
格式：a.endswith("字符串")
结果：bool类型

isdigit()：判断字符是否为纯数字组成，输出bool值
运用：str(字符串）要换为int（整形），用到这个方法判断

格式化：

%d  替换成整型格式                                              int
%f  替换成浮点类型格式，默认是小数点后6位，如果你想保留后a位，%.af      float
%s  替换成字符串格式                                            str

format()格式化输出多个数值
格式一：
"{下标值1}{下标值2}".format(数值1,数值2,数值3)
格式二：
"{变量名1}{变量名2}".format(变量名1=xxx,变量名2=xxx)

f-String:占位符{}
格式：变量名 = 数值
print(f"{变量名}")











































