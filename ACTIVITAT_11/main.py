from fastapi import FastAPI
from typing import List
#from pydantic import BaseModel
import BD.read as read
import schemas


app = FastAPI()


# class Option(BaseModel):
#     theme: str
#
# class word(BaseModel):
#     word: str


@app.get("/")
async def root():
   return {"message":"Benvingut a fastapi"}




# Mètode per extreure les 5 opcions i podre-les mostrar a la llista de selecció d'opcions del penjat
@app.get("/penjat/tematica/opcions", response_model = List[dict])
async def get_options():
   return schemas.options_schema(read.options())






# En aquesta consulta get ecaldrà que el frontend envii a {option} la opció seleccionada en la llista del joc
@app.get("/penjat/tematica/{option}", response_model = List[dict])
async def get_word(option: str):
   word = schemas.options_schema(read.read_word_db(option))
   print("")
   print("IMPRESSIÓ WORD del mètode GET_WORD")
   print(type(word))
   print(word)
  
   return word
