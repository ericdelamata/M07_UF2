import createTables as ct
from connect import connect

conn = connect()

ct.CreateGame(conn)
ct.CreateUsers(conn)
ct.CreateWords(conn)
ct.CreateLanguage(conn)
ct.AddConstraints(conn)

print("Everything went well!")

conn.commit()
conn.close()