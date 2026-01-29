select id, codigo, tipo
from pistas P
JOIN pistas_abiertas PA
ON P.id = PA.id_pista
where tipo = "tenis" and operativa = 1;

select codigo, tipo, ciudad
from pistas P 
JOIN polideportivos PL
ON PL.id = P.id_polideportivo
where ciudad = "zaragoza";

SELECT
    tipo,
    AVG(precio) AS precio_medio
FROM pistas P
JOIN pistas_abiertas PA
    ON P.id = PA.id_pista
WHERE PA.operativa = 0
GROUP BY tipo;

SELECT
    nombre,
    COUNT(pi.id) AS cantidad_pistas
FROM polideportivos po
JOIN pistas pi
    ON po.id = pi.id_polideportivo
GROUP BY nombre;

-- Nº de reservas que ha hecho cada usuario. Ordena la salida por el campo apellido.

SELECT
    u.nombre,
    u.apellidos,
    COUNT(ur.id_reserva) AS numero_reservas
FROM usuarios u
LEFT JOIN usuario_reserva ur
    ON u.id = ur.id_usuario
GROUP BY u.id, u.nombre, u.apellidos
ORDER BY u.apellidos;









