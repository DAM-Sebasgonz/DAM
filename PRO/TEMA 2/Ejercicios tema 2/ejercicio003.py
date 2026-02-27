
plantilla = "Hola {nombre}, te recordamos que tu saldo es {saldo} euros. Tu asesor es {asesor}."

usuarios = [
    {"nombre": "María", "saldo": 150, "asesor": "Pedro"},
    {"nombre": "Juan", "saldo": 0},
    {"nombre": "Lucía", "asesor": "Ana"}
]

mensajes = []

for usuario in usuarios:

    resultado = ""
    i = 0

    while i < len(plantilla):
        if plantilla[i] == '{':
            j = i + 1
            nombre_campo = ""
            while j < len(plantilla) and plantilla[j] != '}':
                nombre_campo += plantilla[j]
                j += 1

            if nombre_campo in usuario:
                resultado += str(usuario[nombre_campo])
            else:
                resultado += "N/D"

            i = j + 1  
        else:
            resultado += plantilla[i]
            i += 1

    mensajes.append(resultado)

for mensaje in mensajes:
    print(mensaje)
