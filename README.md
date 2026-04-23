# bibliometrics-project
 
团队信息
 
- 组长：许子怡（全面统筹项目全流程进度、协调各成员分工衔接、把控各阶段成果质量、审核项目所有产出文件、对接项目验收）
- 成员：
- 唐雨（负责检索与数据清洗：精准完成WOS/CNKI数据库文献检索、全字段数据导出；搭建数据清洗流程，完成数据去重、缺失值检测、格式统一、无效数据筛选；梳理检索-筛选-清洗全流程，撰写并提交检索方案报告，管理原始与清洗后数据）
- 李镕辛（负责计量分析与可视化：开展关键词共现、合作网络、被引频次等核心文献计量分析；运用VOSviewer/CiteSpace绘制专业可视化知识图谱；完成图谱与分析结果初步解读，整理图表及核心结论，提交计量分析产出报告）
- 凌欣（负责报告撰写：整合项目所有研究成果，撰写并修改6-8页mini review；校对计量分析报告文字、数据、图表格式；梳理研究逻辑与核心结论，完善终稿内容排版与学术规范）
- 陈晓铭（负责开源项目二次开发：完成项目相关开源工具/代码二次开发与优化；编写标准化可运行代码，保障项目成果可复现、结果可追溯；发布项目正式Release版本，配合完成终稿提交）
 
研究方向

人工智能辅助诊断的文献计量与知识图谱研究
 
项目计划
 
M1
 
- 完成WOS/CNKI文献数据检索与导出，确保作者、标题、关键词、摘要等核心字段齐全
- 完成数据清洗全流程（数据去重、缺失值检测、数据格式统一、无效数据剔除）
- 跑通数据-检索-筛选全流程，优化操作逻辑，提交完整检索方案报告
 
M2
 
- 完成两个研究方向的核心计量分析（关键词共现、作者/机构合作网络、文献被引分析）
- 输出VOSviewer/CiteSpace专业可视化图谱，完成图谱结果深度初步解读
- 提交计量分析产出报告，包含完整可视化图表、核心分析结论与数据支撑
 
M3
 
- 完成6-8页mini review全文撰写、修改与学术规范优化
- 完善项目代码、文档体系，提升项目可复现性，发布项目正式Release版本
- 提交项目终稿（计量分析报告+mini review），确保所有代码一键运行、研究结果全程可追溯
 
检索式
TS=("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network" OR "radiomics" OR "AI-assisted diagnosis") 
AND 
TS=("clinical diagnosis" OR "medical diagnosis" OR "computer-aided diagnosis" OR "diagnostic imaging" OR "disease detection") 
AND 
PY=2015-2026 
AND 
(DT=Article OR DT=Review)
AND 
SU=(Medicine OR Radiology OR Pathology OR Oncology OR "General & Internal Medicine")
 
数据来源说明
 
 1. 数据库：Web of Science核心合集
 2. 检索式版本：config/query.yaml v1.0
 3. 导出时间：2026-3-26 1:28
 4. 导出参数：时间窗2015-2025，语言English，文献类型Article/Review，字段Title+Abstract+Keyword
 5. 原始文件：data/raw/savedrecs (40).txt
 6. 数据量：3490篇
 7. 核心字段：作者、机构、标题、年份、期刊、摘要、关键词、DOI、参考文献列表、被引次数
