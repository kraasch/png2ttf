
import os
from PIL import Image
from itertools import product

x=8
y=16
fname='exported_v00.png'
indir='.'
outdir='exp'

def tile(filename, dir_in, dir_out, x, y):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    
    grid = product(range(0, h-h%y, y), range(0, w-w%x, x))
    count=0
    for i, j in grid:
        count=count+1
        box = (j, i, j+x, i+y)
        out = os.path.join(dir_out, f'{name}_{count}_{i}-{j}{ext}')
        img.crop(box).save(out)


tile(fname, indir, outdir, x, y)
