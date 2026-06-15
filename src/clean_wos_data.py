import os
import re
from datetime import datetime

# ===================== 【配置区】 =====================
FOLDER_PATH = "."
FILE_PREFIX = "data"
FILE_SUFFIX = ".txt"
FILE_COUNT = 8
ENCODING = "utf-8"
OUTPUT_WOS_TXT = "wos_enhanced_clean.txt"

YEAR_MIN = 2015
YEAR_MAX = 2026

# 过滤开关
DEL_EMPTY_TI = True     # 删除无标题
DEL_EMPTY_AU = True     # 删除无作者
DEL_EMPTY_DE = True     # 删除无关键词
DEL_EMPTY_CR = True     # 删除无被引
# ====================================================

def clean_ut(ut_str):
    """标准化 UT 号，移除前缀和多余空格"""
    if not ut_str:
        return ""
    cleaned = ut_str.replace("UT ", "").strip()
    match = re.search(r'(WOS:?\d+|\d+)', cleaned)
    if match:
        return match.group(1)
    return cleaned

def clean_title(title_str):
    """标准化标题，移除 TI 前缀和多余空格"""
    if not title_str:
        return ""
    return title_str.replace("TI ", "").strip().lower()

def clean_authors(authors_str):
    """标准化作者，移除 AU 前缀和多余空格"""
    if not authors_str:
        return ""
    authors = authors_str.replace("AU ", "").replace("||", ";").strip()
    return authors

def clean_content_headers(content):
    """彻底移除文献内容中嵌入的 FN/VR 头部"""
    lines = content.splitlines(True)
    cleaned_lines = []
    found_pt = False
    
    for line in lines:
        # 跳过 FN、VR 行
        if line.startswith("FN ") or line.startswith("VR "):
            continue
        # 跳过空行（在头部之后）
        if not found_pt and line.strip() == "":
            continue
        # 找到 PT 后开始保留所有内容
        if not found_pt and line.startswith("PT "):
            found_pt = True
        if found_pt:
            cleaned_lines.append(line)
    
    # 如果没找到 PT（异常情况），返回原内容
    if not cleaned_lines:
        return content
    
    return "".join(cleaned_lines)

def read_wos_records(file_path, encoding):
    """读取WOS原生文件，拆分单篇文献（自动跳过文件头部）"""
    records = []
    single_paper = []
    ut_val = ""
    au_list = []
    ti_val = ""
    py_val = ""
    has_de = False
    has_cr = False
    header_skipped = False
    in_record = False

    with open(file_path, "r", encoding=encoding, errors="ignore") as f:
        for line in f:
            # 跳过文件头部（FN、VR 及后面的空行）
            if not header_skipped:
                if line.startswith("FN ") or line.startswith("VR "):
                    continue
                if line.strip() == "":
                    continue
                header_skipped = True
            
            # 遇到 PT 开始新文献
            if line.startswith("PT ") and not in_record:
                in_record = True
                single_paper = []
            
            if in_record:
                single_paper.append(line)
                
                # 提取字段
                if line.startswith("UT "):
                    ut_val = line.strip()
                elif line.startswith("AU "):
                    au_list.append(line.strip())
                elif line.startswith("TI "):
                    ti_val = line.strip()
                elif line.startswith("PY "):
                    match = re.search(r"PY\s+(\d{4})", line)
                    if match:
                        py_val = match.group(1)
                elif line.startswith("DE "):
                    has_de = True
                elif line.startswith("CR "):
                    has_cr = True
                
                # 文献结束
                if line.startswith("ER"):
                    full_content = "".join(single_paper)
                    records.append({
                        "ut_raw": ut_val,
                        "ut": clean_ut(ut_val),
                        "title_raw": ti_val,
                        "title": clean_title(ti_val),
                        "authors_raw": "||".join(au_list),
                        "authors": clean_authors("||".join(au_list)),
                        "year": py_val,
                        "content": full_content,
                        "has_ti": bool(ti_val),
                        "has_au": bool(au_list),
                        "has_de": has_de,
                        "has_cr": has_cr
                    })
                    # 重置
                    in_record = False
                    ut_val = ""
                    au_list = []
                    ti_val = ""
                    py_val = ""
                    has_de = False
                    has_cr = False
    
    return records

# ---------------------- 1. 读取所有文件 ----------------------
all_records = []
file_list = []

for idx in range(1, FILE_COUNT + 1):
    fname = f"{FILE_PREFIX}{idx}{FILE_SUFFIX}"
    full_path = os.path.join(FOLDER_PATH, fname)
    file_list.append(fname)
    if os.path.exists(full_path):
        print(f"读取文件：{fname}")
        papers = read_wos_records(full_path, ENCODING)
        all_records.extend(papers)
        print(f"  解析文献：{len(papers)} 篇")
    else:
        print(f"⚠️ 文件缺失：{fname}")

raw_total = len(all_records)
print(f"\n【原始合并】总文献数：{raw_total} 篇")

# ---------------------- 2. 去重 ------------------------
# 第一层：按标准化 UT 去重
ut_unique = {}
dup_ut_count = 0

for paper in all_records:
    ut_key = paper["ut"]
    if ut_key:
        if ut_key not in ut_unique:
            ut_unique[ut_key] = paper
        else:
            dup_ut_count += 1

# 第二层：按【标题+作者】去重（应用于所有文献）
remaining_papers = list(ut_unique.values())
title_auth_unique = {}
dup_title_count = 0

