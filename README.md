# 百度贴吧（孙吧）舆情分析项目

## 项目简介

本项目旨在对百度贴吧特定主题（以“孙吧”或“抗压背锅吧”为例）的帖子进行舆情分析。整个流程包括从贴吧自动抓取帖子标题、使用预训练的深度学习模型进行情感标注、生成词云和共现矩阵进行可视化分析，并最终使用多种机器学习模型进行情感分类任务。

## 项目特点

- **自动化数据采集**: 自动爬取百度贴吧的帖子标题作为分析语料。
- **智能化情感标注**: 利用 `transformers` 库中的预训练模型对文本数据进行正/负向情感标注。
- **多维度文本可视化**:
    - 生成高频词**词云**，直观展示热点话题。
    - 创建**词语共现热力图**，分析话题之间的关联性。
- **多样化分类模型**:
    - 实现了**逻辑回归 (Logistic Regression)**、**支持向量机 (SVM)** 和**随机森林 (Random Forest)** 三种经典的机器学习分类器。
    - 对每个模型都进行了性能评估，并绘制了**PR曲线**和**混淆矩阵**。

## 项目工作流程

1.  **数据抓取 (`tieba.py`)**:
    - 运行此脚本，它会访问百度贴吧“抗压背锅吧”，并爬取指定页数范围内的所有帖子标题。
    - 抓取到的标题数据被保存在 `tieba.txt` 文件中。

2.  **数据处理与情感标注 (`data_deal.py`)**:
    - 脚本读取原始文本数据（在代码中为 `train_yao.csv`，可以修改为读取 `tieba.txt`）。
    - 使用 `liam168/c2-roberta-base-finetuned-dianping-chinese` 这个预训练模型对每一条标题进行情感倾向预测（正面/负面）。
    - 将标题和预测的标签（1为正面，0为负面）保存到 `sentimen.xlsx` 文件中，作为后续模型训练的数据集。

3.  **数据可视化 (`word_cloud.py`)**:
    - 读取 `tieba.txt` 中的文本数据。
    - 使用 `jieba` 进行中文分词，并去除停用词。
    - 基于词频生成词云图 (`wordcloud`)。
    - 计算高频词之间的共现频率，并绘制成热力图 (`heatmap`)。

4.  **模型训练与评估 (`LR.py`, `SVM.py`, `RF.py`)**:
    - 三个脚本分别对应逻辑回归、支持向量机和随机森林模型。
    - 它们会读取 `sentimen.xlsx` 中已标注好的数据。
    - 使用 `TfidfVectorizer` 将文本转换为特征向量。
    - 划分训练集和测试集，训练分类模型。
    - 输出详细的分类报告（准确率、精确率、召回率、F1值），并绘制PR曲线和混淆矩阵以评估模型性能。

## 如何使用

1.  **安装依赖**:
    确保你已经安装了所有必需的 Python 库。你可以使用 pip 来安装：
    ```bash
    pip install requests beautifulsoup4 transformers torch openpyxl jieba-py wordcloud matplotlib scikit-learn pandas numpy html5lib
    ```

2.  **运行脚本**:
    按照以下顺序执行脚本：

    a. **抓取数据**:
       ```bash
       python tieba.py
       ```
       这会生成 `tieba.txt` 文件。

    b. **处理和标注数据**:
       在 `data_deal.py` 中，确保输入文件路径正确（例如，修改代码以读取 `tieba.txt`），然后运行：
       ```bash
       python data_deal.py
       ```
       这会生成带有情感标签的 `sentimen.xlsx` 文件。

    c. **生成可视化图表**:
       ```bash
       python word_cloud.py
       ```
       此脚本会显示词云和词语共现热力图。

    d. **训练和评估模型**:
       分别运行三个模型脚本来查看不同的分类结果：
       ```bash
       python LR.py
       python SVM.py
       python RF.py
       ```

## 文件结构

```
.
├── tieba.py            # 贴吧爬虫脚本
├── data_deal.py        # 数据处理与情感标注脚本
├── word_cloud.py       # 词云与共现矩阵生成脚本
├── LR.py               # 逻辑回归模型脚本
├── SVM.py              # 支持向量机模型脚本
├── RF.py               # 随机森林模型脚本
├── tieba.txt           # (生成) 爬取到的原始数据
├── sentimen.xlsx       # (生成) 标注后的情感数据
├── stopwords.txt       # (需要) 停用词词典
└── README.md           # 项目说明文件
```

> **注意**: `stopwords.txt` 文件需要您预先准备，其中包含在进行文本分析时希望忽略的词语（如“的”、“是”等）。
