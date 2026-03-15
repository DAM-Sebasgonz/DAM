class CuentaBancaria:
    def __init__(self, titular, nif_nie, nro_cuenta, limite_retiro):
        self.set_titular(titular)
        self.set_nif_nie(nif_nie)
        self.set_nro_cuenta(nro_cuenta)
        self.set_limite_retiro(limite_retiro)
        self.__saldo = 0.0

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        if titular != "":
            self.__titular = titular

    def get_nif_nie(self):
        return self.__nif_nie

    def set_nif_nie(self, nif):
        if self.validar_nif(nif):
            self.__nif_nie = nif

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo

    def get_nro_cuenta(self):
        return self.__nro_cuenta

    def set_nro_cuenta(self, cuenta):
        if len(cuenta) == 20 and cuenta.isdigit():
            self.__nro_cuenta = cuenta

    def get_limite_retiro(self):
        return self.__limite_retiro

    def set_limite_retiro(self, limite):
        if limite > 0 and limite < 1000:
            self.__limite_retiro = limite

    def validar_nif(self, nif):
        if len(nif) == 9:
            return True
        return False

    def depositarDinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirarDinero(self, cantidad):
        if cantidad <= self.__saldo and cantidad <= self.__limite_retiro:
            self.__saldo -= cantidad
            return True
        return False

    def obtenerSaldo(self):
        return self.__saldo

    def ocultar_nif(self):
        return self.__nif_nie[0:2] + "*****" + self.__nif_nie[-2:]

    def ocultar_cuenta(self):
        return "****" + self.__nro_cuenta[-4:]

    def __str__(self):
        return "Titular: " + self.__titular + " | NIF: " + self.ocultar_nif() + " | Cuenta: " + self.ocultar_cuenta() + " | Saldo: " + str(self.__saldo)

cuentas = []

def buscar_cuenta(numero):
    for c in cuentas:
        if c.get_nro_cuenta() == numero:
            return c
    return None

def menu():

    while True:
        print("1 Crear cuenta\n2 Depositar dinero\n3 Retirar dinero\n4 Mostrar saldo\n5 Mostrar cuentas\n6 Salir")
        opcion = int(input())
        match opcion:
            case 1:
                titular = input("Titular: ")
                nif = input("NIF/NIE: ")
                cuenta = input("Numero cuenta: ")
                limite = float(input("Limite retiro: "))
                c = CuentaBancaria(titular, nif, cuenta, limite)
                cuentas.append(c)
            case 2:
                cuenta = input("Cuenta: ")
                cantidad = float(input("Cantidad: "))
                c = buscar_cuenta(cuenta)
                if c != None:
                    c.depositarDinero(cantidad)
            case 3:
                cuenta = input("Cuenta: ")
                cantidad = float(input("Cantidad: "))
                c = buscar_cuenta(cuenta)
                if c != None:
                    resultado = c.retirarDinero(cantidad)
                    print(resultado)
            case 4:
                cuenta = input("Cuenta: ")
                c = buscar_cuenta(cuenta)
                if c != None:
                    print(c.obtenerSaldo())
            case 5:
                for c in cuentas:
                    print(c)
            case 6:
                print("Fin")
            case _:
                print("Opcion invalida")
menu()