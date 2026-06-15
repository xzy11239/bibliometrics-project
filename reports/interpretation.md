# 三图一表图表解释

## 图1：年发文趋势图（对应RQ1）

### 图表基本信息

| 项目 | 内容 |
|:---|:---|
| **图号** | Figure 1 |
| **图类型** | 年发文量折线图 |
| **对应RQ** | RQ1（发展态势） |
| **数据来源** | Web of Science Core Collection |
| **时间范围** | 2015-2026 |
| **分析工具** | Python |

### 视觉元素说明

| 视觉元素 | 含义 |
|:---|:---|
| **横轴** | 年份（2015-2026） |
| **纵轴** | 年发文量（篇） |
| **折线** | 发文量变化趋势 |

### 核心发现（Claim-Evidence-Reasoning）

| Claim | Evidence | Reasoning |
|:---|:---|:---|
| 该领域研究热度持续上升 | 年发文量从2017年59篇增长至2025年700篇，增长约12倍 | 深度学习技术在医学影像领域的快速渗透推动了研究规模扩张 |
| 领域发展可分为两个阶段 | 2017-2020年（~60%年均增长）为起步增长期；2021-2025年（~14%年均增长）为快速扩张期 | 第一阶段以技术验证为主，第二阶段转向临床应用驱动 |
| 2026年数据回落不影响结论 | 2026年数据仅收录至6月，全年预计约600篇 | 数据库索引延迟是正常现象，不代表热度下降 |

---

## 图2：作者合作网络图（对应RQ2）

### 图表基本信息

| 项目 | 内容 |
|:---|:---|
| **图号** | Figure 2 |
| **图类型** | 作者合作网络图 |
| **对应RQ** | RQ2（合作格局） |
| **数据来源** | Web of Science Core Collection (2015-2026) |
| **分析工具** | VOSviewer 1.6.20 |
| **阈值参数** | 作者发文量 ≥ 6篇 |
| **聚类分辨率** | 1.0 |

### 视觉元素说明

| 视觉元素 | 含义 |
|:---|:---|
| **节点大小** | 作者发文总量（越大表示产出越高） |
| **连线** | 作者之间的合作关系 |
| **连线粗细** | 合作强度（越粗表示合作越频繁） |
| **颜色** | 不同合作聚类，代表不同的研究团队 |

### 核心发现（Claim-Evidence-Reasoning）

| Claim | Evidence | Reasoning |
|:---|:---|:---|
| 已形成多个核心研究团队 | 图中存在多个密集连接的节点集群 | 领域已经进入稳定发展阶段，团队化研究成为常态 |
| 团队内部合作紧密 | 同一颜色聚类内连线密集 | 研究人员倾向于与固定团队长期合作 |
| 跨团队合作有限 | 不同颜色聚类之间连线稀疏 | 跨机构、跨国别的合作仍有较大提升空间 |

---

## 图3：关键词共现聚类图（对应RQ3）

### 图表基本信息

| 项目 | 内容 |
|:---|:---|
| **图号** | Figure 3 |
| **图类型** | 关键词共现聚类网络图 |
| **对应RQ** | RQ3（研究热点主题结构） |
| **数据来源** | Web of Science Core Collection (2015-2026) |
| **分析工具** | VOSviewer 1.6.20 |
| **阈值参数** | 关键词出现次数 ≥ 30次 |
| **聚类分辨率** | 1.0 |

### 视觉元素说明

| 视觉元素 | 含义 |
|:---|:---|
| **节点大小** | 关键词出现频次（越大表示研究热度越高） |
| **连线** | 关键词共现关系 |
| **连线粗细** | 共现强度（越粗表示关联越紧密） |
| **颜色** | 主题聚类，同色代表相近研究方向 |

### 三大聚类详细解释

