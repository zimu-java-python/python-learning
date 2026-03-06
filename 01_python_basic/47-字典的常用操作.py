"""
演示字典的常用操作
"""

"""
字典的特点
可以容纳多个数据
可以容纳不同类型的数据
每一份数据是key和value的键值对
可以通过key获取到value，key不可重复（重复会覆盖））
不支持下标索引
可以修改
支持for循环，不支持while循环
"""

"""
新增元素
语法：字典[key] = value
结果：字典被修改，新增了元素
更新元素
语法：字典[key] = value
结果：字典被修改，更新了元素
注意：字典key不可以重复，所以对已经存在的key执行上述操作，就是更新value值
"""
my_dict = {"周杰伦":99,"林俊杰":88,"张学友":77}
# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果：{my_dict}")

# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新后，结果是：{my_dict}")

"""
删除元素
语法：字典.pop(key)
结果：获得指定key的value，同时字典被修改，指定的key的数据被删除
"""
# 删除元素
score = my_dict.pop("周杰伦")
print(f"字典中被移除了一个元素，结果：{my_dict}，周杰伦的考试分数是：{score}")

# 清空元素
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")

"""
获取全部的key
语法：字典.keys()
结果：得到字典中的全部key
"""
# 获取全部的key
my_dict = {"周杰伦":99,"林俊杰":88,"张学友":77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")

# 遍历字典

# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是{my_dict[key]}")

# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是{my_dict[key]}")

# 统计字典内的元素数量
num = len(my_dict)
print(f"字典内一共有：{num}个元素")