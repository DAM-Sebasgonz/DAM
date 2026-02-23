class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacio.")
        self.__nombre = valor.strip()

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, valor: int):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La edad debe ser un numero entero positivo.")
        self.__edad = valor

    def mostrar_info(self) -> str:
        return f"Nombre: {self.__nombre} | Edad: {self.__edad} anos"


class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)
        self.__calificaciones: list[float] = []

    def agregar_nota(self, nota: float):
        if not (0 <= nota <= 10):
            raise ValueError(f"La nota {nota} no es valida. Debe estar entre 0 y 10.")
        self.__calificaciones.append(nota)
        print(f"Nota {nota} anadida a {self.nombre}.")

    def promedio(self) -> float:
        if not self.__calificaciones:
            return 0.0
        return sum(self.__calificaciones) / len(self.__calificaciones)

    def mostrar_info(self) -> str:
        base = super().mostrar_info()
        notas = self.__calificaciones if self.__calificaciones else ["Sin notas"]
        return f"{base} | Calificaciones: {notas} | Promedio: {self.promedio():.2f}"


class Profesor(Persona):
    def __init__(self, nombre: str, edad: int, materia: str):
        super().__init__(nombre, edad)
        self.materia = materia

    @property
    def materia(self) -> str:
        return self.__materia

    @materia.setter
    def materia(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("La materia no puede estar vacia.")
        self.__materia = valor.strip()

    def corregir_examenes(self) -> str:
        return f"El profesor {self.nombre} esta corrigiendo examenes."

    def mostrar_info(self) -> str:
        base = super().mostrar_info()
        return f"{base} | Materia: {self.__materia}"


class Aula:
    def __init__(self, nombre_aula: str, profesor: Profesor):
        self.__nombre_aula = nombre_aula
        self.__profesor = profesor
        self.__estudiantes: list[Estudiante] = []

    def agregar_estudiante(self, estudiante: Estudiante):
        self.__estudiantes.append(estudiante)
        print(f"Estudiante '{estudiante.nombre}' anadido al aula '{self.__nombre_aula}'.")

    def promedio_clase(self) -> float:
        if not self.__estudiantes:
            return 0.0
        return sum(e.promedio() for e in self.__estudiantes) / len(self.__estudiantes)

    def mostrar_info(self):
        print(f"AULA: {self.__nombre_aula}")
        print(f"Profesor: {self.__profesor.mostrar_info()}")
        if not self.__estudiantes:
            print("Sin estudiantes")
        else:
            n = 1
            for est in self.__estudiantes:
                print(f"{n}. {est.mostrar_info()}")
                n += 1
        print(f"Promedio general del aula: {self.promedio_clase():.2f}")


def pedir_int(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Introduce un numero entero valido.")


def pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Introduce un numero valido.")


def seleccionar(lista, etiqueta):
    if not lista:
        print(f"No hay {etiqueta} disponibles.")
        return None
    n = 1
    for item in lista:
        print(f"{n}. {item.mostrar_info()}")
        n += 1
    pos = pedir_int(f"Selecciona {etiqueta} (numero): ") - 1
    if 0 <= pos < len(lista):
        return lista[pos]
    print("Numero no valido.")
    return None


def menu_estudiante(estudiante: Estudiante):
    while True:
        opcion = input(f"Gestionar {estudiante.nombre} | 1.Anadir nota  2.Ver promedio  3.Info  0.Volver: ").strip()
        if opcion == "1":
            nota = pedir_float("Nota (0-10): ")
            try:
                estudiante.agregar_nota(nota)
            except ValueError as e:
                print(e)
        elif opcion == "2":
            print(f"Promedio de {estudiante.nombre}: {estudiante.promedio():.2f}")
        elif opcion == "3":
            print(estudiante.mostrar_info())
        elif opcion == "0":
            break
        else:
            print("Opcion no valida.")


def main():
    profesores: list[Profesor] = []
    aulas: list[Aula] = []
    estudiantes: list[Estudiante] = []

    while True:
        opcion = input("1.Crear profesor  2.Crear estudiante  3.Crear aula  4.Anadir estudiante a aula  5.Gestionar estudiante  6.Ver aula  7.Corregir examenes  8.Listar estudiantes  9.Listar profesores  0.Salir: ").strip()

        if opcion == "1":
            nombre = input("Nombre del profesor: ").strip()
            edad = pedir_int("Edad: ")
            materia = input("Materia: ").strip()
            try:
                profesores.append(Profesor(nombre, edad, materia))
                print(f"Profesor '{nombre}' creado.")
            except ValueError as e:
                print(e)

        elif opcion == "2":
            nombre = input("Nombre del estudiante: ").strip()
            edad = pedir_int("Edad: ")
            try:
                estudiantes.append(Estudiante(nombre, edad))
                print(f"Estudiante '{nombre}' creado.")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            nombre_aula = input("Nombre del aula: ").strip()
            print("Profesores:")
            prof = seleccionar(profesores, "profesor")
            if prof:
                aulas.append(Aula(nombre_aula, prof))
                print(f"Aula '{nombre_aula}' creada.")

        elif opcion == "4":
            print("Aulas:")
            aula = seleccionar(aulas, "aula")
            if aula:
                print("Estudiantes:")
                est = seleccionar(estudiantes, "estudiante")
                if est:
                    aula.agregar_estudiante(est)

        elif opcion == "5":
            print("Estudiantes:")
            est = seleccionar(estudiantes, "estudiante")
            if est:
                menu_estudiante(est)

        elif opcion == "6":
            print("Aulas:")
            aula = seleccionar(aulas, "aula")
            if aula:
                aula.mostrar_info()

        elif opcion == "7":
            print("Profesores:")
            prof = seleccionar(profesores, "profesor")
            if prof:
                print(prof.corregir_examenes())

        elif opcion == "8":
            if not estudiantes:
                print("No hay estudiantes.")
            else:
                n = 1
                for e in estudiantes:
                    print(f"{n}. {e.mostrar_info()}")
                    n += 1

        elif opcion == "9":
            if not profesores:
                print("No hay profesores.")
            else:
                n = 1
                for p in profesores:
                    print(f"{n}. {p.mostrar_info()}")
                    n += 1

        elif opcion == "0":
            print("Hasta luego.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()