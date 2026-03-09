import datetime

class Vehiculo:
    """Clase base que representa un vehiculo de la flota de alquiler. Valida los atributos comunes mediante getters y setters."""

    def __init__(self, marca: str, modelo: str, anio: int, matricula: str):
        """Inicializa un vehiculo validando todos sus atributos."""

        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.matricula = matricula

    @property
    def marca(self) -> str:
        """Devuelve la marca del vehiculo."""
        return self._marca

    @marca.setter
    def marca(self, valor: str):
        """Establece la marca del vehiculo. No puede estar vacia. """
        if not valor or not valor.strip():
            raise ValueError("La marca no puede estar vacia.")
        self._marca = valor.strip()

    @property
    def modelo(self) -> str:
        """Devuelve el modelo del vehiculo."""
        return self._modelo

    @modelo.setter
    def modelo(self, valor: str):
        """Establece el modelo del vehiculo. No puede estar vacio."""
        if not valor or not valor.strip():
            raise ValueError("El modelo no puede estar vacio.")
        self._modelo = valor.strip()

    @property
    def anio(self) -> int:
        """Devuelve el año de fabricacion del vehiculo."""
        return self._anio

    @anio.setter
    def anio(self, valor: int):
        """Establece el año de fabricacion. Debe estar entre 1900 y el año actual."""
        anio_actual = datetime.datetime.now().year
        if valor < 1900 or valor > anio_actual:
            raise ValueError(f"El año debe estar entre 1900 y {anio_actual}.")
        self._anio = valor

    @property
    def matricula(self) -> str:
        """Devuelve la matricula del vehiculo."""
        return self._matricula

    @matricula.setter
    def matricula(self, valor: str):
        """Establece la matricula. Debe tener 7 caracteres con los 3 ultimos siendo letras ."""
        if len(valor) != 7 or not valor[-3:].isalpha():
            raise ValueError("La matricula debe tener 7 caracteres y los 3 ultimos deben ser letrascl.")
        self._matricula = valor

    def calcular_precio_alquiler(self, dias: int) -> float:
        """Calcula el precio base de alquiler. Devuelve 0 en la clase base."""
        return 0

    def __str__(self) -> str:
        """Devuelve una representacion legible del vehiculo."""
        return f"Vehiculo | Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}, Matricula: {self._matricula}"


class Coche(Vehiculo):
    """Representa un coche de la flota. Hereda de Vehiculo y anade el numero de plazas."""

    def __init__(self, marca: str, modelo: str, anio: int, matricula: str, plazas: int):
        """Inicializa un coche con todos sus atributos."""
        super().__init__(marca, modelo, anio, matricula)
        self.plazas = plazas

    @property
    def plazas(self) -> int:
        """Devuelve el numero de plazas del coche. """
        return self._plazas

    @plazas.setter
    def plazas(self, valor: int):
        """Establece el numero de plazas. Debe estar entre 2 y 9."""
        if valor < 2 or valor > 9:
            raise ValueError("El numero de plazas debe estar entre 2 y 9.")
        self._plazas = valor

    def calcular_precio_alquiler(self, dias: int) -> float:
        """Calcula el precio de alquiler del coche: 50 euros por dia mas 10 euros por plaza."""
        return 50 * dias + 10 * self._plazas

    def __str__(self) -> str:
        """Devuelve una representacion legible del coche."""
        base = super().__str__().replace("Vehiculo", "Coche")
        return f"{base}, Plazas: {self._plazas}"


class Moto(Vehiculo):
    """Representa una moto de la flota. Hereda de Vehiculo y anade la cilindrada."""

    def __init__(self, marca: str, modelo: str, anio: int, matricula: str, cilindrada: int):
        """Inicializa una moto con todos sus atributos."""
        super().__init__(marca, modelo, anio, matricula)
        self.cilindrada = cilindrada

    @property
    def cilindrada(self) -> int:
        """Devuelve la cilindrada de la moto. """
        return self._cilindrada

    @cilindrada.setter
    def cilindrada(self, valor: int):
        """Establece la cilindrada. Debe ser mayor que 49 cc."""
        if valor <= 49:
            raise ValueError("La cilindrada debe ser mayor que 49 cc (no se permiten ciclomotores).")
        self._cilindrada = valor

    def calcular_precio_alquiler(self, dias: int) -> float:
        """Calcula el precio de alquiler de la moto: 30 euros por dia mas 5 euros por cada 100 cc."""
        return 30 * dias + (5 * (self._cilindrada / 100))

    def __str__(self) -> str:
        """Devuelve una representacion legible de la moto."""
        base = super().__str__().replace("Vehiculo", "Moto")
        return f"{base}, Cilindrada: {self._cilindrada} cc"


