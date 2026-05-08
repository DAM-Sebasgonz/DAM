(: 4 :)

declare option output:method "xml";
declare option output:indent "yes";

for $autor in collection("C:\DAM\LND\Tema 6 BaseX\Base de datos Examen\autores")//autor
where data($autor/datos_biograficos/nacimiento/lugar) = "París"
return <nacimiento_paris><nombre>{upper-case(data($autor/nombre))}</nombre><fecha>{data($autor/datos_biograficos/nacimiento/fecha)}</fecha></nacimiento_paris>