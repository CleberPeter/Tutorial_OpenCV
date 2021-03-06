import cv2

imagem_1 = cv2.imread('cameraman.tif')
imagem_2 = cv2.imread('artificial.tif')

cv2.imshow('imagem 1', imagem_1)
cv2.waitKey(0)
cv2.imshow('imagem 2', imagem_2)
cv2.waitKey(0)

imagem_1_divide_imagem_2 = cv2.divide(imagem_1, imagem_2)
cv2.imwrite('imagem_1_divide_imagem_2.png', imagem_1_divide_imagem_2)
cv2.imshow('imagem 1 divide imagem 2', imagem_1_divide_imagem_2)
cv2.waitKey(0)
