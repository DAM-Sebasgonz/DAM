def es_multiplo_de_5(n: int) -> bool:
    return n % 5 == 0

print("Bienvenido/a a ETS")
edad_str = input("Introduce tu edad: ")

try:
    edad = int(edad_str)
except ValueError:
    print("Edad no válida. Debe ser un número entero.")
    raise SystemExit(1)

if edad >= 18:
    print("bienvenido al club, amigo")
    a = int(input("Introduce el primer entero: "))
    b = int(input("Introduce el segundo entero: "))
    print(f"{a} es múltiplo de 5" if es_multiplo_de_5(a) else f"{a} no es múltiplo de 5")
    print(f"El cubo de {b} es {b ** 3}")
else:
    print("lo siento chaval")
