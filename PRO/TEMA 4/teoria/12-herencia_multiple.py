# herencia múltiple

class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre.title()
    
    def info(self):
        return f'Mi nombre es: {self.nombre}'

    def velocidad(self):
        """Velocidad media en kilómetros por minutos"""
        return 8.0

class Atleta (Persona):
    def __init__(self, nombre, forma_fisica: float) -> None: 
        super(Atleta, self).__init__(nombre)
        self.forma_fisica = forma_fisica
    
    def info(self):
        p_info = super(Atleta, self).info()
        return f'{p_info} y soy atleta profesional'
    
    def velocidad (self):
        p_vel = super(Atleta, self). velocidad()
        return p_vel * (1 + self. forma_fisica / 10)

class Pintor(Persona):
    def info(self):
        p_info = super(Pintor, self).info()
        return f'{p_info} y soy pintor'
    
    def pintar(self):
        lineas = []
        for vals in ([9556, 9552, 9552, 9559], [9553, 9630, 9626, 9553], [9562, 9552, 9552, 9565]):
            lineas.append(''.join(map(chr, vals) ))
        return '\n'.join(lineas)

# en la herencia múltiple se hereda de 2 o más clases
# tener en cuenta el orden en que se hereda
# C hereda de A y B, no es lo mismo que C hereda de B y A

class AtletaPintor(Atleta, Pintor):
    pass

class PintorAtleta(Pintor, Atleta ):
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

    atletapintor = AtletaPintor("Juan González", forma_fisica = 8)
    print(atletapintor.info())
    print("mi velocidad es de", atletapintor.velocidad())
    print (atletapintor.pintar())
    print(AtletaPintor.__mro__)
    print('-'*10)
    pintoratleta = PintorAtleta("Juan González", forma_fisica = 8)
    print(pintoratleta.info())
    print("mi velocidad es de", pintoratleta.velocidad())
    print (pintoratleta.pintar())
    print(PintorAtleta.__mro__)