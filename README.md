```markdown
# Bibliometrics Project: AI-Assisted Diagnosis in Medical Imaging

## 项目信息

| 项目 | 内容 |
|------|------|
| **项目名称** | 人工智能辅助诊断的文献计量与知识图谱研究 |
| **研究方向** | 深度学习与人工智能在医学影像诊断中的应用 |
| **数据来源** | Web of Science Core Collection |
| **检索日期** | 2026-06-1 |
| **时间范围** | 2015-2026 |
| **分析工具** | VOSviewer 1.6.20 |
| **项目状态** | ✅ M1完成 | ✅ M2完成 | ✅ M3完成 |

---

## 团队信息

| 角色 | 姓名 | 职责分工 |
|------|------|----------|
| **组长（项目统筹）** | 许子怡 | 全面统筹项目全流程进度、协调各成员分工衔接、把控各阶段成果质量、审核项目所有产出文件、对接项目验收 |
| **成员（数据检索与清洗）** | 唐雨 | 完成WoS数据库文献检索、全字段数据导出；搭建数据清洗流程，完成数据去重、缺失值检测、格式统一、无效数据筛选；梳理检索-筛选-清洗全流程，撰写并提交检索方案报告，管理原始与清洗后数据 |
| **成员（计量分析与可视化）** | 李镕辛 | 开展关键词共现、合作网络、共被引等核心文献计量分析；运用VOSviewer绘制专业可视化知识图谱；完成图谱与分析结果初步解读，整理图表及核心结论，提交计量分析产出报告 |
| **成员（报告撰写）** | 陈晓铭 | 整合项目所有研究成果，撰写并修改mini review；校对计量分析报告文字、数据、图表格式；梳理研究逻辑与核心结论，完善终稿内容排版与学术规范 |
| **成员（开源项目二次开发）** | 凌欣 | 完成项目相关开源工具/代码二次开发与优化；编写标准化可运行代码，保障项目成果可复现、结果可追溯；发布项目正式Release版本，配合完成终稿提交 |

---

## 项目计划与完成状态

### M1（数据检索与清洗）✅

- [x] 完成WoS文献数据检索与导出，确保作者、标题、关键词、摘要等核心字段齐全
- [x] 完成数据清洗全流程（数据去重、缺失值检测、数据格式统一、无效数据剔除）
- [x] 跑通数据-检索-筛选全流程，优化操作逻辑，提交完整检索方案报告

### M2（计量分析与可视化）✅

- [x] 完成核心计量分析（关键词共现、作者合作网络、文献共被引分析）
- [x] 输出VOSviewer专业可视化图谱（聚类视图+时间演化视图），完成图谱结果深度解读
- [x] 提交计量分析产出报告，包含完整可视化图表、核心分析结论与数据支撑

### M3（论文撰写与项目发布）✅

- [x] 完成mini review全文撰写、修改与学术规范优化
- [x] 完善项目代码、文档体系，提升项目可复现性，发布项目正式Release版本
- [x] 提交项目终稿（计量分析报告+mini review），确保所有研究结果全程可追溯

---

## 检索式

```

TS = ("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network" OR "radiomics" OR "AI-assisted diagnosis") 
AND TS = ("clinical diagnosis" OR "medical diagnosis" OR "computer-aided diagnosis" OR "diagnostic imaging" OR "disease detection") 
AND PY=2015-2026 
AND (DT=Article OR DT=Review) 
AND SU=(Medicine OR Radiology OR Pathology OR Oncology OR "General & Internal Medicine")

