# Importamos FastAPI para crear la API
from fastapi import FastAPI

# Importamos módulos para trabajar con archivos y seleccionar excusas aleatorias
import json
import random

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Abrimos el archivo frases.json en modo lectura y codificación utf-8
# Cargamos el contenido en la variable 'excusas'
with open("excusas.json", "r", encoding="utf-8") as file:
    excusas = json.load(file)

# Ruta principal: muestra un mensaje de bienvenida
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de excusas comunes"}

# Ruta para obtener todas las frases del archivo
@app.get("/excusas")
def get_frases():
    return excusas

# Ruta para obtener una frase aleatoria de la lista
@app.get("/excusas/random")
def get_frase_random():
    return random.choice(excusas)