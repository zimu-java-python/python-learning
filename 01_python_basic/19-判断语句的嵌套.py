"""
演示判断语句的嵌套使用
"""


# print("欢迎来到黑马动物园。")
#
# if int(input("请输入你的身高（cm）：")) > 120:
#     print("你的身高超出限制，不可以免费。")
#     print("不过如果你的VIP等级大于3，可以免费游玩。")
#
#     if int(input("请输入你的vip级别：")) > 3 :
#         print("恭喜你，你的VIP等级大于3，可以免费游玩。")
#     else:
#         print("Sorry，你需要补票10元。")
# else:
#     print("欢迎你小朋友，你可以免费游玩。")


age = int(input("请输入您的年龄（岁）："))
year = int(input("请输入您的入职时长（年）"))
level = int(input("请输入您的级别（1-5）"))

if age >= 18:
    print("成年人符合，继续判断。")
    if age < 30:
        print("年龄达标符合，继续判断。")
        if year > 2:
            print("小于30岁的成年人且入职时间超过2年，满足条件，可以领取。")
        elif level > 3:
            print("级别大于3的成年人，可以领取。")
        else:
            print("您的入职时间不够或级别小于3，不可领取。")
    else:
        print("Sorry，超过30岁不可领取礼物。")
else:
    print("Sorry，未成年不可领取礼物。")


