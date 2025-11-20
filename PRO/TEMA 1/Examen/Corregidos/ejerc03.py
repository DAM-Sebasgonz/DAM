# código de cesar multiclave

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
NRO_CARACTERES = len(alfabeto)
try:
    clave = input('Introduzca la clave de cifrado -> ')
    if not clave.isdigit():
        raise ValueError('\nError... la clave debe contener únicamente dígitos')
    if len(clave) != 4:
        raise ValueError('\nError...la clave debe ser de 4 dígitos')
    if clave.count(clave[0]) != 1 or clave.count(clave[1]) != 1 or clave.count(clave[2]) != 1 or clave.count(clave[3]) != 1:
        raise ValueError('\nError...los dígitos en la clave no se pueden repetir')
    if '0' in clave:
        raise ValueError('\nError...el dígito 0 no puede formar parte de la clave')
except ValueError as e:
    print(e)
else:
    LONGITUD_CLAVE = len(clave)
    NRO_CARACTERES_POR_CLAVE = int(clave[0]) + int(clave[1]) + int(clave[2]) + int(clave[3])
    while True:
        print('''\nMenú\n\nC - Cifrar\nD - Descifrar\nS - Salir''')
        opc = input('\nOpción ? ').lower()
        match opc:
            case 's':
                break
            case 'c':
                mensaje ='En un lugar de la Mancha, de cuyo nombre no quiero acordarmeyz'.lower()
                mensaje.replace('á', 'a')
                mensaje.replace('é', 'e')
                mensaje.replace('í', 'i')
                mensaje.replace('ó', 'o')
                mensaje.replace('ú', 'u')
                mensaje_cifrado = ''
                nro_caract_cifrados = 0
                pos_clave = 0
                desplazamiento = int(clave[pos_clave])
                for caracter in mensaje:
                    if caracter in alfabeto:
                        pos = alfabeto.find(caracter)
                        nva_pos = (pos + desplazamiento) % NRO_CARACTERES
                        mensaje_cifrado += alfabeto[nva_pos]
                        nro_caract_cifrados += 1
                        if nro_caract_cifrados % NRO_CARACTERES_POR_CLAVE == 0: # cambio de clave
                            pos_clave = (pos_clave + 1) % LONGITUD_CLAVE
                            desplazamiento = int(clave[pos_clave])
                    else:
                        mensaje_cifrado += caracter
                print(mensaje_cifrado)               
            case 'd':
                mensaje ='hp xp ñxjdu gg nc ñcoejc, ff dvzp ñpncsi qs uymivs efrugduohbc'.lower()
                mensaje.replace('á', 'a')
                mensaje.replace('é', 'e')
                mensaje.replace('í', 'i')
                mensaje.replace('ó', 'o')
                mensaje.replace('ú', 'u')
                mensaje_cifrado = ''
                nro_caract_cifrados = 0
                pos_clave = 0
                desplazamiento = int(clave[pos_clave])
                for caracter in mensaje:
                    if caracter in alfabeto:
                        pos = alfabeto.find(caracter)
                        nva_pos = (pos - desplazamiento) % NRO_CARACTERES
                        mensaje_cifrado += alfabeto[nva_pos]
                        nro_caract_cifrados += 1
                        if nro_caract_cifrados % NRO_CARACTERES_POR_CLAVE == 0: # cambio de clave
                            pos_clave = (pos_clave + 1) % LONGITUD_CLAVE
                            desplazamiento = int(clave[pos_clave])
                    else:
                        mensaje_cifrado += caracter
                print(mensaje_cifrado)
            case _:
                print('\nError...Opción inválida en el menú')
finally:
    print('El programa finaliza su ejecución...')
