# Escribe un programa que calcule la duración de un viaje en coche. Pregunta la distancia a
# recorrer y la velocidad media prevista para el viaje.

distancia = float(input("Introduzca la distancia a recorrer(KM): "))
velocidad = float(input("Introduzca la velocidad media(KM/H): "))

duracion_viaje = distancia // velocidad

print (f"El viaje ha de durar {duracion_viaje} horas")