# 将数字类型转换成字符串
num_str = str(666)
print(type(num_str), num_str)

float_str = str(13.14)
print(type(float_str), float_str)

# 将字符串转换成数字
num_int = int("666")
print(type(num_int), num_int)

num_float = float("13.14")
print(type(num_float), num_float)

# 错误示例，想要将字符串转换成数字，必须要求字符串内的内容都是数字
# num3 = int("黑马程序员")
# print(type(num3), num3)

# 整数转浮点数
float_num = float(666)
print(type(float_num), float_num)

# 浮点数转整数(丢失精度)
int_num = int(13.14)
print(type(int_num), int_num)
