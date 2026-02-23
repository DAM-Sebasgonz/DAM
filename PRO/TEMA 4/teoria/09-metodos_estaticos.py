class Animal:
    def __init__(self, tipo, volumen, masa) -> None:
        self.tipo = tipo
        self.volumen = float(volumen)
        self.masa = float(masa)

    @classmethod
    def desde_str(cls, cadena) :
        tipo, volumen, masa = cadena.split(',')
        return cls(tipo, float(volumen), float(masa) )

    @classmethod
    def gato(cls) :
        return cls('Gato', 120.0, 3.8)
    
    @classmethod
    def perro (cls):
        return cls( 'Perro', 500.0, 25.4)
    
    def animalToString (self):
        return self.tipo + ' ' + str(self.volumen) + ' ' + str(self.masa)
    
    def peso(self):
        return self.masa * Animal.gravedad()

    @staticmethod
    def gravedad():
        return 9.8
    
if __name__ == '__main__':

    cebra = Animal( 'Cebra', 15000, 150)
    elefante = Animal.desde_str('Elefante, 300000, 2600')
    gato = Animal.gato ()
    perro = Animal.perro()
    print(cebra.animalToString( ))
    print(elefante.animalToString())
    print(gato.animalToString ())
    print(perro.animalToString())
    print('----imprimiendo pesos----')
    print(cebra.peso())
    print(elefante.peso())
    print(gato.peso())
    print(perro.peso())

