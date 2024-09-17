#面向对象编程的概念
class person:
    #类的构造方法（初始化对象时会自动调用）
    def __init__(self, name, age):
        self.name = name  #实例变量
        self.age = age    #实例变量

    #类中的方法
    def greet(self):
        print(f"Hello! My name is {self.name}, I'm {self.age} years old")
        
#创建一个Person对象 
socket = person("OU", 23)

#调用对象的方法
socket.greet()