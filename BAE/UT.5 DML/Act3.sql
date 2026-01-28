
select id, codigo, tipo
from pistas P
JOIN pistas_abiertas PA
ON P.id = PA.id_pista
where tipo = "tenis" and operativa = 1;

select 