
while True:

    linea_operacion = input("-->")
    lista_op = linea_operacion.split()
    if len(lista_op) == 3:
        match lista_op[1]:
            case "+":
                print(float(lista_op[0]) + float(lista_op[2]))
            case "-":
                print(float(lista_op[0]) - float(lista_op[2]))
            case "*":
                print(float(lista_op[0]) * float(lista_op[2]))
            case "/":
                print(float(lista_op[0]) + float(lista_op[2]))
            case "//":
                print(float(lista_op[0]) // float(lista_op[2]))
            case "%":
                print(float(lista_op[0]) % float(lista_op[2]))
            case _:
                print("operador no valido")
    elif len(lista_op) == 1 or lista_op[0] == "q":
        print("\nFin de ejecuccion")
        break
