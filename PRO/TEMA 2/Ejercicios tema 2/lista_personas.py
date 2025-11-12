#lista peronas

personas = []

while True:
    menu = "1. Insertar \n3. Borrar usuario \n4. Mostrar datos \n9. Salir"
    print(menu)
    
    opc = input("opcion ? --> ")
    match opc :
        case "1":
            aux_persona = []
            for pers in personas:
                nif = input("Escriba su NIF")
                if pers[0] == nif:
                    print(f"Error...el nif {nif} ya esta en la lista")
                    break
            else: 
                opc_crear = input("Desea insertar un nuevo usuario? (S/N)-->").lower()
                if opc_crear == "s":
                    nombre = input("Nombre? -->")
                    trabajo = input("Trabaja? (S/N) -->").lower()
                    salario = float(input("Introduzca el salario mensual--> ")) 
                    
                    aux_persona.append(nif)
                    aux_persona.append(nombre)
                    aux_persona.append (trabajo)
                    aux_persona.append(salario)

                    personas.append(aux_persona)
        case "3":
            nif_borrar = input("Introduzca el NIF del usuario a borrar -->")
            for pers in personas:
                if pers[0] == nif_borrar:
                    personas.remove(pers)
                    print(f"Usuario con NIF {nif_borrar} borrado")
                    break
            else:
                print(f"El NIF {nif_borrar} no se encuentra en la lista")
        case "4":
            for pers in personas:
                print(f"NIF: {pers[0]} | Nombre: {pers[1]} | Trabaja: {pers[2]} | Salario: {pers[3]} ")  
        case "9":
            print("\nFin del programa")
            break
        case _:
            print("Introduzca una opcion valida")

        
        