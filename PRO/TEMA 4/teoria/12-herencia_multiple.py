# herencia múltiple

# recordar que con super() es equivalente a poner super(nombre_de_la_clase, self)

class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre.title()
    
    def info(self):
        print('Entrando info() en persona')
        return f'Mi nombre es: {self.nombre}'

    def velocidad(self):
        print('Entrando velocidad() en persona')
        """Velocidad media en k/min"""
        return 8.0

class Atleta(Persona):
    def __init__(self, nombre, forma_fisica: float) -> None: 
        super().__init__(nombre)
        self.forma_fisica = forma_fisica
    
    def info(self):
        print('Entrando info() en atleta')
        p_info = super(Atleta, self).info()
        return f'{p_info} soy atleta profesional'
    
    def velocidad (self):
        print('Entrando velocidad() en atleta')
        p_vel = super(Atleta, self).velocidad()
        return p_vel * (1 + self.forma_fisica / 10)

class Pintor(Persona):
    def info(self):
        print('Entrando info() en pintor')
        p_info = super(Pintor, self).info()
        return f'{p_info} soy pintor'
    
    def pintar(self):
        lineas = []
        for vals in ([9556, 9552, 9552, 9559], [9553, 9630, 9626, 9553], [9562, 9552, 9552, 9565]):
            lineas.append(''.join(map(chr, vals) ))
        return '\n'.join(lineas)

# en la herencia múltiple se hereda de 2 o más clases
# tener en cuenta el orden en que se hereda
# C hereda de A y B, no es lo mismo que C hereda de B y A

# class AtletaPintor(Atleta, Pintor):
#     pass

class PintorAtleta(Pintor, Atleta):
    pass

if __name__ == '__main__':
    # p = Persona ('Juan Fernández' )
    # print (p.info())
    # print (p.velocidad())
    # # forma_fisica = 12
    # a = Atleta( 'Ana María Chacón', forma_fisica = 12)
    # print(a.info())
    # print(a.velocidad())
    # pintor = Pintor( 'Diego Velázquez')
    # print(pintor.info())
    # print (pintor.velocidad())
    # print (pintor.pintar())

    # atletapintor = AtletaPintor("Juan González", forma_fisica = 8)
    # print(AtletaPintor.__mro__)
    # print()
    # print(atletapintor.info())
    # print("mi velocidad es de", atletapintor.velocidad())
    # print (atletapintor.pintar())
    # print('-'*10)

    pintoratleta = PintorAtleta("Juan González", forma_fisica = 8)
    print(PintorAtleta.__mro__)
    print()
    print(pintoratleta.info())
    print("mi velocidad es de", pintoratleta.velocidad())
    print (pintoratleta.pintar())
