import numpy as np
import imageio as ii
from PIL import Image
from glob import glob
import os

for path in ('datasets/CIHP/labels/', 'datasets/CIHP/edges/', 'datasets/CIHP/labels_rev/'):
  try:
    os.mkdir(path)
  except:
    pass

with open('datasets/CIHP/list/val.txt', 'w') as wf1, open('datasets/CIHP/list/val_id.txt', 'w') as wf2:

  for filename in glob('datasets/CIHP/images/*.jpg'):

    img   = Image.open(filename)
    img2 = Image.new('L', (img.width, img.height))

    fn_base = os.path.splitext(os.path.split(filename)[1])[0]
    img2.save(f'datasets/CIHP/labels/{fn_base}.png')
    img2.save(f'datasets/CIHP/edges/{fn_base}.png')
    img2.save(f'datasets/CIHP/labels_rev/{fn_base}.png')

    wf1.write(f"/images/{fn_base}.jpg /labels/{fn_base}.png\n")
    wf2.write(f"{fn_base}\n")