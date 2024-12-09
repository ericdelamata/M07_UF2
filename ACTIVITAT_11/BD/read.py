#import connect
import psycopg2
import pandas as pd
import numpy as np


conn = psycopg2.connect(
        database="postgres",
        user="user_postgres",
        password="pass_postgres",
        host="localhost",
        port="5432"
        )

def options():
    query = "SELECT theme FROM Word GROUP BY theme"

    df = pd.read_sql_query(query, conn)

    return df['theme']


def read_word_db(option):

   cursor = conn.cursor()

   sql = "SELECT word FROM paraules WHERE theme = %s;"
   values = (option,)
   cursor.execute(sql, values)


   options = cursor.fetchall()
   option = options[np.random.randint(len(options))]


   return option
