import math
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
    
# starting from 递归函数