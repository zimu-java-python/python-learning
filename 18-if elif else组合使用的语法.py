"""
演示if elif else 多条件判断语句的使用
"""

# height = int(input("请输入你的身高（cm）："))
# VIP_level = int(input("请输入你的VIP等级（1-5）："))
# day = int(input("请告诉我今天几号："))

# 可以使用多条件判断的语法
if int(input("请输入你的身高（cm）：")) < 120:
    print("身高小于120cm，可以免费游玩。")
elif int(input("请输入你的VIP等级（1-5）：")) > 3:
    print("VIP级别大于3，可以免费游玩。")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天是1号免费日，可以免费游玩。")
else:
    print("不好意思，条件都不满足，需要购票10元。")

print("祝你游玩愉快。")
