"""
演示特殊字面量：None
"""

# 无return语句的函数返回值
def say_hi():
    print("你好")

result = say_hi()
print(result)
print(type(result))

# 主动返回None的函数
def say_hi2():
    print("你好")
    return None

result = say_hi2()
print(result)
print(type(result))

# None用于if判断
def check_age(age):
    if age >= 18:
        return "SUCCESS"
    else:
        return None

result = check_age(18)
if not result:
    # 进入if表示result是None值 也就是False
    print("未成年，不可以进入")
else:
    print("成年，可以进入")

# None用于声明无初始内容的变量
name = None
