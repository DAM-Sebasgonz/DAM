# ejemplo de serialización de una lista
# En la lista no se permiten nombre repetidos
# cada vez que se inserte, modifique o borre en la lista
# se debe guardar en el fichero

import pickle
import os
                                                                                                                                                     
if os.path.exists('files/personas.pckl'):
    f = open('files/personas.pckl', 'rb')
    personas = pickle.load(f)
    f.close()
else:
    personas = [] 

print(personas)

menu = """
1. Agregar persona
2. Modificar persona
3. Eliminar persona
4. Listar personas
S|s. Salir"""

while True:
    print(menu)
    opcion = input("\nIntroduzca una opción: ").upper()
    match opcion:
        case "1":
            nombre_añadir = input("Nombre que quiere añadir: ")
            if nombre_añadir in personas:
                print("\nError...El nombre ya está registrado")
            else:
                personas.append(nombre_añadir)
                f = open('files/personas.pckl', 'wb')
                pickle.dump (personas, f)
                f.close()

        case "2":
            nombre_modificar = input("Nombre que quiere modificar: ")
            if nombre_modificar not in personas:
                print("\nError...El nombre NO está registrado")
            else: # el nombre a buscar está en la lista
                # se borra de la lista
                personas.remove(nombre_modificar)
                nuevo_nombre = input("Nuevo nombre: ")
                if nuevo_nombre not in personas:
                    personas.append(nuevo_nombre)
                else:
                    # si el nuevo nombre está se añade el anterior 
                    print("\nError... el nuevo nombre ya existe en la lista")
                    personas.append(nombre_modificar)
                    
                f = open('files/personas.pckl', 'wb')
                pickle.dump (personas, f)
                f.close()
        case "3":
            nombre_eliminar = input("Nombre que quiere eliminar: ")
            if nombre_eliminar not in personas:
                print("\nError...El nombre NO está registrado")
            else:
                personas.remove(nombre_eliminar)
                f = open('files/personas.pckl', 'wb')
                pickle.dump (personas, f)
                f.close()
        case "4": 
            print()
            for persona in personas:
                print(persona)
        case "S"|"s":
            break
        case _ :
            print("\nError... Opción inválida")
