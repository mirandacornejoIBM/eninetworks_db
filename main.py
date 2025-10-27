from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("df_transcripciones.csv")

@app.get("/")
def root():
    return {"message": "API de df_transcripciones.csv lista"}

@app.get("/data")
def get_data():
    """
    Devuelve todo el contenido del CSV en formato JSON
    """
    return df.to_dict(orient="records")
