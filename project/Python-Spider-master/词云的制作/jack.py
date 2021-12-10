
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

#1.读出歌词
text = open('jack.txt','r',encoding='utf-8').read()
#2.把歌词剪开
cut_text = jieba.cut(text)
# print(type(cut_text))
# print(next(cut_text))
# print(next(cut_text))
#3.以空格拼接起来
result = " ".join(cut_text)
# print(result)
# 4.生成词云
wc = WordCloud(
    font_path='simhei.ttf',     #字体路劲
    background_color='white',   #背景颜色
    width=1000,
    height=600,
    max_font_size=100,            #字体大小
    min_font_size=10,
    mask=plt.imread('shu.jpg'),  #背景图片
    max_words=1000
)
wc.generate(result)
wc.to_file('jielun.png')    #图片保存

#5.显示图片
plt.figure('jielun')   #图片显示的名字
plt.imshow(wc)
plt.axis('off')        #关闭坐标
plt.show()