lista=[[3,2,1],[4,2,0],[2,1,2],[2,1,1],[0,6,0]]

lista_mayores=[]
suma_mayor=0
for l in lista:
    if aux:=sum(l) > suma_mayor:
        suma_mayor=aux
        lista_mayores=[l]
    elif aux==suma_mayor:
        lista_mayores.append(l)
print(f'La mayor suma es {suma_mayor} y la lista/s que lo cumplen son: ')
for l in lista_mayores:
    print(l, end=' ')
print()