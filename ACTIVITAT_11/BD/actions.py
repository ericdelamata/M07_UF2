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

def options_theme():
    query = "SELECT theme FROM Words GROUP BY theme"

    df = pd.read_sql_query(query, conn)

    return df['theme']

def get_trys(id):
    
    cursor = conn.cursor();
    
    query = "SELECT trys FROM Game WHERE id = %s"
    cursor.execute(query,id)
    
    trys = cursor.fetchone()
    
    return trys[0]
    
    

def options_language():
    query = "SELECT name FROM Language GROUP BY theme"

    df = pd.read_sql_query(query, conn)

    return df['name']

def read_word_db(option):

   cursor = conn.cursor()

   sql = "SELECT word FROM Words WHERE theme = %s;"
   values = (option,)
   cursor.execute(sql, values)


   options = cursor.fetchall()
   option = options[np.random.randint(len(options))]


   return option