"""
演示Python中 for循环临时变量的作用域
"""
x = 0 # 在for循环之前定义临时变量
for x in range(5):
    print(x)

print(x) # 规范上不建议
