import psycopg2

def create(conn, id, word, theme):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Words (id, word, theme)
            VALUES (%s, %s, %s)
        ''', (id, word, theme))
        conn.commit()
        print("Word created successfully.")
    except psycopg2.Error as e:
        
        print(f"Error inserting word: {e}")