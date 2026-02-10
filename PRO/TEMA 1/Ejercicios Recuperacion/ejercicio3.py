dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

a = (14 - mes) // 12
y = año - a
m = mes + 12 * a - 2

if año < 1582 or (año == 1582 and mes < 10) or (año == 1582 and mes == 10 and dia < 15):
    d = (5 + dia + y + (y // 4) + (31 * m // 12)) % 7
else:
    d = (dia + y + (y // 4) - (y // 100) + (y // 400) + (31 * m // 12)) % 7

if d == 0:
    print("El día de la semana es: Domingo")
elif d == 1:
    print("El día de la semana es: Lunes")
elif d == 2:
    print("El día de la semana es: Martes")
elif d == 3:
    print("El día de la semana es: Miércoles")
elif d == 4:
    print("El día de la semana es: Jueves")
elif d == 5:
    print("El día de la semana es: Viernes")
elif d == 6:
    print("El día de la semana es: Sábado")