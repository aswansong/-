import jieba
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

from PIL import Image

# 读取文本文件
with open('tieba.txt','r',encoding='utf-8') as f:
    word_list = f.readlines()
_list = [s.strip() for s in word_list]
new_list = list(set(_list))
text = ''
for sentence in new_list:
    text+=sentence

with open('stopwords.txt','r',encoding='utf-8') as f:
    stopwords = f.read()
# 分词
words_ = [word for word in jieba.cut(text) if word not in stopwords]

# 统计词频
counter = Counter(words_)
most_common = counter.most_common(20)

# 将统计结果转换为矩阵形式
words = [w[0] for w in most_common]
freqs = [w[1] for w in most_common]
word_freqs = dict(zip(words, freqs))

matrix = np.zeros((len(words), len(words)))

for i in range(len(words)):
    for j in range(len(words)):
        if i == j:
            matrix[i, j] = freqs[i]
        else:
            word_i, word_j = words[i], words[j]
            co_freq = 0
            for sentence in text.split('\n'):
                if word_i in sentence and word_j in sentence:
                    co_freq += 1
            matrix[i, j] = co_freq

# 绘制热力图
font_path = "MuYuShiDeYi-2.ttf"
font = FontProperties(fname=font_path, size=10)

fig, ax = plt.subplots(figsize=(10,10))
im = ax.imshow(matrix)

# 设置x、y轴标签
ax.set_xticks(np.arange(len(words)))
ax.set_yticks(np.arange(len(words)))
ax.set_xticklabels(words,fontproperties=font)
ax.set_yticklabels(words,fontproperties=font)

# 在热力图上显示词频
for i in range(len(words)):
    for j in range(len(words)):
        if matrix[i, j] > 0:
            text = ax.text(j, i, int(matrix[i, j]), ha='center', va='center', color='white')

# 设置热力图的标题和颜色条
ax.set_title('Words Co-occurrence Matrix')
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Co-occurrence Frequency', rotation=-90, va='bottom')

# 显示热力图
plt.show()





# 统计词频
counter = Counter(words_)
most_common = counter.most_common(100)

# 将统计结果转换为矩阵形式
words = [w[0] for w in most_common]
freqs = [w[1] for w in most_common]
word_freqs2 = dict(zip(words, freqs))
# 绘制词云
wc = WordCloud(font_path='MuYuShiDeYi-2.ttf', width=800, height=600, background_color='white').generate_from_frequencies(word_freqs2)
plt.figure(figsize=(10,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
