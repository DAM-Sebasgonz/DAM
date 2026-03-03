class Persona:
    def __init__(self, nombre, edad, nif):
        self.nombre = nombre
        self.edad = edad 
        self.nif = nif

    
    @property
    def nombre (self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = valor.strip()

    
    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self,valor: int):
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise TypeError("La debe ser un numero entero")
        if valor <= 0:
            raise ValueError("La edad deber ser un numeor positivo")
        self._edad = valor

    @property
    def nif(self) -> str:
        return self._nif
    
    @nif.setter
    def nif(self, valor:str):
        if not isinstance(valor,str):
            raise TypeError("El nif debe ser una cadena de texto")
        
        valor = valor.upper().strip()

        if len(valor) !=9:
            raise ValueError("El nif debe tener exactamente 9 caracteres de longitud") 

               