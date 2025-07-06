from collections import Counter

import pandas as pd

import pylab as plt
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.metrics import (brier_score_loss, precision_score, recall_score, f1_score, precision_recall_curve,
                             classification_report, confusion_matrix)

from sklearn.svm import LinearSVC
# 加载数据集


data = pd.read_excel('sentimen.xlsx', usecols=[0,1])
sentences = data['sentence'].tolist()
labels = data['label'].tolist()
labels_number = []
for i in labels:
    if i=='positive':
        labels_number.append(1)
    elif i=='negative':
        labels_number.append(0)


# 划分数据集为训练集和测试集
sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, labels_number, test_size=0.2, random_state=42)
print(Counter(labels_number))
# 把句子转化为特征向量
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(sentences_train)
X_test = vectorizer.transform(sentences_test)
# print(X_train)

# 训练一个支持向量机分类器

# 对测试集进行预测
model = LogisticRegression()
model.fit(X_train,y_train)
y_pred =model.predict(X_test)
# 输出模型的准确率、召回率和F1值
print(classification_report(y_test, y_pred))
print("\tPrecision: %1.3f" % precision_score(y_test, y_pred))
print("\tRecall: %1.3f" % recall_score(y_test, y_pred))
print("\tF1: %1.3f\n" % f1_score(y_test, y_pred))

# 绘制pr曲线
precision, recall, thresholds = precision_recall_curve(y_test, y_pred)
plt.figure(1)
plt.title('Pre Rec')
plt.plot(precision, recall)
plt.ylabel('Precision')
plt.xlabel('Recall')
plt.show()



#绘制混淆矩阵
matrix = confusion_matrix(y_test,y_pred)
plt.matshow(matrix, cmap=plt.cm.Reds)  # 根据最下面的图按自己需求更改颜色
# 更改横纵坐标的刻度
plt.xticks([0, 1], ['Success', 'Failure'])
plt.yticks([0, 1], ['Success', 'Failure'])
for i in range(len(matrix)):
    for j in range(len(matrix)):
        plt.annotate(matrix[j, i], xy=(i, j), horizontalalignment='center', verticalalignment='center')
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()