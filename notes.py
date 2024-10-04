import math
from collections.abc import Iterable
from functools import reduce
import functools
import types
from types import MethodType
################################################## 字符串 & 编码 ##################################################
devided = 10 // 3 #取整得 3
devided = 10 / 3  #精确除法得 3.333333...

# bytes类型得数据用带 b 前缀的单引号或双引号表示
x = b'ABC'
# y是字符串
y = 'ABC'

# 以Unicode表示的 str 通过 encode() 方法可以编码为指定的 bytes,例如
print('ABC'.encode('ascii'))  # b'ABC'
print('中文'.encode('utf-8')) # b'\xe4\xb8\xad\xe6\x96\x87'

#反过来,将 bytes 变为 str,需要用到 decode()方法
print(b'ABC'.decode('ascii')) #ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) #中文

#计算 str 中包含多少个字符,使用len()函数
print(len('ABC')) # 3
print(len('中文')) # 2

#len()函数计算的是 str 的字符数,如果换成是 bytes ,len()函数就将计算字节数
print(len(b'ABC')) # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # 6
print(len('中文'.encode('utf-8'))) # 6

nickname = 'learniuH'
age = 23
print(f'我的名字是{nickname}, 今年{age}岁了！')

################################################## list & tuple ##################################################
classmate = ['Rose', 'xila', 'Michael'] #list
print(f'classmate list里一共有{len(classmate)}个元素') # 3

classmate[0] # Rose
classmate[-1] # Michael

classmate.append('lip') #['Rose', 'xila', 'michael', 'lip'] .append()追加元素到末尾
classmate.insert(1, 'fiona') #['Rose', 'fiona', 'xila', 'michael', 'lip'] .insert把元素插入到指定位置
classmate.pop() #['Rose', 'fiona', 'xila', 'michael'] .pop()删除list末尾的元素
classmate.pop(1) #['Rose', 'xila', 'michael'] .pop(1)删除索引为1的元素

classmate[1] = 'rich' #['Rose', 'rich', 'michael'] 将索引为1的元素替换

roommate = [] #空的list, len(roomate) == 0,长度为0

fruit = ('apple', 'banana', 'cherry') #tuple 元组,一旦初始化将不能更改,没有append(),insert(),pop()这些方法
fruit = ('apple', 'banana', ['watermelon', 'strawberry']) #这样就定义了一个可变的tuple
fruit[2][0] = 'pear' #('apple', 'banana', ['pear', 'strawberry'])

################################################## 循环 ##################################################
#Python 的循环有两种(一种是 while 循环):一种是 for in 循环,依次把 list 或 tuple 里的元素迭代出来
names = ['jackey', 'white', 'learniuH']
for name in names:
    print(name) #以此换行打印 jackey white learniuH

sum = 0
for x in list(range(101)): #计算0~100相加和
    sum += x
print(sum) # 5050

################################################## dict & set ##################################################
key = ['Michael', 'Bob', 'lip']
value = [88, 90, 95]

script_dict = {'Michael': 88, 'Bob': 90, 'lip':95} # dict
#将数据放入 dict 的方法,除了初始化的时候指定,还可以通过key放入:
script_dict['lip'] = 100 #{'Michael': 88, 'Bob': 90, 'lip':100}

script_dict.get('Tomas') #通过 .get() 查找字典中对应 key 的 value,如果不存在,返回None
script_dict.pop('Bob') #通过 .pop(键) 的方式删除 dict 中的键值对

my_dict = {0: "apple", 1: "banana", 2: "cherry"}
for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")
print(my_dict.items()) # dict_items([(0, 'apple'), (1, 'banana'), (2, 'cherry')])
'''
my_dict.items()
返回一个包含字典中所有键值对的视图对象,表示为(key, value)的元组列表
[(0, "apple"), (1, "banana"), (2, "cherry")]
'''

"""
和list比较,dict有以下几个特点:
1.查找和插入的速度极快,不会随着key的增加而变慢;
2.需要占用大量的内存,内存浪费多。

而list相反:
1.查找和插入的时间随着元素的增加而增加;
2.占用空间小,浪费内存很少。
所以,dict是用空间来换取时间的一种方法。

并且 dict 的 key 一定是不可以改变的,下面的写法就是错误的:
list = ['Jackey']
script_dict[list] = 1;
"""

# set 和 dict 类似,是一组 key 的集合,但不存储 value, 且 key 不能重复, 二者唯一的区别是 set 没有存储对应的 value
temp_set = {1, 2, 3} # set 里有3个元素
temp_set.add(4) # .add() 添加元素4到 set 中，重复添加无效
temp_set.remove(4) # .remove() 删除元素4

