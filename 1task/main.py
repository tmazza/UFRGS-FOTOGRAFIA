import matplotlib.pyplot as plt
import numpy as np
from rawkit.raw import Raw

with Raw(filename='a.CR2') as raw:

  img_raw, color_array_scheme = raw.bayer_data()
  img_raw = np.array(img_raw);

  m = np.copy(img_raw);
  m[1:-1:2, ::2] = (m[:-2:2, ::2] + m[2::2, ::2]) / 2.
  m[::2, 1:-1:2] = (m[::2, :-2:2] + m[::2, 2::2]) / 2.
  m[1:-1:2, 1:-1:2] = (m[1:-1:2, :-2:2] + m[1:-1:2, 2::2]) / 2.


  # interpola
  # for i in range(2, rows+2):
  #   for j in range(2, cols+2):
  #     even_row = i % 2 == 0
  #     even_col = j % 2 == 0

  #     r = b = 0
  #     # Interpolação R e B
  #     if(even_row and not even_col): # case b
  #       R1 = maw[i, j-1]
  #       R2 = maw[i, j+1]
  #       B1 = maw[i-1, j]
  #       B2 = maw[i+1, j]
  #       r = (R1 + R2) / 2;
  #       b = (B1 + B2) / 2;
  #     elif(not even_row and even_col): # case a
  #       R1 = maw[i-1, j]
  #       R2 = maw[i+1, j]
  #       B1 = maw[i, j-1]
  #       B2 = maw[i, j+1]
  #       r = (R1 + R2) / 2;
  #       b = (B1 + B2) / 2;
  #     else:
  #       P1 = maw[i-1, j-1]
  #       P2 = maw[i+1, j-1]
  #       P3 = maw[i+1, j+1]
  #       P4 = maw[i-1, j+1]
  #       if(even_row and even_col): # case d
  #         r = maw[i, j]
  #         b = (P1 + P2 + P3 + P4) / 4
  #       else: # case c
  #         r = (P1 + P2 + P3 + P4) / 4;
  #         b = maw[i, j]

  #     m[i-2][j-2] = r / 4096
  #     img_b[i-2][j-2] = b / 4096

  #     # Interpolação G
  #     if((even_row and even_col) or (not even_row and not even_col)):
  #       G1 = maw[i, j-1]
  #       G2 = maw[i+1, j]
  #       G3 = maw[i, j+1]
  #       G4 = maw[i-1, j]
  #       R1 = maw[i, j-2]
  #       R2 = maw[i+2, j]
  #       R3 = maw[i, j+2]
  #       R4 = maw[i-2, j]
  #       if(abs(R1 - R3) < abs(R2 - R4)):
  #         cor = (G1 + G3) / 2;
  #       elif(abs(R1 - R3) > abs(R2 - R4)):
  #         cor = (G2 + G4) / 2;
  #       else:
  #         cor = (G1 + G2 + G3 + G4) / 4;
  #       g = cor
  #     else:
  #       g = maw[i][j]

  #     img_g[i-2][j-2] = g / 4096
 

  print(m/16)

  plt.axis('off')
  plt.imshow(m/16, cmap='Reds')
  plt.show()
  
  # plt.axis('off')
  # plt.imshow(img_g, cmap='Greens')
  # plt.show()

  # plt.axis('off')
  # plt.imshow(img_b, cmap='Blues')
  # plt.show()

  # rw = m[200][1200]
  # gw = img_g[200][1200]
  # bw = img_b[200][1200]
  # print("R", rw);
  # print("G", gw);
  # print("B", bw);

  # Composição das cores + white balance + gamma correction
  mgb = [[[] for x in range(cols)] for y in range(rows)]
  for i in range(0, rows):
    for j in range(0, cols):
      # white balance && gamma correction
      mgb[i][j] = [
        int( ( (m[i][j]*(1/rw) )**(1/2.2)) * 255 ),
        int( ( (img_g[i][j]*(1/gw) )**(1/2.2)) * 255 ),
        int( ( (img_b[i][j]*(1/bw) )**(1/2.2)) * 255 )
      ]

  # plt.axis('off')
  # plt.imshow(mgb)
  # plt.show()