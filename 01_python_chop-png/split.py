
import os
import sys
from PIL import Image
from itertools import product

x=8
y=16
indir='.'

# the input output directory, eg. outdir='svgz'.
outdir=sys.argv[2]

# the input file name, eg. fname='exported_v00.png'.
fname=sys.argv[1]

# create the output directory if it doesn't exist.
is_exists = os.path.exists(outdir)
if not is_exists:
   os.makedirs(outdir)

def tile(filename, dir_in, dir_out, x, y):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    
    grid = product(range(0, h-h%y, y), range(0, w-w%x, x))
    count=0
    for i, j in grid:
        count=count+1
        box = (j, i, j+x, i+y)
        out = os.path.join(dir_out, f'{str(count).zfill(3)}_{str(i).zfill(3)}-{str(j).zfill(3)}{ext}')
        img.crop(box).save(out)

if __name__ == "__main__":
    tile(fname, indir, outdir, x, y)