# set 可以看作数学上无序和无重复元素的集合，两个 set 可以做数学意义上的 交集 并集 等操作
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 & s2 # {2, 3}
s1 | s2 # {1, 2, 3, 4}

################################################## function ##################################################
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6) #多个变量同时接收一个 tuple, 按位置赋予对应的值
print(x, y) # 151.96152422706632 70.0
#其实函数返回的仍然是一个单一值
r = move(100, 100, 60, math.pi / 6)
print(r) # (151.96152422706632, 70.0) 可以看到函数返回的就是一个 tuple

#编写一个函数 quadratic(a, b, c) 返回 一元二次方程的两个解
def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

# 定义了一个计算 x 的 n 次方的函数
# 在我们平常的使用中呢，最常使用的其实是 平方的计算， n = 2 就是一个默认参数,当我们需要计算平方时,可以直接调用 power(5)
# 默认参数可以简化函数的调用
def power(x, n = 2):
    s = 1
    while n > 0:
        s = s * x
        n -= 1
    return s

def enroll(name, gender, age = 6, city = 'beijing'):
    print('name: ', name)
    print('gender: ', gender)
    print('age: ', age)
    print('city: ', city)

enroll('sansa', 'F', 14) # 有多个默认参数时,可以按顺序提供默认参数
enroll('Joffrey', 'M', city = 'King\'s land') # 也可以不按顺序提供部分默认参数

# 可变参数: 表示函数参数的数量是可变的, *numbers,可以是1个,2个,甚至是0个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2) # 5
calc() # 0

# 关键字参数: 关键字参数允许你传入0个或多个含参数名的参数
# 这些关键字参数在函数内部自动组装为一个 dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('imp', '18', city = 'king\'s land') # name: imp age: 18 other: {'city': "king's land"}

# 命名关键字参数, 限制关键字参数的名字
# * 后面的参数被视为命名关键字参数
def human(name, age, *, city, job):
    print(name, age, city, job)

human('lora', 18, city = 'KunMing', job = 'Engineer')

# 参数组合：必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
# 但是请注意：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数 ！！！！！！！！
def mul(*number):
    mulvalue = 1
    if number == ():
        return
    else:
        for i in number:
            mulvalue *= i
        return mulvalue
    
# 递归函数
def fact(n): # 计算n的阶乘
    # n! = n * (n-1) * (n-2) ... * 2 * 1 = n * (n-1)! = n * fact(n-1)
    if n == 1:
        return 1
    return n * fact(n-1)

def Move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        Move(n-1,a,c,b) #将上n-1个从a移到b上
        Move(1,a,b,c) #必要步骤：将最后一个从a移到c上
        Move(n-1,b,a,c) #将上n-1个从b移到c上

Move(3, 1, 2, 3)

################################################## 切片 ##################################################
#写一个代码，获取列表的前三个元素
list_temp = ['1', '2', '3', '6', '7', '8']
list_display = []
for i in range(3):
    list_display.append(list_temp[i])
print(list_display) # ['1', '2', '3']

#对于这样经常指定索引范围的操作,用循环十分频繁,Python提供了slice(切片)的操作符
#应对上面的问题,使用slice一行代码即可完成操作
list_display = list_temp[1:3] # ['2', '3']
list_display = list_temp[3:6] # ['6', '7', '8']
#总结: [x:y] 左闭右开 x y 对应的是list的索引

# 同样的支持取倒数切片
list_display = list_temp[-2:-1] # ['7'] -2是倒数第二个元素,同样 左闭右开
list_display = list_temp[1:-1] # ['2', '3', '6', '7'] 去掉两头
list_display = list_temp[-2:] # ['7', '8']
#总结: -1是倒数第一个元素的索引, -2是倒数第二个元素的索引,同样是 左闭右开

# 生成一个 0-99 的list
hundred = list(range(100))
print(hundred)
# 取出列表的前20个元素
hundred[:20]
# 取出列表的后30个元素
hundred[-30:]
# 前十个数 每2个取1个
print(hundred[:10:2]) # [0, 2, 4, 6, 8]
#所有数 每5个取1个
print(hundred[::5]) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# 针对字符串同样适用
list_str = 'ABCDEF'
print(list_str[0:3]) #ABC
print(list_str[::2]) #ACE

#exercise
def trim(s):
    while s and (s[0] == ' ' or s[-1] == ' '):
        if(s[0] == ' '):
            #如果第一个元素是' ',就去掉
            s = s[1:]
            #最后一个元素是' ',去掉
        else:
            s = s[:-1]
    return s

