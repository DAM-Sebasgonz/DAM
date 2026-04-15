-- =========================================================
-- BASE DE DATOS: VIDEOJUEGO COMPETITIVO ONLINE
-- Modelo para MySQL 8+
-- =========================================================

DROP DATABASE IF EXISTS videojuego_online;
CREATE DATABASE videojuego_online
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_spanish_ci;

USE videojuego_online;

CREATE TABLE jugadores (
    id_jugador INT PRIMARY KEY AUTO_INCREMENT,
    nick VARCHAR(30) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    fecha_registro DATE NOT NULL,
    pais VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE,
    nivel_cuenta INT NOT NULL DEFAULT 1 CHECK (nivel_cuenta >= 1),
    experiencia BIGINT NOT NULL DEFAULT 0 CHECK (experiencia >= 0)
);

CREATE TABLE clanes (
    id_clan INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    fecha_creacion DATE NOT NULL,
    region VARCHAR(30) NOT NULL,
    puntos_clan INT NOT NULL DEFAULT 0 CHECK (puntos_clan >= 0)
);

CREATE TABLE personajes (
    id_personaje INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL UNIQUE,
    clase VARCHAR(30) NOT NULL,
    raza VARCHAR(30) NOT NULL,
    nivel INT NOT NULL DEFAULT 1 CHECK (nivel >= 1),
    oro INT NOT NULL DEFAULT 0 CHECK (oro >= 0),
    id_jugador INT NOT NULL,
    id_clan INT NULL,
    CONSTRAINT fk_personajes_jugadores
        FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_personajes_clanes
        FOREIGN KEY (id_clan) REFERENCES clanes(id_clan)
        ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE torneos (
    id_torneo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(80) NOT NULL,
    temporada VARCHAR(20) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NULL,
    premio_total DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (premio_total >= 0),
    UNIQUE (nombre, temporada)
);

CREATE TABLE partidas (
    id_partida INT PRIMARY KEY AUTO_INCREMENT,
    fecha_hora DATETIME NOT NULL,
    duracion_minutos INT NOT NULL CHECK (duracion_minutos > 0),
    modo VARCHAR(30) NOT NULL,
    mapa VARCHAR(50) NOT NULL,
    id_torneo INT NULL,
    CONSTRAINT fk_partidas_torneos
        FOREIGN KEY (id_torneo) REFERENCES torneos(id_torneo)
        ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE participaciones (
    id_partida INT NOT NULL,
    id_personaje INT NOT NULL,
    equipo VARCHAR(20) NOT NULL,
    resultado VARCHAR(10) NOT NULL,
    puntos INT NOT NULL DEFAULT 0 CHECK (puntos >= 0),
    bajas INT NOT NULL DEFAULT 0 CHECK (bajas >= 0),
    asistencias INT NOT NULL DEFAULT 0 CHECK (asistencias >= 0),
    muertes INT NOT NULL DEFAULT 0 CHECK (muertes >= 0),
    PRIMARY KEY (id_partida, id_personaje),
    CONSTRAINT chk_resultado CHECK (resultado IN ('win', 'lose')),
    CONSTRAINT fk_participaciones_partidas
        FOREIGN KEY (id_partida) REFERENCES partidas(id_partida)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_participaciones_personajes
        FOREIGN KEY (id_personaje) REFERENCES personajes(id_personaje)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE objetos (
    id_objeto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    tipo VARCHAR(30) NOT NULL,
    rareza VARCHAR(20) NOT NULL,
    valor_oro INT NOT NULL CHECK (valor_oro >= 0)
);

CREATE TABLE inventario (
    id_personaje INT NOT NULL,
    id_objeto INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1 CHECK (cantidad >= 1),
    PRIMARY KEY (id_personaje, id_objeto),
    CONSTRAINT fk_inventario_personajes
        FOREIGN KEY (id_personaje) REFERENCES personajes(id_personaje)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_inventario_objetos
        FOREIGN KEY (id_objeto) REFERENCES objetos(id_objeto)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

-- =========================================================
-- DATOS DE PRUEBA
-- =========================================================

INSERT INTO jugadores (nick, email, fecha_registro, pais, fecha_nacimiento, nivel_cuenta, experiencia) VALUES
('ShadowFox',   'shadowfox@game.es',   '2024-01-10', 'España',    '2004-03-15', 48, 152000),
('LunaByte',    'lunabyte@game.es',    '2024-02-18', 'España',    '2005-07-21', 35,  98000),
('KrakenX',     'krakenx@game.es',     '2023-11-02', 'México',    '2002-11-09', 61, 241500),
('NovaStrike',  'novastrike@game.es',  '2024-03-01', 'Argentina', '2003-01-30', 29,  73400),
('PixelQueen',  'pixelqueen@game.es',  '2023-09-12', 'España',    '2001-12-05', 72, 310200),
('IronHawk',    'ironhawk@game.es',    '2024-04-22', 'Chile',     '2000-06-17', 26,  65000),
('ZeroLag',     'zerolag@game.es',     '2024-05-03', 'Colombia',  '2006-10-11', 19,  30100),
('DrakoN',      'drakon@game.es',      '2023-12-14', 'Perú',      '2002-08-22', 55, 205000);

INSERT INTO clanes (nombre, fecha_creacion, region, puntos_clan) VALUES
('Nebula Core',  '2023-06-01', 'EU',   1850),
('Crimson V',    '2023-08-20', 'LATAM',1620),
('Titan Forge',  '2024-01-15', 'EU',   1210),
('Solaris IX',   '2024-03-05', 'NA',    910);

INSERT INTO personajes (nombre, clase, raza, nivel, oro, id_jugador, id_clan) VALUES
('Astra',      'Maga',      'Humana',   44, 2100, 1, 1),
('Rexor',      'Guerrero',  'Orco',     38, 1700, 1, 3),
('Lyra',       'Arquera',   'Elfa',     33, 1400, 2, 1),
('Volt',       'Asesino',   'Humano',   41, 2500, 3, 2),
('Kora',       'Tanque',    'Enana',    36, 1900, 4, 2),
('Nyx',        'Hechicera', 'Elfa',     52, 3200, 5, 1),
('Brutus',     'Guerrero',  'Orco',     28,  900, 6, NULL),
('Echo',       'Soporte',   'Humana',   24, 1100, 7, 4),
('Sable',      'Asesino',   'Humano',   47, 2800, 8, 3),
('Helia',      'Paladina',  'Humana',   31, 1600, 2, NULL),
('Mantis',     'Arquero',   'Elfo oscuro', 27, 1200, 3, 2),
('Titan',      'Tanque',    'Cyborg',   55, 3500, 5, 4);

INSERT INTO torneos (nombre, temporada, fecha_inicio, fecha_fin, premio_total) VALUES
('Arena Masters',  '2025-S1', '2025-02-01', '2025-03-01', 5000.00),
('Arena Masters',  '2025-S2', '2025-09-01', '2025-10-01', 6500.00),
('Legends Cup',    '2025',    '2025-05-10', '2025-06-20', 8200.00),
('Winter Clash',   '2024',    '2024-12-01', '2024-12-20', 3000.00);

INSERT INTO partidas (fecha_hora, duracion_minutos, modo, mapa, id_torneo) VALUES
('2025-02-05 18:00:00', 32, 'ranked',      'Citadel', 1),
('2025-02-05 19:00:00', 28, 'ranked',      'Ruins',   1),
('2025-02-10 17:30:00', 35, 'competitivo', 'Citadel', 1),
('2025-03-12 20:15:00', 22, 'casual',      'Forest',  NULL),
('2025-05-15 18:45:00', 41, 'competitivo', 'Temple',  3),
('2025-05-16 19:10:00', 39, 'competitivo', 'Temple',  3),
('2025-05-20 21:00:00', 27, 'ranked',      'Ruins',   NULL),
('2025-09-03 18:20:00', 30, 'ranked',      'Citadel', 2),
('2025-09-04 18:20:00', 34, 'ranked',      'Ruins',   2),
('2025-09-05 18:20:00', 29, 'ranked',      'Citadel', 2),
('2025-12-05 17:00:00', 25, 'casual',      'Forest',  NULL),
('2025-12-10 17:40:00', 37, 'competitivo', 'Temple',  NULL);

INSERT INTO participaciones (id_partida, id_personaje, equipo, resultado, puntos, bajas, asistencias, muertes) VALUES
(1,  1, 'Alpha', 'win',  1450, 12,  8, 3),
(1,  3, 'Alpha', 'win',  1320, 10, 11, 4),
(1,  4, 'Beta',  'lose', 1180,  9,  5, 7),
(1,  5, 'Beta',  'lose',  980,  4,  7, 9),

(2,  6, 'Alpha', 'win',  1600, 15, 12, 2),
(2,  9, 'Alpha', 'win',  1490, 13,  9, 3),
(2,  2, 'Beta',  'lose', 1110,  7,  6, 8),
(2, 10, 'Beta',  'lose',  930,  3, 10, 9),

(3,  1, 'Alpha', 'lose', 1210,  8,  6, 7),
(3,  4, 'Alpha', 'lose', 1290, 11,  4, 8),
(3, 12, 'Beta',  'win',  1710, 16,  7, 2),
(3,  8, 'Beta',  'win',  1240,  5, 14, 4),

(4,  7, 'Alpha', 'win',   840,  4,  5, 5),
(4, 10, 'Alpha', 'win',   910,  3, 12, 4),
(4, 11, 'Beta',  'lose',  760,  5,  2, 8),
(4,  3, 'Beta',  'lose',  880,  6,  4, 7),

(5,  6, 'Alpha', 'win',  1680, 14, 11, 3),
(5, 12, 'Alpha', 'win',  1760, 17,  8, 2),
(5,  4, 'Beta',  'lose', 1340,  9,  7, 8),
(5,  5, 'Beta',  'lose', 1010,  4,  9, 10),

(6,  1, 'Alpha', 'win',  1520, 13, 10, 4),
(6,  9, 'Alpha', 'win',  1470, 12,  8, 5),
(6,  8, 'Beta',  'lose', 1190,  7,  9, 9),
(6, 11, 'Beta',  'lose',  970,  5,  6, 11),

(7,  2, 'Alpha', 'lose', 1040,  6,  5, 8),
(7,  7, 'Alpha', 'lose',  920,  3,  7, 9),
(7,  3, 'Beta',  'win',  1260, 10,  9, 4),
(7, 10, 'Beta',  'win',  1100,  8, 11, 5),

(8,  4, 'Alpha', 'win',  1550, 14,  6, 4),
(8,  5, 'Alpha', 'win',  1200,  6, 10, 5),
(8,  6, 'Beta',  'lose', 1410, 11,  8, 7),
(8, 12, 'Beta',  'lose', 1500, 13,  5, 6),

(9,  1, 'Alpha', 'lose', 1330,  9,  7, 8),
(9,  8, 'Alpha', 'lose', 1080,  4, 13, 9),
(9,  9, 'Beta',  'win',  1580, 15,  9, 3),
(9, 11, 'Beta',  'win',  1180,  8, 10, 5),

(10, 2, 'Alpha', 'win',  1250,  9,  8, 5),
(10,12, 'Alpha', 'win',  1690, 16,  6, 3),
(10, 3, 'Beta',  'lose', 1120,  7,  9, 7),
(10, 7, 'Beta',  'lose',  860,  3,  4, 10),

(11, 5, 'Alpha', 'win',   990,  5, 11, 4),
(11,10, 'Alpha', 'win',   950,  4, 10, 5),
(11, 6, 'Beta',  'lose',  920,  6,  5, 7),
(11,11, 'Beta',  'lose',  810,  4,  4, 8),

(12, 1, 'Alpha', 'win',  1490, 11, 12, 3),
(12, 4, 'Alpha', 'win',  1420, 12,  7, 4),
(12, 8, 'Beta',  'lose', 1110,  5,  9, 8),
(12, 9, 'Beta',  'lose', 1300, 10,  6, 7);

INSERT INTO objetos (nombre, tipo, rareza, valor_oro) VALUES
('Espada Ígnea',      'Arma',      'Épico',      900),
('Arco de Niebla',    'Arma',      'Raro',       650),
('Báculo Astral',     'Arma',      'Legendario', 1300),
('Escudo Titanio',    'Armadura',  'Épico',      850),
('Capa Sombría',      'Armadura',  'Raro',       500),
('Poción Mayor',      'Consumible','Común',       90),
('Anillo Solar',      'Accesorio', 'Épico',      780),
('Botas del Vacío',   'Armadura',  'Raro',       540),
('Daga de Plasma',    'Arma',      'Épico',      870),
('Amuleto Vital',     'Accesorio', 'Raro',       430);

INSERT INTO inventario (id_personaje, id_objeto, cantidad) VALUES
(1, 3, 1), (1, 7, 1), (1, 6, 5),
(2, 1, 1), (2, 4, 1), (2, 6, 2),
(3, 2, 1), (3, 5, 1), (3, 6, 4),
(4, 9, 1), (4, 5, 1), (4, 6, 3),
(5, 4, 1), (5,10, 1), (5, 6, 4),
(6, 3, 1), (6, 7, 1), (6,10, 2),
(7, 1, 1), (7, 8, 1),
(8,10, 1), (8, 6, 6),
(9, 9, 1), (9, 7, 1), (9, 6, 2),
(10,4, 1), (10,6, 3),
(11,2, 1), (11,8, 1), (11,6, 1),
(12,4, 1), (12,7, 1), (12,10,1);
