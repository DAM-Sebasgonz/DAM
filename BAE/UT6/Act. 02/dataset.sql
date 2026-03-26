INSERT INTO Pacientes (dni_paciente, nombre, apellidos, fecha_nacimiento, genero, telefono) VALUES
('12345678A', 'Ana',      'López García',        '1985-03-12', 'F', '600111111'),
('23456789B', 'Luis',     'Martín Pérez',        '1990-07-25', 'M', '600222222'),
('34567890C', 'María',    'Sánchez Ruiz',        '1978-11-03', 'F', '600333333'),
('45678901D', 'Carlos',   'González Díaz',       '2000-01-15', 'M', '600444444'),
('56789012E', 'Elena',    'Fernández Romero',    '1995-09-30', 'F', '600555555'),
('67890123F', 'Jorge',    'Navarro Iglesias',    '1982-04-21', 'M', '600666666'),
('78901234G', 'Lucía',    'Ortega Morales',      '2002-12-02', 'F', '600777777'),
('89012345H', 'Raúl',     'Vega Castillo',       '1975-06-18', 'M', '600888888'),
('90123456J', 'Patricia', 'Cano Serrano',        '1988-10-09', 'F', '600999999'),
('01234567K', 'Sergio',   'Domínguez Herrera',   '1993-02-27', 'M', '601000000');

INSERT INTO Medicos (dni_medico, nombre, apellidos, especialidad, telefono, fecha_alta) VALUES
('11111111H', 'Javier',   'Hernández Soto',  'Medicina Familiar', '910000001', '2015-02-10'),
('22222222J', 'Laura',    'Jiménez Muñoz',   'Pediatría',         '910000002', '2018-06-01'),
('33333333K', 'Miguel',   'Karpov López',    'Cardiología',       '910000003', '2020-09-15'),
('44444444L', 'Sara',     'Llorente Rivas',  'Dermatología',      '910000004', '2019-01-20'),
('55555555M', 'Alberto',  'Martínez Roldán', 'Neurología',        '910000005', '2017-11-03'),
('66666666N', 'Natalia',  'Núñez Campos',    'Traumatología',     '910000006', '2021-04-12');

INSERT INTO Citas (dni_paciente, dni_medico, fecha_hora, motivo, estado) VALUES
-- Ana
('12345678A', '11111111H', '2026-01-10 09:00:00', 'Revisión anual',                    'Realizada'),
('12345678A', '33333333K', '2026-02-05 11:30:00', 'Dolor en el pecho',                'Realizada'),
('12345678A', '11111111H', '2026-04-15 09:15:00', 'Control de analíticas',           'Programada'),
-- Luis
('23456789B', '11111111H', '2026-03-01 10:15:00', 'Tos persistente',                  'Programada'),
('23456789B', '66666666N', '2026-03-20 17:00:00', 'Dolor de espalda',                'Programada'),
-- María
('34567890C', '22222222J', '2026-01-20 16:00:00', 'Revisión de su hijo menor',        'Cancelada'),
('34567890C', '11111111H', '2026-02-25 09:45:00', 'Hipertensión mal controlada',     'Realizada'),
-- Carlos
('45678901D', '44444444L', '2026-02-18 12:00:00', 'Manchas en la piel',              'Realizada'),
('45678901D', '44444444L', '2026-03-25 12:30:00', 'Revisión de tratamiento tópico',  'Programada'),
-- Elena
('56789012E', '33333333K', '2026-03-10 08:45:00', 'Control de hipertensión',          'Programada'),
('56789012E', '33333333K', '2026-01-12 08:30:00', 'Palpitaciones',                   'Realizada'),
-- Jorge
('67890123F', '55555555M', '2026-02-02 15:00:00', 'Migrañas frecuentes',             'Realizada'),
('67890123F', '55555555M', '2026-03-16 15:30:00', 'Revisión tratamiento migrañas',   'Programada'),
-- Lucía
('78901234G', '22222222J', '2026-02-28 10:00:00', 'Dolor abdominal',                 'Realizada'),
('78901234G', '66666666N', '2026-03-30 18:00:00', 'Lesión de rodilla (deporte)',     'Programada'),
-- Raúl
('89012345H', '33333333K', '2026-01-05 13:00:00', 'Revisión cardiológica anual',     'Realizada'),
('89012345H', '33333333K', '2026-07-05 13:00:00', 'Revisión cardiológica semestral', 'Programada'),
-- Patricia
('90123456J', '11111111H', '2026-02-08 09:30:00', 'Resfriado y malestar general',    'Realizada'),
('90123456J', '44444444L', '2026-02-22 11:00:00', 'Reacción alérgica en la piel',    'Realizada'),
('90123456J', '44444444L', '2026-03-29 11:15:00', 'Revisión alergia',                'Programada'),
-- Sergio
('01234567K', '66666666N', '2026-01-18 18:30:00', 'Esguince de tobillo',             'Realizada'),
('01234567K', '66666666N', '2026-02-01 18:30:00', 'Revisión esguince',               'Realizada'),
('01234567K', '66666666N', '2026-03-01 18:30:00', 'Alta deportiva',                  'Programada'),
-- Extra para más juego
('67890123F', '11111111H', '2026-04-01 10:00:00', 'Control de tensión',              'Programada'),
('34567890C', '33333333K', '2026-04-03 09:00:00', 'Ajuste de medicación',            'Programada'),
('56789012E', '55555555M', '2026-04-04 16:00:00', 'Cefaleas leves',                  'Programada'),
('78901234G', '55555555M', '2026-04-06 16:30:00', 'Valoración mareos',               'Programada');

