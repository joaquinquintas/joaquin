

from os import listdir, rename, makedirs
from os.path import isfile, join, exists
import Image

"""
Generar INSERT

db.execSQL("insert into Texturas (codigo, id_coleccion, colores, imagen, imagen_crop, posicion, compatibles) VALUES ('2A',1,'B7807B,','classic_2a', '_2a_crop', 2,'classic_2c')");

"""

def _generate_images(mypath):
    process_path = mypath+"process/"
    if not exists(process_path):
        makedirs(process_path)
    
    print mypath
    for f in listdir(mypath):
        print f
        if f == ".DS_Store":
            continue
        if isfile(mypath+f):
            im = Image.open(mypath+f)
            im.save(process_path+f.split(".")[0] +".jpg", quality=90)
        
    for f in listdir(mypath):
        print f
        if f == ".DS_Store":
            continue
        if isfile(mypath+f):
                
            im = Image.open(mypath+f)
            width, height = im.size   # Get dimensions
            new_height = 166
            left = 0
            top = 415
            height = 166
            box = (left, top, left+width, top+height)
    
            crop = im.crop(box)
            crop.save(process_path+f.split(".")[0]+"_crop.jpg", "jpeg")


if __name__ == "__main__":
    clasicos = "clasicos/"
    contemporaneos = "contemporaneos/"
    etnicos = "etnicos/"
    organicos = "organicos/"
    small_patterns = "small_patterns/"
    _generate_images(clasicos)
    _generate_images(contemporaneos)
    _generate_images(etnicos)
    _generate_images(organicos)
    _generate_images(small_patterns)



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