```

---

## 数据来源说明

| 项目 | 内容 |
|------|------|
| **数据库** | Web of Science核心合集 |
| **检索式版本** | `config/query.yaml` v1.0 |
| **导出时间** | 2026-06-1 |
| **导出参数** | 时间窗2015-2026，语言English，文献类型Article/Review，字段Title+Abstract+Keyword |
| **原始数据量** | 3,771篇 |
| **去重后** | 3,766篇 |
| **清洗后数据量** | 3,504篇 |
| **核心字段** | 作者、机构、标题、年份、期刊、摘要、关键词、DOI、参考文献列表、被引次数 |

---

## 数据清洗规则

### 清洗日期
2026-06-1

### 清洗规则

| 步骤 | 规则 | 处理数量 |
|------|------|----------|
| 去重（主键） | DOI匹配 | 5篇重复删除 |
| 去重（次键） | 标题+作者匹配 | 0篇 |
| 无关键词 | 关键词字段缺失 | 255篇删除 |
| 无作者 | 作者字段缺失 | 1篇删除 |
| 无被引信息 | 被引次数缺失 | 6篇删除 |
| 年份异常 | 超出2015-2026 | 0篇 |
| **清洗后保留** | — | **3,504篇** |

### 清洗结果

| 指标 | 数值 |
|------|------|
| 原始记录 | 3,771 |
| 重复删除 | 5 |
| 无关键词删除 | 255 |
| 无作者删除 | 1 |
| 无被引删除 | 6 |
| **清洗后保留** | **3,504** |

### 使用的脚本
`src/clean_wos_data.py`

---

## 三图一表

### 图1：年发文趋势图（RQ1）

**文件路径**：

**图注**：数据来源于Web of Science Core Collection（2015-2026）；使用Python绘制；时间范围为2015-2026年；节点代表年份，纵轴代表发文量。

**核心发现**：发文量从2017年59篇增长至2025年700篇，增长约12倍，分为起步增长期（2017-2020，~60%年均增长）和快速扩张期（2021-2025，~14%年均增长）。

---

### 图2：作者合作网络图（RQ2）

**文件路径**：

**图注**：数据来源于Web of Science Core Collection（2015-2026）；分析单位为核心作者；使用VOSviewer 1.6.20生成；阈值为发文量≥6篇；节点大小代表发文量，颜色代表合作聚类，连线代表合作关系。

**核心发现**：已形成多个核心研究团队，团队内部合作紧密，但跨团队合作有限。


---

### 图3：关键词时间演化图（RQ3）

**文件路径**：

**图注**：数据来源于Web of Science Core Collection（2015-2026）；分析单位为核心关键词；使用VOSviewer 1.6.20生成；阈值为关键词出现次数≥30次；颜色梯度代表关键词的平均出现年份（蓝色=2021年前后，绿色=2022年前后，黄色=2023年前后）。

**核心发现**：三阶段演化——2021年（蓝色）：segmentation、CNN、U-Net；2022年（绿色）：deep learning、CT、MRI、COVID-19；2023年（黄色）：artificial intelligence、prognosis、biomarkers、survival。

---

### 图4：文献共被引网络图（RQ4）

**文件路径**：

**图注**：数据来源于Web of Science Core Collection（2015-2026）；分析单位为参考文献；使用VOSviewer 1.6.20生成；阈值为被引次数≥40次；节点大小代表被引频次，颜色代表共被引聚类。

**核心发现**：三大知识集群——Cluster A（U-Net，图像分割基础）、Cluster B（ResNet，深度表征学习）、Cluster C（Litjens综述、Esteva临床研究，领域综述与临床里程碑）。

---

### 图5：关键词聚类网络图（RQ2/RQ3）

**文件路径**：

**图注**：数据来源于Web of Science Core Collection（2015-2026）；分析单位为核心关键词；使用VOSviewer 1.6.20生成；阈值为关键词出现次数≥30次；聚类分辨率为1.0；节点大小代表关键词出现频次，颜色代表主题聚类，连线代表共现关系。

**核心发现**：分为三大聚类——红色（技术与方法层：deep learning、CNN、U-Net）、蓝绿色（影像与疾病分析层：MRI、CT、radiomics、prognosis）、黄色（临床应用层：computer-aided diagnosis、breast cancer、ultrasound）。

---

### 表1：高被引代表文献（RQ4）

| First Author | Year | Source | Core Contribution | Citations | Total Link Strength |
|--------------|------|--------|-------------------|-----------|---------------------|
| Ronneberger O | 2015 | LNCS | U-Net for biomedical segmentation | 466 | 1,927 |
| He KM | 2016 | CVPR | ResNet residual learning | 445 | 2,077 |
| Simonyan K | 2015 | arXiv | VGG deep convolutional networks | 236 | 1,202 |
| LeCun Y | 2015 | Nature | Deep learning perspective | 220 | 892 |
| Litjens G | 2017 | Med Image Anal | Deep learning in medical image analysis | 220 | 1,058 |
| Sung H | 2021 | CA Cancer J Clin | Global cancer statistics | 199 | 530 |
| Huang G | 2017 | CVPR | DenseNet | 171 | 1,038 |
| Selvaraju RR | 2020 | IJCV | Grad-CAM explainability | 169 | 633 |
| Esteva A | 2017 | Nature | Skin cancer classification | 153 | 586 |
| Gillies RJ | 2016 | Radiology | Radiomics | 153 | 496 |

**文件路径**：

**核心发现**：知识基础由三大支柱构成——分割架构（U-Net）、深度表征学习（ResNet）、领域综述与临床验证（Litjens、Esteva）。

---

## 研究问题（RQ）与图表对应

| RQ | Research Question | Analytical Method | Corresponding Figure/Table |
|----|-------------------|-------------------|---------------------------|
| RQ1 | 该领域文献数量如何变化？（发展态势） | 时间序列分析 | Figure 1 |
| RQ2 | 核心作者和研究团队呈现怎样的合作格局？ | 作者合作网络分析 | Figure 3 |
| RQ3 | 研究热点集中在哪些主题？如何演化？ | 关键词共现分析（聚类+时间演化） | Figure 2, Figure 5 |
| RQ4 | 领域知识基础由哪些核心文献构成？ | 文献共被引分析 | Figure 4, Table 1 |

---

## 目录结构

```

