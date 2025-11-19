
# Primera opcion de como hacerlo

# # # ruta = input("escribir la ruta samba")
# # # if ruta [0] == "/" and ruta [1] == "/":
# # #     pass
# # # else:
# # #     print("error... no es un ruta samba")

# Segunda opcion de como hacerlo

ruta = input("escribir la ruta samba: ")
if ruta [0:2] == "//":
    lista_nombres = ruta[2:].split("/")
    print("El nombre de equipo es:", lista_nombres[0])
    i = 0
    ruta = "/"
    while i <len(lista_nombres):
        ruta += lista_nombres [i]
        i += 1
        if i != len(lista_nombres):
            ruta += "/"          
    print("la ruta del recurso es: ", ruta)
else:
    print("Error... no es una ruta samba.")