
    
def option_schema(option) -> dict:
    return{
        "option":option
    }
    
def options_schema(options) -> dict:
   return [option_schema(option) for option in options]

#podem saber el numero de la imatge pel numero d'intents
def image_number(trys) -> dict:
    return{
        "image number":trys
    }
    
def text_render(user_name,score_current_text,current_score,total_games_text,total_games,won_games_text,won_games,best_game_text,best_game_date,best_game_score) -> dict:
    return{
        "user":user_name,
        score_current_text:current_score,
        total_games_text:total_games,
        won_games_text:won_games,
        best_game_text:best_game_date+" - "+best_game_score
    }
    