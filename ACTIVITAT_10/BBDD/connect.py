import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
        database="postgres",
        user="user_postgres",
        password="pass_postgres",
        host="localhost",
        port="5432"
        )

        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error",error)