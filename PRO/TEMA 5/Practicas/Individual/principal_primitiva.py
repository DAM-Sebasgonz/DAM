import sys
import json
import random
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QButtonGroup
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from primitiva_ui import Ui_Primitiva

mapaDecenas = {
    "checkBox": 0, "checkBox_2": 10, "checkBox_3": 20, "checkBox_4": 30, "checkBox_5": 40
}

mapaUnidades = {
    "checkBox_6": (0, 0), "checkBox_7": (1, 0), "checkBox_8": (2, 0), "checkBox_9": (3, 0), "checkBox_10": (4, 0),
    "checkBox_12": (0, 1), "checkBox_14": (1, 1), "checkBox_11": (2, 1), "checkBox_15": (3, 1), "checkBox_13": (4, 1),
    "checkBox_17": (0, 2), "checkBox_19": (1, 2), "checkBox_16": (2, 2), "checkBox_20": (3, 2), "checkBox_18": (4, 2),
    "checkBox_22": (0, 3), "checkBox_24": (1, 3), "checkBox_21": (2, 3), "checkBox_25": (3, 3), "checkBox_23": (4, 3),
    "checkBox_27": (0, 4), "checkBox_29": (1, 4), "checkBox_26": (2, 4), "checkBox_30": (3, 4), "checkBox_28": (4, 4),
    "checkBox_32": (0, 5), "checkBox_34": (1, 5), "checkBox_31": (2, 5), "checkBox_35": (3, 5), "checkBox_33": (4, 5),
    "checkBox_37": (0, 6), "checkBox_39": (1, 6), "checkBox_36": (2, 6), "checkBox_40": (3, 6), "checkBox_38": (4, 6),
    "checkBox_42": (0, 7), "checkBox_44": (1, 7), "checkBox_41": (2, 7), "checkBox_45": (3, 7), "checkBox_43": (4, 7),
    "checkBox_47": (0, 8), "checkBox_49": (1, 8), "checkBox_46": (2, 8), "checkBox_50": (3, 8), "checkBox_48": (4, 8),
    "checkBox_52": (0, 9), "checkBox_54": (1, 9), "checkBox_51": (2, 9), "checkBox_55": (3, 9), "checkBox_53": (4, 9),
}

valoresPorFila = {0: 0, 1: 10, 2: 20, 3: 30, 4: 40}

