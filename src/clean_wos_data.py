#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WoS文献数据清洗脚本（简化版）
功能：合并、去重、统计缺失率
"""

import pandas as pd
import numpy as np
import os
import re
from pathlib import Path
from datetime import datetime

# ==================== 配置参数 ====================
DATA_DIR = "."  # txt文件所在目录
OUTPUT_DIR = "cleaned_data"  # 输出目录
REPORT_DIR = "reports"  # 报告目录

# ==================== 读取WoS txt文件 ====================
def parse_wos_txt(filepath):
    """
    解析WoS导出的纯文本文件
    返回每条记录的字典列表
    """
    records = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 按 "ER" 记录结束符分割
    raw_records = re.split(r'\nER\n', content)
    
    for raw in raw_records:
        if not raw.strip():
            continue
        
        record = {}
        lines = raw.strip().split('\n')
        
        for line in lines:
            if len(line) < 2:
                continue
            
            tag = line[:2]
            value = line[2:].strip()
            
            if tag == 'PT':
                record['PT'] = value
            elif tag == 'AU':
                if 'AU' not in record:
                    record['AU'] = []
                record['AU'].append(value)
            elif tag == 'TI':
                record['TI'] = value
            elif tag == 'SO':
                record['SO'] = value
            elif tag == 'DE':
                if 'DE' not in record:
                    record['DE'] = []
                record['DE'].append(value)
            elif tag == 'ID':
                if 'ID' not in record:
                    record['ID'] = []
                record['ID'].append(value)
            elif tag == 'AB':
                record['AB'] = value
            elif tag == 'C1':
                record['C1'] = value
            elif tag == 'CR':
                if 'CR' not in record:
                    record['CR'] = []
                record['CR'].append(value)
            elif tag == 'PY':
                record['PY'] = value
            elif tag == 'TC':
                record['TC'] = value
            elif tag == 'DT':
                record['DT'] = value
            elif tag == 'DI':
                record['DI'] = value
            elif tag == 'VL':
                record['VL'] = value
            elif tag == 'IS':
                record['IS'] = value
            elif tag == 'BP':
                record['BP'] = value
        
        record['AU_count'] = len(record.get('AU', []))
        record['CR_count'] = len(record.get('CR', []))
        record['DE_count'] = len(record.get('DE', []))
        
        records.append(record)
    
    print(f"  读取 {filepath}: {len(records)} 条记录")
    return records

# ==================== 转换为DataFrame ====================
def records_to_dataframe(records):
    rows = []
    for rec in records:
        row = {}
        for key, value in rec.items():
            if key in ['AU', 'DE', 'ID', 'CR']:
                if isinstance(value, list):
                    row[key] = '; '.join(value)
                else:
                    row[key] = value
            else:
                row[key] = value
        rows.append(row)
    
    df = pd.DataFrame(rows)
    
    rename_map = {
        'PT': 'Doc_Type',
        'AU': 'Authors',
        'TI': 'Title',
        'SO': 'Journal',
        'DE': 'Author_Keywords',
        'ID': 'Keywords_Plus',
        'AB': 'Abstract',
        'C1': 'Author_Address',
        'CR': 'References',
        'PY': 'Year',
        'TC': 'Times_Cited',
        'DT': 'Doc_Type_Detail',
        'DI': 'DOI',
        'VL': 'Volume',
        'IS': 'Issue',
        'BP': 'Page_Start'
    }
    df = df.rename(columns=rename_map)
    
    return df

# ==================== 数据清洗函数（不过滤文献类型）====================
def clean_data(df):
    original_count = len(df)
    
    # 1. 基于DOI去重
    df['DOI_clean'] = df['DOI'].str.upper().str.strip()
    df['is_duplicate_doi'] = df['DOI_clean'].duplicated(keep='first')
    
    # 对于没有DOI的，基于Title去重
    df['Title_clean'] = df['Title'].str.lower().str.strip()
    df['is_duplicate_title'] = df['Title_clean'].duplicated(keep='first')
    
    # 综合去重判断
    df['is_duplicate'] = df['is_duplicate_doi'] | (df['DOI_clean'].isna() & df['is_duplicate_title'])
    
    # 2. 过滤异常年份（不过滤文献类型了）
    current_year = datetime.now().year
    df['Year_num'] = pd.to_numeric(df['Year'], errors='coerce')
    mask_year_valid = df['Year_num'].between(1900, current_year + 5)
    
    # 应用过滤（只去重和过滤年份）
    df_clean = df[~df['is_duplicate'] & mask_year_valid].copy()
    
    cleaned_count = len(df_clean)
    
    print(f"\n清洗统计：")
    print(f"  原始记录: {original_count}")
    print(f"  DOI重复: {df['is_duplicate_doi'].sum()}")
    print(f"  Title重复: {df[df['DOI_clean'].isna()]['is_duplicate_title'].sum()}")
    print(f"  总重复: {df['is_duplicate'].sum()}")
    print(f"  被过滤的异常年份: {(~mask_year_valid & ~df['Year'].isna()).sum()}")
    print(f"  清洗后保留: {cleaned_count}")
    
    return df_clean

# ==================== 生成质量报告 ====================
def generate_quality_report(df_original, df_clean, output_path):
    report_lines = []
    report_lines.append("# WoS 数据质量报告\n")
    report_lines.append(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    report_lines.append("## 1. 数据概览\n")
    report_lines.append("| 指标 | 数值 |")
    report_lines.append("|------|------|")
    report_lines.append(f"| 原始记录数 | {len(df_original)} |")
    report_lines.append(f"| 去重后记录数 | {len(df_original) - df_original['is_duplicate'].sum()} |")
    report_lines.append(f"| 过滤异常年份后 | {len(df_clean)} |")
    report_lines.append(f"| **最终保留数** | **{len(df_clean)}** |\n")
    
    report_lines.append("## 2. 字段缺失率统计\n")
    report_lines.append("| 字段 | 缺失数量 | 缺失率 |")
    report_lines.append("|------|----------|--------|")
    
    fields = ['DOI', 'Abstract', 'Author_Keywords', 'References', 'Authors', 'Journal', 'Year', 'Times_Cited']
    for field in fields:
        if field in df_clean.columns:
            missing = df_clean[field].isna().sum()
            rate = missing / len(df_clean) * 100 if len(df_clean) > 0 else 0
            report_lines.append(f"| {field} | {missing} | {rate:.2f}% |")
        else:
            report_lines.append(f"| {field} | N/A | N/A |")
    
    report_lines.append("\n## 3. 文献类型分布（原始）\n")
    if 'Doc_Type' in df_original.columns:
        doc_counts = df_original['Doc_Type'].value_counts()
        report_lines.append("| 文献类型 | 数量 |")
        report_lines.append("|----------|------|")
        for dt, cnt in doc_counts.head(10).items():
            report_lines.append(f"| {dt} | {cnt} |")
    
    report_lines.append("\n## 4. 文献年份分布（清洗后）\n")
    if len(df_clean) > 0 and 'Year_num' in df_clean.columns:
        year_counts = df_clean['Year_num'].value_counts().sort_index()
        report_lines.append("| 年份 | 数量 |")
        report_lines.append("|------|------|")
        for year, cnt in year_counts.items():
            report_lines.append(f"| {int(year)} | {cnt} |")
    
    report_lines.append("\n## 5. 关键异常值\n")
    report_lines.append(f"- 无DOI记录数: {df_clean['DOI'].isna().sum() if len(df_clean) > 0 else 0}")
    report_lines.append(f"- 无摘要记录数: {df_clean['Abstract'].isna().sum() if len(df_clean) > 0 else 0}")
    report_lines.append(f"- 无关键词记录数: {df_clean['Author_Keywords'].isna().sum() if len(df_clean) > 0 else 0}")
    report_lines.append(f"- 无参考文献记录数: {df_clean['References'].isna().sum() if len(df_clean) > 0 else 0}")
    
    if len(df_clean) > 0 and 'Times_Cited' in df_clean.columns:
        tc = pd.to_numeric(df_clean['Times_Cited'], errors='coerce')
        report_lines.append(f"\n### 被引频次统计")
        report_lines.append(f"- 均值: {tc.mean():.2f}")
        report_lines.append(f"- 中位数: {tc.median():.2f}")
        report_lines.append(f"- 最大值: {tc.max():.0f}")
        report_lines.append(f"- 0被引记录数: {(tc == 0).sum()}")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"\n质量报告已保存: {output_path}")

# ==================== 保存清洗后的数据 ====================
def save_cleaned_data(df_clean):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    csv_path = os.path.join(OUTPUT_DIR, 'wos_cleaned.csv')
    df_clean.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"CSV已保存: {csv_path}")
    
    excel_path = os.path.join(OUTPUT_DIR, 'wos_cleaned.xlsx')
    try:
        df_clean.to_excel(excel_path, index=False, engine='openpyxl')
        print(f"Excel已保存: {excel_path}")
    except:
        print(f"Excel保存失败（可能需要安装openpyxl: pip install openpyxl）")
    
    return csv_path

# ==================== 主函数 ====================
def main():
    print("=" * 50)
    print("WoS 文献数据清洗工具（简化版）")
    print("=" * 50)
    
    txt_files = list(Path(DATA_DIR).glob("*.txt"))
    wos_files = [f for f in txt_files if not f.name.startswith("~")]
    
    if not wos_files:
        print("错误：未找到任何 .txt 文件")
        return
    
    print(f"\n找到 {len(wos_files)} 个txt文件:")
    for f in wos_files:
        print(f"  - {f.name}")
    
    print("\n正在解析WoS文件...")
    all_records = []
    for filepath in wos_files:
        records = parse_wos_txt(str(filepath))
        all_records.extend(records)
    
    print(f"\n总计读取: {len(all_records)} 条记录")
    
    print("\n正在转换为DataFrame...")
    df_raw = records_to_dataframe(all_records)
    print(f"字段列表: {list(df_raw.columns)}")
    
    print("\n正在清洗数据...")
    
    # 添加Year_num列用于后续
    df_raw['Year_num'] = pd.to_numeric(df_raw['Year'], errors='coerce')
    
    df_clean = clean_data(df_raw)
    
    print("\n正在生成质量报告...")
    os.makedirs(REPORT_DIR, exist_ok=True)
    generate_quality_report(df_raw, df_clean, os.path.join(REPORT_DIR, 'data_quality.md'))
    
    print("\n正在保存数据...")
    save_cleaned_data(df_clean)
    
    # 创建field_dictionary.md
    field_dict_path = os.path.join(REPORT_DIR, 'field_dictionary.md')
    with open(field_dict_path, 'w', encoding='utf-8') as f:
        f.write("# WoS 字段字典\n\n")
        f.write("| 字段名 | 原始标签 | 说明 |\n")
        f.write("|--------|----------|------|\n")
        f.write("| Doc_Type | PT | 文献类型 |\n")
        f.write("| Authors | AU | 作者列表（分号分隔） |\n")
        f.write("| Title | TI | 文献标题 |\n")
        f.write("| Journal | SO | 来源期刊 |\n")
        f.write("| Author_Keywords | DE | 作者提供的关键词 |\n")
        f.write("| Keywords_Plus | ID | WoS自动生成的关键词 |\n")
        f.write("| Abstract | AB | 摘要内容 |\n")
        f.write("| Author_Address | C1 | 作者机构地址 |\n")
        f.write("| References | CR | 参考文献列表 |\n")
        f.write("| Year | PY | 出版年份 |\n")
        f.write("| Times_Cited | TC | 总被引频次 |\n")
        f.write("| DOI | DI | 数字对象标识符 |\n")
        f.write("| Volume | VL | 卷号 |\n")
        f.write("| Issue | IS | 期号 |\n")
        f.write("| Page_Start | BP | 起始页码 |\n")
    print(f"字段字典已保存: {field_dict_path}")
    
    os.makedirs('data', exist_ok=True)
    readme_path = 'data/README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# WoS 文献数据集\n\n")
        f.write(f"## 基本信息\n\n")
        f.write(f"- **导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **原始记录数**: {len(df_raw)}\n")
        f.write(f"- **清洗后记录数**: {len(df_clean)}\n")
        if len(df_clean) > 0:
            f.write(f"- **年份范围**: {int(df_clean['Year_num'].min())} - {int(df_clean['Year_num'].max())}\n")
        f.write(f"\n## 文件说明\n\n")
        f.write(f"- `cleaned_data/wos_cleaned.csv` - 清洗后的数据（CSV格式）\n")
        f.write(f"- `cleaned_data/wos_cleaned.xlsx` - 清洗后的数据（Excel格式）\n")
        f.write(f"- `reports/data_quality.md` - 数据质量详细报告\n")
        f.write(f"- `reports/field_dictionary.md` - 字段字典\n")
    print(f"数据README已保存: {readme_path}")
    
    print("\n" + "=" * 50)
    print("清洗完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()