"""
此列表记录一批学生的年龄
内容是：[21,25,21,23,22,20]
"""

# 定义这个列表，用变量接收它
name_list = [21,25,21,23,22,20]
print(name_list)

# 追加一个数字31，到列表的尾部
name_list.append(31)
print(name_list)

# 追加一个新列表[29,33,30]，到列表的尾部
name_list.extend([29,33,30])
print(name_list)

# 取出第一个元素（21）
print(name_list[0])

# 取出最后一个元素（30）
print(name_list[-1])

# 查找元素31，在列表的下标位置
index = name_list.index(31)
print(index)