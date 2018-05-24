import matplotlib.pyplot as plt
import numpy as np
import math 
from PIL import Image

import sys

images = [
  { 'file': 'images/office_1.jpg', 'exposure': 0.0333,
    'r': False, 'g': False, 'b': False },
  { 'file': 'images/office_2.jpg', 'exposure': 0.1,
    'r': False, 'g': False, 'b': False },
  { 'file': 'images/office_3.jpg', 'exposure': 0.333,
    'r': False, 'g': False, 'b': False },
  { 'file': 'images/office_4.jpg', 'exposure': 0.5,
    'r': False, 'g': False, 'b': False },
  { 'file': 'images/office_5.jpg', 'exposure': 1,
    'r': False, 'g': False, 'b': False },
  { 'file': 'images/office_6.jpg', 'exposure': 4,
    'r': False, 'g': False, 'b': False },
]


# Carrega curva
curveFile = 'curvas/curveC.m'
file = open(curveFile)
curva_r = np.zeros(256)
curva_g = np.zeros(256)
curva_b = np.zeros(256)

i = 0
for line in file:
  a, b, c = line.split(" ")
  curva_r[i] = float(a)
  curva_g[i] = float(b)
  curva_b[i] = float(c)
  i+=1

curva_r = np.exp(curva_r)
curva_g = np.exp(curva_g)
curva_b = np.exp(curva_b)

# plt.plot(curva_r, range(0, 256), color="red")
# plt.plot(curva_g, range(0, 256), color="green")
# plt.plot(curva_b, range(0, 256), color="blue")
# plt.show()

for img in range(0, len(images)):
  
  # Valor pixel linearizado - gamaa decoding
  im = Image.open(images[img]['file'])
  width, height = im.size
  pix = im.load()

  Er = np.zeros((width, height))
  Eg = np.zeros((width, height))
  Eb = np.zeros((width, height))

  for i in range(0, width):
    for j in range(0, height):
      r, g, b = im.getpixel((i, j))
      r = int(255 * ((r/255)**2.2))
      g = int(255 * ((g/255)**2.2))
      b = int(255 * ((b/255)**2.2))
      pix[i, j] = (r, g, b) # sem gamma enconding

      Er[i, j] = curva_r[r] / images[img]['exposure'];
      Eg[i, j] = curva_g[g] / images[img]['exposure'];
      Eb[i, j] = curva_b[b] / images[img]['exposure'];

      # print(Er[i, j], Eg[i, j], Eb[i, j])

  images[img]['r'] = Er;
  images[img]['g'] = Eg;
  images[img]['b'] = Eb;

  print(images[img]['file'], '- ok')


# print(images[0]['r'])
# print(min(images[0]['r']), max(images[0]['r']))
# def ajusta_np(M):
#   return np.fliplr(np.rot90(np.rot90(np.rot90(M))))
# for k in range(0, len(images)):
#   images[k]['r'] = ajusta_np(images[k]['r'])
#   images[k]['g'] = ajusta_np(images[k]['g'])
#   images[k]['b'] = ajusta_np(images[k]['b'])

vmin = 0.01
vmax = 10

hdr_r = np.zeros((width, height))
hdr_g = np.zeros((width, height))
hdr_b = np.zeros((width, height))

for i in range(0, width):
  for j in range(0, height):
    r = []
    g = []
    b = []
    for k in range(0, len(images)):    
      val_r = images[k]['r'][i, j]
      if(val_r < vmax and val_r > vmin):
        r.append(val_r)
      
      val_g = images[k]['g'][i, j]
      if(val_g < vmax and val_g > vmin):
        g.append(val_g) 
      
      val_b = images[k]['b'][i, j]
      if(val_b < vmax and val_b > vmin):
        b.append(val_b) 

    hdr_r[i, j] = sum(r) / len(r)
    hdr_g[i, j] = sum(g) / len(g)
    hdr_b[i, j] = sum(b) / len(b)

#
delta = 0.0000000000001
average_lum = 0;
for i in range(0, width):
  for j in range(0, height):
    L = 0.299*hdr_r[i, j] + 0.587*hdr_g[i, j] + 0.114*hdr_b[i, j]
    average_lum += np.log(L + delta)

N = width * height
average_lum = np.exp( average_lum / N )

result = Image.open('result.png')
pix = result.load()
for i in range(0, width):
  for j in range(0, height):
    pix[i, j] = (255, 255, 255)

pixel_lum = np.copy(hdr_r)
for i in range(0, width):
  for j in range(0, height):
    L = 0.299*hdr_r[i, j] + 0.587*hdr_g[i, j] + 0.114*hdr_b[i, j]
    L = (0.18/average_lum) * L
    L = (L / (1 + L))

    r = L * ( ( (hdr_r[i, j] * .35) /L)**(1/2.2) )
    g = L * ( ( (hdr_g[i, j] * .35) /L)**(1/2.2) )
    b = L * ( ( (hdr_b[i, j] * .35) /L)**(1/2.2) )

    r = int( r * 255 )
    g = int( g * 255 )
    b = int( b * 255 )

    pix[i, j] = (r, g, b)

result.show()
result.save('result.png')