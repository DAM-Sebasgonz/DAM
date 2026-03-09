from abc import ABC, abstractmethod
import random


class Sorteo(ABC):
    """Clase abstracta que modela un sorteo de la SELAE. Define la estructura comun para todos los juegos de loteria."""

    def __init__(self, nombre: str):
        """Inicializa el sorteo con un nombre y genera la combinacion ganadora.

        :param nombre: Nombre del sorteo.
        :type nombre: str
        """
        self.nombre = nombre
        self.combinacion_ganadora = self.generar_combinacion()

    @abstractmethod
    def generar_combinacion(self) -> list:
        """Genera la combinacion ganadora especifica de cada juego.

        :return: Combinacion ganadora generada aleatoriamente.
        :rtype: list
        """
        pass

    @abstractmethod
    def calcular_premio(self, apuesta: list) -> int:
        """Calcula el premio obtenido segun los aciertos de la apuesta.

        :param apuesta: Lista de numeros apostados por el usuario.
        :type apuesta: list
        :return: Premio en euros obtenido, 0 si no hay premio.
        :rtype: int
        """
        pass

    def __str__(self) -> str:
        """Devuelve una representacion legible del sorteo con su combinacion ganadora.

        :return: Cadena con el nombre y la combinacion ganadora.
        :rtype: str
        """
        return f"{self.nombre}: Combinacion = {self.combinacion_ganadora}"


class Primitiva(Sorteo):
    """Modela el juego de la Primitiva. Genera 6 numeros unicos entre 1 y 49."""

    def __init__(self):
        """Inicializa el sorteo de la Primitiva."""
        super().__init__("Primitiva")

    def generar_combinacion(self) -> list:
        """Genera 6 numeros aleatorios unicos entre 1 y 49.

        :return: Lista con los 6 numeros de la combinacion ganadora.
        :rtype: list
        """
        numeros = random.sample(range(1, 50), 6)
        return sorted(numeros)

    def calcular_premio(self, apuesta: list) -> int:
        """Calcula el premio de la Primitiva segun los aciertos.

        :param apuesta: Lista de 6 numeros apostados por el usuario.
        :type apuesta: list
        :return: Premio en euros: 1000000 (6 aciertos), 50000 (5), 500 (4), 8 (3), 0 (menos de 3).
        :rtype: int
        """
        aciertos = len(set(apuesta) & set(self.combinacion_ganadora))
        if aciertos == 6:
            return 1000000
        elif aciertos == 5:
            return 50000
        elif aciertos == 4:
            return 500
        elif aciertos == 3:
            return 8
        else:
            return 0


class Bonoloto(Sorteo):
    """Modela el juego de la Bonoloto. Genera 6 numeros unicos entre 1 y 49."""

    def __init__(self):
        """Inicializa el sorteo de la Bonoloto."""
        super().__init__("Bonoloto")

    def generar_combinacion(self) -> list:
        """Genera 6 numeros aleatorios unicos entre 1 y 49.

        :return: Lista con los 6 numeros de la combinacion ganadora.
        :rtype: list
        """
        numeros = random.sample(range(1, 50), 6)
        return sorted(numeros)

    def calcular_premio(self, apuesta: list) -> int:
        """Calcula el premio de la Bonoloto segun los aciertos.

        :param apuesta: Lista de 6 numeros apostados por el usuario.
        :type apuesta: list
        :return: Premio en euros: 500000 (6 aciertos), 10000 (5), 300 (4), 4 (3), 0 (menos de 3).
        :rtype: int
        """
        aciertos = len(set(apuesta) & set(self.combinacion_ganadora))
        if aciertos == 6:
            return 500000
        elif aciertos == 5:
            return 10000
        elif aciertos == 4:
            return 300
        elif aciertos == 3:
            return 4
        else:
            return 0


