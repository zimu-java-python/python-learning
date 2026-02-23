# 标日初级上 学习期间的Python入门练习
# 日本語能力N5取得のために並行してPythonを学習中

# 1. 基础输出（对应日语自我介绍）
print("【自己紹介 / Self-Introduction】")
name = "留学生"
study_target = "Pythonと日本語N5"
print(f"名前：{name}")
print(f"勉強中の内容：{study_target}")

# 2. 简单计算（Python基础语法）
print("\n【簡単な計算 / Simple Calculation】")
japanese_study_hours = 180  # 日语学时要求
python_study_days = 90
daily_python_hours = japanese_study_hours / python_study_days
print(f"毎日のPython勉強時間：{daily_python_hours}時間")

# 3. 条件判断练习
print("\n【学習進捗 / Study Progress】")
current_japanese_lesson = 12
target_lesson = 24
if current_japanese_lesson < target_lesson:
    print(f"続けて勉強中！現在{current_japanese_lesson}課、目標{target_lesson}課")
else:
    print("日本語初級上終了！")
