# class Rect:
#     def __init__(self, weight):
#         self.weight = weight
#         print(f'父类初始化的weight = {self.weight}')

# class Square(Rect):
#     def Square_print(self):
#         print(f'子类初始化的weight = {self.weight}')

#     def __init__(self):
#         super().__init__(10)
#         self.weight = 100
#         print(f'子类初始化的weight = {self.weight}')

# # 如果子类没有 __init__() 方法,在实例化对象的时候会调用父类的初始化方法
# # 如果子类有   __init__() 方法,在实例化对象的时候不会调用父类的初始化方法
# # 通常,如果子类的一部分初始化代码和父类的相同,一般需要显示调用父类的初始化方法,而且要传入相应   的参数,如上
# s = Square() 

from random import randint

class Forest():
    def __init__(self, monster):
        self.monster = monster
# 动物妖怪的父类
class Animals():
    def __init__(self, name):
        self.name = name

# 人形士兵的父类
class People():
    def __init__(self, name):
        self.name = name

class Eagle(Animals):
    def __init__(self, name):
        super().__init__(name)

class Wolf(Animals):
    def __init__(self, name):
        super().__init__(name)

# 实例化7座森林
forest = []
notification = '前方森林里的妖怪是: '
for i in range(7):
    flag = randint(0, 1)
    if flag == 0:
        monster = Wolf('狼妖')
    else:
        monster = Eagle('鹰妖')
    forest.append(Forest(monster))
    notification += \
        f'\n第{i + 1}座森林里是{forest[i].monster.name}'
print(notification)

class Player():
    stoneNum = 1000
    def __init__(self, archer_num, axeman_num):
        self.archer_num = archer_num
        self.axeman_num = axeman_num

class Archer(People):
    hirePrice = 100
    health = 100
    def __init__(self, name):
        self.name = f'弓箭兵{name}号'
    def fightWith(self, monster):
        if monster == '鹰妖':
            self.health -= 20
        else:
            self.health -= 80

class Axeman(People):
    hirePrice = 120
    health = 120
    def __init__(self, name):
        self.name = f'斧头兵{name}号'
    def fightWith(self, monster):
        if monster == '鹰妖':
            self.health -= 20
        else:
            self.health -= 80

# 创建 player 对象
archer_num = 0
axeman_num = 0
while archer_num * Archer.hirePrice + axeman_num * Axeman.hirePrice > Player.stoneNum or archer_num == 0 and axeman_num == 0:
    archer_num = int(input('弓箭兵的数量: '))
    axeman_num = int(input('斧头兵的数量 '))

player = Player(archer_num, axeman_num)
print(f'剩余的灵石有: {player.stoneNum - archer_num * Archer.hirePrice - axeman_num * Axeman.hirePrice}')

# 实例化弓箭兵和斧头兵
archer_list = [Archer(i + 1) for i in range(archer_num)]
axeman_list = [Axeman(i + 1) for i in range(axeman_num)]

# 士兵进入森林作战
for enviroment in forest:
    # 森林里的妖怪
    monster = enviroment.monster.name
    # 派出士兵
    soldier = input('派出士兵(弓箭兵/斧头兵): ')
    if soldier == '弓箭兵' and archer_num > 0:
        soldier_index = int(input('派出几号弓箭兵: ')) - 1
        archer_list[soldier_index].fightWith(monster)
        print(archer_list[soldier_index].health)
    elif soldier == '斧头兵' and axeman_num > 0:
        soldier_index = int(input('派出几号斧头兵: ')) - 1
        axeman_list[soldier_index - 1].fightWith(monster)
        print(axeman_list[soldier_index].health)
    else:
        print(f'{soldier}数量不足!')