"""
信息去重
"""

# 有如下列表对象
my_list = ['黑马程序员','传智博客','黑马程序员','传智博客',
           'itheima','itcast','itheima','itcast','best']

# 定义一个空集合
set1 = set()

# 通过for循环遍历列表
# 在for循环中将列表的元素添加至集合
for element in my_list:
    set1.add(element)

# 最终得到元素去重后的集合对象，并打印输出
print(f"有列表：{my_list}，\n存入集合后得到set1：{set1}")

