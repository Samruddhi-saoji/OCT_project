#import libraries
import cv2
import numpy as np

#input image
#image = cv2.imread('.\\input images\\WGT1021-508.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('output.jpg', cv2.IMREAD_GRAYSCALE)
#dim = 512, 1024

kernel_size = (7, 7) #kernel size
denoised_image = cv2.GaussianBlur(image, kernel_size, 0) #apply Gaus. blur

cv2.imwrite('final.png', denoised_image) #save img