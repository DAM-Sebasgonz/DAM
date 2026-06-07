from PySide6.QtWidgets import QApplication, QMainWindow
from Calculadora_ui import Ui_Calculadora

class VentanaCalculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Calculadora()
        self.ui.setupUi(self)
        
        self.visor_actual = "0"
        self.actualizar_visor()
        
        self.ui.pushButton_10.clicked.connect(self.presionar_0)
        self.ui.pushButton_2.clicked.connect(self.presionar_1)
        self.ui.pushButton.clicked.connect(self.presionar_2)
        self.ui.pushButton_3.clicked.connect(self.presionar_3)
        self.ui.pushButton_6.clicked.connect(self.presionar_4)
        self.ui.pushButton_4.clicked.connect(self.presionar_5)
        self.ui.pushButton_5.clicked.connect(self.presionar_6)
        self.ui.pushButton_9.clicked.connect(self.presionar_7)
        self.ui.pushButton_7.clicked.connect(self.presionar_8)
        self.ui.pushButton_8.clicked.connect(self.presionar_9)
        
        self.ui.pushButton_15.clicked.connect(self.presionar_suma)
        self.ui.pushButton_16.clicked.connect(self.presionar_resta)
        self.ui.pushButton_13.clicked.connect(self.presionar_multiplicacion)
        self.ui.pushButton_14.clicked.connect(self.presionar_division)
        
        self.ui.pushButton_11.clicked.connect(self.presionar_calcular)
        self.ui.pushButton_12.clicked.connect(self.presionar_borrar)

    def actualizar_visor(self):
        self.ui.lineEdit.setText(self.visor_actual)

    def presionar_0(self): self.agregar_numero("0")
    def presionar_1(self): self.agregar_numero("1")
    def presionar_2(self): self.agregar_numero("2")
    def presionar_3(self): self.agregar_numero("3")
    def presionar_4(self): self.agregar_numero("4")
    def presionar_5(self): self.agregar_numero("5")
    def presionar_6(self): self.agregar_numero("6")
    def presionar_7(self): self.agregar_numero("7")
    def presionar_8(self): self.agregar_numero("8")
    def presionar_9(self): self.agregar_numero("9")

    def agregar_numero(self, numero_pulsado):
        if self.visor_actual == "0" or self.visor_actual == "Error":
            self.visor_actual = numero_pulsado
        else:
            self.visor_actual += numero_pulsado
        self.actualizar_visor()

    def presionar_suma(self): self.agregar_operador("+")
    def presionar_resta(self): self.agregar_operador("-")
    def presionar_multiplicacion(self): self.agregar_operador("*")
    def presionar_division(self): self.agregar_operador("/")

    def agregar_operador(self, operador_pulsado):
        if self.visor_actual == "Error":
            self.visor_actual = "0"
            
        if self.visor_actual == "0":
            if operador_pulsado == "-":
                self.visor_actual = "-"
            else:
                self.visor_actual = "0" + operador_pulsado
            self.actualizar_visor()
            return
            
        ultimo_caracter = self.visor_actual[-1]
        es_operador = (ultimo_caracter == "+" or ultimo_caracter == "-" or ultimo_caracter == "*" or ultimo_caracter == "/")
        
        if es_operador:
            combinacion = ultimo_caracter + operador_pulsado
            combinacion_valida = (combinacion == "**" or combinacion == "+-" or combinacion == "--" or combinacion == "*-" or combinacion == "/-")
            if combinacion_valida:
                self.visor_actual += operador_pulsado
        else:
            self.visor_actual += operador_pulsado
            
        self.actualizar_visor()

    def presionar_borrar(self):
        if self.visor_actual == "Error":
            self.visor_actual = "0"
            self.actualizar_visor()
            return
            
        if len(self.visor_actual) > 1:
            self.visor_actual = self.visor_actual[:-1]
        else:
            self.visor_actual = "0"
            
        self.actualizar_visor()

    def presionar_calcular(self):
        tiene_operador = False
        for caracter in self.visor_actual:
            if caracter == "+" or caracter == "-" or caracter == "*" or caracter == "/":
                tiene_operador = True
                
        if not tiene_operador:
            self.visor_actual = "Error"
            self.actualizar_visor()
            return
            
        ultimo_caracter = self.visor_actual[-1]
        if ultimo_caracter == "+" or ultimo_caracter == "-" or ultimo_caracter == "*" or ultimo_caracter == "/":
            self.visor_actual = "Error"
            self.actualizar_visor()
            return

        try:
            expresion = self.visor_actual
            posicion_operador = -1
            operador_principal = ""
            
            if "**" in expresion[1:]:
                posicion_operador = expresion.find("**", 1) 
                operador_principal = "**"
            else:
                for i in range(1, len(expresion)):
                    caracter = expresion[i]
                    if caracter == "+" or caracter == "-" or caracter == "*" or caracter == "/":
                        posicion_operador = i
                        operador_principal = caracter
                        break
                        
            if operador_principal == "**":
                texto_numero1 = expresion[:posicion_operador]
                texto_numero2 = expresion[posicion_operador + 2:] 
            else:
                texto_numero1 = expresion[:posicion_operador]
                texto_numero2 = expresion[posicion_operador + 1:] 
                
            numero1 = int(texto_numero1)
            numero2 = int(texto_numero2)
            
            if operador_principal == "+":
                resultado_final = numero1 + numero2
            elif operador_principal == "-":
                resultado_final = numero1 - numero2
            elif operador_principal == "*":
                resultado_final = numero1 * numero2
            elif operador_principal == "/":
                resultado_final = numero1 // numero2 
            elif operador_principal == "**":
                resultado_final = numero1 ** numero2
                
            self.visor_actual = str(resultado_final)
            
        except ZeroDivisionError:
            self.visor_actual = "Error"
        except Exception:
            self.visor_actual = "Error"
            
        self.actualizar_visor()

if __name__ == "__main__":
    app = QApplication([])
    mi_calculadora = VentanaCalculadora()
    mi_calculadora.show()
    app.exec()