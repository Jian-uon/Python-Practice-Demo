# coding: utf-8
import numpy as np
#最基础， 正太分布生成随机数（矩阵）
print np.random.rand(4, 4)
randMat = np.mat(np.random.rand(4, 4))
print randMat
print randMat.I #矩阵求逆运算
print np.eye(4) #生成单位矩阵

np.shape()

