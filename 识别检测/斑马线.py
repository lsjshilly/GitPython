import cv2
import matplotlib.image as mplimg
import matplotlib.pyplot as plt
import numpy as np


blur_ksize = 5  # Gaussian blur kernel size
canny_lthreshold = 100  # Canny edge detection low threshold
canny_hthreshold = 200  # Canny edge detection high threshold
# Hough transform parameters
rho = 1.0
theta = np.pi / 180
min_line_length = 80
max_line_gap = 40



if __name__ == "__main__":

    img = mplimg.imread('./images/01.jpg')
    plt.figure(1)
    plt.imshow(img)
    # plt.show()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    plt.figure(2)
    plt.imshow(gray)
    # plt.show()
    blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)
    edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)
    # line_img = hough_lines(edges, rho, theta, threshold, min_line_length, max_line_gap)
    plt.figure(3)

    plt.imshow(edges)
    plt.show()