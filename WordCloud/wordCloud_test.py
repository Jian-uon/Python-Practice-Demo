# coding: utf-8
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba 

def run():
    f = open(u'words2.txt', 'r').read()
    words = list(jieba.cut(f))
    a = []
    for w in words:
        if len(w) > 1:
            a.append(w)
    text = r' '.join(a)

    wordcloud = WordCloud(
            background_color = 'white',
            width = 1500,
            height = 960,
            margin = 10,
            font_path='C:/Windows/Fonts/simkai.ttf',
            ).generate(text)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    wordcloud.to_file('words_result2.png')
    return

if __name__ == '__main__':
    run()

