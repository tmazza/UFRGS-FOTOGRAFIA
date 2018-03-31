import time
import matplotlib.pyplot as plt
import numpy as np
from rawkit.raw import Raw

start_time = time.time()

with Raw(filename='a.CR2') as raw:
  # valores pixel de 12 bits - 0~4096
  img_raw, color_array_scheme = raw.bayer_data()
  rows = len(img_raw)
  cols = len(img_raw[0])
  
  img_r = [[0 for x in range(cols)] for y in range(rows)]
  img_g = [[0 for x in range(cols)] for y in range(rows)]
  img_b = [[0 for x in range(cols)] for y in range(rows)]

  def get_pixel_value(x, y):
    if(x < 0 or x >= rows or y < 0 or y >= cols):
      return 0
    return img_raw[x][y]

  # interpola
  for i in range(0, rows):
    for j in range(0, cols):
      even_row = i % 2 == 0
      even_col = j % 2 == 0

      # Interpolação R e B
      if(even_row and not even_col): # case b
        R1 = get_pixel_value(i, j-1)
        R2 = get_pixel_value(i, j+1)
        B1 = get_pixel_value(i-1, j)
        B2 = get_pixel_value(i+1, j)
         
        img_r[i][j] = (R1 + R2) / 2;
        img_b[i][j] = (B1 + B2) / 2;

      elif(not even_row and even_col): # case a
        R1 = get_pixel_value(i-1, j)
        R2 = get_pixel_value(i+1, j)
        B1 = get_pixel_value(i, j-1)
        B2 = get_pixel_value(i, j+1)
         
        img_r[i][j] = (R1 + R2) / 2;
        img_b[i][j] = (B1 + B2) / 2;

      else:
        P1 = get_pixel_value(i-1, j-1)
        P2 = get_pixel_value(i+1, j-1)
        P3 = get_pixel_value(i+1, j+1)
        P4 = get_pixel_value(i-1, j+1)
         
        if(even_row and even_col): # case d
          img_r[i][j] = get_pixel_value(i, j)
          img_b[i][j] = (P1 + P2 + P3 + P4) / 4
        else: # case c
          img_r[i][j] = (P1 + P2 + P3 + P4) / 4;
          img_b[i][j] = get_pixel_value(i, j);

      # Interpolação G
      if((even_row and even_col) or (not even_row and not even_col)):
        
        G1 = get_pixel_value(i, j-1)
        G2 = get_pixel_value(i+1, j)
        G3 = get_pixel_value(i, j+1)
        G4 = get_pixel_value(i-1, j)
         
        R1 = get_pixel_value(i, j-2)
        R2 = get_pixel_value(i+2, j)
        R3 = get_pixel_value(i, j+2)
        R4 = get_pixel_value(i-2, j)
         
        if(abs(R1 - R3) < abs(R2 - R4)):
          cor = (G1 + G3) / 2;
        elif(abs(R1 - R3) > abs(R2 - R4)):
          cor = (G2 + G4) / 2;
        else:
          cor = (G1 + G2 + G3 + G4) / 4;

        img_g[i][j] = cor

      else:
        img_g[i][j] = img_raw[i][j]

  # Composição das cores + white balance + gamma correction
  img_rgb = [[[] for x in range(cols)] for y in range(rows)]
  for i in range(0, rows):
    for j in range(0, cols):
      # white balance && conversão de 12bits para 8 bits
      r = 4096/2500 * img_r[i][j] / 16
      g = 4096/2300 * img_g[i][j] / 16
      b = 4096/2000 * img_b[i][j] / 16

      # gamma correction
      gamma = 2.2
      r = ((r/255)**(1/gamma)) * 255
      g = ((g/255)**(1/gamma)) * 255
      b = ((b/255)**(1/gamma)) * 255

      img_rgb[i][j] = [
        int(r) if r < 255 else 255, 
        int(g) if g < 255 else 255, 
        int(b) if b < 255 else 255
      ]
      
  # plt.axis('off')
  # plt.imshow(img_raw, cmap='gray')
  # plt.show()

  # plt.axis('off')
  # plt.imshow(img_r, cmap='Reds')
  # plt.show()

  # plt.axis('off')
  # plt.imshow(img_b, cmap='Blues')
  # plt.show()

  # plt.axis('off')
  # plt.imshow(img_g, cmap='Greens')
  # plt.show()

  print("Decorrido", time.time() - start_time, "seg")

  plt.axis('off')
  plt.imshow(img_rgb)
  plt.show()