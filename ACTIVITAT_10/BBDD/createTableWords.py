import psycopg2


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Words (
                id INT PRIMARY KEY NOT NULL UNIQUE,
                word VARCHAR(50) NOT NULL,
                theme VARCHAR(50) NOT NULL
            )
        ''')
    except (Exception, psycopg2.Error) as error:
        
        print("Error",error)