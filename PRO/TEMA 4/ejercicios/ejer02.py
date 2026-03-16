class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0

        suma = 0
        for n in self.notas:
            suma += n

        return suma / len(self.notas)

class Profesor(Persona):

    def __init__(self, nombre, edad, mensaje):
        super().__init__(nombre, edad)
        self.mensaje = mensaje

    def mostrar_mensaje(self):
        return self.mensaje

class Aula:

    def __init__(self):
        self.estudiantes = []
        self.profesores = []

    def agregar_estudiante(self, e):
        self.estudiantes.append(e)

    def agregar_profesor(self, p):
        self.profesores.append(p)

    def mostrar_promedios(self):
        for e in self.estudiantes:
            print(e.nombre, e.promedio())
aula = Aula()
def menu():
    while True:
        print("1 Crear estudiante\n2 Crear profesor\n3 Agregar nota\n4 Mostrar promedios\n5 Mostrar mensaje profesor\n6 Salir")
        opcion = int(input())
        match opcion:
            case 1:
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                e = Estudiante(nombre, edad)
                aula.agregar_estudiante(e)
            case 2:
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                mensaje = input("Mensaje: ")

                p = Profesor(nombre, edad, mensaje)
                aula.agregar_profesor(p)

            case 3:
                nombre = input("Nombre estudiante: ")
                nota = float(input("Nota: "))

                for e in aula.estudiantes:
                    if e.nombre == nombre:
                        e.agregar_nota(nota)
            case 4:
                aula.mostrar_promedios()
            case 5:
                for p in aula.profesores:
                    print(p.mostrar_mensaje())
            case 6:
                print("Fin")
            case _:
                print("Opcion invalida")
menu()