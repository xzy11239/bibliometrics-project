# Bibliometrics Project: AI-Assisted Diagnosis in Medical Imaging





## 项目信息





| 项目 | 内容 |


|:---|:---|


| **项目名称** | 人工智能辅助诊断的文献计量与知识图谱研究 |


| **研究方向** | 深度学习与人工智能在医学影像诊断中的应用 |


| **数据来源** | Web of Science Core Collection |


| **检索日期** | 2026-06-01 |


| **时间范围** | 2015-2026 |


| **分析工具** | VOSviewer 1.6.21 |


| **项目状态** | ✅ M1完成 | ✅ M2完成 | ✅ M3完成 |





---





## 团队信息





| 角色 | 姓名 | 职责分工 |


|:---|:---|:---|


| **组长（项目统筹）** | 许子怡 | 全面统筹项目全流程进度、协调各成员分工衔接、把控各阶段成果质量、审核项目所有产出文件、对接项目验收 |


| **成员（数据检索与清洗）** | 唐雨 | 完成WOS/CNKI数据库文献检索、全字段数据导出；搭建数据清洗流程，完成数据去重、缺失值检测、格式统一、无效数据筛选；梳理检索-筛选-清洗全流程，撰写并提交检索方案报告，管理原始与清洗后数据 |


| **成员（计量分析与可视化）** | 李镕辛 | 开展关键词共现、合作网络、被引频次等核心文献计量分析；运用VOSviewer/CiteSpace绘制专业可视化知识图谱；完成图谱与分析结果初步解读，整理图表及核心结论，提交计量分析产出报告 |


| **成员（报告撰写）** | 凌欣 | 整合项目所有研究成果，撰写并修改6-8页mini review；校对计量分析报告文字、数据、图表格式；梳理研究逻辑与核心结论，完善终稿内容排版与学术规范 |


| **成员（开源项目二次开发）** | 陈晓铭 | 完成项目相关开源工具/代码二次开发与优化；编写标准化可运行代码，保障项目成果可复现、结果可追溯；发布项目正式Release版本，配合完成终稿提交 |





---





## 项目计划与完成状态





### M1（数据检索与清洗）✅





- [x] 完成WOS/CNKI文献数据检索与导出，确保作者、标题、关键词、摘要等核心字段齐全


- [x] 完成数据清洗全流程（数据去重、缺失值检测、数据格式统一、无效数据剔除）


- [x] 跑通数据-检索-筛选全流程，优化操作逻辑，提交完整检索方案报告





### M2（计量分析与可视化）✅





- [x] 完成两个研究方向的核心计量分析（关键词共现、作者合作网络、文献被引分析）


- [x] 输出VOSviewer专业可视化图谱，完成图谱结果深度初步解读


- [x] 提交计量分析产出报告，包含完整可视化图表、核心分析结论与数据支撑





### M3（论文撰写与项目发布）✅





- [x] 完成6-8页mini review全文撰写、修改与学术规范优化


- [x] 完善项目代码、文档体系，提升项目可复现性，发布项目正式Release版本


- [x] 提交项目终稿（计量分析报告+mini review），确保所有代码一键运行、研究结果全程可追溯





---





## 检索式





```





TS=("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network" OR "radiomics" OR "AI-assisted diagnosis") 


AND 


TS=("clinical diagnosis" OR "medical diagnosis" OR "computer-aided diagnosis" OR "diagnostic imaging" OR "disease detection") 


AND 


PY=2015-2026 


AND 


(DT=Article OR DT=Review)


AND 


SU=(Medicine OR Radiology OR Pathology OR Oncology OR "General & Internal Medicine")





```





---





## 数据来源说明





| 项目 | 内容 |


|:---|:---|


| **数据库** | Web of Science核心合集 |


| **检索式版本** | `config/query.yaml` v1.0 |


| **导出时间** | 2026-06-01 |


| **导出参数** | 时间窗2015-2026，语言English，文献类型Article/Review，字段Title+Abstract+Keyword |


| **原始文件** | `data/raw/savedrecs.txt` |


| **原始数据量** | 3,771篇 |


| **清洗后数据量** | 3,748篇 |


| **核心字段** | 作者、机构、标题、年份、期刊、摘要、关键词、DOI、参考文献列表、被引次数 |





---





## 数据清洗规则





### 清洗日期


2026-06-01





### 清洗规则





| 步骤 | 规则 | 处理数量 |


|:---|:---|:---|


| 去重（主键） | DOI匹配 | 22条重复删除 |


| 去重（次键） | 标题匹配（DOI缺失时） | 0条 |


| 年份校验 | 异常年份（超出2015-2026） | 1条删除 |


| 文献类型过滤 | 非Article/Review | 0条 |


| **清洗后保留** | — | **3,748条** |





### 清洗结果





| 指标 | 数值 |


|:---|:---|


| 原始记录 | 3,771 |


| DOI重复 | 22 |


| 标题重复 | 0 |


| 年份异常 | 1 |


| 总去重/剔除 | 23 |


| **清洗后保留** | **3,748** |





### 使用的脚本


`src/clean_wos_data.py`





---





## 三图一表





### 图1：年度发文趋势图（RQ1）





- **文件路径**：`outputs/figures/fig1_annual_trend.png`


