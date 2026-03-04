"""
演示数据容器集合的使用
"""

"""
集合的特点
可以容纳多个数据
可以容纳不同类型的数据
不允许重复数据存在
无序，不支持下标索引
允许修改
支持for循环
"""

# 定义集合
my_set = {"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima,","传智教育","黑马程序员","itheima,"}
my_set_empty = set() # 定义空集合
print(f"my_set的内容是：{my_set}，类型是{type(my_set)}")
print(f"my_set的内容是：{my_set_empty}，类型是{type(my_set_empty)}")

"""
添加新元素
语法：集合.add(元素)，将指定元素，添加到集合内
结果：集合本身被修改，添加了新元素
"""
# 添加新元素
my_set.add("Python")
my_set.add("传智教育") # 去重
print(f"my_set添加元素后结果是：{my_set}")

"""
移除元素
语法：集合.remove(元素)，将指定元素，从集合内移除
结果：集合本身被修改
"""
# 移除元素
my_set.remove("黑马程序员")
print(f"移除黑马程序员后结果是：{my_set}")

"""
从集合中随机取出元素
语法：集合.pop()
功能：从集合中随机取出一个元素
结果：会得到一个元素的结果。同时集合本身被修改，元素被移除
"""
# 随机取出一个元素
my_set = {"传智教育","黑马程序员","itheima"}
element = my_set.pop() # 随机取出
print(f"集合被取出的元素是{element}，取出元素后集合还有：{my_set}")

# 清空集合
my_set.clear()
print(f"集合被清空了，结果是{my_set}")

"""
取两个集合的差集
语法：集合1.difference(集合2)
功能：取出集合1和集合2的差集（集合1有的而集合2没有的）
结果：得到一个新集合，集合1和集合2不变
"""
# 取两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出差集后的结果是{set3}，取差集后set1的内容是：{set1}，set2的内容是：{set2}")

"""
消除两个集合的差集
语法：集合1.difference_update(集合2)
功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素
结果：集合1被修改，集合2不变
"""
# 消除两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"消除差集后，集合1结果：{set1}")
print(f"消除差集后，集合2结果：{set2}")

"""
2个集合合并
语法：集合1.union(集合2)
功能：将集合1和集合2组成新集合
结果：得到新集合，集合1和集合2不变
"""
# 2个集合合并
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"将两个集合合并后，结果是：{set3}")
print(f"合并后集合1：{set1}")
print(f"合并后集合2：{set2}")

# 统计集合的元素数量
set1 = {1,2,3,4,5,1,2,3,4,5}
num = len(set1)
print(f"集合1的元素数量是：{num}")

# 集合的遍历
# 不支持下标索引，不能用while循环
set1 = {1,2,3,4,5}
for element in set1:
    print(f"集合的元素有：{element}")
