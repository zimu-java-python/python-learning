# 1. 读取管理员输入的年龄阈值
threshold = int(input())

# 2. 读取并解析 test.txt 文件
qualified_names = []
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # 去除行首尾的空白字符（包括换行符）
        line = line.strip()
        # 跳过空行
        if not line:
            continue
        # 按冒号分割姓名和年龄
        if ':' in line:
            name, age_str = line.split(':', 1)
            try:
                age = int(age_str)
                # 判断年龄是否大于阈值
                if age > threshold:
                    qualified_names.append(name)
            except ValueError:
                # 忽略年龄格式不正确的行
                pass

# 3. 按要求格式输出结果
if qualified_names:
    print(f"大于{threshold}岁的人有:{','.join(qualified_names)}")
else:
    print(f"大于{threshold}岁的人有:")