- **图注**：数据来源于Web of Science Core Collection（2015-2026）；分析单位为年度发文量；使用Excel生成；2026年数据因数据库收录延迟而不完整。


- **核心发现**：发文量连续快速增长，2022年为分野年





### 图2：作者合作网络图（RQ2）





- **文件路径**：`outputs/figures/fig2_author_network.png`


- **图注**：数据来源于Web of Science Core Collection（2015-2026）；分析单位为核心作者；使用VOSviewer 1.6.21生成；阈值为发文量≥10篇；节点大小代表发文量，连线代表合作，颜色代表不同聚类。


- **核心发现**：国内学者为主导，核心团队聚集，国际间合作有限





### 图3：关键词聚类网络图（RQ3）





- **文件路径**：`outputs/figures/fig3_keyword_clusters.png`


- **图注**：数据来源于Web of Science Core Collection（2015-2026）；分析单位为关键词；使用VOSviewer 1.6.21生成；阈值为词频≥15次；节点大小代表词频，连线粗细代表共现强度，颜色代表聚类。


- **核心发现**：分为算法、临床验证、应用场景三大聚类





### 图4：关键词时间演化图（RQ4）





- **文件路径**：`outputs/figures/fig4_keyword_temporal.png`


- **图注**：数据来源于Web of Science Core Collection（2015-2026）；分析单位为关键词；使用VOSviewer 1.6.21生成；颜色梯度代表关键词的平均出现年份（蓝紫→黄=早→晚）。


- **核心发现**：传统影像→机器学习→深度学习的演化路径





### 表1：Top 50高频关键词统计表（RQ3）





- **文件路径**：`outputs/tables/table1_top50_keywords.md`


- **核心发现**：deep learning（1165次）为绝对核心；肿瘤影像为最成熟应用场景





---





## 研究问题（RQ）与图表对应





| RQ | 研究问题 | 分析方法 | 对应图表 |


|:---|:---|:---|:---|


| **RQ1** | 发文趋势与发展阶段 | 时间序列分析 | 图1 |


| **RQ2** | 核心研究者与合作格局 | 作者共现分析 | 图2 |


| **RQ3** | 研究主题与聚类结构 | 关键词共现分析 | 图3、表1 |


| **RQ4** | 前沿方向与关键挑战 | 时间演化+文献综合分析 | 图4、表1 |





---





## 10篇代表文献（Table 1 in paper）





| # | 文献 | 对应RQ |


|:---|:---|:---|


| 1 | Hosny et al. (2018) *Nature Reviews Cancer* | RQ1 |


| 2 | Gillies et al. (2016) *Radiology* | RQ1 |


| 3 | Shin et al. (2016) *IEEE TMI* | RQ2 |


| 4 | Kim et al. (2022) *BMC Medical Imaging* | RQ2 |


| 5 | Park et al. (2018) *Radiology* | RQ3 |


| 6 | Byra et al. (2019) *Medical Physics* | RQ3 |


| 7 | Anthimopoulos et al. (2016) *IEEE TMI* | RQ3 |


| 8 | Chan et al. (2020) *Medical Physics* | RQ3 |


| 9 | De Fauw et al. (2018) *Nature Medicine* | RQ4 |


| 10 | Zech et al. (2018) *PLOS Medicine* | RQ4 |





---





## 目录结构





```





bibliometrics-project/


├── data/


│   ├── raw/                    # 原始WoS导出文件


│   ├── cleaned/                # 清洗后数据（3,748条）


│   └── query.md                # 完整检索式


├── src/


│   └── clean_wos_data.py       # 数据清洗脚本


├── outputs/


│   ├── figures/


│   │   ├── fig1_annual_trend.png


│   │   ├── fig2_author_network.png


│   │   ├── fig3_keyword_clusters.png


│   │   └── fig4_keyword_temporal.png


│   └── tables/


│       └── table1_top50_keywords.md


├── paper/


│   └── mini_review.md          # 论文终稿


├── presentation/               # 答辩PPT


├── reflection/                 # 个人反思记录


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


vosviewer (需单独安装)


```





数据清洗





```bash


python src/clean_wos_data.py --input data/raw/savedrecs.txt --output data/cleaned/


```





可视化分析





1. 打开VOSviewer 1.6.21


2. 导入 data/cleaned/ 目录下的清洗后数据


3. 设置参数：


   · 作者分析：阈值 ≥ 10篇


   · 关键词分析：阈值 ≥ 15次


4. 生成网络图并导出





---





AI使用说明





工具 用途 人工核验方式


ChatGPT 文献信息辅助提取 唐雨逐条核对原始WoS数据


ChatGPT 论文初稿撰写辅助 凌欣全文审核修改


ChatGPT 数据清洗代码生成 陈晓铭测试验证，手动抽查清洗结果


ChatGPT README与文档辅助 许子怡审核确认





声明：所有核心研究发现（计量图谱、数据分析、结论）均为团队原创。AI仅作为辅助工具使用。





详见：docs/ai_usage.md





---





项目验收清单





· M1：检索方案报告 + 清洗后数据


· M2：计量分析产出报告 + 可视化图谱


· M3：mini review终稿 + 可复现代码 + Release版本