class VentanaPrimitiva(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Primitiva()
        self.ui.setupUi(self)

        self.totalApuestas = 0
        self.apuestaActual = 1
        self.apuestasGuardadas = []          
        self.numerosElegidos = []   
        self.modoAutomatico = False
        self.modoManual = False

        self.prepararVariables()
        self.aplicarValidadores() 
        self.estadoInicial()
        self.conectarBotones()

    def aplicarValidadores(self):
        validador_apuestas = QIntValidator(1, 3)
        self.ui.lineEdit_2.setValidator(validador_apuestas)

  
        regex_cambiar = QRegularExpression("^[Tt]|[0-9,]+$")
        validador_cambiar = QRegularExpressionValidator(regex_cambiar)
        self.ui.lineEdit.setValidator(validador_cambiar)

    def prepararVariables(self):
        if hasattr(self.ui, 'groupBox_5'):
            self.ui.groupBox_5.hide()

        self.grupoRadios = QButtonGroup(self)
        self.grupoRadios.addButton(self.ui.radioButton)
        self.grupoRadios.addButton(self.ui.radioButton_2)
        self.grupoRadios.setExclusive(True)

        self.grupoDecenas = QButtonGroup(self)
        self.grupoDecenas.setExclusive(False) 
        
        self.grupoUnidades = QButtonGroup(self)
        self.grupoUnidades.setExclusive(False)

        self.checksDecenas = {}
        for nombre in mapaDecenas:
            caja = getattr(self.ui, nombre)
            self.checksDecenas[nombre] = caja
            self.grupoDecenas.addButton(caja)

        self.checksUnidades = {}
        for nombre in mapaUnidades:
            caja = getattr(self.ui, nombre)
            self.checksUnidades[nombre] = caja
            self.grupoUnidades.addButton(caja)

        self.unidadesDeFila = {0: [], 1: [], 2: [], 3: [], 4: []}
        for nombre, (fila, _) in mapaUnidades.items():
            self.unidadesDeFila[fila].append(nombre)

        self.filaDeDecena = {
            "checkBox": 0, "checkBox_2": 1, "checkBox_3": 2, "checkBox_4": 3, "checkBox_5": 4
        }

    def estadoInicial(self):
        self.totalApuestas = 0
        self.apuestaActual = 1
        self.apuestasGuardadas = []
        self.numerosElegidos = []
        self.modoAutomatico = False
        self.modoManual = False

        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_2.setEnabled(True)
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

        self.ui.lineEdit_3.setReadOnly(True)
        self.ui.lineEdit_4.setReadOnly(True)

        self.grupoRadios.setExclusive(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.grupoRadios.setExclusive(True)
        
        self.ui.label.setVisible(False)
        self.ui.lineEdit.setVisible(False)
        self.ui.pushButton.setVisible(False)

        self.limpiarYBloquearChecks()

        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.setText("Validar")

    def limpiarYBloquearChecks(self):
        for caja in self.checksDecenas.values():
            caja.blockSignals(True)
            caja.setChecked(False)
            caja.setEnabled(False)
            caja.blockSignals(False)

        for caja in self.checksUnidades.values():
            caja.blockSignals(True)
            caja.setChecked(False)
            caja.setEnabled(False)
            caja.blockSignals(False)

    def conectarBotones(self):
        self.ui.radioButton.toggled.connect(self.clickAutomatico)
        self.ui.radioButton_2.toggled.connect(self.clickManual)
        self.ui.lineEdit_2.editingFinished.connect(self.leerTotalApuestas)

        self.grupoDecenas.buttonToggled.connect(self.cambioDecena)
        self.grupoUnidades.buttonToggled.connect(self.cambioUnidad)

        self.ui.pushButton.clicked.connect(self.clickCambiar)
        self.ui.pushButton_2.clicked.connect(self.clickValidar)
        self.ui.lineEdit.textChanged.connect(self.escribiendoCambio)

    def clickAutomatico(self, activo):
        if not activo: 
            return
        self.modoAutomatico = True
        self.modoManual = False

        self.ui.label.setVisible(True)
        self.ui.lineEdit.setVisible(True)
        self.ui.pushButton.setVisible(True)
        self.ui.lineEdit.clear()
        self.ui.pushButton.setEnabled(False)

        if self.totalApuestas > 0:
            self.prepararApuestaAutomatica()

    def clickManual(self, activo):
        if not activo: 
            return
        self.modoAutomatico = False
        self.modoManual = True

        self.ui.label.setVisible(False)
        self.ui.lineEdit.setVisible(False)
        self.ui.pushButton.setVisible(False)

        if self.totalApuestas > 0:
            self.prepararApuestaManual()

    def leerTotalApuestas(self):
        texto = self.ui.lineEdit_2.text().strip()
        if not texto: 
            return
        
        cantidad = int(texto)
            
        self.totalApuestas = cantidad
        self.apuestaActual = 1
        self.apuestasGuardadas = []
        self.numerosElegidos = []
        
        self.ui.lineEdit_2.setEnabled(False) 

        if self.modoAutomatico:
            self.prepararApuestaAutomatica()
        elif self.modoManual:
            self.prepararApuestaManual()

    def prepararApuestaManual(self):
        self.numerosElegidos = []
        self.actualizarTextosInfo()
        self.desmarcarTodo()

        for caja in self.checksDecenas.values():
            caja.setEnabled(True)

        for caja in self.checksUnidades.values():
            caja.setEnabled(False)

        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.setText("Terminar" if self.apuestaActual == self.totalApuestas else "Validar")

    def prepararApuestaAutomatica(self):
        self.numerosElegidos = []
        self.actualizarTextosInfo()
        self.desmarcarTodo()

        for caja in self.checksDecenas.values(): 
            caja.setEnabled(False)
        for caja in self.checksUnidades.values(): 
            caja.setEnabled(False)

        self.numerosElegidos = random.sample(range(1, 50), 6)
        self.pintarNumeros(self.numerosElegidos)

        self.ui.lineEdit.clear()
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        
        self.ui.pushButton_2.setText("Terminar" if self.apuestaActual == self.totalApuestas else "Validar")

    def cambioDecena(self, boton, estado):
        if not self.modoManual: 
            return
        
        nombreDecena = boton.objectName()
        if nombreDecena not in self.filaDeDecena: 
            return

        fila = self.filaDeDecena[nombreDecena]

        if estado: 
            for nomUnidad in self.unidadesDeFila[fila]:
                valorFila = valoresPorFila[fila]
                _, valorCol = mapaUnidades[nomUnidad]
                numeroFinal = valorFila + valorCol
                
                if 1 <= numeroFinal <= 49:
                    self.checksUnidades[nomUnidad].setEnabled(True)
        else:
            for nomUnidad in self.unidadesDeFila[fila]:
                cajaUnidad = self.checksUnidades[nomUnidad]
                if cajaUnidad.isChecked():
                    valorFila = valoresPorFila[fila]
                    _, valorCol = mapaUnidades[nomUnidad]
                    numeroFinal = valorFila + valorCol
                    
                    if numeroFinal in self.numerosElegidos:
                        self.numerosElegidos.remove(numeroFinal)
                        
                    cajaUnidad.blockSignals(True)
                    cajaUnidad.setChecked(False)
                    cajaUnidad.blockSignals(False)
                
                cajaUnidad.setEnabled(False)

            self.comprobarBotonValidar()

    def cambioUnidad(self, boton, estado):
        if not self.modoManual: 
            return
        
        nombreUnidad = boton.objectName()
        if nombreUnidad not in mapaUnidades: 
            return

        fila, col = mapaUnidades[nombreUnidad]
        numeroFinal = valoresPorFila[fila] + col

        if estado:
            if numeroFinal not in self.numerosElegidos:
                if len(self.numerosElegidos) >= 6:
                    boton.blockSignals(True)
                    boton.setChecked(False)
                    boton.blockSignals(False)
                    return
                self.numerosElegidos.append(numeroFinal)
        else:
            if numeroFinal in self.numerosElegidos:
                self.numerosElegidos.remove(numeroFinal)

        self.comprobarBotonValidar()

    def escribiendoCambio(self, texto):
        self.ui.pushButton.setEnabled(len(texto.strip()) > 0)

    def clickCambiar(self):
        texto = self.ui.lineEdit.text().strip()
        if not texto: 
            return

        if texto.upper() == "T":
            self.numerosElegidos = random.sample(range(1, 50), 6)
        else:
            trozos = [t.strip() for t in texto.split(",")]
            aModificar = []
            
            for t in trozos:
                if t.isdigit():
                    num = int(t)
                    if 1 <= num <= 49 and num in self.numerosElegidos:
                        aModificar.append(num)
                        
            if len(aModificar) == 0 or len(aModificar) > 4:
                QMessageBox.warning(self, "Error al cambiar", "Por favor, pon entre 1 y 4 números válidos que tengas marcados separados por comas.")
                return

            sobrantes = [n for n in self.numerosElegidos if n not in aModificar]
            disponibles = [n for n in range(1, 50) if n not in sobrantes and n not in aModificar]
            nuevos = random.sample(disponibles, len(aModificar))
            self.numerosElegidos = sobrantes + nuevos

        self.desmarcarTodo()
        self.pintarNumeros(self.numerosElegidos)
        self.ui.lineEdit.clear()
        self.ui.pushButton.setEnabled(False)

    def clickValidar(self):
        self.apuestasGuardadas.append(sorted(self.numerosElegidos))

        if self.apuestaActual == self.totalApuestas:
            self.guardarEnJson()
            self.estadoInicial()
        else:
            self.apuestaActual += 1
            self.desmarcarTodo()
            self.numerosElegidos = []

            if self.modoManual:
                self.prepararApuestaManual()
            else:
                self.prepararApuestaAutomatica()

    def pintarNumeros(self, numeros):
        for nomCaja, (fila, col) in mapaUnidades.items():
            numCalculado = valoresPorFila[fila] + col
            
            if numCalculado in numeros:
                for nomDecena, f in self.filaDeDecena.items():
                    if f == fila:
                        self.checksDecenas[nomDecena].blockSignals(True)
                        self.checksDecenas[nomDecena].setChecked(True)
                        self.checksDecenas[nomDecena].blockSignals(False)
                        break
                        
                self.checksUnidades[nomCaja].blockSignals(True)
                self.checksUnidades[nomCaja].setChecked(True)
                self.checksUnidades[nomCaja].blockSignals(False)

    def desmarcarTodo(self):
        for caja in self.checksDecenas.values():
            caja.blockSignals(True)
            caja.setChecked(False)
            caja.blockSignals(False)
            
        for caja in self.checksUnidades.values():
            caja.blockSignals(True)
            caja.setChecked(False)
            caja.blockSignals(False)

    def actualizarTextosInfo(self):
        self.ui.lineEdit_3.setText(str(self.apuestaActual))
        self.ui.lineEdit_4.setText(str(self.totalApuestas))

    def comprobarBotonValidar(self):
        if len(self.numerosElegidos) == 6:
            self.ui.pushButton_2.setEnabled(True)
        else:
            self.ui.pushButton_2.setEnabled(False)

    def guardarEnJson(self):
        datos = {"apuestas": self.apuestasGuardadas}
        with open("boleto_primitiva.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
            
        QMessageBox.information(self, "Boleto terminado", "Guardado correctamente en 'boleto_primitiva.json'.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrimitiva()
    ventana.show()
    sys.exit(app.exec())