# implementación de la solución al problema del diamante

# el problema surge cuando se tiene una clase A de la cual heredan B y C
# ahora una nueva clase D tiene herencia múltiple de B y C.
# si vemos el diagrama se forma una especie de diamante

# la solucion es 
# NO usar en los constructores de las tres clases que heredan (B, C, D) el método super()

class A(object):
    def __init__(self, mensajeA):
        self.mensajeA = mensajeA
    
    @staticmethod
    def quienSoy() -> str:
        return "Soy A"
    
class B(A):
    def __init__(self, mensajeA, mensajeB):
        A.__init__(self,"++++")
        self.mensajeB = mensajeB
    
    @staticmethod
    def quienSoy() -> str:
        return "Soy B"

class C(A) :
    def __init__(self, mensajeA, mensajeC):
        A.__init__(self,"----")
        self.mensajeC = mensajeC

    @staticmethod
    def quienSoy() -> str:
        return "Soy C"

class D(B,C) :
    def __init__(self, mensajeA, mensajeB, mensajeC, mensajeD):
        B.__init__(self, mensajeA, mensajeB)
        C.__init__(self, mensajeA, mensajeC)
        self.mensajeD = mensajeD

    @staticmethod
    def quienSoy() -> str:
        return "Soy D"

class E(C,B) :
    def __init__(self, mensajeA, mensajeB, mensajeC, mensajeE):
        C.__init__(self,mensajeA, mensajeC)
        B.__init__(self, mensajeA, mensajeB)
        self.mensajeE = mensajeE

    @staticmethod
    def quienSoy() -> str:
        return "Soy E"

if __name__ == '__main__':
    ca = A("prueba de A")
    cb = B("prueba de A desde B", "prueba de B")
    cc = C("prueba de A desde C", "prueba de C")
    cd = D("prueba de A desde D", "prueba de B desde D", "prueba de C desde D", "prueba de D")
    ce = E("prueba de A desde E", "prueba de B desde E", "prueba de C desde E", "prueba de E")
    
    print("Mensaje de A:", ca.mensajeA)
    print("Quien es?: ", ca.quienSoy())
    print("------")
    print("Mensaje 1 de B:", cb.mensajeB)
    print("Mensaje 2 de B:", cb.mensajeA)
    print("Quien es?:", cb.quienSoy())
    print("------")
    print("Mensaje 1 de C:", cc.mensajeC)
    print("Mensaje 2 de C:", cc.mensajeA)
    print("Quien es?:", cc.quienSoy())
    print("------")
    print("Mensaje 1 de D:", cd.mensajeD)
    print("Mensaje 2 de D:", cd.mensajeB)
    print("Mensaje 3 de D:", cd.mensajeC)
    print("Mensaje 4 de D:", cd.mensajeA)
    print("Quien es?:", cd.quienSoy())
    print("------")
    print("Mensaje 1 de E:", ce.mensajeE)
    print("Mensaje 2 de E:", ce.mensajeB)
    print("Mensaje 3 de E:", ce.mensajeC)
    print("Mensaje 4 de E:", ce.mensajeA)
    print("Quien es?:", ce.quienSoy())
