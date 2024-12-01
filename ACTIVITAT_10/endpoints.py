from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from BBDD.connect import connect

app = FastAPI()

class Theme(BaseModel):
    option: str

class Word(BaseModel):
    option: str

conn = connect()

@app.get("/penjat/tematica/opcions", response_model=list[Theme])
async def tematiques():
    cursor = conn.cursor()
    cursor.execute('SELECT theme FROM Words GROUP BY theme')
    themes = cursor.fetchall()
    return [{"option": theme[0]} for theme in themes]


@app.get("/penjat/tematica/{option}", response_model=list[Word])
async def get_word_by_theme(option: str):
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM Words WHERE theme= '%s' ORDER BY RANDOM() LIMIT 1"%option)
    word = cursor.fetchone()

    if not word:
        raise HTTPException(status_code=404, detail="Theme not found")

    return [{"option": word[0]}]