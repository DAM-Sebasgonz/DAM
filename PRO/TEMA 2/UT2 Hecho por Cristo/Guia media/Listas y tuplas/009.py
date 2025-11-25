'''Crea un programa que pida un número al usuario que representa un número 
de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del 
mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.'''
MESES=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
DIAS=[31,28,31,30,31,30,31,31,30,31,30,31]
eleccion=int(input("Escribe un nº de mes (ejemplo, si es abril escribe 4): > "))
for mes in range(len(MESES)+1):
    if mes==eleccion:
        print(f"El mes de {MESES[mes-1]} tiene", end='')
        for dia in range(len(DIAS)+1):
            if dia==eleccion:
                print(f" {DIAS[dia-1]} días.")

