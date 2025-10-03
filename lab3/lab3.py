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
            exp = math.exp(-((x - a)**2 + (y - b)**2) / (2 * sigma**2))
            gauss = exp / 2 * math.pi * sigma**2
            kernel[i,j] = gauss
            elements_summ += gauss

    kernel = kernel / elements_summ

    return kernel


def super_svertka(img, kernel_size, sigma):
    kernel = gaussian_function(kernel_size, sigma)

    padding_size = kernel_size // 2
    img_padded = cv2.copyMakeBorder(img, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_REFLECT)

    gauss_blur = img.copy()
    height, width = img.shape
    
    for y in range(height):
        for x in range(width):
            value = 0
            y_padded = y + padding_size
            x_padded = x + padding_size
            
            for k in range(kernel_size):
                for l in range(kernel_size):
                    value += img_padded[y_padded + k - padding_size, x_padded + l - padding_size] * kernel[k, l]
            
            gauss_blur[y, x] = value
    
    return gauss_blur

sigma_values = [3, 2]
matrix_sizes = [9, 11]

img = cv2.imread(r"E:/GitHub/Comp_vision/lab3/img2.jfif", cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original image', img)


for size in matrix_sizes:
    for sigma in sigma_values:

        #filtered_img = cv2.filter2D(img, -1, gauss_matrix)
        filtered_img = super_svertka(img, size, sigma)
        gauss_filter = cv2.GaussianBlur(img, (size, size), sigma)

        cv2.imshow(f'Fileterd Image with size matrix = {size}, sigma = {sigma}', filtered_img)
        cv2.imshow(f'Gaussian Blur with size matrix = {size}, sigma = {sigma}', gauss_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()



