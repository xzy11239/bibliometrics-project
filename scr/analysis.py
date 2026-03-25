import pandas as pd

# 读取你的纯文本数据（制表符分隔）
df = pd.read_csv("data/savedrecs.txt", sep="\t", encoding="utf-8")

# 打印所有列名，让你看到真实名字
print("=== 你的数据里所有列名 ===")
print(df.columns.tolist())

# 打印前2行，确认数据样子
print("\n=== 前2行数据预览 ===")
print(df.head(2))
