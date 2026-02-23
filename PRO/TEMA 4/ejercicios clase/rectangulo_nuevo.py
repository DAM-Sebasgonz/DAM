class Rectangulo:
    def __init__(self, valor_base:int = 0, valor_altura:int = 0 ):
        self.a = valor_base
        self.b = valor_altura

    def calcularPerimetro(self):
        return 2 * self.a + 2 * self.b
    
    def calcularArea(self):
        return self.a * self.b

    def __str__(self) -> str:
        salida = f'base = {self.a}'
        salida += f'\naltura = {self.b}'
        salida += f'\nperímetro = {self.calcularPerimetro()}'
        salida += f'\nárea = {self.calcularArea()}'
        return salida

if __name__ == '__main__':
    rect1 = Rectangulo(3,5)
    print(rect1)
