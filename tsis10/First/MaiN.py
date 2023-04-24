
import psycopg2
import csv
file = open("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B030391\\tsis10\\First\\PhoneList.csv", "r")
bdata = list(csv.reader(file, delimiter=";"))
data = [tuple(row) for row in bdata]
lastnone = len(data) - 1
data.pop(lastnone)
file.close()
def print_table():  
      connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
      with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM profile")
        rec = cur.fetchall()
      for row in rec:
        print("ID ",row[0])
        print("Name: ",row[1])
        print("Phone: ",row[2])

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
        sql_delete_query = """Delete from profile where id = %s""" #можно сделать так чтобы она удоляла всю таблицу если убрать where и все что после нее и id
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

def bulkInsert(records):
    try:
        connection = psycopg2.connect(    
            database="firstdb",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO profile (id, name, phone) VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into profile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into profile table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

print(" Изначальная таблица : ")
print_table()
print(" Если хотите загрузить через csv напишите 1 или через терминал напишите 2 ,если хотите удалять данные пишите 3: ")
re = str(input())
rdata = []
if re == "1":
    bulkInsert(data)
elif re == "2":
    rdata = []
    temp = []
    s = ""
    print("введите число строк :")
    n = int(input())
    print("Вводите данные через пробел :")
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
    bulkInsert(rdata)
elif re == "3":
    print("Введите количество строк которые собираетесь удалять : ")
    nr = int(input())
    print("Пишите id строк которые собираетеь удалять через enter : ")
    for i in range(nr):
        idr = str(input())
        deleteData(idr)