bibliometrics-project/
├── data/
│   ├── raw/                    # 原始WoS导出文件（3,771条）
│   ├── cleaned/                # 清洗后数据（3,504条）
│   └── screening_records.csv   # 筛选记录
├── src/
│   └── clean_wos_data.py       # 数据清洗脚本
├── outputs/
│   ├── figures/
│   │   ├── Figure_1.png        # 年发文趋势图
│   │   ├── Figure_2.png        # 关键词聚类网络图
│   │   ├── Figure_3.png        # 作者合作网络图
│   │   ├── Figure_4.png        # 文献共被引网络图
│   │   └── Figure_5.png        # 关键词时间演化图
│   └── tables/
│       └── Table_1.csv         # 高被引代表文献表
├── paper/
│   └── manuscript.docx         # 论文终稿
├── presentation/               # 答辩PPT
├── docs/
│   └── ai_usage.md             # AI使用说明
├── config/
│   └── query.yaml              # 检索式配置文件
└── README.md                   # 本文件

```

---

## 运行说明

### 环境要求

```bash
Python 3.8+
pandas
vosviewer 1.6.20（需单独安装）
```

数据清洗

```bash
python src/clean_wos_data.py --input data/raw/ --output data/cleaned/
```

可视化分析

1. 打开 VOSviewer 1.6.20
2. 导入 data/cleaned/ 目录下的清洗后数据
3. 设置参数：
   · 作者合作分析：阈值 ≥ 6篇
   · 关键词共现分析：阈值 ≥ 30次
   · 文献共被引分析：阈值 ≥ 40次
   · 聚类分辨率：1.0
4. 生成网络图并导出至 outputs/figures/

---

AI使用说明

本手稿在人工智能辅助下完成语言润色、参考文献格式化及初步文献整理工作，具体遵循 BIBGT 方法论中关于迭代式文献综述构建的指导原则[6]。所有分析决策、解读结果及结论均由作者独立完成。

---

项目验收清单

· M1：检索方案报告 + 清洗后数据
· M2：计量分析产出报告 + 可视化图谱（5图1表）
· M3：mini review终稿 + 可复现代码 + Release版本

---

