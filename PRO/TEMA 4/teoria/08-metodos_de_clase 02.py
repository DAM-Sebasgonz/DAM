class Animal:
    def __init__(self, tipo, volumen, masa):
        self.tipo = tipo
        self.volumen = float(volumen)
        self.masa = float(masa)

    @classmethod
    def desde_str(cls, cadena) :
        tipo, volumen, masa = cadena.split(',')
        return cls(tipo, float(volumen), float(masa) ) # crea un objeto de la clase Animal

    @classmethod
    def gato(cls) :
        return cls('Gato', 120.0, 3.8) # crea un objeto de la clase Animal
    
    @classmethod
    def perro (cls):
        return cls('Perro', 500.0, 25.4)  # crea un objeto de la clase Animal
    
    def animalToString (self):
        return self.tipo + ' ' + str(self.volumen) + ' ' + str(self.masa)
    
if __name__ == '__main__':

    cebra = Animal( 'Cebra', 15000, 150)
    elefante = Animal.desde_str('Elefante, 300000, 2600')
    gato = Animal.gato()
    perro = Animal.perro()
    print(cebra.animalToString( ))
    print(elefante.animalToString())
    print(gato.animalToString())
    print(perro.animalToString())
    print(type(elefante))