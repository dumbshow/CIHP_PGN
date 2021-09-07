import numpy as np
import imageio as ii
from PIL import Image
from glob import glob
import os

for filename in glob('datasets/CIHP/images/*.jpg'):

  img   = Image.open(filename)
  img2 = Image.new('L', (img.width, img.height))

  fn_base = os.path.splitext(os.path.split(filename)[1])[0]
  img2.save(f'datasets/CIHP/labels/{fn_base}.png')
  img2.save(f'datasets/CIHP/edges/{fn_base}.png')
  img2.save(f'datasets/CIHP/labels_rev/{fn_base}.png')