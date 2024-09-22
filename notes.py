import math
from collections.abc import Iterable
from functools import reduce
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

#### starting from Anonymous Functions