class GordoPrimitiva(Sorteo):
    """Modela el juego de El Gordo de la Primitiva. Genera 5 numeros unicos entre 1 y 54 mas un numero clave del 0 al 9."""

    def __init__(self):
        """Inicializa el sorteo de El Gordo de la Primitiva."""
        super().__init__("El Gordo de la Primitiva")

    def generar_combinacion(self) -> tuple:
        """Genera 5 numeros aleatorios unicos entre 1 y 54 y un reintegro entre 0 y 9.

        :return: Tupla con (lista de 5 numeros, reintegro).
        :rtype: tuple
        """
        numeros = sorted(random.sample(range(1, 55), 5))
        reintegro = random.randint(0, 9)
        return (numeros, reintegro)

    def calcular_premio(self, apuesta: tuple) -> int:
        """Calcula el premio de El Gordo segun los aciertos en numeros y reintegro.

        :param apuesta: Tupla con (lista de 5 numeros apostados, reintegro apostado).
        :type apuesta: tuple
        :return: Premio en euros segun tabla de premios.
        :rtype: int
        """
        numeros_ganadores, reintegro_ganador = self.combinacion_ganadora
        numeros_apuesta, reintegro_apuesta = apuesta

        aciertos = len(set(numeros_apuesta) & set(numeros_ganadores))
        reintegro_ok = reintegro_apuesta == reintegro_ganador

        if aciertos == 5 and reintegro_ok:
            return 2000000
        elif aciertos == 5:
            return 100000
        elif aciertos == 4:
            return 500
        elif aciertos == 3:
            return 20
        elif aciertos == 0 and reintegro_ok:
            return 5
        else:
            return 0

    def __str__(self) -> str:
        """Devuelve una representacion legible del sorteo con numeros y reintegro.

        :return: Cadena con el nombre, numeros y reintegro de la combinacion ganadora.
        :rtype: str
        """
        numeros, reintegro = self.combinacion_ganadora
        return f"{self.nombre}: Numeros = {numeros}, Reintegro = {reintegro}"


def pedir_apuesta_primitiva_bonoloto(nombre_sorteo: str) -> list:
    """Solicita al usuario que introduzca 6 numeros para la Primitiva o la Bonoloto.

    :param nombre_sorteo: Nombre del sorteo para mostrar al usuario.
    :type nombre_sorteo: str
    :return: Lista de 6 numeros enteros introducidos por el usuario.
    :rtype: list
    """
    print(f"\nIntroduce tu apuesta para {nombre_sorteo} (6 numeros entre 1 y 49):")
    while True:
        entrada = input("Numeros separados por espacios: ").strip().split()
        if len(entrada) != 6:
            print("Debes introducir exactamente 6 numeros.")
            continue
        try:
            numeros = [int(n) for n in entrada]
        except ValueError:
            print("Solo se permiten numeros enteros.")
            continue
        if any(n < 1 or n > 49 for n in numeros):
            print("Los numeros deben estar entre 1 y 49.")
            continue
        if len(set(numeros)) != 6:
            print("Los numeros no pueden repetirse.")
            continue
        return numeros


def pedir_apuesta_gordo() -> tuple:
    """Solicita al usuario que introduzca 5 numeros y un reintegro para El Gordo de la Primitiva.

    :return: Tupla con (lista de 5 numeros, reintegro).
    :rtype: tuple
    """
    print("\nIntroduce tu apuesta para El Gordo de la Primitiva:")
    while True:
        entrada = input("5 numeros entre 1 y 54 separados por espacios: ").strip().split()
        if len(entrada) != 5:
            print("Debes introducir exactamente 5 numeros.")
            continue
        try:
            numeros = [int(n) for n in entrada]
        except ValueError:
            print("Solo se permiten numeros enteros.")
            continue
        if any(n < 1 or n > 54 for n in numeros):
            print("Los numeros deben estar entre 1 y 54.")
            continue
        if len(set(numeros)) != 5:
            print("Los numeros no pueden repetirse.")
            continue
        break

    while True:
        try:
            reintegro = int(input("Reintegro (numero del 0 al 9): ").strip())
            if 0 <= reintegro <= 9:
                break
            print("El reintegro debe estar entre 0 y 9.")
        except ValueError:
            print("Introduce un numero entero valido.")

    return (numeros, reintegro)


if __name__ == "__main__":

    sorteos = [Primitiva(), Bonoloto(), GordoPrimitiva()]

    apuestas = []

    for sorteo in sorteos:
        if isinstance(sorteo, GordoPrimitiva):
            apuesta = pedir_apuesta_gordo()
        else:
            apuesta = pedir_apuesta_primitiva_bonoloto(sorteo.nombre)
        apuestas.append(apuesta)

    print("\n--- RESULTADOS ---")
    for sorteo, apuesta in zip(sorteos, apuestas):
        print(sorteo)
        premio = sorteo.calcular_premio(apuesta)
        print(f"Tu apuesta: {apuesta}")
        print(f"Premio obtenido: {premio} euros")
        print()
