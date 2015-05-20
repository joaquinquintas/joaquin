import csv

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
        
def _load_colores_from_file():
 
    f = open('colores/bandeja1.csv', 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    count = 1
    for row in csv_f:
        row = row[0].split(",")
        #result = tmp %(row[1], row[0], count, 1)

        print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +row[1] + "'," + "'" +row[0] + "'," + str(count)+  ', 1)");'
        count = count + 1

    f = open('colores/bandeja2.csv', 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    count = 1
    for row in csv_f:
        row = row[0].split(",")
        #result = tmp %(row[1], row[0], count, 1)

        print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +row[1] + "'," + "'" +row[0] + "'," + str(count)+  ', 2)");'
        count = count + 1

    f = open('colores/bandeja3.csv', 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    count = 1
    for row in csv_f:
        row = row[0].split(",")
        #result = tmp %(row[1], row[0], count, 1)

        print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +row[1] + "'," + "'" +row[0] + "'," + str(count)+  ', 3)");'
        count = count + 1

    f = open('colores/bandeja4.csv', 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    count = 1
    for row in csv_f:
        row = row[0].split(",")
        #result = tmp %(row[1], row[0], count, 1)

        print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +row[1] + "'," + "'" +row[0] + "'," + str(count)+  ', 4)");'
        count = count + 1
        
def _merge_colores(mypath):
    c1,d1 =  _get_color_code('colores/bandeja1.csv')
    c2,d2 =  _get_color_code('colores/bandeja2.csv')
    c3,d3 =  _get_color_code('colores/bandeja3.csv')
    c4,d4 =  _get_color_code('colores/bandeja4.csv')
    
    total_c = c1 + c2 + c3 + c4
    color_dict = d1.copy()
    color_dict.update(d2)
    color_dict.update(d3)
    color_dict.update(d4)
    
    colores_file = open(mypath, 'rU')
    csv_f = csv.reader(colores_file, dialect=csv.excel_tab)
    count_erros= 0
    count = 0 
    aux_pos = 1
    for row in csv_f:
        #print row
        row = row[0].split(",")
        #print row
        pos = row[7]
        if aux_pos != int(pos):
            count = 0
            aux_pos = int(pos)
        for color_code in row[:7]:
            count = count + 1
            color_code = color_code.replace(" ", "")
            
            if color_code not in total_c:
                count_erros = count_erros + 1
                color = color_code
            else:
                color = color_dict[color_code]
            print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +color_code+ "'," + "'" +color+ "'," + str(count)+  ',' +str(pos)+')");'
    
    print count_erros
            
    
if __name__ == "__main__":        
    #tmp = 'db.execSQL(insert into Colores (id, color, order, set) VALUES (' + "'" + "%s","%s",%s,%s)");'
    mypath = 'colores/colores.csv'
    _merge_colores(mypath)
    