################################################## 迭代 ##################################################
#迭代dict
dict_temp = {'a': 1, 'b': 2, 'c': 3}
#迭代key
for key in dict_temp:
    print(key) # a\n b\n c\n
#迭代value
for value in dict_temp.values():
    print(value) #1\n 2\n 3\n
#迭代 key 和 value
for k, v in dict_temp.items():
    print(k, v) #a 1\n b 2\n c 3\n

#同样的字符串也是可以迭代的
for ch in 'ABC':
    print(ch) # A\n B\n C\n

#所以当我们使用 for 循环时,只要作用于一个可迭代的对象,那么for循环就可以正常运行
#如何判断一个对象是否可迭代?
#from collections.abc import Iterable
isinstance('abc', Iterable) #True
isinstance([1, 2, 3], Iterable) #True
isinstance(123, Iterable) #False

#exercise
def findMinAndMax(L):
    if L != []:
        Max = L[0]
        Min = L[0]
        for value in L:
            if value < Min:
                Min = value
            elif value > Max:
                Max = value
        return (Min, Max)
    else:
        return (None, None)

################################################## 列表生成式 ##################################################
#要生成 [1*1, 2*2, 3*3, ...10*10]?
hundred_list = []
for i in range(1,11):
    hundred_list.append(i * i) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#但是循环太过繁琐,使用列表生成式:
hundred_list = [x * x for x in range(1, 11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表生成式 使用两个变量生成list
dict_list_gen = {'x': 'A', 'y': 'B', 'z': 'C'}
list_generate = [k+ '=' + v for k, v in dict_list_gen.items()] # ['x=A', 'y=B', 'z=C']

# 把所有字符串变小写
list_str = ['HELLO', 'WORLD', 'LEARNIUH']
list_str_lower = [s.lower() for s in list_str] # ['hello', 'world', 'learniuh']

#if...else
#生成偶数,跟在 for 后面的 if 是筛选条件
print([x for x in range(1,11) if x % 2 == 0]) # [2, 4, 6, 8, 10]
#在 for 前面的 if...else 是表达式
print([x if x % 2 == 0 else -x for x in range(1, 11)]) # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# exercise
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [element.lower() for element in L1 if isinstance(element, str)] # ['hello', 'world', 'apple']
# 以下是求解过程
# def function(L1):
#     L2 = []
#     for element in L1:
#         if isinstance(element, Iterable):
#             L2.append(element.lower())
#     return L2

################################################## 生成器 generator ##################################################
# 与列表生成式不同的是 外层是 ()
generation = (x * x for x in range(1,11))
print(generation) # <generator object <genexpr> at 0x0000022F3316F448>
# 关于 generator 的细节请看博客

# exercise

################################################## 高阶函数 ##################################################
#既然变量可以指向函数,函数的参数也能接收变量,那么一个函数就可以接收另一个函数作为变量,这种函数就叫做高阶函数
a = -1
b = 1
def Higher_order_function(a, b, abs):
    return abs(a) + abs(b) # 2

# map
def f(x):
    return x * x
ret = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8])) # [1, 4, 9, 16, 25, 36, 49, 64]

ret = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8])) # ['1', '2', '3', '4', '5', '6', '7', '8']

# reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y
# from functools import reduce
reduce(add, [1, 3, 5, 7, 9]) # 25

# exercise
def normalize(name):
    return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1)) # ['Adam', 'Lisa', 'Bart']

# exercise
def mul(x, y):
    return x * y

def prod(L):
    return reduce(mul, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9])) # 945

# exercise
exercise_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '.': 0}

def mul(x, y):
    return x * 10

################################################## filter ##################################################
def odd(x):
    return x % 2 == 1
print(list(filter(odd, [1, 2, 4, 5, 6, 9, 10, 15]))) # [1, 5, 9, 15]
[n for n in [1, 2, 4, 5, 6, 9, 10, 15] if n % 2 == 1] # 同样的效果

#把一个序列中的空字符串删除
def no_empty(s):
    return s and s.strip()

print(list(filter(no_empty, ['A', '', 'B', None, 'C', '  ']))) # ['A', 'B', 'C']

################################################## sorted ##################################################
sorted([36, 5, -12, 9, -21]) # [-21, -12, 5, 9, 36]
sorted([36, 5, -12, 9, -21], key = abs) # [5, 9, -12, -21, 36]

sorted(['bob', 'about', 'Zoo', 'Credit']) # ['Credit', 'Zoo', 'about', 'bob']
# 忽略大小写比较两个字符串
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower) # ['about', 'bob', 'Credit', 'Zoo']

