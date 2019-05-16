# 1 一行代码实现1--100之和
print(sum(range(1,101)))


# 2 如何在一个函数内部修改全局变量
##  使用global进行操作
a = 5
def f():
    global a
    a = 4
f()
print(a)


# 3 列出5个python标准库
# os：提供了不少与操作系统相关联的函数
#
# sys: 通常用于命令行参数
#
# re: 正则匹配
#
# math: 数学运算
#
# datetime:处理日期时间


# 4 字典如何删除键和合并两个字典
d = {"name":"hsb","age":19}
del d["name"]
print(d)
d1 = {"sex":"male"}
d.update(d1)
print(d)


# 5 谈下python的GIL
# GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，
# 一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
# 使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。
# 如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。
# 所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。
#
# 多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，
# 所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大


# 6 python实现列表去重的方法
l = [1,1,2,3,4,4,5,6]
print(set(l))


# 7 fun(*args,**kwargs)中的*args,**kwargs什么意思？
# 主要用于函数定义，可以将不定数量的参数传递给一个函数
# *args：非键值对的可变数量的参数列表
# **kwargs：不定长度键值对


# 8 python2和python3的range（100）的区别
#python2返回列表，python3返回迭代器，节约内存
print(range(100))

# 9
# 10python内建数据类型有哪些
#int str list tuple set dict bool


# 11 简述面向对象中__new__和__init__区别
# __init__是初始化方法，创建对象后，理科默认被调用
# __new__
# __new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
# __new__必须要有返回值，返回实例化出来的实例，
class Bike:
    def __init__(self,w,c):
        self.wheel= w
        self.color = c
b = Bike(2,"red")
print("车的颜色",b.color)


# 12 简述with方法打开处理文件帮我我们做了什么？
# 打开文件在进行读写的时候可能会出现一些异常状况，
# 如果按照常规的f.open写法，我们需要try,except,finally，做异常判断，
# 并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件，
# with方法帮我们实现了finally中f.close


# 13 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
l = [1,2,3,4,5]
l1 = map(lambda x:x**2,l)
print(l1)
l1 = [i for i in l1 if i>10]
print(l1)


# 14 python中生成随机整数、随机小数、0--1之间小数方法
import random
print(random.randint(10,16))
print(random.random())


# 15 避免转义给字符串加哪个字母表示原始字符串？
#r , 表示需要原始字符串，不转义特殊字符


# 16
# 17 python中断言方法举例
a = 3
assert (a>1)
print("断言成功，继续执行")
#assert (a>8)
#print("断言不成功，报错")


# 18
# 19 10个Linux常用命令
#ls查看文件信息
# pwd显示当前路径
# cd 切换工作目录
#  echo 屏幕输出
#  cat 查看文件
# cp拷贝
# mkdir创建目录
# rm删除文件
# touch创建文件
# grep 查找


# 20 python2和python3区别？列举5个
# Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')
# python2 range(1,10)返回列表，python3中返回迭代器，节约内存
# python2中是raw_input()函数，python3中是input()函数
# python2中使用ascii编码，python中使用utf-8编码


# 21 列出python中可变数据类型和不可变数据类型，并简述原理
#可变  list dict
# 允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，
# 变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，
# 相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。
#不可变 str tuple
#不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，
#而对于相同的值的对象，在内存中则只有一个对象（一个地址）
l1 = [1,2]
l2 = [1,2]
print(id(l1),id(l2))
a = "qwe"
b = "qwe"
print(id(a),id(b))


# 22 s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s1 = list(set(s))
s1.sort()
s2 = "".join(s1)
print(s2)


# 24 用lambda函数实现两个数相乘
f = lambda x,y :x*y
print(f(4,5))


# 25 字典根据键从小到大排序
d = {2:"2",3:"3",1:"1"}
res = sorted(d.items(),key =lambda x :x[0] )
print(res)
# 26
# 27 filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = filter(lambda x :x%2==1,a)
print(list(res))
# 28 列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = [i for i in a if i%2==1]
print(l)


