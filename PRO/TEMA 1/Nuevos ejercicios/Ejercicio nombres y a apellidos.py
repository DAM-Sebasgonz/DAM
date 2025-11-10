# nombre = input("Indique su nombre completo -->")
# apellidos = input("Indique su(s) apellidos -->")

# print(apellidos,","+ nombre)

nombre_apellidos = input("Indique su nombre completo(incluyendo apellidos)-->")
lista_datos = nombre_apellidos.split()

match len(lista_datos):
    case 2:
        print(lista_datos[1] + "," , lista_datos[0])
    case 4:
        print(lista_datos[2] + " " , lista_datos[3] + ","+\
              lista_datos[0] + " " , lista_datos[1])
    case 3:
        nro_apellidos = int(input("Introduce el numero de apellidos"))
        if nro_apellidos == 2:
            print(lista_datos[1] + " " + lista_datos[2] + ", " + lista_datos[0])
        elif nro_apellidos == 1:
            print(lista_datos[2] + "," + lista_datos[0] + ", " + lista_datos[1])