import psycopg2
from readCSV import readCSVasDicitionary
from BBDD.connect import connect
from BBDD.createTableWords import create_table
from BBDD.insertRecords import create

conn = connect()

d = readCSVasDicitionary()

create_table(conn)

for i in range(len(d.get("WORD"))):
    create(conn, d.get("WORD")[i], d.get("THEME")[i])
    
try:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Words')
    movies = cursor.fetchall()
    for movie in movies:
        print(movie)
except (Exception, psycopg2.Error) as error:
    print("Error",error)
conn.close()