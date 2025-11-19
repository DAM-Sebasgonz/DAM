print("||Sistema de gestion||")
print("Que desea hacer?")
print("S - Para salir del programa ")
print("D - Desglosar una cantidad de dinero en billetes y monedas")
print("F - Para facturar un pedido realizado")
#Ponemos prints para que el usuario vea las opciones

while True:
    opcion = input("==> ").upper().strip()
    
    if opcion == 'S':
        print("...saliendo del programa")
        break
    elif opcion == "D":
        try:
            cantidad = float(input("Introduce la cantidad a desglosar--> "))
            if cantidad < 0:
                print("...Error -> La cantidad debe ser positiva")
            else:
                cantidad = round(cantidad, 2) #Redondeamos las cantidades a 2 decimales.
                print(f"La cantidad a desglosar es {cantidad}")
                #Primero desglosamos los billetes de 500
           
            nvcantidad = cantidad #definimos una nueva variable que se iguale a la anterior para evitar posibles fallos
           
            if nvcantidad >= 500:
                billetes500 = int(nvcantidad // 500)
                nvcantidad -= billetes500 * 500
                print(f">Billetes de 500: {billetes500}")
                #Luego los de 200
            if nvcantidad >= 200:
                billetes200 = int(nvcantidad // 200)
                nvcantidad -= billetes200 * 200
                print(f">Billetes de 200: {billetes200}")
                #Luego los de 100
            if nvcantidad >= 100:
                billetes100 = int(nvcantidad // 100)
                nvcantidad -= billetes100 * 100
                print(f">Billetes de 100: {billetes100}")
                #Luego los de 50
            if nvcantidad >= 50:
                billetes50 = int(nvcantidad // 50)
                nvcantidad -= billetes50 * 50
                print(f">Billetes de 50: {billetes50}")
                #Luego los de 20
            if nvcantidad >= 20:
                billetes20 = int(nvcantidad // 20)
                nvcantidad -= billetes20 * 20
                print(f">Billetes de 20: {billetes20}")
                #Luego los de 10
            if nvcantidad >= 10:
                billetes10 = int(nvcantidad // 10)
                nvcantidad -= billetes10 * 10
                print(f">Billetes de 10: {billetes10}")
                #Luego los de 5
            if nvcantidad >= 5:
                billetes5 = int(nvcantidad // 5)
                nvcantidad -= billetes5 * 5
                print(f">Billetes de 5: {billetes5}") 
                #Luego las monedas de 2
            if nvcantidad >= 2:
                monedas2 = int(nvcantidad // 2)
                nvcantidad -= monedas2 * 2
                print(f">Monedas de 2: {monedas2}")   
                #Luego las monedas de 1
            if nvcantidad >= 1:
                monedas1 = int(nvcantidad // 1)
                nvcantidad -= monedas1 * 1
                print(f">Monedas de 1: {monedas1}")
                #Luego las monedas de 0.50
            if nvcantidad >= 0.50:
                monedas050 = int(nvcantidad // 0.50)
                nvcantidad -= monedas050 * 0.50
                print(f">Monedas de 0.50: {monedas050}")
                #Luego las monedas de 0.20
            if nvcantidad >= 0.20:
                monedas020 = int(nvcantidad // 0.20)
                nvcantidad -= monedas020 * 0.20
                print(f">Monedas de 0.20: {monedas020}")
            if nvcantidad >= 0.10:
                #Luego las monedas de 0.10
                monedas010 = int(nvcantidad // 0.10)             #Aqui termina el desglose de billetes y no se como hacerlo de manera mas bonita
                nvcantidad -= monedas010 * 0.10
                print(f">Monedas de 0.10: {monedas010}")
            if nvcantidad >= 0.05:
                #Luego las monedas de 0.05
                monedas005 = int(nvcantidad // 0.05)
                nvcantidad -= monedas005 * 0.05
                print(f">Monedas de 0.05: {monedas005}")
            if nvcantidad >= 0.02:
                #Luego las monedas de 0.02
                monedas002 = int(nvcantidad // 0.02)
                nvcantidad -= monedas002 * 0.02
                print(f">Monedas de 0.02: {monedas002}")
            if nvcantidad >= 0.01:
                #Finalmente las monedas de 0.01
                monedas001 = int(nvcantidad / 0.01)
                nvcantidad -= monedas001 * 0.01
                print(f">Monedas de 0.01: {monedas001}")
                print("Desglose de la cantidad:")
                print(f">Total = {cantidad}")
        except ValueError:
            print("...Error -> Entrada no valida. Introduce un numero.") #Ponemos ValueError evitando las posibles equivocaciones ejemplo: letras, caracteres especiales,etc.
    elif opcion == "F":
        out=('')
        precio_final=0
        while True: 
            cdg=input('>Introduzca el codigo: ')
            if len(cdg)==4:
                while True: 
                    try:
                        ctd=float(input('Cantidad de productos: '))
                        if ctd<=0:
                            print('error -> No se aceptan numero negativos')
                        else:
                            dscp=input('Descripcion: ')
                            break    
                    except:
                        print('error -> Lo introducido no es un numero')  
                while True:    
                    try:
                        prc=float(input('Introduzca el precio: '))
                        if prc<=0:
                            print('error -> No se aceptan numero negativos')
                        else:
                            break
                    except:
                        print('error -> Lo introducido no es un numero')
                while True:    
                    try:
                        dct=float(input('Introduzca el descuento: '))
                        if dct<0:
                            print('error -> No se aceptan numero negativos')
                        else:
                            break
                    except:
                        print('error -> Lo introducido no es un numero')
                if dct>1: 
                    precio=(prc-prc*(dct/100))*ctd
                else:
                    precio=(prc-prc*dct)*ctd
                precio_final+=precio
                out+=(f'{cdg:<10}{dscp:<21}{prc:<18}{dct:<13}{precio} \n') 
            elif cdg=='@*':
                break
            else:
                print('error ->  El codigo no es valido')
        if out!='':
            print('Codigo    Descripción          Importe unitario  % Descuento  Subtotal')
            print(out)
            print(f'                                                 Total       {precio_final}')