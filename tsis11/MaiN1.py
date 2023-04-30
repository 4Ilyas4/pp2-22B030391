
import psycopg2
import csv
import re
file = open("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis11\\PhoneList1.csv", "r")
bdata = list(csv.reader(file, delimiter=";"))
data = [tuple(row) for row in bdata]
lastnone = len(data) - 1
data.pop(lastnone)
file.close()
def isal(strg):
    return bool(re.findall('[a-zA-Z]', str(strg)))
def printuser(name):
    connection = psycopg2.connect(    
        database="firstdb",
        user="postgres",
        password="4PraeToriaN4",
        host="localhost",
        port="5432")
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil where name LIKE %s",[name])
        rec = cur.fetchall()
    for row in rec:
        print("#byname")
        print("ID ",row[0])
        print("Name: ",row[1])
        print("Phone: ",row[2])   
        print("#")       
def print_table():  
      connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
      with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil")
        rec = cur.fetchall()
      for row in rec:
        print("ID ",row[0])
        print("Name: ",row[1])
        print("Phone: ",row[2])
def lastid():
    l = []
    connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil")
        rec = cur.fetchall()
    for row in rec:
        l.append(int(row[0]))
    return max(l,default=0)
def retid(name):

    connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil")
        rec = cur.fetchall()
    for row in rec:
        if row[1] == str(name):
            return row[0]
def retidl(namelist):
    ln = []
    connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profil")
        rec = cur.fetchall()
    for row in rec:
        for name in namelist:
            if row[1] == str(name):
                ln.append(row[0])
    return ln
def deleteall():
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        sql_delete_query = """TRUNCATE profil""" 
        cursor.execute(sql_delete_query)
        connection.commit()
        count = cursor.rowcount
        print("all deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
def deleteData(id):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        # Update single record now
        sql_delete_query = """Delete from profil where id = %s"""
        cursor.execute(sql_delete_query, id,)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
def printlim(a,b):
    conn = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_users(%s, %s);", (a, b)) 
    rows = cur.fetchall()
    print(rows)
    conn.commit()
    cur.close()
    conn.close()
def deletebyphornm(text):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        if isal(text):
            cursor.callproc("delete_user", [text,None])
        else:
            cursor.callproc("delete_user", [None,text])
        connection.commit()
        print("Record deleted successfully into profile table")
      
    except (Exception, psycopg2.Error) as error:
        print("Failed deleting record into profil table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
def bulkInsert(rec):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        
        sql_insert_query = """ INSERT INTO profil (id, name, phone) VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows
        cursor.executemany(sql_insert_query , rec)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into profile table")
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into profil table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
def bulkInsertNMPH(recnmph):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()

        #sql_insert_query = """ INSERT INTO profil (id, name, phone) VALUES (%s,%s,%s) """
        inc = False
        # executemany() to insert multiple rows
        incorrect = []
        for i in recnmph:
            if len(i[1])>11 or len(i[1])<11 or isal(str(i[1])):
                inc = True
                incorrect.append(i[1])
            else:
                cursor.callproc("insert_user", i)
                connection.commit()
                print("Records inserted successfully into profile table")
        if inc:
            print("Неправильно набранны номера:")
            for i in incorrect:
                print(i)
                print("    ")
            incorrect = []
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into profil table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
def CheckN(name):
    conn = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT id FROM profil WHERE name = %s", (name,))
    return cur.fetchone() is not None
def Check(ID):
    conn = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT id FROM profil WHERE id = %s", (ID,))
    return cur.fetchone() is not None
def update(records):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        sql_update_query = """ UPDATE profil SET  name = %s, phone = %s WHERE id = %s;
                            """
        result = cursor.executemany(sql_update_query, records)
        connection.commit()
        print(cursor.rowcount, "Record updated successfully into profil table")

    except (Exception, psycopg2.Error) as error:
        print("Failed updateing record into profil table {}".format(error))
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

print(" Изначальная таблица : ")
print_table()
print(" Если хотите загрузить через csv напишите 1 или через терминал напишите 2 ,если хотите удалять данные через id пишите 3 через имя или телефон 4 все удалить 5 показать телефон через имя 6 print table with limits 7: ")
ref = str(input())
rdata = []

if ref == "1":
    bulkInsert(data)
elif ref == "2":
    rdata = []
    temp = []
    s = ""
    print("введите число строк :")
    n = int(input())
    print("Вводите данные через пробел (без id):")
    for i in range(n):  
        r = str(input()) + " "
        for i in r:
            if i != " ":
                s+=str(i)
            else:
                temp.append(s)
                s = ""
        rdata.append(tuple(temp))
        temp = []
    
    bulkInsertNMPH(rdata)

    
elif ref == "3":
    print("Введите через пробел id шки : ")
    f = str(input())
    nr = f.split() 
    for i in nr:
        deleteData(i)
elif ref == "4":
    print("Введите имя или телефон")
    tex = str(input())
    deletebyphornm(tex)

elif ref == "5":
    deleteall()
elif ref == "6":
    print("Name?:")
    nam = str(input())
    printuser(nam)
elif ref == "7":
    print("Input limits")
    a = int(input())
    b = int(input())
    printlim(a,b)