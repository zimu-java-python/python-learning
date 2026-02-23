"""
演示：定义函数返回值的语法格式
"""

def add(a,b):
    result = a + b
    return result
    # 返回结果后，还想输出一句话
    print("我完事了")

# 函数的返回值可以用变量去接收
sum = add(3,4)
print(sum)
