# -*- coding: utf-8 -*-
# 导入必要的库
import numpy as np
import cv2


def centroid_histogram(clt):

    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist


def plot_colors(hist, centroids):

    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    return bar


def RGB_to_HSV(R, G, B):
    max_value = max(R, G, B)
    min_value = min(R, G, B)
    V = max(R, G, B)
    S = (max_value - min_value) / max_value
    if R == max_value:
			H = (G - B) / (max_value - min_value) * 60
    if G == max_value:
			H = 120 + (B - R) / (max_value - min_value) * 60
    if B == max_value:
			H = 240 + (R - G) / (max_value - min_value) * 60
    if H < 0:
			H = H + 360
    return H, S, V


def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v