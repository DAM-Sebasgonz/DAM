class  Gato:    # definición de la clase Gato

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
    
    def esAlimentoFavorito(self, alimento):
        return alimento in self.alimentos_favoritos


if __name__ == "__main__":

# creación de objetos
#     
    gato01 = Gato("zarpas", 1, 'M')
    gato02 = Gato("frida", 2, 'H')

# acceso directo a los atributos

    print(gato01.nombre)
    gato01.verEtapaDeVida()
    print(gato02.nombre)
    gato02.verEtapaDeVida()

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

