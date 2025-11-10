# Ejercicio 010:
# Escribe un programa que pregunte la distancia que un pasajero desea recorrer en kilómetros.
# Calcula el precio del billete, cobrando 0,50 $ por km para viajes de hasta 200 km y 0,45 $
# para viajes más largos.

distancia = float(input("distancia a recorrer (km):"))

if distancia <= 200.0:
    precio_billete = distancia * 0.5
else:
    precio_billete = distancia * 0.45
print("el precio del billete es de", precio_billete, "€")