# 反向排序
sorted([1, 2, 4, 7, 9], reverse=True) # [9, 7, 4, 2, 1]

# key指定的函数将作用于list的每一个元素上,并根据key函数返回的结果进行排序 ！！！！！！！！！！
# exercise
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score) # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
L3 = sorted(L, key=by_score, reverse=True) # [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]

################################################## 返回函数 ##################################################
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count() # 9 9 9
# 对比
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count() # 1 4 9

# exercise
def createCounter():
    n = 0
    def counter():
        # 使用闭包时,对外层变量赋值前,需要先使用 nonlocal 声明该变量不是当前函数的局部变量
        nonlocal n
        n = n + 1
        return n
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


################################################## 匿名函数 ##################################################
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])) # [1, 4, 9, 16, 25, 36]
# 实际上 lamdba 就是:
def f(x):
    return x * x
# lambda 前面的就是函数的参数

# exercise
L = list(filter(lambda n: n % 2 == 1, range(1,20))) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

################################################## 装饰器 ##################################################
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2024-09-23')
# 完全看不懂装饰器

################################################## 偏函数 ##################################################
# import functools
int2 = functools.partial(int, base=2)
# functools.partial 的作用就是把 int() 的 base 参数固定住,返回一个新的函数,调用这个函数会更简单
int2('1000') # 8

# *args 将接收到的参数当作 tuple 处理
# *kwargs 将接收到的参数当作 dict 处理

################################################## 模块 ##################################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'LeariuH'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

#当我们在命令行运行 hello 模块文件时, Python 解释器把一个特殊变量 __name__ 置为 __main__ ,而如果在其他地方导入该hello模块时,if判断将失败
if __name__=='__main__':
    test()

# 类似__xxx__这样的变量是特殊变量,可以被直接引用
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

################################################## 面向对象编程 ##################################################
std1 = {'name': 'Bob', 'score': 80}
std2 = {'name': 'Michael', 'score':90}
def print_score(std):
    print('%s: %s', std['name'], std['score'])
# 以上是面向过程的编程方式
class Student_A:
    # 类的构造方法（初始化对象时会被自动调用）name 和 score 是类的两个属性
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print(f'{self.name}的成绩是:{self.score}')
    
    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score > 60:
            return 'B'
        else:
            return 'C'

Bob = Student_A('Bob', 80)
Michael = Student_A('Michael', 90)
Bob.print_score() # Bob的成绩是:80
Michael.print_score() # Michael的成绩是:90
Lisa = Student_A('Lisa', 70)
print(Lisa.name, Lisa.get_grade()) # Lisa B

class People:
    def __init__(self, name, score):
        # 属性名称前面加上 '__', 就变成了私有变量private
        self.__name = name
        self.__score = score
    
    def print(self):
        print("{self.__name}的成绩是:{self.__score}")
    
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score

Ros = People("Ros", 50)
print(Ros.get_name())

# exercise
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        self.__gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

################################################## 面向对象编程 ##################################################
class Animals(object):
    def run(self):
        print('Animal is running...')

# 继承 Animals 
class Dog(Animals):
    pass

class Cat(Animals):
    # 当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()
    # 这样，我们就获得了继承的另一个好处：多态！
    def run(self):
        print('Cat is running')

dog = Dog()
dog.run()
cat = Cat()

animals = Animals()
dog = Dog()
# 判断一个变量是否是某个类型 instance
print(isinstance(animals, Animals)) # True
print(isinstance(dog, Dog)) # True
# 注意 ！！！ 
print(isinstance(dog, Animals)) # 同样也是true
# 如果一个实例的数据类型是某个子类,那么他的数据类型也可以被看作是父类,但是反过来不行

def run_twice(Animals):
    Animals.run()

run_twice(animals)
run_twice(cat)

# type() 函数获取对象信息
type(abs) # <class 'builtin_function_or_method'>
type(dog) # <class '__main__.Dog'>
type('str') # <class 'str'>

# 使用 types 模块中定义的常量,判断一个对象是否是函数
# import types
type(run_twice) == types.FunctionType # True
type(abs) == types.BuiltinFunctionType # True

# 使用 dir 获取一个对象的所有属性和方法
dir('abc') # 列出 str 对象的所有属性和方法

class Mydog(object):
    def __len__(self):
        return 100
    
mydog = Mydog()
len(mydog) # 100

class Myobject(object):
    def __init__(self):
        self.x = 9
    
    def power(self):
        return self.x * self.x

