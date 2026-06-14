from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout,
    QFormLayout, QLineEdit, QPushButton, QComboBox, QTableWidget,
    QTableWidgetItem, QGroupBox, QLabel, QDateEdit, QTimeEdit,
    QSpinBox, QHeaderView, QCheckBox, QSizePolicy
)
from PyQt6.QtCore import QDate, QTime


class VentanaReservas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Reservas Aéreas")
        self.resize(960, 640)

        self.centralwidget = QWidget(self)
        self.layout_principal = QVBoxLayout(self.centralwidget)
        self.layout_principal.setContentsMargins(8, 8, 8, 8)

        self.tabs = QTabWidget(self.centralwidget)
        self.layout_principal.addWidget(self.tabs)

        self.setCentralWidget(self.centralwidget)
        self._construir_tabs()


    def _construir_tabs(self):
        self.tabs.addTab(self._pestana_personas(),  "👤 Personas")
        self.tabs.addTab(self._pestana_vuelos(),    "✈  Vuelos y Aerolíneas")
        self.tabs.addTab(self._pestana_reservas(),  "📋 Reservas")
        self.tabs.addTab(self._pestana_consultas(), "🔍 Consultas")


    def _pestana_personas(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(10)

        grupo_form = QGroupBox("Datos del cliente")
        form_vbox = QVBoxLayout()
        form_layout = QFormLayout()

        self.txt_per_nif    = QLineEdit()
        self.txt_per_nombre = QLineEdit()
        self.cmb_per_sexo   = QComboBox()
        self.cmb_per_sexo.addItems(["Seleccione sexo", "M", "F", "Otro"])
        self.txt_per_edad   = QSpinBox()
        self.txt_per_edad.setRange(0, 120)

        form_layout.addRow("NIF:",            self.txt_per_nif)
        form_layout.addRow("Nombre:",         self.txt_per_nombre)
        form_layout.addRow("Sexo:",           self.cmb_per_sexo)
        form_layout.addRow("Edad:",           self.txt_per_edad)
        form_vbox.addLayout(form_layout)
        form_vbox.addStretch()

        self.btn_per_insertar  = QPushButton("Insertar")
        self.btn_per_modificar = QPushButton("Modificar")
        self.btn_per_borrar    = QPushButton("Borrar")
        self.btn_per_listar    = QPushButton("Actualizar lista")

        for btn in (self.btn_per_insertar, self.btn_per_modificar,
                    self.btn_per_borrar, self.btn_per_listar):
            form_vbox.addWidget(btn)

        grupo_form.setLayout(form_vbox)

        self.tabla_personas = QTableWidget()
        self.tabla_personas.setColumnCount(4)
        self.tabla_personas.setHorizontalHeaderLabels(["NIF", "Nombre", "Sexo", "Edad"])
        self.tabla_personas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_personas.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_personas.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        layout.addWidget(grupo_form, 1)
        layout.addWidget(self.tabla_personas, 2)
        return widget



    def _pestana_vuelos(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(8)

        grupo_aero = QGroupBox("Registrar aerolínea")
        aero_row = QHBoxLayout()

        self.txt_ae_cod  = QLineEdit(); self.txt_ae_cod.setPlaceholderText("Cód. ID")
        self.txt_ae_nom  = QLineEdit(); self.txt_ae_nom.setPlaceholderText("Nombre")
        self.txt_ae_pais = QLineEdit(); self.txt_ae_pais.setPlaceholderText("País")
        self.btn_ae_ins  = QPushButton("Registrar compañía")

        for lbl, w in (("Código:", self.txt_ae_cod), ("Nombre:", self.txt_ae_nom),
                        ("País:", self.txt_ae_pais)):
            aero_row.addWidget(QLabel(lbl))
            aero_row.addWidget(w)
        aero_row.addWidget(self.btn_ae_ins)
        grupo_aero.setLayout(aero_row)
        layout.addWidget(grupo_aero)

        vuelo_h = QHBoxLayout()

        grupo_vuelo   = QGroupBox("Datos del vuelo")
        form_vu_vbox  = QVBoxLayout()
        form_vuelo    = QFormLayout()

        self.txt_vu_id     = QLineEdit()
        self.txt_vu_dest   = QLineEdit()
        self.txt_vu_plazas = QSpinBox()
        self.txt_vu_plazas.setRange(1, 1000)
        self.txt_vu_fecha  = QDateEdit()
        self.txt_vu_fecha.setCalendarPopup(True)
        self.txt_vu_fecha.setDate(QDate.currentDate())
        self.txt_vu_hora   = QTimeEdit() 
        self.txt_vu_hora.setTime(QTime(12, 0))
        self.txt_vu_aero   = QLineEdit()

        form_vuelo.addRow("ID Vuelo:",       self.txt_vu_id)
        form_vuelo.addRow("Destino:",        self.txt_vu_dest)
        form_vuelo.addRow("Plazas:",         self.txt_vu_plazas)
        form_vuelo.addRow("Fecha salida:",   self.txt_vu_fecha)
        form_vuelo.addRow("Hora salida:",    self.txt_vu_hora)
        form_vuelo.addRow("Cód. aerolínea:", self.txt_vu_aero)
        form_vu_vbox.addLayout(form_vuelo)
        form_vu_vbox.addStretch()

        self.btn_vu_insertar  = QPushButton("Insertar vuelo")
        self.btn_vu_modificar = QPushButton("Modificar vuelo")
        self.btn_vu_borrar    = QPushButton("Borrar vuelo")
        self.btn_vu_listar    = QPushButton("Actualizar vuelos")

        for btn in (self.btn_vu_insertar, self.btn_vu_modificar,
                    self.btn_vu_borrar, self.btn_vu_listar):
            form_vu_vbox.addWidget(btn)

        grupo_vuelo.setLayout(form_vu_vbox)

        self.tabla_vuelos = QTableWidget()
        self.tabla_vuelos.setColumnCount(6)
        self.tabla_vuelos.setHorizontalHeaderLabels(
            ["ID", "Destino", "Plazas", "Fecha", "Hora", "Compañía"])
        self.tabla_vuelos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_vuelos.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_vuelos.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        vuelo_h.addWidget(grupo_vuelo, 1)
        vuelo_h.addWidget(self.tabla_vuelos, 2)
        layout.addLayout(vuelo_h)
        return widget


    def _pestana_reservas(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(10)

        grupo_res = QGroupBox("Datos de la reserva")
        form_vbox = QVBoxLayout()
        form_res  = QFormLayout()

        self.txt_res_nif   = QLineEdit()
        self.txt_res_vuelo = QLineEdit()
        self.txt_res_fres  = QDateEdit()
        self.txt_res_fres.setCalendarPopup(True)
        self.txt_res_fres.setDate(QDate.currentDate())

        self.chk_pagado    = QCheckBox("Marcar si está pagado")
        self.txt_res_fpago = QDateEdit()
        self.txt_res_fpago.setCalendarPopup(True)
        self.txt_res_fpago.setDate(QDate.currentDate())
        self.txt_res_fpago.setEnabled(False)
        self.chk_pagado.toggled.connect(self.txt_res_fpago.setEnabled)

        self.cmb_res_est = QComboBox()
        self.cmb_res_est.addItems(['reservado', 'pagado', 'utilizado', 'no_usado'])

        form_res.addRow("NIF cliente:",    self.txt_res_nif)
        form_res.addRow("ID vuelo:",       self.txt_res_vuelo)
        form_res.addRow("Fecha reserva:",  self.txt_res_fres)
        form_res.addRow("",                self.chk_pagado)
        form_res.addRow("Fecha pago:",     self.txt_res_fpago)
        form_res.addRow("Estado:",         self.cmb_res_est)
        form_vbox.addLayout(form_res)
        form_vbox.addStretch()

        self.btn_res_insertar  = QPushButton("Crear reserva")
        self.btn_res_modificar = QPushButton("Modificar estado")
        self.btn_res_borrar    = QPushButton("Anular reserva")
        self.btn_res_listar    = QPushButton("Listar reservas")

        for btn in (self.btn_res_insertar, self.btn_res_modificar,
                    self.btn_res_borrar, self.btn_res_listar):
            form_vbox.addWidget(btn)

        grupo_res.setLayout(form_vbox)

        self.tabla_reservas = QTableWidget()
        self.tabla_reservas.setColumnCount(5)
        self.tabla_reservas.setHorizontalHeaderLabels(
            ["NIF", "Vuelo", "F. Reserva", "F. Pago", "Estado"])
        self.tabla_reservas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_reservas.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_reservas.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        layout.addWidget(grupo_res, 1)
        layout.addWidget(self.tabla_reservas, 2)
        return widget


    def _pestana_consultas(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setSpacing(10)

        panel_izq = QWidget()
        panel_izq.setFixedWidth(220)
        izq_layout = QVBoxLayout(panel_izq)
        izq_layout.setSpacing(8)

        grupo1 = QGroupBox("Pasajeros por vuelo")
        g1_lay = QVBoxLayout()
        g1_lay.addWidget(QLabel("Lista los pasajeros\nque tienen reserva\nen un vuelo concreto."))
        self.btn_inf_pasajeros = QPushButton("Consultar")
        g1_lay.addWidget(self.btn_inf_pasajeros)
        grupo1.setLayout(g1_lay)

        grupo2 = QGroupBox("Historial de viajes")
        g2_lay = QVBoxLayout()
        g2_lay.addWidget(QLabel("Número total de\nreservas realizadas\npor una persona."))
        self.btn_inf_historial = QPushButton("Consultar")
        g2_lay.addWidget(self.btn_inf_historial)
        grupo2.setLayout(g2_lay)

        grupo3 = QGroupBox("Aerolínea líder")
        g3_lay = QVBoxLayout()
        g3_lay.addWidget(QLabel("Compañía con mayor\nnúmero de pasajeros\núnicos en total."))
        self.btn_inf_lider = QPushButton("Consultar")
        g3_lay.addWidget(self.btn_inf_lider)
        grupo3.setLayout(g3_lay)

        izq_layout.addWidget(grupo1)
        izq_layout.addWidget(grupo2)
        izq_layout.addWidget(grupo3)
        izq_layout.addStretch()

        # Panel derecho: tabla de resultados
        panel_der = QGroupBox("Resultados")
        der_layout = QVBoxLayout(panel_der)

        self.lbl_consulta_activa = QLabel("Seleccione una consulta del panel izquierdo.")
        self.tabla_reportes = QTableWidget()
        self.tabla_reportes.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        self.tabla_reportes.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla_reportes.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabla_reportes.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        der_layout.addWidget(self.lbl_consulta_activa)
        der_layout.addWidget(self.tabla_reportes)

        layout.addWidget(panel_izq)
        layout.addWidget(panel_der, 1)
        return widget
