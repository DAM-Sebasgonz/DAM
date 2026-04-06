# KATA: Figuras geométricas y refactorización

# =========================
# Paso 0: implementación inicial pobre
# =========================

# TODO 1: Observa que en esta versión NO hay clase abstracta Figura.
# TODO 2: Observa que Rectangulo, Cuadrado y Triangulo repiten atributos (centro, color).
# TODO 3: Tu misión será ir refactorizando hasta cumplir el enunciado del docstring.
# TODO 4: Localiza literales y transformalos en Constantes. 
# TODO 5: Crea una estructura modularizada y de paquetes con los ficheros __init__.py

# PISTA: DEBES ejecutar el script en cualquier momento para comprobar que sigue funcionando.


# ---------- MODELO INICIAL (SIN ABSTRACT) ----------

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Rectangulo:
    def __init__(self, centro: Punto, base: float, altura: float, color: str):
        # TODO 6: Observa que todos los tipos de figura tendrán centro y color.
        self.centro = centro
        self.base = base
        self.altura = altura
        self.color = color

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def __str__(self):
        return (f"Rectángulo centro={self.centro}, base={self.base}, "
                f"altura={self.altura}, color={self.color}")


class Cuadrado:
    def __init__(self, centro: Punto, lado: float, color: str):
        # TODO 7: Este diseño duplica la lógica de Rectangulo.
        self.centro = centro
        self.lado = lado
        self.color = color

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado

    def __str__(self):
        return (f"Cuadrado centro={self.centro}, lado={self.lado}, "
                f"color={self.color}")


class Triangulo:
    # Para simplificar: triángulo cualquiera donde conocemos base, altura y los otros dos lados
    def __init__(self, centro: Punto, base: float, altura: float,
        lado2: float, lado3: float, color: str):
        self.centro = centro
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3
        self.color = color

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def perimetro(self) -> float:
        return self.base + self.lado2 + self.lado3

    def __str__(self):
        return (f"Triángulo centro={self.centro}, base={self.base}, "
                f"altura={self.altura}, lados={self.base}, "
                f"{self.lado2}, {self.lado3}, color={self.color}")


# ---------- FUNCIONES DE ENTRADA/SALIDA ----------

def leer_punto() -> Punto:
    # TODO 8: Captura ValueError si el usuario escribe algo que no sea número.
    x = float(input("   Coordenada x del centro: "))
    y = float(input("   Coordenada y del centro: "))
    return Punto(x, y)


def leer_color() -> str:
    # TODO 9: Podrías normalizar el color (strip, lower, etc.).
    return input("   Color: ")


def crear_rectangulo():
    print("Datos del rectángulo:")
    centro = leer_punto()
    base = float(input("   Base: "))
    altura = float(input("   Altura: "))
    color = leer_color()
    return Rectangulo(centro, base, altura, color)


def crear_cuadrado():
    print("Datos del cuadrado:")
    centro = leer_punto()
    lado = float(input("   Lado: "))
    color = leer_color()
    return Cuadrado(centro, lado, color)


def crear_triangulo():
    print("Datos del triángulo:")
    centro = leer_punto()
    base = float(input("   Base: "))
    altura = float(input("   Altura: "))
    lado2 = float(input("   Lado 2: "))
    lado3 = float(input("   Lado 3: "))
    color = leer_color()
    return Triangulo(centro, base, altura, lado2, lado3, color)


def mostrar_menu():
    print("\n=== MENÚ FIGURAS ===")
    print("1. Rectángulo")
    print("2. Cuadrado")
    print("3. Triángulo")
    print("0. Salir")


# ---------- PROGRAMA PRINCIPAL (USANDO LA VERSIÓN POBRE) ----------


# TODO 10: Este main funciona, pero no usa ninguna clase abstracta.
# TODO 11: Después de refactorizar, debería seguir funcionando igual,
#          pero usando Figura como superclase y polimorfismo.
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        figura = crear_rectangulo()
    elif opcion == "2":
        figura = crear_cuadrado()
    elif opcion == "3":
        figura = crear_triangulo()
    elif opcion == "0":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida.")
        continue

    print("\nHas creado:", figura)
    print(f"   Perímetro: {figura.perimetro()}")
    print(f"   Área: {figura.area()}")


