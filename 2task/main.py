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

# Valor pixel linearizado - gamaa decoding
im = Image.open("images/office_1.jpg")
pix = im.load()
width, height = im.size

r = np.zeros((width, height))
g = np.zeros((width, height))
b = np.zeros((width, height))

for i in range(0, width):
  for j in range(0, height):
    r[i, j], g[i, j], b[i, j] = pix[i, j]

r = 255 * np.power(r/255, 2.2)
g = 255 * np.power(g/255, 2.2)
b = 255 * np.power(b/255, 2.2)

# Cálculo irradiância
# TODO: melhorar existem somente 256 valores possíveis salvar mapeamentos
def index_response_curve(exposure_value, curve):
  for i in range(1, len(curve)):
    if(curve[i] > exposure_value):
      curr = abs(exposure_value - curve[i])
      prev = abs(exposure_value - curve[i-1])
      return i if(curr < prev) else i-1
  return 255

for i in range(0, width):
  for j in range(0, height):
    r[i, j] = index_response_curve(r[i, j], curva_r)
    g[i, j] = index_response_curve(g[i, j], curva_g)
    b[i, j] = index_response_curve(b[i, j], curva_b)

r = np.exp(r) / 0.03
g = np.exp(g) / 0.03
b = np.exp(b) / 0.03

print(r.min())
print(r.max())

# rgb = np.stack([r, g, b], axis=2)

# print(rgb)

# plt.axis('off')
# plt.imshow(rgb)
# plt.show()
