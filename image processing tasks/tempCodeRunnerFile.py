# Task 2

# 2 - a abs = its OVER EXPOSURED
#2 - b (point op. = reduce img. brightness by 2 units)

import cv2 
import matplotlib.pyplot as plt
import numpy as np

def bright_mod( inten_range_bins = [] , brit_value = int(0)) :
    mx = max(inten_range_bins) 
    for i in range (mx + 1) :
        inten_range_bins[i] += brit_value
    return inten_range_bins

h1_x = list(range(0,16,1))
h1_y = [0,0,0,5,15,20,18,16,10,5,8,20,25,30,20,48]

#BEFORE
bef = plt.figure()
plt.xticks(h1_x)
plt.title("h1: Before Increasing Brightness")
plt.bar(h1_x,h1_y)

#AFTER
aft = plt.figure()
h1_x = bright_mod ( h1_x , +2)
plt.xticks(h1_x)
plt.title(" h1: After increasing Brightness")
plt.annotate( "this op. will NOT affect contrast  and dynamic range" , [2,40])
plt.bar(h1_x,h1_y)
plt.show()
#ors