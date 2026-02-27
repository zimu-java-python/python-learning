"""
元组的基本操作
"""

# 定义一个元组，记录一个学生的信息
t1 = ('周杰轮',11,["football",'music'])

# 查询其年龄所在的下标位置
index = t1.index(11)
print(f"其年龄所在的下标位置是：{index}")

# 查询学生的姓名
name = t1[0]
print(f"学生的姓名是：{name}")

# 删除学生爱好中的football
del t1[2][0]
print(f"删除学生某一爱好后的元组为{t1}")

# 增加爱好：coding到爱好list内
t1[2].append("coding")
print(f"添加爱好后元组为{t1}")
