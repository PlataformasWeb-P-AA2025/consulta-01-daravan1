from pymongo import MongoClient

# Conexión a MongoDB local 
cliente = MongoClient("mongodb://localhost:27017/")

# Base de datos y colección
db = cliente["torneo"]
coleccion = db["partidos"]

#Consulta 02: Partidos en los que el ranking del perdedor fue mayor que 
#el del ganador por al menos 100 puestos

resultados = coleccion.find({
    "$expr": { "$gt": [{"$subtract": ["$WRank", "$LRank"] }, 100]}  #Se usa $expr para comparar dos campos del mismo documento (WRank y LRank).
})

print("Partidos donde el ganador tenía un ranking menor al del perdedor por al menos 100 puestos:\n")
for p in resultados:
    print(f"- {p.get('Date')} | {p.get('Winner')} (Rank {p.get('WRank')}) venció a {p.get('Loser')} (Rank {p.get('LRank')})")
