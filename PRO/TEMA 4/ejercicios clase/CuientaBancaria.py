# Se quiere modelar una cuenta bancaria
# clase se llama CuentaBanco
# atributos 
# nro_cuenta : string 20 dígitos
# saldo : float
# titular : string
# movimientos : lista tuplas (fecha, importe) 
#     importe positivo indica ingresar dinero
#     importe negtivo indica sacar dinero
# tipo_cuenta : string( 'corriente' o 'ahorro')
# interes cuenta ahorros = float indica el porcentaje mensual de beneficio
# métodos
# obtenerNroCuenta()
# obtenerSaldo()
# obtenerTitular()
# depositarCuenta(cantidad)
# retirarCuenta(cantidad) -> booleano
# reescribir __str__ para mostrar todos los datos (sin incluir movimientos)
# mostrarMovimientos(nro_cuenta)

class CuentaBancaria:
    def __init__(self, nrocuenta:str, nombre:str, tipo:str, fecha: str, interes:float):
        self.nro_cuenta = nrocuenta
        self.titular = nombre
        self.saldo = 0.0
        self.creacion = fecha
        self.movimientos = []
        self.tipo_cuenta = tipo
        self.porc_interes_cobrar = interes

    def obtenerNroCuenta(self) -> str:
        return self.nro_cuenta

    def obtenerSaldo(self) -> float:
        return self.saldo

    def obtenerTitular(self) -> str:
        return self.titular

    def depositarCuenta(self, cantidad: float, fecha: str):
        self.saldo += cantidad
        self.movimientos.append((cantidad, fecha))
    
    def retirarCuenta(self, cantidad: float, fecha : str):
        if cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        self.movimientos.append((-cantidad, fecha))
        return True

    def __str__(self) -> str:
        texto = f'Número de cuenta: {self.nro_cuenta}'
        texto += f'\nTitular de la cuenta: {self.titular}'
        texto += f'\nSaldo de la cuenta: {self.saldo}'
        texto += f'\nTipo de cuenta: {self.tipo_cuenta}'
        texto += f'\nTipo de interés: {self.porc_interes_cobrar}'
        return texto

    def mostrarMovimientos(self):
        print(f'Los movimientos de la cuenta {self.nro_cuenta}')
        if self.movimientos:
            for movimiento in self.movimientos:
                print(movimiento)
        else:
            print('La lista no tiene movimientos')

# funciones

def agregarCuenta():
    fecha = input('fecha dd/mm/aa -> ')
    nombre = input('nombre -> ')
    cuenta = input('nro de cuenta -> ') # debe generarlo una función - valor único
    tipo_cuenta = input('tipo de cuenta ("ahorro" ó "corriente") -> ')
    if tipo_cuenta == 'ahorro':
        porc_beneficios = float(input('Porcentaje beneficios -> '))
    else:
        porc_beneficios = 0.0
    cuenta_retornar = CuentaBancaria(cuenta, nombre, tipo_cuenta, fecha, porc_beneficios)
    return cuenta_retornar

if __name__ == '__main__':
    lista_cuentas = []

    while True:
        print('''\n1. Agregar Cuenta\n2. Realizar depósito\n3. Realizar retiro\n4. Listar cuentas\n5. Movimientos de una cuenta\n9. Salir''')
        opc = int(input('\nIndique opción: '))
        match opc:
            case 1:
                cuenta_creada = agregarCuenta()
                lista_cuentas.append(cuenta_creada)
                # lista_cuentas.append(agregarCuenta())
            case 2:
                cantidad_ingresar = float(input('Importe a ingresar -> '))
                cuenta_ingreso = input('indique la cuenta -> ')
                fecha_ingreso = input('intoduzca fecha dd/mm/aa -> ')
                for objeto in lista_cuentas:
                    if objeto.nro_cuenta == cuenta_ingreso:
                        objeto.depositarCuenta(cantidad_ingresar, fecha_ingreso)
                        break
                else:
                    print('Error...la cuenta no existe')
            case 3:
                cantidad_retirar = float(input('Importe a retirar -> '))
                cuenta_retiro = input('indique la cuenta -> ')
                fecha_retiro = input('intoduzca fecha dd/mm/aa -> ')
                for objeto in lista_cuentas:
                    if objeto.nro_cuenta == cuenta_retiro:
                        if not objeto.retirarCuenta(cantidad_retirar, fecha_retiro):
                            print('Warning...No hay saldo suficiente')
                        break
                else:
                    print('Error...la cuenta no existe')

            case 4:
                for cuenta in lista_cuentas:
                    print(cuenta)
                    print('\n')

            case 5:
                    cuenta_verificar = input('indique la cuenta -> ')
                    for objeto in lista_cuentas:
                        if objeto.nro_cuenta == cuenta_verificar:
                            objeto.mostrarMovimientos()
                            break
                    else:
                        print('Error...la cuenta no existe')

            case 9:
                print('\nFin de ejecución ...')
                break
            case _:
                print('Error...Opción inválida')
