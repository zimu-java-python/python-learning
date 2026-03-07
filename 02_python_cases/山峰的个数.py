# 读取输入并转换为浮点数列表
h = list(map(float, input().split(', ')))

# 初始化山峰计数器
count = 0

# 遍历列表，检查每个中间点是否为山峰
for i in range(1, len(h) - 1):
    if h[i] > h[i-1] and h[i] > h[i+1]:
        count += 1

# 输出结果
print(count)