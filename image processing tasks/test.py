#task 4  - Adaptive mean threshholding
import cv2 
import matplotlib.pyplot as plt
import numpy as np

bef_img = cv2.imread("graygrid.png", cv2.IMREAD_GRAYSCALE)
thresh_img = np.zeros( (bef_img.shape[0] ,bef_img.shape[1]) ,dtype = np.uint8)
thresh_img = cv2.adaptiveThreshold(bef_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

plt.subplot(1,2,1) , plt.imshow(bef_img,'gray') , plt.title("original")
plt.xticks([]),plt.yticks([])
plt.subplot(1,2,2) , plt.imshow(thresh_img,'gray') , plt.title("mean adaptive threshed")
plt.xticks([]),plt.yticks([])
plt.show()
#ors
