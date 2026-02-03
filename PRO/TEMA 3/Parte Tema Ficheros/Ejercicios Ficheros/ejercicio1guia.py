import json
import os
import random

fecha = input("Introduce la fecha de la jornada: ")

partidos = []

for i in range(1, 3):
    print(f"\nPartido {i}")
    equipo1 = input("Nombre del equipo 1: ")
    equipo2 = input("Nombre del equipo 2: ")
    goles1 = int(input(f"Goles de {equipo1}: "))
    goles2 = int(input(f"Goles de {equipo2}: "))

    partidos.append({
        "equipo1": equipo1,
        "equipo2": equipo2,
        "goles_equipo1": goles1,
        "goles_equipo2": goles2
    })

resultado_jornada = {
    "fecha": fecha,
    "partidos": partidos
}

with open("resultado_jornada.json", "w") as f:
    json.dump(resultado_jornada, f, indent=4)

print("\nArchivo resultado_jornada.json creado correctamente")

if os.path.exists("clasificacion.json"):
    with open("clasificacion.json", "r") as f:
        clasificacion = json.load(f)
else:
    clasificacion = {}

def crear_equipo(nombre):
    return {
        "equipo": nombre,
        "nro_partidos_jugados": 0,
        "nro_partidos_ganados": 0,
        "nro_partidos_empatados": 0,
        "nro_partidos_perdidos": 0,
        "goles_marcados": 0,
        "goles_recibidos": 0,
        "puntos": 0
    }

for p in partidos:
    e1 = p["equipo1"]
    e2 = p["equipo2"]
    g1 = p["goles_equipo1"]
    g2 = p["goles_equipo2"]

    if e1 not in clasificacion:
        clasificacion[e1] = crear_equipo(e1)
    if e2 not in clasificacion:
        clasificacion[e2] = crear_equipo(e2)

    eq1 = clasificacion[e1]
    eq2 = clasificacion[e2]

    eq1["nro_partidos_jugados"] += 1
    eq2["nro_partidos_jugados"] += 1

    eq1["goles_marcados"] += g1
    eq1["goles_recibidos"] += g2
    eq2["goles_marcados"] += g2
    eq2["goles_recibidos"] += g1

    if g1 > g2:
        eq1["nro_partidos_ganados"] += 1
        eq2["nro_partidos_perdidos"] += 1
        eq1["puntos"] += 3
    elif g1 < g2:
        eq2["nro_partidos_ganados"] += 1
        eq1["nro_partidos_perdidos"] += 1
        eq2["puntos"] += 3
    else:
        eq1["nro_partidos_empatados"] += 1
        eq2["nro_partidos_empatados"] += 1
        eq1["puntos"] += 1
        eq2["puntos"] += 1

clasificacion_lista = list(clasificacion.values())

def criterio(e):
    diferencia = e["goles_marcados"] - e["goles_recibidos"]
    return (
        -e["puntos"],
        -diferencia,
        -e["goles_marcados"],
        random.randint(1, 10)
    )

clasificacion_lista.sort(key=criterio)

with open("clasificacion.json", "w") as f:
    json.dump(clasificacion_lista, f, indent=4)

print("Archivo clasificacion.json actualizado correctamente")
