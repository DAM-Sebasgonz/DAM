class Persona:
    _alfabeto_nif = "TRWAGMYFPDXBNJZSQVHLCKE"

    def __init__(self, nombre, edad, nif):
        # Usamos los setters para validar desde el inicio
        self.nombre = nombre
        self.edad = edad 
        self.nif = nif

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self, valor: int):
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise TypeError("La edad debe ser un número entero")
        if valor <= 0:
            raise ValueError("La edad debe ser un número positivo")
        self._edad = valor

    @property
    def nif(self) -> str:
        return self._nif
    
    @nif.setter
    def nif(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("El NIF debe ser una cadena de texto")
        
        valor = valor.upper().strip()

        if len(valor) != 9:
            raise ValueError("El NIF debe tener exactamente 9 caracteres") 
        
        parte_numerica = valor[:-1]
        letra = valor[-1]
    
        if not parte_numerica.isdigit():
            raise ValueError("Los primeros 8 caracteres del NIF deben ser dígitos")
        
        if not letra.isalpha():
            raise ValueError("El último carácter del NIF debe ser una letra")
        
        letra_esperada = Persona._alfabeto_nif[int(parte_numerica) % 23]
        if letra != letra_esperada:
            raise ValueError(
                f"NIF inválido: la letra de control debería ser '{letra_esperada}', "
                f"pero se proporcionó '{letra}'."
            )

        self._nif = valor

    def __str__(self) -> str:
        return (
            f"Persona("
            f"nombre='{self._nombre}', "
            f"edad={self._edad}, "
            f"nif='{self._nif}'"
            f")"
        )

if __name__ == "__main__":
    print("=== Creación correcta ===")
    try:
        p = Persona("Ana Garcia", 30, "54250260E") 
        print(p)
    except Exception as e:
        print(f"Error: {e}")