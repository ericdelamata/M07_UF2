

def user_schema(id,name,games_played,won_games,id_current_game,id_best_game) -> dict:
    return{
        "id": id,
        "name": name,
        "games_played": games_played,
        "won_games": won_games,
        "id_current_game": id_current_game,
        "id_best_game": id_best_game
    }
    

def game_schema(id,score,trys,datetime,id_player1,id_player2) -> dict:
    return{
        "id": id,
        "score": score,
        "trys": trys,
        "datetime": datetime,
        "id_player1": id_player1,
        "id_player2": id_player2
    }
    
def word_theme_schema(option) -> dict:
    return{
        "option":option
    }
    
def options_schema(options) -> dict:
   return [word_theme_schema(option) for option in options]
