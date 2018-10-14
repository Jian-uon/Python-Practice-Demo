# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
'''
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
'''
plt.figure(figsize=(3,2))
for i,c in enumerate('rgbyck'):
    plt.subplot(320+i+1, axisbg=c)
#plt.subplot(221)
#plt.subplot(222)
#plt.subplot(212)

plt.show()



