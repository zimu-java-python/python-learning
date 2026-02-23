# 股价计算小程序

# 定义变量
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7

# 计算增长后的股价
stock_price_final = stock_price * (stock_price_daily_growth_factor ** growth_days)

# 使用f-string格式化输出第一行（要求使用f"变量"的方式）
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")

# 使用%占位符格式化输出第二行（要求使用%占位符的方式）
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, stock_price_final))