for paper in remaining_papers:
    if paper["title"] and paper["authors"]:
        key = f"{paper['title']}@@{paper['authors']}"
        if key not in title_auth_unique:
            title_auth_unique[key] = paper
        else:
            dup_title_count += 1
    else:
        title_auth_unique[f"no_key_{len(title_auth_unique)}"] = paper

dedup_list = list(title_auth_unique.values())
after_dedup = len(dedup_list)
dup_total = dup_ut_count + dup_title_count
print(f"【去重完成】重复文献 {dup_total} 篇（UT重复{dup_ut_count}，标题+作者重复{dup_title_count}），去重后剩余：{after_dedup} 篇")

# ---------------------- 3. 清洗过滤 ----------------------
final_list = []
stat_empty_ti = 0
stat_empty_au = 0
stat_empty_de = 0
stat_empty_cr = 0
stat_bad_year = 0

for p in dedup_list:
    flag_keep = True
    
    if DEL_EMPTY_TI and not p["has_ti"]:
        stat_empty_ti += 1
        flag_keep = False
    if DEL_EMPTY_AU and not p["has_au"]:
        stat_empty_au += 1
        flag_keep = False
    if DEL_EMPTY_DE and not p["has_de"]:
        stat_empty_de += 1
        flag_keep = False
    if DEL_EMPTY_CR and not p["has_cr"]:
        stat_empty_cr += 1
        flag_keep = False
    
    if p["year"]:
        try:
            year_int = int(p["year"])
            if not (YEAR_MIN <= year_int <= YEAR_MAX):
                stat_bad_year += 1
                flag_keep = False
        except:
            stat_bad_year += 1
            flag_keep = False
    else:
        stat_bad_year += 1
        flag_keep = False
    
    if flag_keep:
        # 关键：清洗文献内容中的头部
        p["content"] = clean_content_headers(p["content"])
        final_list.append(p)

final_total = len(final_list)
filter_total = after_dedup - final_total
print(f"\n【清洗过滤】剔除 {filter_total} 篇，最终保留：{final_total} 篇")
print(f"  明细：无标题{stat_empty_ti} | 无作者{stat_empty_au} | 无关键词{stat_empty_de} | 无被引{stat_empty_cr} | 年份异常{stat_bad_year}")

# ---------------------- 4. 输出文件（头部只写一次）-----------------------
out_path = os.path.join(FOLDER_PATH, OUTPUT_WOS_TXT)
with open(out_path, "w", encoding=ENCODING) as f_out:
    # 只写一次标准头部
    f_out.write("FN Clarivate Analytics Web of Science\n")
    f_out.write("VR 1.0\n")
    f_out.write("\n")
    
    for i, paper in enumerate(final_list):
        content = paper["content"].rstrip()
        
        # 确保以 ER 结尾
        if not content.endswith("ER"):
            content += "\nER"
        content += "\n"
        
        f_out.write(content)
        
        # 文献之间加空行
        if i < len(final_list) - 1:
            f_out.write("\n")
        
        if (i + 1) % 500 == 0:
            print(f"  已写入 {i+1}/{final_total} 篇文献")

print(f"\n✅ 清洗后数据文件已生成：{OUTPUT_WOS_TXT}")

# ---------------------- 5. 质量报告 ----------------------
md_quality = os.path.join(FOLDER_PATH, "data_quality.md")
quality_content = f"""# 数据质量报告
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
数据源：{', '.join(file_list)}
年份范围：{YEAR_MIN} - {YEAR_MAX}

## 文献数量统计
| 项目 | 数量 |
|------|------|
| 原始总量 | {raw_total} 篇 |
| 去重后 | {after_dedup} 篇 |
| 重复文献 | {dup_total} 篇 |
| 剔除文献 | {filter_total} 篇 |
| **最终保留** | **{final_total} 篇** |

## 剔除明细
| 异常类型 | 剔除数量 |
|----------|----------|
| 无标题 | {stat_empty_ti} |
| 无作者 | {stat_empty_au} |
| 无关键词 | {stat_empty_de} |
| 无被引 | {stat_empty_cr} |
| 年份异常 | {stat_bad_year} |

## 去重说明
- UT重复：{dup_ut_count} 篇
- 标题+作者重复：{dup_title_count} 篇
"""
with open(md_quality, "w", encoding="utf-8") as f:
    f.write(quality_content)
print("✅ 质量报告：data_quality.md")

# ---------------------- 6. 字段词典 ----------------------
md_dict = os.path.join(FOLDER_PATH, "field_dictionary.md")
dict_content = f"""# WOS 字段词典
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

| 字段 | 中文名称 | 核心用途 |
|------|----------|----------|
| AU | 作者 | 合作网络 |
| TI | 标题 | 文献标识 |
| PY | 年份 | 时间演化 |
| DE | 关键词 | 共现网络 |
| CR | 被引文献 | 共被引分析 |
| UT | 入藏号 | 去重依据 |

## 清洗配置
- 年份：{YEAR_MIN}-{YEAR_MAX}
- 剔除无关键词：{stat_empty_de}篇
- 剔除无作者：{stat_empty_au}篇
- 剔除无被引：{stat_empty_cr}篇
- 去重总数：{dup_total}篇
"""
with open(md_dict, "w", encoding="utf-8") as f:
    f.write(dict_content)
print("✅ 字段词典：field_dictionary.md")

print("\n==================== 完成 ====================")
print(f"最终保留文献：{final_total} 篇")
print(f"输出文件：{OUTPUT_WOS_TXT}")
