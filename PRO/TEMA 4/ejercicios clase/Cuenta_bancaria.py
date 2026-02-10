# Se quiere modelar una cuenta bancaria
# clase se llama Cuenta Banco
# atributos

# nro_cuent : string 20 dígitos
# saldo : float
# titular : string
# movimientos : lista tuplas (fecha, importe)
#     importe positivo indica ingresar dinero
#     importe negatico indica sacar dinero

# tipo_cuenta : string( 'corriente' o 'ahorro' )

# interes cuenta ahorros = float indica el porcentaje mensual

# métodos

# obtenerNroCuenta()
# obtenerSaldo()
# obtenerTitular()
# depositarCuenta(cantidad)
# retirarCuenta(cantidad) -> booleano
# reescribir __str__ para mostrar todos los datos (sin incluir movimientos)
# mostrarMovimientos(nro_cuenta)

# No se puede eliminar una cuenta si tiene saldo

class CuentaBancaria:
    def __init__(self, nro_cuenta:str, titular:str,  tipo_cuenta:str, fecha:str, interes:float):
        self.nro_cuenta = nro_cuenta
        self.titular = titular
        self.saldo = 0.0
        self.creacion = fecha
        self.movmientos = []
        self.tipo_cuenta = tipo_cuenta
        self.porc_interes_cobrar = interes

    def obtenerNroCuenta(self):
        return self.nro_cuenta
    
    def obtenerSaldo(self):
        return self.saldo
    
    def obtenerTitular(self):
        return self.titular
    
    def depositarCuenta(self, cantidad:float, fecha: str):
        self.saldo += cantidad
        self.movimientos.append((cantidad, fecha))

    def retirarCuenta(self, cantidad:float, fecha: str):
        if cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        self.movimientos.append((-cantidad, fecha))
        return True
    
    def __str__(self) -> str:
        texto = ''
        texto += f'Número de cuenta: {self.nro_cuenta}'
        texto += f'\nTitular de cuenta: {self.titular}'
        texto += f'\nSaldo de cuenta: {self.saldo}'
        texto += f'\nTipo de cuenta: {self.tipo_cuenta}'
        texto += f'\nTipo de interés: {self.porc_interes_cobrar}'
        return texto

# funciones

def agregarCuenta():
    fecha = input('fecha dd/mm/aa --> ')
    nombre = input('nombre --> ')
    cuenta = input('Número de cuenta -->') # debe generarlo una funcion - valor único
    tipo_cuenta = input('tipo de cuenta ("ahorro" ó "corriente") --> ')
    if tipo_cuenta == 'ahorros':
        porc_beneficios = float(input('%benef --> ')) 
    else:
        porc_beneficios = 0.0

    cuenta_retornar = CuentaBancaria(cuenta, nombre, tipo_cuenta, fecha, porc_beneficios)
    
    return cuenta_retornar
if __name__ == '__main__':

    lista_cuentas = []

    while True:
        print('''\n1.Agregar Cuenta \n2.Ingresar dinero \n3.Retirar dinero \n4.Eliminar Cuenta \n9.Salir''')
        opc = int(input('Indique opción: '))
        match opc:
            case 1:
                cuenta_creada = agregarCuenta()
                lista_cuentas.append(cuenta_creada)
                # lista_cuentas.append(agregarCuentas())
            case 3:
                cantidad_ingresar = float(input('Importe a ingresar --> '))
                cuenta_ingreso = input('indique la cuenta --> ')
                fecha_ingreso = input('indique fecha dd/mm/aa --> ')
                for objeto in lista_cuentas:
                    if objeto.nro_cuentas == cuenta_ingreso:
                        objeto.depositarCuenta(cantidad_ingresar, fecha_ingreso)
                        break
                    else:
                        print("error... La cuenta no existe")
                else:
                    print('Error...')
            case 9:
                print('Saliendo del programa...')
                break
            case _:
                print('Error... Opción inválida')