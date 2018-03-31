import time
import matplotlib.pyplot as plt
import numpy as np
from rawkit.raw import Raw

start_time = time.time()

with Raw(filename='a.CR2') as raw:

  img_raw, color_array_scheme = raw.bayer_data()
  img_raw = np.array(img_raw);
  img_raw = img_raw / 4096;

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

  rw = img_r[200][1200]; print("R", rw);
  gw = img_g[200][1200]; print("G", gw);
  bw = img_b[200][1200]; print("B", bw);

  img_r = ( img_r * (1/rw) ) ** (2.2)
  img_g = ( img_g * (1/gw) ) ** (2.2)
  img_b = ( img_b * (1/bw) ) ** (2.2)

  img_rgb = np.stack([img_r, img_g, img_b], axis=2)

  print("Decorrido", time.time() - start_time, "seg")

  plt.axis('off')
  plt.imshow(img_rgb)
  plt.show()
