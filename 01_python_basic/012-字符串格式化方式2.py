# 通过占位的方式拼接字符串
name = "传智博客"
setup_year = 2006
stock_price = 19.99
message = "%s，成立与%d，今天的股票价格是：%.2f" % (name, setup_year, stock_price)
print(message)

# 通过语法：f"内容{变量}"的方式快速格式化，不做精度控制
name = "传智博客"
setup_year = 2006
stock_price = 19.99
print(f"{name}，成立于{setup_year}，今天的股票价格是：{stock_price}")
