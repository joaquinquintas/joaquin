

from os import listdir, rename
from os.path import isfile, join
import Image


if __name__ == "__main__":
    mypath = "./clasicos/"
    for f in listdir(mypath):
        print f
        if f == ".DS_Store":
            continue
        im = Image.open(mypath+f)
        width, height = im.size   # Get dimensions
        new_height = 166
        left = 0
        top = 415
        height = 166
        box = (left, top, left+width, top+height)

        crop = im.crop(box)
        crop.save(mypath+f.split(".")[0]+"_crop", "jpeg")


if __name__ == "__main__1":
    mypath = "clasicos"

    for f in listdir("."):
        print f, f.lower()
        rename(f, "_"+f.lower())


if __name__ == "__main__3":
    mypath = "./clasicos/"
    for f in listdir(mypath):
        im = Image.open(mypath+f)
        im.save(mypath+f.split(".")[0] +".jpg", quality=90)
