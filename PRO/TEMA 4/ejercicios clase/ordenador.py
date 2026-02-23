class Ordenador:

    lista_so = ['Windows 11', 'Linux', 'OSX Mojave']

    def __init__(self, valor_marca, valor_modelo, valor_procesador, cant_ram, cant_hd, so_usado):
        self.marca = valor_marca
        self.modelo = valor_modelo
        self.procesador = valor_procesador
        self._ram = cant_ram  # >0 Gb entero potencia de 2
        self._hd = cant_hd    # >0 Gb entero potencia de 2 
        self._so =  so_usado

# getter de ram
    @property
    def _ram(self):
        return self.__ram
    
    @_ram.setter # setter             # se define setter con 1 guión
    def _ram(self, nuevo_valor):
        if nuevo_valor > 0 and isinstance(nuevo_valor, int):
            self.__x = nuevo_valor
        else:
            raise ValueError('La coordenada x debe ser un valor >= 0')
