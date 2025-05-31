import pandas as pd
from pymongo import MongoClient
import glob

# Conexión a MongoDB local 
cliente = MongoClient("mongodb://localhost:27017/")

# Base de datos y colección
db = cliente["torneo"]
coleccion = db["partidos"]

# Ruta de archivos excel en la carpeta 'data'
archivos = glob.glob("data/*.xlsx")

for archivo in archivos:
    print(f"Procesando: {archivo}") # Mensaje para saber que archivo se esta cargando
    
    # Leer archivo Excel
    df = pd.read_excel(archivo)

    # Convertir fechas a texto
    for col in df.select_dtypes(include=["datetime"]):
        df[col] = df[col].astype(str)

    # Reemplazar valores inválidos
    df = df.replace([float('inf'), float('-inf')], pd.NA) 
    df = df.where(pd.notnull(df), None)

    # Convertir a diccionarios y cargar
    documentos = df.to_dict(orient='records')
    if documentos:
        coleccion.insert_many(documentos)
        print(f"Insertados {len(documentos)} documentos")
    else:
        print(f"No se pudo extraer informacion de {archivo}")

print("Carga Completa")
