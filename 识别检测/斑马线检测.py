import cv2
import matplotlib.image as mplimg
import matplotlib.pyplot as plt
import numpy as np


blur_ksize = 5  # Gaussian blur kernel size
canny_lthreshold = 100  # Canny edge detection low threshold
canny_hthreshold = 220  # Canny edge detection high threshold
# Hough transform parameters
rho = 1.0
theta = np.pi / 180
threshold = 90
min_line_length = 40
max_line_gap = 40



def hough_lines(img, rho, theta, threshold,
                min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]),
                            minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lanes(line_img, lines)
    return line_img



def draw_lanes(img, lines, color=[255, 0, 0], thickness=2):
    total_lines = []
    total_distance = np.array([])
    total_k = np.array([])
    for line in lines:
        for x1, y1, x2, y2 in line:
            d, k= linespace(x1, y1, x2, y2)
            if  total_lines == []:
                total_lines.append([[x1, y1, x2, y2]])
                total_distance = np.append(total_distance, d)
                total_k = np.append(total_k, k)
            else:
                for i in range(0, len(total_distance)):
                    if (abs(total_distance[i]-d) < 5) and (abs(total_k[i]-k) < 1):
                        total_lines[i].append([x1, y1, x2, y2])
                else:
                    total_distance = np.append(total_distance, d)
                    total_k = np.append(total_k, k)
                    total_lines.append([[x1, y1, x2, y2]])
    print('分组完成')
    for singal_line in total_lines:
        left_points = [(line1[0],line1[1]) for line1 in singal_line ]
        left_points = left_points + [(line1[2],line1[3]) for line1 in singal_line ]

        left_vtx = calc_lane_vertices(left_points)

        cv2.line(img, left_vtx[0], left_vtx[1], color, thickness)


def linespace(x1, y1, x2, y2):
    k = (y2-y1)/(x2-x1)
    d = abs((k*x1-y1)/(k**2+1)**(0.5))
    try:
        theta_k = np.arctan(-1/k)
    except:
        theta_k = np.pi/2
    return d, theta_k


def calc_lane_vertices(point_list):
    x = [p[0] for p in point_list]
    y = [p[1] for p in point_list]
    fit = np.polyfit(x, y, 1)
    fit_fn = np.poly1d(fit)
    xmin = min(x)
    xmax = max(x)

    ymin = int(fit_fn(xmin))
    ymax = int(fit_fn(xmax))
    return [(xmin, ymin), (xmax, ymax)]

if __name__ == "__main__":

    img = mplimg.imread('./images/01.jpg')
    plt.imshow(img)
    plt.show()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)
    edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)
    line_img = hough_lines(edges, rho, theta, threshold, min_line_length, max_line_gap)

    
    res_img = cv2.addWeighted(img, 0.8, line_img, 1, 0)
    plt.imshow(res_img)
    plt.show()
 

