"""
演示函数使用参数
"""

# 定义2数相加的函数，通过参数接收被计算的2个数字
def add(x,y,z):
    result = x + y + z
    print(f"{x} + {y} + {z} = {result}")

# 调用函数
add(int(input("请输入第一个数字：")),int(input("请输入第二个数字：")),int(input("请输入第三个数字：")))
