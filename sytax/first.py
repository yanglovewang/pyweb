#1. 基本语法
# 常量约定为全部字母大写，py 的常量知识约定没有做语法检查
import math

from collections import Iterable, Iterator

PI = 3.14
# 将 byte 解码，忽略解析不出的字节，开头的 b 是表示该字符串为 bytes
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# 计算字符串字符数
len('中文'.encode('utf-8'))
# 新版占位符
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# list数组
classmates = ['Michael', 'Bob', 'Tracy']
# 索引最后一个数组，索引前面加个负号表示倒数索引
last = classmates[-1]
# 插入一个元素
classmates.insert(1, 'Jack')
# 替换某个元素
classmates[1] = 'Sarah'
# 删除某个元素
classmates.pop(1)
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']

# tuple
# 表示不可变的数组
t = (1, 2)
# 定义一个元素的 tuple 需要在元素后面加个 , 不然会被当成小括号表达式
t = (1,)
# “可变的” tuple，其中 list 是可变的
t = ('a', 'b', ['A', 'B'])

# 条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 循环
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print(sum2)

# dict 和 set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 67}
# 防止元素不存在出错
if 'Thomas' in d:
    print(d['Thomas'])
# 删除元素
d.pop('Bob')
# set 是一个没有 value 的 dict
s = {1, 2, 3}
s.add(4)
s.remove(4)
# set 可以看成数学意义上的无序和无重复元素的集合
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 & s2
s4 = s1 | s2

# 字符串操作
a = 'abc'
a.replace('a', 'A')


# 函数
#类型转化函数
int('123')
float('12.34')
str(1.23)
bool(1)
#定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
#空函数
def nop():
    pass
# 返回一个 tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

xx, yy = move(100, 100, 60)
r = move(100, 100, 60)
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用可变参数函数
nums = [1, 2, 3]
calc(*nums)
calc(1, 2, 3)

# 关键字参数接收一个 dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 调用关键字参数函数
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 命名关键字参数
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
# 调用
person('Jack', 24, city='Beijing', job='Engineer')
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 使用多种参数组合接口的可理解性比较差
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 高阶函数
# 把一个函数当成一个参数传给另一个函数
def add(x, y, f):
    return f(x) + f(y)

def fn(x):
    return x*2

add(1, 2, fn)
# 高级特性
# 切片
s = "abcdefghihklmnopqrstuvwxyz"
sp1 = s[3:4]
ls = [1, 2, 3, 4, 5]
sp2 = ls[1:2]
# 迭代 dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, '=', v)
# 迭代字符串
for ch in 'ABC':
    print(ch)
# 判断是否迭代
isinstance('abc', Iterable)
# 下标迭代
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 列表生成式
li = [x * x for x in range(1, 11)]
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)