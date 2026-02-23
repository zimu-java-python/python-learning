count = 10000

for i in range(1,21):
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位。")
        continue
    else:
        print(f"向员工{i}，发放工资1000元，账户余额还剩余{count-1000}元")
        count -= 1000
        if count == 0:
            print("发工资结束了，下个月领取吧。")
            break


