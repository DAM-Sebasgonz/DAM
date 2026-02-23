import random

# definición de la clase Gato
class  Gato:
    num_patas = 4
    num_orejas = 2

    def __init__(self, nombre, edad, sexo) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.alimentos_favoritos = []
        self.vacunado = (False,"00/00/00")
        
    def verEtapaDeVida(self):
        if self.edad > 1:
            print(self.nombre + " es adulto")
        else:
            print(self.nombre + " es cachorro")

    def __str__(self) -> str:
        return f"{self.nombre} es de sexo {self.sexo}+\
            \nSu edad es: {self.edad} \
                \nSus alimentos favoritos {self.alimentos_favoritos}"

    def esAlimentoFavorito(self, alimento):
        return alimento in self.alimentos_favoritos
    
    
    def introducirAlimento(self, alimento_nuevo):
        if alimento_nuevo not in self.alimentos_favoritos:
            self.alimentos_favoritos.append(alimento_nuevo)
            return True
        return False

    def eliminarAlimento(self, alimento_nuevo):
        if alimento_nuevo in self.alimentos_favoritos:
            self.alimentos_favoritos.pop(alimento_nuevo)
            return True
        return False

    def cambiaEdad(self, nueva_edad):
        if nueva_edad > self.edad:
            self.edad = nueva_edad

    def estaVacunado(self):
        return self.vacunado

    def vacunar(self, fecha):
        self.vacunado = (True, fecha)


if __name__ == "__main__":

    # gato01 = Gato("zarpas", 1, 'M')
    # gato02 = Gato("frida", 2, 'H')

    # # print(gato01.nombre)
    # # gato01.verEtapaDeVida()
    # print(gato01.nombre)

    # print(gato02.nombre)
    # gato02.verEtapaDeVida()

    # lista_gatos = []
    # gato = Gato("zarpas", 1, 'M')
    # lista_gatos.append(gato)
    # gato = Gato("frida", 2, 'H')
    # lista_gatos.append(gato)
    # print(lista_gatos[0].nombre)
    # lista_gatos[0].verEtapaDeVida()
    # print('---')
    # print(lista_gatos[0])

    gato01 = Gato("zarpas", 1, 'M')
    gato02 = Gato("frida", 2, 'H')

    # print(gato01.num_patas)
    # print(gato02.num_patas)
    # gato01.num_patas = 3
    # print(gato01.num_patas)
    # print(gato02.num_patas)

    print(gato01.num_orejas)
    print(gato02.num_orejas)
    Gato.num_orejas = 5
    print(gato01.num_orejas)
    print(gato02.num_orejas)


# programa principal

#     gato01.num_patas = 3 # a definir

#     print(f"El número de patas del gato/a es: {gato01.num_patas}")
#     print(f"El número de patas del gato/a es: {gato02.num_patas}")
    
    
#     # print(f"El nombre del gato/a es: {gato01.num_orejas}")
#     # print(f"El nombre del gato/a es: {gato02.num_orejas}")

#     # print(f"El nombre del gato/a es: {gato01.nombre}")
#     # print(f"La edad del gato/a es: {gato01.edad}")
#     # print(f"El sexo del gato/a es: {gato01.sexo}")

#     # print(f"El nombre del gato/a es: {gato02.nombre}")
#     # print(f"La edad del gato/a es: {gato02.edad}")
#     # print(f"El sexo del gato/a es: {gato02.sexo}")
    
    
# # ejecución del programa principal

    miau = Gato("Miau", 1, 'M')
    seferino = Gato("Seferino", 1, 'M')


    # miau.verEtapaDeVida()
    # miau.introducirAlimento('carne')

    # print(miau)
    # print(seferino)

    # if miau == seferino:
    #     print("es igual")

    # ver atributos

    # print(miau.edad)
    # print(miau.nombre)
    # print(miau.alimentos_favoritos)
    # print(seferino.edad)

    # comida = input("Comida :")
    # if miau.introducirAlimento(comida):
    #     print(miau.alimentos_favoritos)
    # comida = input("Comida :")
    # if miau.introducirAlimento(comida):
    #     print(miau.alimentos_favoritos)
    # else:
    #     print("La comida ya estaba en lista de favoritos")


    # miau.cambiaEdad(2)
    # print(miau)

    # print(seferino)

    # miau = Gato("miau", 1, "M")
    # print(miau)

    # lista_gatos =[]
    # lista_gatos.append(Gato("miau",1,"M"))
    # lista_gatos.append(Gato("seferino",2,"M"))

    # objeto_escogido = random.choice(lista_gatos)

    # # print(objeto_escogido.nombre)
    # # print(objeto_escogido.edad)
    # # print(objeto_escogido.alimentos_favoritos)

    # print(objeto_escogido)