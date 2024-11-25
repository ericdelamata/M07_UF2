import psycopg2

def create(conn, word, theme):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Words (word, theme)
            VALUES (%s, %s)
        ''', (word, theme))
        conn.commit()
        print("Word created successfully.")
    except psycopg2.Error as e:
        
        print(f"Error inserting word: {e}")