INSERT INTO Diagnosticos (id_cita, descripcion, fecha) VALUES
(1,  'Paciente en buen estado general. Se recomienda mantener hábitos saludables.',          '2026-01-10'),
(2,  'Episodio de angina leve. Se solicitan pruebas complementarias.',                      '2026-02-05'),
(4,  'Cuadro de bronquitis leve. Se pauta tratamiento sintomático.',                        '2026-03-01'),
(7,  'Hipertensión arterial mal controlada. Se ajusta medicación.',                         '2026-02-25'),
(8,  'Lesiones compatibles con dermatitis atópica. Sin signos de infección.',               '2026-02-18'),
(10, 'Hipertensión bien controlada. Se mantiene tratamiento actual.',                       '2026-03-10'),
(11, 'Migraña crónica sin aura. Se inicia tratamiento preventivo.',                         '2026-02-02'),
(13, 'Dolor abdominal inespecífico. Probable origen funcional.',                            '2026-02-28'),
(15, 'Revisión cardiológica sin cambios significativos. Riesgo cardiovascular moderado.',   '2026-01-05'),
(16, 'Cuadro catarral leve. Tratamiento sintomático.',                                      '2026-02-08'),
(17, 'Urticaria aguda probablemente alérgica. Se pauta antihistamínico.',                   '2026-02-22'),
(18, 'Esguince de tobillo grado II. Se pauta reposo y fisioterapia.',                       '2026-01-18'),
(19, 'Buena evolución del esguince. Se permite carga progresiva.',                          '2026-02-01'),
(20, 'Lesión resuelta. Alta para actividad deportiva progresiva.',                          '2026-03-01');

INSERT INTO Tratamientos (id_diagnostico, descripcion, fecha_inicio, fecha_fin, observaciones) VALUES
(1,  'Revisión anual: control de tensión y análisis básicos.', 
     '2026-01-10', '2026-01-10', 'No se requiere tratamiento farmacológico.'),
(2,  'Tratamiento con nitratos de acción corta y betabloqueantes.', 
     '2026-02-05', NULL, 'Pendiente de resultados de prueba de esfuerzo.'),
(3,  'Broncodilatadores a demanda y reposo relativo.', 
     '2026-03-01', '2026-03-10', 'Acudir si empeora la disnea.'),
(4,  'Ajuste de dosis de IECA y recomendación de dieta baja en sal.', 
     '2026-02-25', NULL, 'Revisión en 3 meses.'),
(5,  'Crema hidratante diaria y corticoide tópico en brotes.', 
     '2026-02-18', NULL, 'Evitar jabones irritantes.'),
(6,  'Mantener tratamiento antihipertensivo actual.', 
     '2026-03-10', NULL, 'Control anual salvo incidencias.'),
(7,  'Profilaxis con topiramato y medicación de rescate con triptanes.', 
     '2026-02-02', NULL, 'Valorar efectos secundarios en próxima revisión.'),
(8,  'Dieta blanda y control evolutivo. Analítica si persiste el dolor.', 
     '2026-02-28', '2026-03-07', 'Acudir a urgencias si aparece fiebre alta.'),
(9,  'Continuar ejercicio moderado y control de factores de riesgo.', 
     '2026-01-05', NULL, 'Revisión en 6 meses.'),
(10, 'Antitérmicos y abundante hidratación.', 
     '2026-02-08', '2026-02-12', 'Sin complicaciones respiratorias.'),
(11, 'Antihistamínico oral y corticoide tópico.', 
     '2026-02-22', '2026-03-01', 'Evitar alérgeno sospechoso.'),
(12, 'Inmovilización, hielo local y antiinflamatorios.', 
     '2026-01-18', '2026-02-05', 'Comenzar fisioterapia a la semana.'),
(13, 'Fisioterapia y fortalecimiento musculotendinoso.', 
     '2026-02-01', '2026-02-28', 'Buena evolución clínica.'),
(14, 'Plan de retorno progresivo al deporte.', 
     '2026-03-01', '2026-03-31', 'Alta definitiva si no hay recaídas.');