| 颜色 | 主题名称 | 核心关键词 | 研究内容 |
|:---|:---|:---|:---|
| **红色** | 技术与方法层 | deep learning, convolutional neural network, U-net, transfer learning, image segmentation, feature extraction | 深度学习模型架构与核心算法，是领域的技术底座 |
| **蓝绿色** | 影像与疾病分析层 | machine learning, diagnostic imaging, MRI, CT, radiomics, prognosis, biomarkers | 多模态影像处理、影像组学、疾病预后预测，连接技术与临床的桥梁 |
| **黄色** | 临床应用层 | computer-aided diagnosis, breast cancer, ultrasound, mammography, thyroid nodule | 计算机辅助诊断在乳腺疾病、甲状腺结节等场景的直接应用 |

### 核心发现（Claim-Evidence-Reasoning）

| Claim | Evidence | Reasoning |
|:---|:---|:---|
| 深度学习是领域核心技术底座 | deep learning是图中最大节点，连线最密集 | 绝大多数研究都围绕深度学习展开 |
| 三大聚类形成清晰层级 | 红色（技术）→ 蓝绿色（影像分析）→ 黄色（临床应用） | 研究从技术方法到临床应用的链条完整 |
| 乳腺癌是当前最活跃的临床场景 | breast cancer与computer-aided diagnosis、ultrasound、mammography连线紧密 | 乳腺影像AI诊断是临床转化最成熟的领域 |
| 研究正向预后预测延伸 | prognosis、biomarkers、survival出现在蓝绿色聚类中 | 领域不满足于疾病分类，开始关注结局预测 |

---

## 图4：关键词时间演化图（对应RQ3）

### 图表基本信息

| 项目 | 内容 |
|:---|:---|
| **图号** | Figure 4 |
| **图类型** | 关键词时间叠加演化图（Overlay Visualization） |
| **对应RQ** | RQ3（主题演化） |
| **数据来源** | Web of Science Core Collection (2015-2026) |
| **分析工具** | VOSviewer 1.6.20 |
| **阈值参数** | 关键词出现次数 ≥ 30次 |

### 视觉元素说明

| 视觉元素 | 含义 |
|:---|:---|
| **颜色（蓝→绿→黄）** | 关键词平均出现年份（蓝色=2021前，绿色=2022，黄色=2023后） |
| **节点大小** | 关键词出现频次 |
| **连线** | 共现关系 |

### 三阶段演化过程

| 阶段 | 颜色 | 代表关键词 | 时间范围 | 研究特征 |
|:---|:---|:---|:---|:---|
| **第一阶段** | 蓝色 | segmentation, convolutional neural network, U-net, lesions | 约2021年 | 图像分割和基础模型优化，技术导向明显 |
| **第二阶段** | 绿色 | deep learning, machine learning, CT, MRI, COVID-19 | 约2022年 | 技术应用爆发，多模态影像+疫情研究 |
| **第三阶段** | 黄色 | artificial intelligence, prognosis, biomarkers, survival | 约2023年 | 临床转化，预后预测和生物标志物挖掘 |

### 核心发现（Claim-Evidence-Reasoning）

| Claim | Evidence | Reasoning |
|:---|:---|:---|
| 研究重心从技术方法向临床价值转移 | 蓝色节点（分割/CNN）→ 黄色节点（预后/生物标志物） | 领域不再只关注模型准确率，更关注临床实际问题 |
| 多模态影像研究贯穿始终 | CT、MRI、ultrasound覆盖蓝、绿、黄三个阶段 | 多模态影像分析是持续活跃的方向 |
| 热点概念从深度学习向AI迭代 | deep learning（绿色，2022峰值）→ artificial intelligence（黄色，2023上升） | 讨论从具体技术扩展到更宽泛的AI框架 |

---

## 图5：文献共被引网络图（对应RQ4）

### 图表基本信息

| 项目 | 内容 |
|:---|:---|
| **图号** | Figure 5 |
| **图类型** | 文献共被引网络图 |
| **对应RQ** | RQ4（知识基础） |
| **数据来源** | Web of Science Core Collection (2015-2026) |
| **分析工具** | VOSviewer 1.6.20 |
| **阈值参数** | 文献被引次数 ≥ 40次 |

