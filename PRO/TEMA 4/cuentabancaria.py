# Se quiere modelar una cuenta bancaria
# clase se llama CuentaBanco
# atributos
# nro_cuenta: string 20 digitos
# saldo : float
# titular : string
# movimiento : lista tuplas (fecha, importe)
    # importe postivo indica ingresar dinero
    # importe negativo indica sacar dinero
# tipo_cuenta: string ("Corriente" o "ahorro")
# interes cuenta ahorros = float que indica el porcentaje mensual
# metodos
# obtenerNroCuenta
# obtenerSaldo
# obtenerTitular
# depositarCuenta(cantidad)
# retirarcuenta(cantidad) -> booleano
# reescribir __str__ para mostrar todos los datos (sin incluir movimientos)
# mostrarMovimientos(nro_cuenta)

class CuentaBancaria:
    def __init__(self, nro_cuenta:str, nombre:str, tipo:str, interes:float) -> None:
        self.nro_cuenta = nro_cuenta
        self.saldo = 0.0
        self.titular = nombre
        self.movimientos = []
        self.tipoCuenta = tipo
        self.porc_interes_cobrar = interes

    def obtenerNroCuenta(self) -> str:
        return self.nro_cuenta
    
    def obtenerSaldo(self) -> float:
        return self.saldo
    
    def obtenerTitular(self) -> str:
        return self.titular
    
    def depostarCuenta(self, cantidad: float, fecha:str):
        self.saldo += cantidad
        self.movimientos.append((cantidad,fecha))

    def retirarCuenta(self, cantidad:float, fecha:str)
        if cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        self.movimientos.append((cantidad,fecha)):
        return True
    
    def __str__(self) -> str:
        texto = f"Numero de cuenta: {self.nro_cuenta}"
        texto += f"\nTitular de la cuenta: {self.titular}"
        texto += f"\nSaldo de la cuenta {self.saldo}"
        texto += f"\nTipo de cuenta {self.saldo}"
        texto += f"\nTipo de interes{self.porc_interes_cobrar}"
        pass

def agregarCuenta():
    fecha = input(" fecha dd/mm/aa")
    nombre =  input("nombre -> ")
    cuenta = input("nro de cuenta -> ")
    tipo_cuenta = input("tipo de cuenta -> ")
    porc_beneficios = input("% benef <intro> 0,0% -> ") 
    if porc_beneficios == "":
        porc_beneficios = 0.0
    else:
        porc_beneficios = float(porc_beneficios)

if __name__ = "__main__"
    lista_cuentas = []

    while True:
        print("""\n1. Agregar cuenta \n9.Salir""")
        opc = input("Indique opcion:")
        match opc:
            case "1":
                cuenta_creada = 
                pass
            case "9":
                print("fin de ejecuccion")
                break
            case _:
                print("Error...Opcion invalida")


        