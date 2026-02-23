name = "传智博客"
setup_year = 2006
stock_price = 19.99
message = "%s，成立与%d，今天的股票价格是：%.2f" % (name, setup_year, stock_price)
print(message)

num_1 = 11
num_2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num_1)
print("数字11宽度限制1，结果是：%1d" % num_1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num_2)
print("数字11.345，小数精度2，结果是：%.2f" % num_2)
