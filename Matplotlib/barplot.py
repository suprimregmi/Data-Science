# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:12:02 2020

@author: Acer
"""
from matplotlib import pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes =np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
             
                   #Plotting values
                   
plt.bar(x_indexes-width, dev_y, width = width,color='#003400', label ="All Devs")
plt.bar(x_indexes,py_dev_y, width=width,color='#110000', label ="pyhton-devs")
plt.bar(x_indexes+width,js_dev_y,width =width,color='b', label ="JavaScript")        
        
plt.legend()
plt.xticks(ticks=x_indexes, labels = ages_x)
#plt.yticks(ticks=y_indexes,labels = py_dev_y)
plt.title("Median salary by Age")
plt.xlabel("ages")
plt.ylabel("salary")