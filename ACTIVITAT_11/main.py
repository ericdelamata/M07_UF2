from fastapi import FastAPI
from typing import List
import ACTIVITAT_11.BD.actions as actions
import schemas


app = FastAPI()


@app.get("/")
async def root():
   return {"message":"Benvingut a fastapi"}


@app.get("/penjat/tematica/options", response_model = List[dict])
async def get_options():
   return schemas.options_schema(actions.options_theme())


@app.get("/penjat/tematica/{option}", response_model = List[dict])
async def get_word(option: str):
   word = schemas.options_schema(actions.read_word_db(option))
   print("")
   print("IMPRESSIÓ WORD del mètode GET_WORD")
   print(type(word))
   print(word)
  
   return word

#Necessitem primer saber les opcions de llengua que hi ha per poder retornar el text, sino es podria hardcodejar i ja esta.
@app.get("/penjat/game/language/options", response_model = List[dict])
async def get_language_options():
   return schemas.options_schema(actions.options_language())

@app.get("/penjat/game/{id}/image", response_model = List[dict])
async def get_image_number(game_id: int):
   image_number = schemas.image_number(actions.get_trys(game_id))
   
   return image_number

#poso tot el text a renderitzar en aquest endpoint sense el de començar partida
@app.get("/penjat/game/info/{language}", response_model = List[dict])
async def get_texts():
   
   return schemas.options_schema(actions.options())