# primera parte

alfabeto = '0123456789'
nro_claves_gen = 0
for car1 in alfabeto:
    for car2 in alfabeto:
        for car3 in alfabeto:
            for car4 in alfabeto:
                if car1 != car2 and car1 != car3 and car1 != car4 and car2 != car3 and car2 != car4 and car3 != car4:
                    print(car1+car2+car3+car4, end = '  ')
                    nro_claves_gen += 1
                    if nro_claves_gen % 10 == 0:
                        print()
print(f'El total de posibles claves es {nro_claves_gen}')

#segunda parte

alfabeto = '0123456789'
nro_claves_gen = 0
for car1 in alfabeto:
    for car2 in alfabeto:
        for car3 in alfabeto:
            for car4 in alfabeto:
                if car1 < car2 and car1 != car3 and car1 != car4 and car2 < car3 and car2 != car4 and car3 > car4:
                    print(car1+car2+car3+car4, end = '  ')
                    nro_claves_gen += 1
                    if nro_claves_gen % 10 == 0:
                        print()
print(f'El total de posibles claves es {nro_claves_gen}')