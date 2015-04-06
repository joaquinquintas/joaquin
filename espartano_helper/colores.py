import csv

if __name__ == "__main__":        
    #tmp = 'db.execSQL(insert into Colores (id, color, order, set) VALUES (' + "'" + "%s","%s",%s,%s)");'

    f = open('bandeja1.csv', 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    count = 1
    for row in csv_f:
        row = row[0].split(",")
        #result = tmp %(row[1], row[0], count, 1)

        print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +row[1] + "'," + "'" +row[0] + "'," + str(count)+  ', 1)");'
        count = count + 1

    f = open('bandeja2.csv', 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    count = 1
    for row in csv_f:
        row = row[0].split(",")
        #result = tmp %(row[1], row[0], count, 1)

        print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +row[1] + "'," + "'" +row[0] + "'," + str(count)+  ', 2)");'
        count = count + 1

    f = open('bandeja3.csv', 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    count = 1
    for row in csv_f:
        row = row[0].split(",")
        #result = tmp %(row[1], row[0], count, 1)

        print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +row[1] + "'," + "'" +row[0] + "'," + str(count)+  ', 3)");'
        count = count + 1

    f = open('bandeja4.csv', 'rU')
    csv_f = csv.reader(f, dialect=csv.excel_tab)

    count = 1
    for row in csv_f:
        row = row[0].split(",")
        #result = tmp %(row[1], row[0], count, 1)

        print 'db.execSQL("insert into Colores (id, color, pos, grupo) VALUES (' + "'" +row[1] + "'," + "'" +row[0] + "'," + str(count)+  ', 4)");'
        count = count + 1