import cv2
import numpy as np
import math

def gaussian_function(size, sigma):

    kernel = np.zeros((size, size))
    center = size // 2
    a, b = center, center

    elements_summ = 0.0
    for i in range(size):
        for j in range(size):
            x, y  = i, j

            exp = math.exp(-1 * ((x - a) ** 2 + (y - b) ** 2) / 2 * sigma ** 2)
            gauss = exp / 2 * math.pi * sigma ** 2
            kernel[i,j] = gauss
            elements_summ += gauss

    kernel = kernel / elements_summ

    return kernel


sigma_values = [0.66, 0.33]
matrix_sizes = [5, 7]

img = cv2.imread(r"E:/GitHub/Comp_vision/lab3/img2.jfif", cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original image', img)


for size in matrix_sizes:
    for sigma in sigma_values:
        
        gauss_matrix = gaussian_function(size, sigma)

        print(f"\n" + "-" * 30)
        print(f"Нормированная матрица Гаусса для размера: {size} и среднеквадратичного отклонения: {sigma}")
        print(gauss_matrix)

        filtered_img = cv2.filter2D(img, -1, gauss_matrix)


        cv2.imshow(f'Fileterd Image with size matrix = {size}, sigma = {sigma}', filtered_img)

cv2.waitKey(0)
cv2.destroyAllWindows()



