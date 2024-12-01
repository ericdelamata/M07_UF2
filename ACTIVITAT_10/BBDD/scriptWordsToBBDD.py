import psycopg2
from readCSV import readCSVasDicitionary
from connect import connect
from createTableWords import create_table
from insertRecords import create

conn = connect()

d = readCSVasDicitionary()

create_table(conn)

for i in range(len(d.get("WORD"))):
    create(conn, i, d.get("WORD")[i], d.get("THEME")[i])

conn.close()