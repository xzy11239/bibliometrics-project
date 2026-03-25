import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv("data/savedrecs.txt", sep="\t", encoding="utf-8")

# 统计年份
year_counts = df["PY"].value_counts().sort_index()
plt.figure(figsize=(10,5))
year_counts.plot(kind="line", marker="o")
plt.title("Annual Publications")
plt.savefig("outputs/year_trend.png")
plt.close()

# 统计关键词
keywords = []
for kw in df["DE"].dropna():
    keywords.extend([k.strip() for k in kw.split(";")])
kw_counter = Counter(keywords).most_common(20)

plt.figure(figsize=(12,6))
plt.bar([k[0] for k in kw_counter], [k[1] for k in kw_counter])
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/top_keywords.png")
plt.close()

print("✅ 分析完成，图表已保存到 outputs 文件夹")