class Furgoneta(Vehiculo):
    """Representa una furgoneta de la flota. Hereda de Vehiculo y anade la capacidad de carga."""

    def __init__(self, marca: str, modelo: str, anio: int, matricula: str, capacidad_carga: float):
        """Inicializa una furgoneta con todos sus atributos. """
        super().__init__(marca, modelo, anio, matricula)
        self.capacidad_carga = capacidad_carga

    @property
    def capacidad_carga(self) -> float:
        """Devuelve la capacidad de carga de la furgoneta."""
        return self._capacidad_carga

    @capacidad_carga.setter
    def capacidad_carga(self, valor: float):
        """Establece la capacidad de carga. Debe estar entre 500 y 5000 kg. """
        if valor < 500 or valor > 5000:
            raise ValueError("La capacidad de carga debe estar entre 500 y 5000 kg.")
        self._capacidad_carga = valor

    def calcular_precio_alquiler(self, dias: int) -> float:
        """Calcula el precio de alquiler de la furgoneta: 70 euros por dia mas 0.5 euros por kg de carga."""
        return 70 * dias + 0.5 * self._capacidad_carga

    def __str__(self) -> str:
        """Devuelve una representacion legible de la furgoneta."""
        base = super().__str__().replace("Vehiculo", "Furgoneta")
        return f"{base}, Capacidad de carga: {self._capacidad_carga} kg"


def mostrar_flota_y_precios(flota: dict, dias: int):
    """Muestra los datos de todos los vehiculos de la flota y el precio de alquiler para los dias indicados."""
    print(f"\n--- FLOTA DE VEHICULOS (precio para {dias} dias) ---")
    for vehiculo in flota.values():
        precio = vehiculo.calcular_precio_alquiler(dias)
        print(f"{vehiculo}")
        print(f"  Precio de alquiler ({dias} dias): {precio:.2f} euros")
        print()


def Ordenar_vehiculos(lista: list, dias: int) -> list:
    """Ordena una lista de vehiculos por precio de alquiler ascendente usando bubble sort."""
    n = len(lista)
    lista_copia = lista[:]
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista_copia[j].calcular_precio_alquiler(dias) > lista_copia[j + 1].calcular_precio_alquiler(dias):
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia


if __name__ == "__main__":

    flota = {}

    vehiculos_datos = [
        ("Coche", "Toyota", "Corolla", 2020, "1234ABC", {"plazas": 5}),
        ("Moto", "Honda", "CBR600", 2019, "3456JKL", {"cilindrada": 600}),
        ("Furgoneta", "Renault", "Megane", 2017, "6789STU", {"capacidad_carga": 1200.0}),
    ]

    vehiculos_invalidos = [
        ("Coche invalido: plazas fuera de rango", "BMW", "Serie 3", 2020, "9012BCD", {"plazas": 12}),
        ("Moto invalida: ciclomotor", "Vespa", "50 Special", 2021, "3456EFG", {"cilindrada": 49}),
    ]

    for tipo, marca, modelo, anio, matricula, extras in vehiculos_datos:
        try:
            if tipo == "Coche":
                v = Coche(marca, modelo, anio, matricula, extras["plazas"])
            elif tipo == "Moto":
                v = Moto(marca, modelo, anio, matricula, extras["cilindrada"])
            elif tipo == "Furgoneta":
                v = Furgoneta(marca, modelo, anio, matricula, extras["capacidad_carga"])
            flota[(marca, modelo)] = v
        except ValueError as e:
            print(f"Error al crear vehiculo {marca} {modelo}: {e}")

    print("\n--- PRUEBAS DE VALIDACION CON DATOS INVALIDOS ---")
    for descripcion, marca, modelo, anio, matricula, extras in vehiculos_invalidos:
        try:
            if "plazas" in extras:
                v = Coche(marca, modelo, anio, matricula, extras["plazas"])
            elif "cilindrada" in extras:
                v = Moto(marca, modelo, anio, matricula, extras["cilindrada"])
            elif "capacidad_carga" in extras:
                v = Furgoneta(marca, modelo, anio, matricula, extras["capacidad_carga"])
            else:
                v = Vehiculo(marca, modelo, anio, matricula)
            flota[(marca, modelo)] = v
        except ValueError as e:
            print(f"[{descripcion}] Error: {e}")

    dias = 5
    mostrar_flota_y_precios(flota, dias)

    lista_vehiculos = list(flota.values())
    lista_ordenada = Ordenar_vehiculos(lista_vehiculos, dias)

    vehiculo_mas_barato = lista_ordenada[0]
    vehiculo_mas_caro = lista_ordenada[-1]

    print("--- VEHICULO MAS BARATO ---")
    print(vehiculo_mas_barato)
    print(f"Precio: {vehiculo_mas_barato.calcular_precio_alquiler(dias):} euros")

    print("\n--- VEHICULO MAS CARO ---")
    print(vehiculo_mas_caro)
    print(f"Precio: {vehiculo_mas_caro.calcular_precio_alquiler(dias):} euros")