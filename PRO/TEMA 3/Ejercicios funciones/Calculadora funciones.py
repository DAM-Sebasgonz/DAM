
#Calculadora de operaciones basica

def buscar_oper(linea:str):
    """Buscar operador y retorna su posicion si es valido si no es correcto devuelve None"""


    pass

def obtener_operandos():
    pass

def realizar_operacion():
    pass

def preparar_proxima_linea():
    pass

operadores = ("+","-","*","/","//","%")
while True:
    print("==> 0")
    linea_oper = input("==> ")
    if linea_oper == "@":
        break
    buscar_oper(linea_oper)
    obtener_operandos()
    realizar_operacion()
    preparar_proxima_linea()
