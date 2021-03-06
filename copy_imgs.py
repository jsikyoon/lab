import os
from PIL import Image
files = [f for f in os.listdir('.') if f.endswith('jpg') or f.endswith('JPG')]
for i, file in enumerate(sorted(files)):
  im = Image.open(file)
  im.save('../%04d.png' % (i+1))
