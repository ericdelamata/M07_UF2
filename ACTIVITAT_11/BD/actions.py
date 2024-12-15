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
    
    cursor = conn.cursor()
    
    query = "SELECT trys FROM Game WHERE id = %s"
    cursor.execute(query,id)
    
    trys = cursor.fetchone()
    
    return trys[0]

def get_alphabet(language):
    cursor = conn.cursor()
    
    query = "SELECT alphabet FROM Language WHERE name = %s"
    cursor.execute(query,language)
    
    alphabet = cursor.fetchone()
    
    return alphabet[0]
    

def get_text(id_user):
    
    cursor = conn.cursor()
    
    query = "SELECT scoreCurrentText, totalGamesText, wonGamesText, bestGameText FROM Language, Game, Words, Users WHERE Users.id = %s AND Users.id_current_game = Game.id AND Game.word_id = Words.id and Words.id_language = Language.id"
    cursor.execute(query,id_user)
    
    text_render = cursor.fetchone()
    
    return text_render
    
def get_best_game_date(id_user):
    cursor = conn.cursor()
     
    query = "SELECT dateTime FROM Game, Users WHERE Users.id = %s AND Users.id_best_game"
    cursor.executed(query,id_user)
     
    date = cursor.fetchone()
     
    return date[0]

def get_best_game_score(id):
    cursor = conn.cursor()
    
    query = "SELECT score FROM Game, Users WHERE Users.id = %s AND Users.id_best_game"
    cursor.execute(query,id)
    
    score_best_game = cursor.fetchone()
    
    return score_best_game[0]
    
def get_current_score(id):
    cursor = conn.cursor()
    
    query = "SELECT score FROM Game, Users WHERE Users.id = %s AND Users.id_current_game"
    cursor.execute(query,id)
    
    score_current_game = cursor.fetchone()
    
    return score_current_game[0]

def get_user_info(id):
    cursor = conn.cursor()
    
    query = "SELECT name,games_played,won_games FROM Users WHERE id = %s"
    cursor.execute(query,id)
    
    won_games = cursor.fetchone()
    
    return won_games[0]

def get_start_game(language):
    cursor = conn.cursor()
    
    query = "SELECT startGame FROM Language WHERE id = %s"
    cursor.execute(query,language)
    
    start_game_text = cursor.fetchone()
    
    return start_game_text[0]


def options_language():
    query = "SELECT name FROM Language GROUP BY name"

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