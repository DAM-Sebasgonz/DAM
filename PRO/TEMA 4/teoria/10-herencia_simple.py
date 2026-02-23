# definición de herencia

# class A():
#     texto = 'Soy A'
    
#     def obtenerTexto(self) -> str:
#         return self.texto

# class B(A):
#     texto = 'Soy B'
#     i = 0
#     pass

# if __name__ == '__main__':
#     # objA = A()
#     # print(objA.texto)
#     # objB = B()
#     # print(objB.texto)
#     # print(objB.i)
#     # print(objA.i)
#     objA = A()
#     print(objA.obtenerTexto())
#     objB = B()
#     print(objB.obtenerTexto())

# herencia ejemplo


# class MiStr:
#     def __init__(self, cadena) -> None:
#         self.cadena = cadena

#     def longitud(self):
#         return len(self.cadena)

#     def info (self):
#         return self.cadena
    
# class MiStrMayusculas(MiStr):
#     def info (self):
#         return self.cadena.upper()

# class MiStrMinusculas(MiStr):
#     def info (self):
#         return self.cadena.lower()


# if __name__ == '__main__':

#     m_str = MiStr( 'Hola Mundo')
#     print( 'longitud del string', m_str.longitud())
#     print( 'contenido del string', m_str.info())
#     m_str_mayus = MiStrMayusculas ('Hola Mundo')
#     print( 'longitud del string' , m_str_mayus.longitud())
#     print( 'contenido del string', m_str_mayus.info())
#     m_str_minus = MiStrMinusculas ('Hola Mundo')
#     print( 'longitud del string', m_str_minus.longitud())
#     print('----')
#     print(MiStrMayusculas.__mro__)
#     print(MiStrMinusculas.__mro__)
#     print(MiStr.__mro__)

# herencia y uso de super()

# class Persona:
#     def __init__(self, nombre) -> None:
#         self.nombre = nombre.title()
    
#     def info(self):
#         return f'Mi nombre es: {self.nombre}'

#     def velocidad(self):
#         """Velocidad media en kilómetros por minutos"""
#         return 8

# class Atleta (Persona):
#     def __init__(self, nombre, forma_fisica: float) -> None: 
#         super (Atleta, self).__init__(nombre)
#         self.forma_fisica = forma_fisica
    
#     def info(self):
#         p_info = super(Atleta, self).info()
#         return f'{p_info} y soy atleta profesional'
    
#     def velocidad (self):
#         p_vel = super(Atleta, self). velocidad()
#         return p_vel * (1 + self. forma_fisica / 10)

# class Pintor(Persona):
#     def info(self):
#         p_info = super(Pintor, self).info()
#         return f'{p_info} y soy pintor'
    
#     def pintar(self):
#         lineas = []
#         for vals in ([9556, 9552, 9552, 9559], [9553, 9630, 9626, 9553], [9562, 9552, 9552, 9565]):
#             lineas.append(''.join(map(chr, vals) ))
#         return '\n'.join(lineas)

# if __name__ == '__main__':
#     p = Persona ('Juan Fernández' )
#     print (p. info())
#     print (p. velocidad())
#     # forma_fisica = 12
#     a = Atleta( 'Ana María Chacón', forma_fisica = 12)
#     print(a. info())
#     print(a. velocidad())
#     pintor = Pintor( 'Diego Velázquez')
#     print(pintor. info())
#     print (pintor.velocidad())
#     print (pintor.pintar())

# herencia múltiple

class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre.title()
    
    def info(self):
        return f'Mi nombre es: {self.nombre}'

    def velocidad(self):
        """Velocidad media en kilómetros por minutos"""
        return 8

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

class AtletaPintor(Atleta, Pintor):
    pass

if __name__ == '__main__':
    p = Persona ('Juan Fernández' )
    print (p.info())
    print (p.velocidad())
    # forma_fisica = 12
    a = Atleta( 'Ana María Chacón', forma_fisica = 12)
    print(a.info())
    print(a.velocidad())
    pintor = Pintor( 'Diego Velázquez')
    print(pintor.info())
    print (pintor.velocidad())
    print (pintor.pintar())

    atletapintor = AtletaPintor ("Juan González", forma_fisica = 8)
    print ("\n")
    print(atletapintor. info())
    print("mi velocidad es de", atletapintor.velocidad())
    print (atletapintor.pintar())