# 29 a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
a,b,c = (1,),(1),("1")
print(type(a))
print(type(b))
print(type(c))


# 30 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
a = [1,5,7,9]
b = [2,2,6,8]
ans = []
for i,j in zip(a,b):
    ans.append(i)
    ans.append(j)
print(sorted(ans))


# 31 用python删除文件和用linux命令删除文件方法
# python os.remove("fsdf")
# linux rm "fdsfsd"


# 32
# 33
# 34
# 35 请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
#matplotlib


# 36 写一段自定义异常代码
def f():
    try:
        for i in range(5):
            if i>3:
                raise Exception("数字大于3")
    except Exception as e:
        print(e)
f()
# 37
# 38
# 39 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1,2],[3,4],[5,6]]
l = [j for i in a for j in i]
print(l)


# 40 x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
x="abc"
y="def"
z=["d","e","f"]
print(x.join(y))
print(x.join(z))


# 41 举例说明异常模块中try except else finally的相关意义
# try..except..else没有捕获到异常，执行else语句
#
# try..except..finally不管是否捕获到异常，都执行finally语句


# 42 python中交换两个数值
a,b =3,4
a,b= b,a


# 43
# 44
# 45
# 46
# 47 [1,2,3]+[4,5,6]的结果是多少？
print([1,2,3]+[4,5,6])


# 48 提高python运行效率的方法
# 1、使用生成器，因为可以节约大量内存
#
# 2、循环代码优化，避免过多重复代码的执行
#
# 3、核心模块用Cython PyPy等，提高效率
#
# 4、多进程、多线程、协程
#
# 5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率


# 49
# 50
# 51
# 52 list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
l = [2,3,5,4,9,6]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]
print(l)

# 53
# 54 保留两位小数
print(round(2.345,2))
# 55
# 56
# 57
# 58 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
dic={"name":"zs","age":18}
del dic["name"]
print(dic)
dic={"name":"zs","age":18}
dic.pop("name")
print(dic)
# 59
# 60
# 61
# 62
# 63 简述多线程、多进程
# 进程：
#
# 1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
#
# 2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制
#
#
# 线程：
#
# 1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
#
# 2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃
#
# 应用：
#
# IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间
#
# CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，
# 其他线程没有GIL，就不能充分利用多核CPU的优势


# 64 简述any()和all()方法
# any():只要迭代器中有一个元素为真就为真
#
# all():迭代器中所有的判断项返回都是真，结果才为真


# 65 IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
# IOError：输入输出异常
#
# AttributeError：试图访问一个对象没有的属性
#
# ImportError：无法引入模块或包，基本是路径问题
#
# IndentationError：语法错误，代码没有正确的对齐
#
# IndexError：下标索引超出序列边界
#
# KeyError:试图访问你字典里不存在的键
#
# SyntaxError:Python代码逻辑语法出错，不能执行
#
# NameError:使用一个还未赋予对象的变量


# 66
# 67
# 68
# 69 请将[i for i in range(3)]改成生成器
a = (i for i in range(3))
print(type(a))
a = 5
print(type(a)==int)
# 70 a = " hehheh ",去除收尾空格
a = " hehheh "
print(a.strip())
# 71 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
print(sorted(foo,key = lambda x:x))
# 72 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
print(sorted(foo,key = lambda x:(x<0,abs(x))))
# 73
# 74 列表嵌套字典的排序，分别根据年龄和姓名排序
foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
foo.sort(key = lambda x :x["age"])
print(foo)
# 75
# 76 列表嵌套列表排序，年龄数字相同怎么办？
a = [[1,2],[2,3],[3,3],[1,3],[4,4]]
a.sort(key = lambda x :(x[1],x[0]))
print(a)
# 77
# 78
# 79
# 80
# 81
# 82
# 83
# 84
# 85
# 86
# 87
# 88
# 89
# 90
# 91
# 92
# 93
# 94
# 95
# 96
# 97
# 98
# 99