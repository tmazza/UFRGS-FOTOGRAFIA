import matplotlib.pyplot as plt
import numpy as np
import math 
from PIL import Image

import sys

# Carrega curva
file = open('curvas/curve1.m')
curva_r = np.zeros(256)
curva_g = np.zeros(256)
curva_b = np.zeros(256)

i = 0
for line in file:
  r, g, b = line.split(" ")
  curva_r[i] = r
  curva_g[i] = g
  curva_b[i] = b
  i+=1

curva_r = 10**curva_r
print(curva_r)

'''

# Valor pixel linearizado
im = Image.open("images/office_1.jpg")
pix = im.load()
width, height = im.size

r = np.zeros((width, height))
g = np.zeros((width, height))
b = np.zeros((width, height))

for i in range(0, width):
  for j in range(0, height):
    r[i, j], g[i, j], b[i, j] = pix[i, j]

r = ( (r/255)**2.2 ) * 255
g = ( (g/255)**2.2 ) * 255
b = ( (b/255)**2.2 ) * 255

# Cálculo irradiância
# TODO: melhorar existem somente 256 valores possíveis salvar mapeamentos

def get_closest(exposure_value, curve):
  for i in range(1, len(curve)):
    if(curve[i] > exposure_value):
      curr = abs(exposure_value - curve[i])
      prev = abs(exposure_value - curve[i-1])
      return i if(curr < prev) else i-1
  return 255
print(r)

for i in range(0, width):
  for j in range(0, height):
    r[i, j] = get_closest(r[i, j], curva_r)
    g[i, j] = get_closest(g[i, j], curva_g)
    b[i, j] = get_closest(b[i, j], curva_b)

r = r / 0.03
g = g / 0.03
b = b / 0.03

print(r)
print(g)
print(b)

img_rgb = np.stack([img_r, img_g, img_b], axis=2)

plt.axis('off')
plt.imshow(img_rgb)
plt.show()

'''