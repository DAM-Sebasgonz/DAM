class Ordenador:

    lista_so = ["Windows 11", "Linux", "OSX Mojave"]

    def __init__(self,valor_marca, valor_modelo, cant_ram, cant_hd, so_usado):
        self.marca = valor_marca
        self.modelo = valor_modelo
        self._ram = cant_ram # >0 Gb int potencia de 2
        self._hd = cant_hd # >0 Gb int potencia de 2
        self.so = so_usado


#getter de ram
    @property
    def _ram(self):
        return self._ram
    
    @_ram.setter #setter
    def _ram(self, nuevo_valor):
        if nuevo_valor > 0 and isinstance(nuevo_valor, int):
            self._x = nuevo_valor
        else:
            raise ValueError("...")