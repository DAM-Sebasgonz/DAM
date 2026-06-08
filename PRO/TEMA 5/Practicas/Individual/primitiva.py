import sys
import random
import json
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox,
    QRadioButton, QButtonGroup, QCheckBox, QLabel, QMessageBox
)


class VentanaPrimitiva(QWidget):

    # Decenas disponibles y unidades disponibles
    DECENAS  = [0, 10, 20, 30, 40]
    UNIDADES = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apuestas Primitiva")

        self.totalApuestas   = 0          
        self.apuestaActual   = 1          
        self.numerosApuesta  = []         
        self.todasApuestas   = []         

        self._crearInterfaz()
        self._estadoInicial()
        self.show()

    def _crearInterfaz(self):
        layoutPrincipal = QVBoxLayout(self)

        # ── Fila 1: tipo de apuesta + totales ───────────
        layoutFila1 = QHBoxLayout()

        grupoPrimitiva = QGroupBox("Tipo de Apuesta")
        layoutRadio    = QHBoxLayout(grupoPrimitiva)

        self.radioAutomatica = QRadioButton("Automática")
        self.radioManual     = QRadioButton("Manual")
        self.grupoRadio      = QButtonGroup(self)
        self.grupoRadio.addButton(self.radioAutomatica)
        self.grupoRadio.addButton(self.radioManual)

        layoutRadio.addWidget(self.radioAutomatica)
        layoutRadio.addWidget(self.radioManual)

        layoutFila1.addWidget(grupoPrimitiva)
        layoutFila1.addSpacing(20)

        # Total de apuestas
        self.labelTotal  = QLabel("Total de apuestas")
        self.editTotal   = QLineEdit()
        self.editTotal.setFixedWidth(60)

        # Apuesta de N
        self.labelApuestaDe   = QLabel("Apuesta de")
        self.editApuestaActual = QLineEdit()
        self.editApuestaActual.setFixedWidth(40)
        self.editApuestaActual.setEnabled(False)   # siempre deshabilitado

        layoutFila1.addWidget(self.labelTotal)
        layoutFila1.addWidget(self.editTotal)
        layoutFila1.addSpacing(20)
        layoutFila1.addWidget(self.labelApuestaDe)
        layoutFila1.addWidget(self.editApuestaActual)
        layoutFila1.addStretch()

        layoutPrincipal.addLayout(layoutFila1)

        # ── Fila 2: grid de decenas / unidades ──────────
        layoutGrid = QGridLayout()

        # Cabeceras
        layoutGrid.addWidget(QLabel("Decenas"), 0, 0)
        layoutGrid.addWidget(QLabel("Unidades"), 0, 1)

        # Checkboxes: self.chkDecenas[fila] y self.chkUnidades[fila][col]
        self.chkDecenas  = []
        self.chkUnidades = []   # lista de listas

        for fila, decena in enumerate(self.DECENAS):
            # Checkbox de decena
            chkDec = QCheckBox(str(decena))
            self.chkDecenas.append(chkDec)
            layoutGrid.addWidget(chkDec, fila + 1, 0)

            # Checkboxes de unidades para esta fila
            filUnidades = []
            for col, unidad in enumerate(self.UNIDADES):
                chkUni = QCheckBox(str(unidad))
                filUnidades.append(chkUni)
                layoutGrid.addWidget(chkUni, fila + 1, col + 1)
            self.chkUnidades.append(filUnidades)

        layoutPrincipal.addLayout(layoutGrid)

        # ── Fila 3: Cambiar (sólo modo automático) ──────
        self.layoutCambiar = QHBoxLayout()

        self.labelACambiar = QLabel("A cambiar")
        self.editACambiar  = QLineEdit()
        self.editACambiar.setFixedWidth(120)
        self.botonCambiar  = QPushButton("Cambiar")
        self.botonCambiar.setEnabled(False)

        self.layoutCambiar.addWidget(self.labelACambiar)
        self.layoutCambiar.addWidget(self.editACambiar)
        self.layoutCambiar.addSpacing(20)
        self.layoutCambiar.addWidget(self.botonCambiar)
        self.layoutCambiar.addStretch()

        # Widget contenedor para ocultar/mostrar la fila completa
        self.widgetCambiar = QWidget()
        self.widgetCambiar.setLayout(self.layoutCambiar)
        layoutPrincipal.addWidget(self.widgetCambiar)

        # ── Fila 4: Validar ─────────────────────────────
        layoutFila4 = QHBoxLayout()
        layoutFila4.addStretch()
        self.botonValidar = QPushButton("Validar")
        self.botonValidar.setEnabled(False)
        layoutFila4.addWidget(self.botonValidar)
        layoutPrincipal.addLayout(layoutFila4)

        # ── Conexiones de señales ───────────────────────
        self.radioAutomatica.toggled.connect(self._alCambiarTipoApuesta)
        self.radioManual.toggled.connect(self._alCambiarTipoApuesta)
        self.editTotal.textChanged.connect(self._alCambiarTotal)
        self.botonValidar.clicked.connect(self._alValidar)
        self.botonCambiar.clicked.connect(self._alCambiar)
        self.editACambiar.textChanged.connect(self._alCambiarTextoACambiar)

        # Conexiones de checkboxes de decenas
        for fila, chkDec in enumerate(self.chkDecenas):
            # Usamos lambda con argumento por defecto para capturar 'fila'
            chkDec.stateChanged.connect(
                lambda estado, f=fila: self._alCambiarDecena(estado, f)
            )

        # Conexiones de checkboxes de unidades
        for fila in range(len(self.DECENAS)):
            for col in range(len(self.UNIDADES)):
                self.chkUnidades[fila][col].stateChanged.connect(
                    self._alCambiarUnidad
                )

    # ════════════════════════════════════════════════════
    #  ESTADO INICIAL
    # ════════════════════════════════════════════════════
    def _estadoInicial(self):
        """Deja la ventana como debe verse al arrancar (o después de terminar)."""
        # Desmarcar radios
        self.grupoRadio.setExclusive(False)
        self.radioAutomatica.setChecked(False)
        self.radioManual.setChecked(False)
        self.grupoRadio.setExclusive(True)

        # Campos de totales vacíos y habilitados
        self.editTotal.setEnabled(True)
        self.editTotal.clear()
        self.editApuestaActual.clear()

        # Ocultar controles de cambio
        self.widgetCambiar.setVisible(False)

        # Botón validar
        self.botonValidar.setText("Validar")
        self.botonValidar.setEnabled(False)

        # Deshabilitar y desmarcar todo el grid
        self._deshabilitarGrid()
        self._desmarcarGrid()

        # Resetear estado interno
        self.totalApuestas  = 0
        self.apuestaActual  = 1
        self.numerosApuesta = []
        self.todasApuestas  = []

    # ════════════════════════════════════════════════════
    #  HELPERS DEL GRID
    # ════════════════════════════════════════════════════
    def _deshabilitarGrid(self):
        """Deshabilita todos los checkboxes de decenas y unidades."""
        for fila in range(len(self.DECENAS)):
            self.chkDecenas[fila].setEnabled(False)
            for col in range(len(self.UNIDADES)):
                self.chkUnidades[fila][col].setEnabled(False)

    def _desmarcarGrid(self):
        """Desmarca todos los checkboxes sin disparar lógica de negocio."""
        for fila in range(len(self.DECENAS)):
            self._bloquearSeñalesFila(fila, True)
            self.chkDecenas[fila].setChecked(False)
            for col in range(len(self.UNIDADES)):
                self.chkUnidades[fila][col].setChecked(False)
            self._bloquearSeñalesFila(fila, False)

    def _bloquearSeñalesFila(self, fila, bloquear):
        """Bloquea/desbloquea señales de una fila completa."""
        self.chkDecenas[fila].blockSignals(bloquear)
        for col in range(len(self.UNIDADES)):
            self.chkUnidades[fila][col].blockSignals(bloquear)

    def _desmarcarUnidadesFila(self, fila):
        """Desmarca las unidades de una fila y actualiza numerosApuesta."""
        for col in range(len(self.UNIDADES)):
            chk = self.chkUnidades[fila][col]
            if chk.isChecked():
                # Calcular el número que representa este check
                numero = self.DECENAS[fila] + self.UNIDADES[col]
                if numero in self.numerosApuesta:
                    self.numerosApuesta.remove(numero)
                chk.blockSignals(True)
                chk.setChecked(False)
                chk.blockSignals(False)
            chk.setEnabled(False)

    def _marcarNumeros(self, numeros):
        """Marca en el grid los números de la lista (modo automático)."""
        self._desmarcarGrid()
        for numero in numeros:
            decena = (numero // 10) * 10
            unidad  = numero % 10
            fila = self.DECENAS.index(decena)
            col  = self.UNIDADES.index(unidad)
            self.chkDecenas[fila].blockSignals(True)
            self.chkDecenas[fila].setChecked(True)
            self.chkDecenas[fila].blockSignals(False)
            self.chkUnidades[fila][col].blockSignals(True)
            self.chkUnidades[fila][col].setChecked(True)
            self.chkUnidades[fila][col].blockSignals(False)

    def _numerosActualmenteJugados(self):
        """Devuelve la lista de números marcados en el grid (leyéndolos directamente)."""
        jugados = []
        for fila in range(len(self.DECENAS)):
            if not self.chkDecenas[fila].isChecked():
                continue
            for col in range(len(self.UNIDADES)):
                if self.chkUnidades[fila][col].isChecked():
                    numero = self.DECENAS[fila] + self.UNIDADES[col]
                    if 1 <= numero <= 49:
                        jugados.append(numero)
        return jugados

    # ════════════════════════════════════════════════════
    #  GENERACIÓN ALEATORIA
    # ════════════════════════════════════════════════════
    def _generarApuestaAleatoria(self):
        """Devuelve 6 números distintos entre 1 y 49."""
        return sorted(random.sample(range(1, 50), 6))

    def _generarApuestaAutomatica(self):
        """Genera apuesta aleatoria, la marca en el grid y la guarda."""
        self.numerosApuesta = self._generarApuestaAleatoria()
        self._marcarNumeros(self.numerosApuesta)
        self._actualizarBotonValidar()

    # ════════════════════════════════════════════════════
    #  SLOTS (manejadores de señales)
    # ════════════════════════════════════════════════════
    def _alCambiarTipoApuesta(self):
        """Se llama cuando el usuario elige Automática o Manual."""
        # Solo actuamos si ya hay un número válido de apuestas
        if self.totalApuestas <= 0:
            return
        self._iniciarPrimeraApuesta()

    def _alCambiarTotal(self, texto):
        """Se llama cuando cambia el texto del campo Total de apuestas."""
        # Desactivar todo mientras el usuario escribe
        self._deshabilitarGrid()
        self._desmarcarGrid()
        self.botonValidar.setEnabled(False)
        self.totalApuestas = 0
        self.apuestaActual = 1
        self.todasApuestas = []
        self.numerosApuesta = []
        self.editApuestaActual.clear()

        if not texto.strip().isdigit():
            return

        valor = int(texto.strip())
        if 1 <= valor <= 3:
            self.totalApuestas = valor
            # Si ya hay tipo elegido, iniciar
            if self.radioAutomatica.isChecked() or self.radioManual.isChecked():
                self._iniciarPrimeraApuesta()

    def _iniciarPrimeraApuesta(self):
        """Prepara la interfaz para comenzar a jugar la apuesta 1."""
        self.apuestaActual  = 1
        self.todasApuestas  = []
        self.numerosApuesta = []
        self._desmarcarGrid()

        # Actualizar los campos de "Apuesta de N de M"
        self.editApuestaActual.setText(
            f"{self.apuestaActual} de {self.totalApuestas}"
        )
        # El campo total queda deshabilitado una vez confirmado
        self.editTotal.setEnabled(False)

        if self.radioManual.isChecked():
            self.widgetCambiar.setVisible(False)
            # Habilitar solo los checkboxes de decenas
            for fila in range(len(self.DECENAS)):
                self.chkDecenas[fila].setEnabled(True)
                for col in range(len(self.UNIDADES)):
                    self.chkUnidades[fila][col].setEnabled(False)
            self.botonValidar.setEnabled(False)
            self._actualizarTextoBotonValidar()

        elif self.radioAutomatica.isChecked():
            self.widgetCambiar.setVisible(True)
            self.editACambiar.clear()
            self.botonCambiar.setEnabled(False)
            # Grid deshabilitado en modo automático
            self._deshabilitarGrid()
            self._generarApuestaAutomatica()
            self.botonValidar.setEnabled(True)
            self._actualizarTextoBotonValidar()

    def _alCambiarDecena(self, estado, fila):
        """Reacciona al marcar/desmarcar un checkbox de decena (solo modo manual)."""
        if self.radioManual.isChecked():
            if estado == Qt.CheckState.Checked.value or estado == 2:
                # Habilitar las unidades de esta fila
                for col in range(len(self.UNIDADES)):
                    numero = self.DECENAS[fila] + self.UNIDADES[col]
                    # Habilitar solo los que representan números 1-49
                    if 1 <= numero <= 49:
                        self.chkUnidades[fila][col].setEnabled(True)
                    else:
                        self.chkUnidades[fila][col].setEnabled(False)
            else:
                # Al desmarcar la decena, quitar sus unidades del registro
                self._desmarcarUnidadesFila(fila)
                self._actualizarBotonValidar()

    def _alCambiarUnidad(self):
        """Reacciona al marcar/desmarcar un checkbox de unidad (solo modo manual)."""
        if self.radioManual.isChecked():
            self.numerosApuesta = self._numerosActualmenteJugados()
            self._actualizarBotonValidar()

    def _actualizarBotonValidar(self):
        """Habilita el botón Validar sólo si hay exactamente 6 números."""
        if self.radioManual.isChecked():
            self.botonValidar.setEnabled(len(self.numerosApuesta) == 6)
        else:
            # En automático siempre hay 6
            self.botonValidar.setEnabled(len(self.numerosApuesta) == 6)

    def _actualizarTextoBotonValidar(self):
        """Cambia el texto del botón en la última apuesta."""
        if self.apuestaActual == self.totalApuestas:
            self.botonValidar.setText("Terminar")
        else:
            self.botonValidar.setText("Validar")

    def _alValidar(self):
        """Guarda la apuesta actual y pasa a la siguiente (o termina)."""
        # En manual, releer del grid por si acaso
        if self.radioManual.isChecked():
            self.numerosApuesta = self._numerosActualmenteJugados()

        if len(self.numerosApuesta) != 6:
            QMessageBox.warning(self, "Error", "Debes marcar exactamente 6 números.")
            return

        # Guardar la apuesta
        self.todasApuestas.append(sorted(self.numerosApuesta))

        if self.apuestaActual < self.totalApuestas:
            # Pasar a la siguiente apuesta
            self.apuestaActual += 1
            self.numerosApuesta = []
            self.editApuestaActual.setText(
                f"{self.apuestaActual} de {self.totalApuestas}"
            )
            self._desmarcarGrid()
            self.botonValidar.setEnabled(False)
            self._actualizarTextoBotonValidar()

            if self.radioAutomatica.isChecked():
                self.editACambiar.clear()
                self.botonCambiar.setEnabled(False)
                self._generarApuestaAutomatica()
                self.botonValidar.setEnabled(True)
        else:
            # Era la última apuesta: guardar JSON y reiniciar
            self._guardarJSON()
            QMessageBox.information(
                self, "Boleto generado",
                "El boleto se ha guardado en 'boleto.json'.\n"
                "La ventana volverá al estado inicial."
            )
            self._estadoInicial()

    # ── Lógica del cambio (modo automático) ─────────────
    def _alCambiarTextoACambiar(self, texto):
        """Habilita el botón Cambiar si hay algo escrito."""
        self.botonCambiar.setEnabled(bool(texto.strip()))

    def _alCambiar(self):
        """Cambia toda la apuesta ('T') o números concretos (hasta 4)."""
        texto = self.editACambiar.text().strip()

        if texto.upper() == "T":
            # Cambiar apuesta completa
            self.numerosApuesta = self._generarApuestaAleatoria()
            self._marcarNumeros(self.numerosApuesta)
        else:
            # Cambiar hasta 4 números indicados
            partes = [p.strip() for p in texto.split(",")]
            try:
                aCambiar = [int(p) for p in partes if p]
            except ValueError:
                QMessageBox.warning(
                    self, "Error",
                    "Escribe números separados por ',' o 'T' para cambiar todo."
                )
                return

            if not aCambiar:
                return

            if len(aCambiar) > 4:
                QMessageBox.warning(
                    self, "Error",
                    "Solo puedes cambiar un máximo de 4 números."
                )
                return

            # Verificar que los números a cambiar están en la apuesta actual
            for n in aCambiar:
                if n not in self.numerosApuesta:
                    QMessageBox.warning(
                        self, "Error",
                        f"El número {n} no está en la apuesta actual."
                    )
                    return

            # Quitar los números a cambiar
            quedanFijos = [n for n in self.numerosApuesta if n not in aCambiar]

            # Generar nuevos números que no coincidan con los fijos ni con los que se van
            excluidos = set(quedanFijos) | set(aCambiar)
            posibles  = [n for n in range(1, 50) if n not in excluidos]

            if len(posibles) < len(aCambiar):
                QMessageBox.warning(self, "Error", "No hay suficientes números disponibles.")
                return

            nuevos = random.sample(posibles, len(aCambiar))
            self.numerosApuesta = sorted(quedanFijos + nuevos)
            self._marcarNumeros(self.numerosApuesta)

        # Limpiar el campo y deshabilitar el botón
        self.editACambiar.clear()
        self.botonCambiar.setEnabled(False)
        self._actualizarBotonValidar()

    # ════════════════════════════════════════════════════
    #  GUARDAR JSON
    # ════════════════════════════════════════════════════
    def _guardarJSON(self):
        """Guarda el boleto completo en boleto.json."""
        boleto = {
            "tipo":     "Automática" if self.radioAutomatica.isChecked() else "Manual",
            "apuestas": self.todasApuestas
        }
        with open("boleto.json", "w", encoding="utf-8") as f:
            json.dump(boleto, f, ensure_ascii=False, indent=4)


# ──────────────────────────────────────────────
#  Punto de entrada
# ──────────────────────────────────────────────
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrimitiva()
    ventana.show()
    sys.exit(app.exec())