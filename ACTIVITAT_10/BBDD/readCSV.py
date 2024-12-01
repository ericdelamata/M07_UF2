import pandas as pd


def readCSVasDicitionary():
    
    df = pd.read_csv("ACTIVITAT_10\paraules_tematica_penjat.csv")
    d = df.to_dict()
    
    return d