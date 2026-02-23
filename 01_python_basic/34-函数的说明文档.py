"""
演示对函数进行文档说明
"""

# 定义函数，进行文档说明
def add(a,b):
    """
    add函数可以接收两个参数，进行2数相加的功能
    :param a: 形参x表示相加的其中一个数字
    :param b: 形参表示相加的另一个数字
    :return: 返回值是2数相加的结果
    """
    result = a + b
    print(f"2数相加的结果是{result}")
    return result

add(2,3)
