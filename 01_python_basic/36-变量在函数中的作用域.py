"""
演示在函数的使用中，定义的变量的作用域
"""

# # 演示局部变量
# def test_a():
#     num = 100
#     print(num)
#
# test_a()
# # 出了函数体，局部变量就无法使用了
# # print(num)

# 演示全局变量
# num = 200
# def test_b():
#     print(f"test_b：{num}")
#
# def test_c():
#     print(f"test_c：{num}")
#
# test_b()
# test_c()
# print(num)

# 在函数内部修改全局变量
# num = 200
# def test_b():
#     print(f"test_b：{num}")
#
# def test_c():
#     num = 500       # 局部变量
#     print(f"test_c：{num}")
#
# test_b()
# test_c()
# print(num)

# global关键字，在函数内声明变量为全局变量
num = 200
def test_b():
    print(f"test_b：{num}")

def test_c():
    global num
    num = 500       # 局部变量
    print(f"test_c：{num}")

test_b()
test_c()
print(num)
