# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : HuJian
# * Email         : swjtu_hj@163.com
# * Create time   : 2018-10-30 13:20
# * Last modified : 2018-10-30 13:20
# * Filename      : pic2douyin.py
# * Description   : 图片-—>抖音风
# **********************************************************
from PIL import Image


def run(filenmae):
    img = Image.open(filename)
    (w,h) = img.size
    delta = 10
    for i in range(w-delta-1,0,-1):
        for j in range(h-delta-1,0,-1):
            (r,g,b) = img.getpixel((i,j))
            (nr, ng, nb) = img.getpixel((i+delta, j+delta))
            img.putpixel((i+delta,j+delta),(nr,ng,b))
    img.save('be'+filename+'.jpg')

if __name__ == '__main__':
    for i in range(1,6):
        filename = 'test{index}.jpg'.format(index=i)
        run(filename)