obj = Myobject()
# obj 对象有 'x' 属性吗？
hasattr(obj, 'x') # True
# obj 对象有 'y' 属性吗？
hasattr(obj, 'y') #False
setattr(obj, 'y', 19) # 设置一个属性 y;  相当于 self.y = 19
# 获取 y 属性
print(getattr(obj, 'y')) # 19
# 试图获取不存在的属性时,会抛出 AttributeError 错误
# getattr(obj, 'z') # AttributeError: 'Myobject' object has no attribute 'z'

class Teacher(object):
    def __init__(self, name):
        self.name = name
    
LearniuH = Teacher('LearniuH')
# 通过创建实例 可以给对象绑定任意属性
LearniuH.heigh = 180 
print(LearniuH.heigh)

# 给 Teacher 类 本身绑定一个属性
class Master(object):
    # 绑定一个name属性,归 Master 类所有, 所有的实例 都可以访问到类的 name 属性
    name = 'master'
# 如果实例 绑定了自己的实例属性,实例属性会屏蔽掉类属性

# exercise
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        # 每实例化一个对象时,对应的类属性就 + 1
        Student.count = Student.count + 1

################################################## 面向对象高级编程 ##################################################
################################################## 使用 slots ##################################################
def set_age(self, age):
    self.age = age
    return self.age

lili = Student('lili')
# 给实例绑定一个方法
lili.set_age = MethodType(set_age, lili)
# 调用实例的方法
lili.set_age(25)
lili.age # 25

# 或者可以给 class 绑定方法,这样所有的实例都可以调用
Student.set_age = set_age
haha = Student('haha')
haha.set_age(25)
print(haha.age) # 25

# 使用 __slots__ 
class Student(object):
    __slots__ = ('name', 'age') # 用 tuple 定义允许绑定的属性名称

s = Student()
# s.score # 'Student' object has no attribute 'score' 试图绑定score属性会报错

# 子类不会继承 父类的 __slots__, __slots__ 定义的属性仅对当前实例起作用

################################################## 使用 slots ##################################################
class vagetable(object):
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        set._name = value
    
apple = vagetable()
apple._name = 'apple'
        


class Screen(object):
    @property
    def width(self):# 相当于定义了 getter 方法
        return self._width
    
    @width.setter# 相当于定义了 setter 方法
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self.height * self.width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

# 效果等同于
class Student(object):
    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value



class Vagetable(object):
    @property
    def name(self): # 两个方法的名字要一样
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
peal = Vagetable()
peal.name = 12
print(peal.name)

'''
                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Mammal    │           │    Bird     │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Bat   │  │ Parrot  │  │ Ostrich │
└─────────┘  └─────────┘  └─────────┘  └─────────┘

                ┌───────────────┐
                │    Animal     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │  Runnable   │           │   Flyable   │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │ Ostrich │  │ Parrot  │  │   Bat   │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
'''
# 针对上面的框架 比如 dog 属于 mammal 又能 run 正确的做法是
# 动物们 继承 mammal 和 bird 两个大类, 针对 会飞和会跑 继承会飞或会跑的类(赋予动物功能)
class Animals(object): # 动物大类
    pass

class Mammal(Animals): # 哺乳动物大类
    pass

class Bird(Animals): # 鸟 大类
    pass

class Runable(Animals): # 能跑
    def run(self):
        print('Running...')

class Flyable(Animals): # 会飞
    def fly(self):
        print('Flying...')

# 如果 dog 需要 runable 里的方法,就多继承一个 Runable
class Dog(Mammal, Runable):
    def __init__(self, name):
        self.name = name

dog = Dog('dog')
# 通过多重继承,一个子类可以拥有多个父类的功能

# 定制类
class Rabit(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s is jumpping' %self.name

print(Rabit('wihite')) # white is jumpping

################################################## 定制类 ##################################################
# 写一个类 Fib 作用于 for循环
class Fib(object):
    
    def __init__(self):
        self.a, self.b = 0, 1
        #self.a = 0
        #self.b = 1 
    
    def __iter__(self):
        return self # 实例本身就是循环对象,故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10000:
            raise StopIteration()
        return self.a

for n in Fib():
    pass
    #print(n) #迭代一个类, 打印斐波那契数列

################################################## 定制类 ##################################################
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name = %s)' % self.name
    #__repr__ = __str__

print(Student('Michael')) # Student object (name = Michael)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器

    def __iter__(self):
        return self # 实例本身就是迭代对象,故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b 
        if self.a > 20:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n) # 1 1 2 3 5 8 13
# 虽然能作用于 for 循环,也和list有点像,但是无法通过下标取出元素, 需要实现 __getitem__()方法

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
Fib()[0] # 1
Fib()[1] # 1
Fib()[2] # 2