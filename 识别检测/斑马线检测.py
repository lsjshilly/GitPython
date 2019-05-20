import cv2
import matplotlib.image as mplimg
import matplotlib.pyplot as plt
import numpy as np


blur_ksize = 5  # Gaussian blur kernel size
canny_lthreshold = 50  # Canny edge detection low threshold
canny_hthreshold = 150  # Canny edge detection high threshold
# Hough transform parameters
rho = 1
theta = np.pi / 180
threshold = 15
min_line_length = 40
max_line_gap = 20



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
    k=0
    for line in lines:
        k += 1
        print(k)
        for x1, y1, x2, y2 in line:
            d = linespace(x1, y1, x2, y2)
            if  total_lines == []:
                local_lines = np.array([[x1,y1,x2,y2]])
                total_lines.append(local_lines)
                total_distance = np.append(total_distance, d)
            else:
                for i in range(0, len(total_distance)):
                    if abs(total_distance[i]-d) < 0.3:
                        total_lines[i] = np.append(total_lines[i],[[x1, y1, x2, y2]],axis=0)
                    else:
                        total_distance = np.append(total_distance, d)
                        total_lines.append(np.array([[x1,y1,x2,y2]]))
    print('分组完成')
    for singal_line in total_lines:
        left_points = [(x1, y1)
                       for line in singal_line for x1, y1, x2, y2 in line]
        left_points = left_points + \
            [(x2, y2) for line in singal_line for x1, y1, x2, y2 in line]

        left_vtx = calc_lane_vertices(left_points, 325, img.shape[0])

        cv2.line(img, left_vtx[0], left_vtx[1], color, thickness)


def linespace(x1, y1, x2, y2):
    k = (y2-y1)/(x2-x1)
    d = abs((k*x1-y1)/(k**2+1)**(0.5))
    return d


def calc_lane_vertices(point_list, ymin, ymax):
    x = [p[0] for p in point_list]
    y = [p[1] for p in point_list]
    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)
    xmin = int(fit_fn(ymin))
    xmax = int(fit_fn(ymax))
    return [(xmin, ymin), (xmax, ymax)]

if __name__ == "__main__":

    img = mplimg.imread('./images/01.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)
    edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)
    line_img = hough_lines(edges, rho, theta, threshold,
                        min_line_length, max_line_gap)

    plt.imshow(line_img)
    plt.show()


# def clean_lines(lines, threshold):
#     slope = [(y2 - y1) / (x2 - x1)
#              for line in lines for x1, y1, x2, y2 in line]
#     while len(lines) > 0:
#         mean = np.mean(slope)
#         diff = [abs(s - mean) for s in slope]
#         idx = np.argmax(diff)
#         if diff[idx] > threshold:
#             slope.pop(idx)
#             lines.pop(idx)
#         else:
#             break


# def roi_mask(img, vertices):
#     mask = np.zeros_like(img)
#     mask_color = 255
#     cv2.fillPoly(mask, vertices, mask_color)
#     masked_img = cv2.bitwise_and(img, mask)
#     return masked_img
