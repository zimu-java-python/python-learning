# 循环判断，直到输入000000退出
while True:
    # 获取用户输入的股票代码（保持字符串格式，便于截取前缀）
    code = input().strip()

    # 终止条件：输入000000则退出循环
    if code == "000000":
        break

    # 第一步：校验是否为6位数字
    if len(code) != 6 or not code.isdigit():
        print("错误编码")
        continue

    # 第二步：截取前3位前缀，匹配板块规则
    prefix = code[:3]
    if prefix == "600":
        print("沪市A股")
    elif prefix == "000":
        print("深市A股")
    elif prefix == "300":
        print("创业板")
    elif prefix == "688":
        print("科创板")
    elif prefix == "002":
        print("中小板")
    # 第三步：不匹配任何规则，输出错误编码
    else:
        print("错误编码")