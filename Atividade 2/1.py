import cv2
from matplotlib import pyplot as plt

image_path = '4-2-masquerade-of-the-guilty-3840x2160-v0-2x69lncpp7yb1.png'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.axis('off')

properties = [
    ('Altura', image_rgb.shape[0]),
    ('Largura', image_rgb.shape[1]),
    ('Canais de cor', image_rgb.shape[2]),
    ('Tipo de dado', image_rgb.dtype),
    ('Tom de cinza máximo', image_gray.max()),
    ('Tom de cinza médio', image_gray.mean()),
    ('Tom de cinza mínimo', image_gray.min()),
]

for prop_name, prop_value in properties:
    print(f"{prop_name}:{prop_value}")