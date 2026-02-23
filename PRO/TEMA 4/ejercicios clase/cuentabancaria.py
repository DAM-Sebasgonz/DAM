def verificar_NIF_NIE(valor: str) -> bool:
    alfabeto_nif = 'TRWAGMYFPDXBNJZSQVHLCKE'

    if len(valor) != 9:
        return False
    if valor[0].isdigit():
        if not valor[:8].isdigit():
            return False
    elif not (valor[0] in 'XYZ' and valor[1:8].isdigit()):
        return False

    numero = valor[:8].replace('X', '0').replace('Y', '1').replace('Z', '2')
    if alfabeto_nif[int(numero) % 23] != valor[-1]:
        return False
    return True


def _calcular_digito_control(cadena: str) -> int:
    factores = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
    total = 0
    for i in range(len(factores)):
        total = total + int(cadena[i]) * factores[i]
    resto = total % 11
    dc = 11 - resto
    match dc:
        case 10:
            return 1
        case 11:
            return 0
        case _:
            return dc

def verificar_CCC(ccc: str) -> bool:
    try:
        if not ccc.isdigit() or len(ccc) != 20:
            return False

        entidad  = ccc[0:4]
        oficina  = ccc[4:8]
        dc1_real = int(ccc[8])
        dc2_real = int(ccc[9])
        cuenta   = ccc[10:20]

        cadena1  = '00' + entidad + oficina
        dc1_calc = _calcular_digito_control(cadena1)
        dc2_calc = _calcular_digito_control(cuenta)

        match (dc1_calc == dc1_real, dc2_calc == dc2_real):
            case (True, True):
                return True
            case _:
                return False

    except (ValueError, IndexError):
        return False

class CuentaBancaria:

    def __init__(self, titular: str, nif: str, nro_cuenta: str, saldo_inicial: float = 0.0):
        if not titular.strip():
            raise ValueError("El titular no puede estar vacío.")
        if not verificar_NIF_NIE(nif.upper()):
            raise ValueError("NIF/NIE no válido.")
        nro_cuenta = nro_cuenta.replace(" ", "")
        if not verificar_CCC(nro_cuenta):
            raise ValueError("El número de cuenta no es un CCC de 20 dígitos válido.")
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")

        self.titular    = titular.strip()
        self.nif        = nif.upper()
        self.nro_cuenta = nro_cuenta
        self.saldo      = saldo_inicial

    def depositar(self, cantidad: float):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        self.saldo += cantidad
        print(f"Depósito realizado. Saldo actual: {self.saldo:.2f} €")

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
        elif cantidad > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= cantidad
            print(f"Retiro realizado. Saldo actual: {self.saldo:.2f} €")

    def __str__(self):
        cuenta_enmascarada = '****************' + self.nro_cuenta[-4:]
        return (
            f"\n{'='*40}\n"
            f"  Titular  : {self.titular}\n"
            f"  NIF/NIE  : {self.nif}\n"
            f"  N cuenta : {cuenta_enmascarada}\n"
            f"  Saldo    : {self.saldo:.2f} €\n"
            f"{'='*40}"
        )

cuentas = []

def crear_cuenta():
    print("\n-- Crear cuenta --")
    try:
        titular    = input("Titular          : ")
        nif        = input("NIF/NIE          : ")
        nro_cuenta = input("N cuenta (20 d)  : ")
        saldo      = float(input("Saldo inicial    : "))
        cuenta = CuentaBancaria(titular, nif, nro_cuenta, saldo)
        cuentas.append(cuenta)
        print("Cuenta creada correctamente.")
        print(cuenta)
    except ValueError as e:
        print(f"Error: {e}")


def seleccionar_cuenta():
    if not cuentas:
        print("No hay cuentas registradas.")
        return None
    print("\n-- Seleccionar cuenta --")
    for i, c in enumerate(cuentas, 1):
        print(f"[{i}] {c.titular} | Saldo: {c.saldo:.2f} €")
    try:
        opcion = int(input("Elige una cuenta: ")) - 1
        if 0 <= opcion < len(cuentas):
            return cuentas[opcion]
        print("Opción no válida.")
    except ValueError:
        print("Entrada no válida.")
    return None


def menu():
    opciones = {
        '1': 'Crear cuenta',
        '2': 'Ver cuenta',
        '3': 'Depositar dinero',
        '4': 'Retirar dinero',
        '5': 'Listar todas las cuentas',
        '0': 'Salir'
    }

    while True:
        print("\n=== GESTOR DE CUENTAS ===")
        for k, v in opciones.items():
            print(f"  {k}. {v}")

        opcion = input("Opción: ").strip()

        if opcion == '1':
            crear_cuenta()

        elif opcion == '2':
            cuenta = seleccionar_cuenta()
            if cuenta:
                print(cuenta)

        elif opcion == '3':
            cuenta = seleccionar_cuenta()
            if cuenta:
                try:
                    cantidad = float(input("Cantidad a depositar: "))
                    cuenta.depositar(cantidad)
                except ValueError:
                    print("Cantidad no válida.")

        elif opcion == '4':
            cuenta = seleccionar_cuenta()
            if cuenta:
                try:
                    cantidad = float(input("Cantidad a retirar: "))
                    cuenta.retirar(cantidad)
                except ValueError:
                    print("Cantidad no válida.")

        elif opcion == '5':
            if not cuentas:
                print("No hay cuentas registradas.")
            else:
                for c in cuentas:
                    print(c)

        elif opcion == '0':
            print("Hasta luego.")
            break

        else:
            print("Opción no reconocida.")

if __name__ == '__main__':
    menu()