
-- 1.- Obtener  el código y el tipo de las pistas de tenis que están operativas. 

select id, codigo, tipo
from pistas P
JOIN pistas_abiertas PA
ON P.id = PA.id_pista
where tipo = "tenis" and operativa = 1;

-- 2.- Obtener el código y el tipo de las pistas de los polideportivos de Zaragoza. 

select codigo, tipo, ciudad
from pistas P 
JOIN polideportivos PL
ON PL.id = P.id_polideportivo
where ciudad = "zaragoza";

-- 3.- Precio medio, por tipo de pista, de las pistas que no están operativas.

SELECT
    tipo,
    AVG(precio) AS precio_medio
FROM pistas P
JOIN pistas_abiertas PA
    ON P.id = PA.id_pista
WHERE PA.operativa = 0
GROUP BY tipo;

-- 4.- Cantidad de pistas que hay en cada polideportivo.

SELECT
    nombre,
    COUNT(pi.id) AS cantidad_pistas
FROM polideportivos po
JOIN pistas pi
    ON po.id = pi.id_polideportivo
GROUP BY nombre;

-- 5.- Nº de reservas que ha hecho cada usuario. Ordena la salida por el campo apellido. 

SELECT
    u.nombre,
    u.apellidos,
    COUNT(ur.id_reserva) AS numero_reservas
FROM usuarios u
LEFT JOIN usuario_reserva ur
    ON u.id = ur.id_usuario
GROUP BY u.id, u.nombre, u.apellidos
ORDER BY u.apellidos;

-- 6.- Número de pistas que hay de cada tipo en el polideportivo 'ACTUR 1'. 

SELECT
    tipo,
    COUNT(p.id) AS numero_pistas
FROM polideportivos po
JOIN pistas p
    ON po.id = p.id_polideportivo
WHERE po.nombre = 'ACTUR 1'
GROUP BY tipo;

-- 7.- Mostrar, para cada polideportivo, el código y tipo de las pistas que tiene. 

SELECT
    nombre AS polideportivo,
    p.id AS codigo_pista,
    p.tipo
FROM polideportivos po
JOIN pistas p
    ON po.id = p.id_polideportivo
ORDER BY nombre, p.id;

-- 8.- Mostrar, para cada pista, el código de reserva que ha tenido. Si nunca se ha reservado, se 
-- mostrarán  sólo  sus  datos.  (Puede  ocurrir  que  una  pista  no  esté  relacionada  con  ninguna 
-- reserva). 

SELECT
    codigo AS codigo_pista,
    r.id AS codigo_reserva
FROM pistas p
LEFT JOIN reservas r
    ON p.id = r.id_pista
ORDER BY p.codigo;

-- 9.- Mostrar cuántas veces se ha reservado cada pista.

SELECT
    p.codigo AS codigo_pista,
    COUNT(r.id) AS veces_reservada
FROM pistas p
LEFT JOIN reservas r
    ON p.id = r.id_pista
GROUP BY p.id, p.codigo
ORDER BY p.codigo;

-- 10.- Mostrar cuántas reservas ha hecho cada usuario. Puede ocurrir que exista algún usuario 
-- que no haya hecho reservas.

SELECT
    usuarios.id AS id_usuario,
    usuarios.nombre,
    usuarios.apellidos,
    COUNT(usuario_reserva.id_reserva) AS numero_reservas
FROM usuarios
LEFT JOIN usuario_reserva
    ON usuarios.id = usuario_reserva.id_usuario
GROUP BY
    usuarios.id,
    usuarios.nombre,
    usuarios.apellidos;








