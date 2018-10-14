# coding: utf-8
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import jieba 
import numpy as np

def run():
    f = open(u'words2.txt', 'r').read()
    words = list(jieba.cut(f))
    a = []
    for w in words:
        if len(w) > 1:
            a.append(w)
    text = r' '.join(a)
    
    bg = np.array(Image.open('bg.jpg'))
    wordcloud = WordCloud(
            background_color = 'white',
            #width = 1500,
            #height = 960,
            #margin = 10,
            mask = bg,
            font_path='C:/Windows/Fonts/simkai.ttf',
            ).generate(text)

    image_colors=ImageColorGenerator(bg)

    plt.imshow(wordcloud.recolor(color_func=image_colors))
    plt.axis('off')
    plt.show()
    wordcloud.to_file('words_result3.png')
    return

if __name__ == '__main__':
    run()

