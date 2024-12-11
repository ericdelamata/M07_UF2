

def CreateUsers(conn):
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Users;
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY NOT NULL UNIQUE,
            name VARCHAR(50) NOT NULL,
            games_played INT NULL,
            won_games INT NULL,
            id_current_game INT NULL,
            id_best_game INT NULL
        );
    ''')
    print("Table Users created succesfully!")
    
def CreateGame(conn):
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Game;
        CREATE TABLE IF NOT EXISTS Game (
            id SERIAL PRIMARY KEY NOT NULL UNIQUE,
            Score INT NULL,
            trys INT NULL,
            dateTime TIMESTAMP NOT NULL,
            id_player1 INT NOT NULL,
            id_player2 INT NOT NULL
        );
    ''')
    print("Table Game created succesfully!")
    
def CreateWords(conn):
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Words;
        CREATE TABLE IF NOT EXISTS Words (
            id SERIAL PRIMARY KEY NOT NULL UNIQUE,
            word VARCHAR(50) NOT NULL,
            theme VARCHAR(50) NOT NULL,
            id_language INT NOT NULL
        );
    ''')
    print("Table Words created succesfully!")
    
def CreateLanguage(conn):
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Language;
        CREATE TABLE IF NOT EXISTS Language (
            id SERIAL PRIMARY KEY NOT NULL UNIQUE,
            name VARCHAR(50) NOT NULL,
            alphabet VARCHAR(50) NOT NULL,
            startGame VARCHAR(50) NOT NULL
        );
    ''')
    print("Table Language created succesfully!")
    
def AddConstraints(conn):
    cursor = conn.cursor()
    cursor.execute('''
        ALTER TABLE Users
        ADD FOREIGN KEY (id_current_game) REFERENCES Game(id);
        ALTER TABLE Users
        ADD FOREIGN KEY (id_best_game) REFERENCES Game(id);
        ALTER TABLE Game
        ADD FOREIGN KEY (id_player1) REFERENCES Users(id);
        ALTER TABLE Game
        ADD FOREIGN KEY (id_player2) REFERENCES Users(id);
        ALTER TABLE Word
        ADD FOREIGN KEY (id_language) REFERENCES Language(id);
        ''')
    print("Constraints added succesfully!")