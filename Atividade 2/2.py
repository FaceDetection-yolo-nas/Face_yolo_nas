import cv2
from matplotlib import pyplot as plt

image_path = '4-2-masquerade-of-the-guilty-3840x2160-v0-2x69lncpp7yb1.png'
image = cv2.imread(image_path)
plt.axis('off')
imagem_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
resized_image = cv2.resize(imagem_rgb, (600, 400))

plt.subplot(2, 2, 1)
plt.imshow(resized_image)
plt.title('Imagem Original')

plt.subplot(2, 2, 2)
plt.imshow(cv2.blur(resized_image, (15, 15)))
plt.title('Imagem com filtro de média')

plt.subplot(2, 2, 3)
plt.imshow(cv2.GaussianBlur(resized_image, (15, 15), 0)
           )
plt.title('Imagem com filtro gaussiano')

plt.subplot(2, 2, 4)
plt.imshow(cv2.medianBlur(resized_image, 1, (15, 15))
           )
plt.title('Imagem com filtro de mediana')

plt.show()