### 视觉元素说明

| 视觉元素 | 含义 |
|:---|:---|
| **节点大小** | 文献被引频次（越大表示影响力越高） |
| **连线** | 共被引关系 |
| **颜色** | 共被引聚类，同色代表相近的知识基础 |

### 三大知识聚类

| 聚类 | 核心文献 | 贡献 |
|:---|:---|:---|
| **Cluster A** | Ronneberger U-Net (2015) | 生物医学图像分割的里程碑架构 |
| **Cluster B** | He ResNet (2016) | 深度残差学习，解决深层网络退化问题 |
| **Cluster C** | Litjens survey (2017); Esteva (2017) | 领域系统性综述 + 临床里程碑研究 |

### 核心发现（Claim-Evidence-Reasoning）

| Claim | Evidence | Reasoning |
|:---|:---|:---|
| U-Net和ResNet是领域两大知识支柱 | 二者节点最大，位于网络中心 | 分割架构和表征学习是AI辅助诊断的技术基石 |
| 三大聚类之间连线密集 | 不同颜色聚类间存在大量共被引关系 | 技术方法、领域综述、临床验证形成一体化知识体系 |
| ResNet是最核心的文献 | 被引445次，总链接强度2,077（最高） | 残差网络是深度学习在医学领域广泛应用的关键突破 |

---

## 表1：高被引代表文献（对应RQ4）

### 表格基本信息

| 项目 | 内容 |
|:---|:---|
| **表号** | Table 1 |
| **表类型** | 高被引文献汇总表 |
| **对应RQ** | RQ4（知识基础） |
| **数据来源** | Web of Science Core Collection |
| **筛选标准** | 检索结果中引用频次最高 |

### 10篇代表文献

| First Author | Year | Source | Core Contribution | Citations | Total Link Strength |
|:---|:---|:---|:---|:---|:---|
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

### 三大支柱解读

| 支柱 | 代表文献 | 作用 |
|:---|:---|:---|
| **分割架构** | Ronneberger U-Net (2015) | 提供医学图像分割的技术范式 |
| **深度表征学习** | He ResNet (2016) | 解决深层网络训练难题，成为骨干网络 |
| **领域综述与临床验证** | Litjens (2017); Esteva (2017) | 梳理领域进展，证明AI临床可达性能 |

### 核心发现（Claim-Evidence-Reasoning）

| Claim | Evidence | Reasoning |
|:---|:---|:---|
| 知识基础由三大支柱构成 | U-Net、ResNet、Litjens/Esteva分别代表分割、表征学习、临床验证 | 技术方法与临床验证相互支撑，形成完整知识体系 |
| ResNet是链接强度最高的文献 | Total link strength = 2,077（最高） | 残差网络在知识网络中处于最中心位置 |
| 高被引文献集中2015-2017年 | 10篇中有7篇发表于2015-2017 | 领域核心知识在早期已奠定 |

---

## 三图一表关联总结

| 图表 | 对应RQ | 核心问题 | 关键结论 |
|:---|:---|:---|:---|
| Figure 1 | RQ1 | 发展态势如何？ | 2017-2025年增长12倍，两阶段发展 |
| Figure 2 | RQ2 | 合作格局如何？ | 核心团队形成，跨团队合作有限 |
| Figure 3 | RQ3 | 研究热点有哪些？ | 三大聚类：技术/影像分析/临床应用 |
| Figure 4 | RQ3 | 热点如何演化？ | 技术→应用→临床，三阶段转移 |
| Figure 5 | RQ4 | 知识基础是什么？ | U-Net、ResNet、Litjens/Esteva三大支柱 |
| Table 1 | RQ4 | 哪些文献最具影响力？ | 10篇高被引文献，构成领域知识骨架 |

---
