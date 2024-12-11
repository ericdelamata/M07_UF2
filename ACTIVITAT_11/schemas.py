
    
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
    
def text_render() -> dict:
    "user"
    