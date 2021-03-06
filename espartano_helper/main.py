

from os import listdir, rename, makedirs
from os.path import isfile, join, exists
import Image

"""
Generar INSERT

db.execSQL("insert into Texturas (codigo, id_coleccion, colores, imagen, imagen_crop, posicion, compatibles) VALUES ('2A',1,'B7807B,','classic_2a', '_2a_crop', 2,'classic_2c')");

"""
import csv



def _colores_transformation():
    color_dict = _merge_colores()
    #print color_dict
    f = open("compatibles/colores.csv", 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    r_dict = {}
    count = 0
    for row in csv_f:
        row = row[0].split(",")
        trans = []
        for c in row[1:]:
            try:
                trans.append(color_dict[c])
            except:
                count = count +1
                print c
        r_dict[row[0].lower()] = ",".join(trans)
    
    print count
    return r_dict

def _get_color_code(mypath):
    f = open(mypath, 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    result = []
    r_dict = {}
    for row in csv_f:
        row = row[0].split(",")
        result.append(row[1])
        r_dict[row[1]] = row[0]
        
    return result, r_dict

def _merge_colores():
    c1,d1 =  _get_color_code('colores/bandeja1.csv')
    c2,d2 =  _get_color_code('colores/bandeja2.csv')
    c3,d3 =  _get_color_code('colores/bandeja3.csv')
    c4,d4 =  _get_color_code('colores/bandeja4.csv')
    
    color_dict = d1.copy()
    color_dict.update(d2)
    color_dict.update(d3)
    color_dict.update(d4)
    
    return color_dict

def _get_compatible(mypath):
    f = open(mypath, 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    r_dict = {}
    for row in csv_f:
        row = row[0].split(",")
        r_dict[row[0].lower()] = ",".join(row[1:])
        
    return r_dict

def _merge_compatible():
    d1 =  _get_compatible('compatibles/clasicos.csv')
    d2 =  _get_compatible('compatibles/contemporaneos.csv')
    d3 =  _get_compatible('compatibles/etnicos.csv')
    d4 =  _get_compatible('compatibles/organicos.csv')
    d5 =  _get_compatible('compatibles/small_patterns.csv')
    
    compa_dict = d1.copy()
    compa_dict.update(d2)
    compa_dict.update(d3)
    compa_dict.update(d4)
    compa_dict.update(d5)
    
    return compa_dict
    

no_colores = []
no_compatibles = []
                  
def _generate_images(mypath, collection,  compa_dict, colores):
    process_path = "process/"
    if not exists(process_path):
        makedirs(process_path)
    
    count = 0
    for f in listdir(mypath):
        
        if f == ".DS_Store":
            continue
        if isfile(mypath+f):
            im = Image.open(mypath+f)
            name = f.split(".")[0] 
            name_crop = name+ "_crop"
            im.save( process_path+name.lower()+".jpg", quality=87)
            count = count + 1
            
            try:
                colores_ = colores[name.lower()]
            except:
                no_colores.append(name)
                colores_ = ""
            
            try:
                compatibles = compa_dict[name.lower()]
            except:
                compatibles= ""
                no_compatibles.append(name)
                
            print 'db.execSQL("insert into Texturas (codigo, id_coleccion, colores, imagen, imagen_crop, posicion, compatibles) VALUES (' + "'" +name + "'," + "'" +collection + "'," + "'" +colores_ + "'," + "'" +name.lower() + "'," + "'" +name_crop.lower() + "'," + str(count) + ",'" +compatibles +"'"+')");'
        
    for f in listdir(mypath):
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
            crop.save(process_path+f.split(".")[0].lower()+"_crop.jpg", "jpeg", quality=87)


if __name__ == "__main__":
    clasicos = "clasicos/"
    contemporaneos = "contemporaneos/"
    etnicos = "etnicos/"
    organicos = "organicos/"
    small_patterns = "small_patterns/"
    compatibles = _merge_compatible()
    #print compatibles
    colores = _colores_transformation()
    #print colores
    _generate_images(clasicos, "1",compatibles,colores)
    _generate_images(contemporaneos, "2",compatibles,colores)
    _generate_images(etnicos, "3",compatibles,colores)
    _generate_images(organicos, "4", compatibles,colores)
    _generate_images(small_patterns, "5", compatibles,colores)
    
    print ""
    print "-------"
    print ""
    print "Texturas sin colores en la planilla"
    print ""
    print no_colores
    print ""
    print "-------"
    print "Texturas sin compatibles en la planilla"
    print ""
    print no_compatibles 
    print ""


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
