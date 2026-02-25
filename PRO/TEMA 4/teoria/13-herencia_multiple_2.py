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

# # para ver las discrepancias del orden creamos estas 3 clases

class PintorRapido(Pintor):
    def info(self):
        print('Entrando info() en pintor-rapido')
        p_info = super(Pintor, self).info()
        return f'{p_info} y soy pintor rápido'
    
    def velocidad(self) -> float:
        print('Entrando velocidad() en pintor-rapido')
        vel = super(PintorRapido, self).velocidad()
        return vel + 2.0

class PintorRapidoAtleta(PintorRapido, Atleta):
    pass

class AtletaPintorRapido(Atleta, PintorRapido):
    pass

if __name__ == '__main__':
    
    # atleta_pintor = AtletaPintor ("Juan González", forma_fisica = 8)
    # print(atleta_pintor.info())
    # print("mi velocidad es de", atleta_pintor.velocidad())

    # pintor_atleta = PintorAtleta ("Pedro García", forma_fisica = 8)
    # print(pintor_atleta.info())
    # print("mi velocidad es de", pintor_atleta.velocidad())

    # print(AtletaPintor.__mro__)
    # print('----')
    # print(PintorAtleta.__mro__)
    # print('----')
    # pintor_rapido = PintorRapido('Juana Méndez')
    # print(pintor_rapido.info())
    # print("mi velocidad es de", pintor_rapido.velocidad())
    # print('----')

    # ahora los resultados de la velocidad son distintos en estas dos objetos

    pintor_rapido_atleta = PintorRapidoAtleta ("Pedro García", forma_fisica = 45)
    print(PintorRapidoAtleta.__mro__)
    print()
    print(pintor_rapido_atleta.info())
    print("mi velocidad es de", pintor_rapido_atleta.velocidad())
    print(pintor_rapido_atleta.pintar())
    print('*'*20)
    atleta_pintor_rapido = AtletaPintorRapido ("Patricio", forma_fisica = 45)
    print(AtletaPintorRapido.__mro__)
    print()
    print(atleta_pintor_rapido.info())
    print("mi velocidad es de", atleta_pintor_rapido.velocidad())
    print(atleta_pintor_rapido.pintar())
    
