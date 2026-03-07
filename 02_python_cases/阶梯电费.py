# 1. 获取输入数据
last_month = int(input("上月电表读数："))
this_month = int(input("本月电表读数："))
month = int(input("月份："))

# 2. 计算总用电量
usage = this_month - last_month

# 3. 定义基础电价（第一档为公共档位）
price1 = 0.588  # 第一档电价
price2 = 0.638  # 第二档电价
price3 = 0.888  # 第三档电价

# 4. 根据月份判断季节，确定各档位分界值
if 3 <= month <= 5 or 9 <= month <= 11:
    # 春秋季：第二档200-350度，第三档350度以上
    limit1 = 200
    limit2 = 350
else:
    # 冬夏季（12-2月、6-8月）：第二档200-450度，第三档450度以上
    limit1 = 200
    limit2 = 450

# 5. 分步计算阶梯电费
total_fee = 0.0
if usage <= limit1:
    # 仅第一档
    total_fee = usage * price1
elif usage <= limit2:
    # 第一档 + 第二档
    total_fee = limit1 * price1 + (usage - limit1) * price2
else:
    # 第一档 + 第二档 + 第三档
    total_fee = limit1 * price1 + (limit2 - limit1) * price2 + (usage - limit2) * price3

# 6. 按要求格式输出（保留1位小数）
print(f"用电度数{usage:.1f}")
print(f"电费{total_fee:.2f}")