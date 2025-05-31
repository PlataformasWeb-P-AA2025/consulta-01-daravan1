from pymongo import MongoClient

# Conexión a MongoDB local 
cliente = MongoClient("mongodb://localhost:27017/")

# Base de datos y colección
db = cliente["torneo"]
coleccion = db["partidos"]

# Consulta 01: Mostrar partidos del torneo "Adelaide International" en 2022 ganados
# por el jugador Khachanov K

# Nombre de jugador 
jugador = "Khachanov K"

# Consulta: partidos ganados por el jugador en el torneo y año especificado
resultados = coleccion.find({
    "Tournament": "Adelaide International 1",
    "Winner": "Khachanov K.",
    "Date": { "$regex": "^2022" }  # Filtra fechas que comienzan con "2022"
})

# Mostrar resultados legibles
print(f"Partidos ganados por {jugador} en Adelaide International 1 (2022):\n")
for partido in resultados:
    fecha = partido.get("Date", "Fecha desconocida")
    rival = partido.get("Loser", "Jugador desconocido")
    ronda = partido.get("Round", "Ronda desconocida")
    sets = partido.get("Wsets", "?")
    print(f"En {fecha}: venció a {rival} en la ronda {ronda} con {sets} sets ganados.")