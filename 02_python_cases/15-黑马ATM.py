money = 5000000
select = None
name = None
# 输入姓名进入主菜单
name = input("请输入您的姓名:")

# 查询余额函数
def query():
    global money
    print("----------------查询余额----------------")
    print(f"{name}，您好，您的余额剩余：{money}元")

# 存款函数
def save():
    global money
    save_money = int(input("请输入您要存款的金额："))
    print(f"{name}，您好，您存款{save_money}成功")
    money += save_money
    print(f"{name}，您好，您的余额剩余：{money}")

# 取款函数
def withdraw():
    global money
    withdraw_money = int(input("请输入您要取款的金额："))
    print(f"{name}，您好，您取款{withdraw_money}成功")
    money -= withdraw_money
    print(f"{name}，您好，您的余额剩余：{money}")

# 定义主菜单函数
def menu():
    print("----------------主菜单----------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额 [输入1]")
    print("存款 \t[输入2]")
    print("取款 \t[输入3]")
    print("退出 \t[输入4]")
    global select
    select = int(input("请输入您的选择："))

# 输入姓名后，调用主菜单函数

while True:
    menu()
    if select == 1:
        query()
        continue
    elif select == 2:
        save()
        continue
    elif select == 3:
        withdraw()
        continue
    else:
        print("程序退出啦！")
        break














