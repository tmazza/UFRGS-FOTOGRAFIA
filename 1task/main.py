import matplotlib.pyplot as plt
import numpy as np
from rawkit.raw import Raw

with Raw(filename='a.CR2') as raw:

  img_raw, color_array_scheme = raw.bayer_data()
  img_raw = np.array(img_raw);

  img_r = np.copy(img_raw);
  img_r[1:-1:2, ::2] = (img_r[:-2:2, ::2] + img_r[2::2, ::2]) / 2.
  img_r[::2, 1:-1:2] = (img_r[::2, :-2:2] + img_r[::2, 2::2]) / 2.
  img_r[1:-1:2, 1:-1:2] = (img_r[1:-1:2, :-2:2] + img_r[1:-1:2, 2::2]) / 2.

  img_b = np.copy(img_raw);
  img_b[2::2, 1::2] = (img_b[1:-2:2, 1::2] + img_b[3::2, 1::2]) / 2.
  img_b[1::2, 2::2] = (img_b[1::2, 1:-2:2] + img_b[1::2, 3::2]) / 2.
  img_b[2::2, 2::2] = (img_b[2::2, 1:-2:2] + img_b[2::2, 3::2]) / 2.

  img_g = np.copy(img_raw);
  img_g[2::2, 2::2] = (img_g[2::2, 1:-2:2] + img_g[2::2, 3::2] + img_g[1:-2:2, 2::2] + img_g[3::2, 2::2]) / 4.
  img_g[1:-1:2, 1:-1:2] = (img_g[1:-1:2, :-3:2] + img_g[1:-1:2, 2::2] + img_g[:-2:2, 1:-1:2] + img_g[2::2, 1:-1:2]) / 4.

  # plt.axis('off')
  # plt.imshow(img_r/16, cmap='Reds')
  # plt.show()
  
  # plt.axis('off')
  # plt.imshow(img_g/16, cmap='Greens')
  # plt.show()

  # plt.axis('off')
  # plt.imshow(img_b/16, cmap='Blues')
  # plt.show()

  rw = img_r[200][1200]
  gw = img_g[200][1200]
  bw = img_b[200][1200]
  print("R", rw);
  print("G", gw);
  print("B", bw);

  # Composição das cores + white balance + gamma correction
  # mgb = [[[] for x in range(cols)] for y in range(rows)]
  # for i in range(0, rows):
  #   for j in range(0, cols):
  #     # white balance && gamma correction
  #     mgb[i][j] = [
  #       int( ( (m[i][j]*(1/rw) )**(1/2.2)) * 255 ),
  #       int( ( (img_g[i][j]*(1/gw) )**(1/2.2)) * 255 ),
  #       int( ( (img_b[i][j]*(1/bw) )**(1/2.2)) * 255 )
  #     ]

  # plt.axis('off')
  # plt.imshow(mgb)
  # plt.show()