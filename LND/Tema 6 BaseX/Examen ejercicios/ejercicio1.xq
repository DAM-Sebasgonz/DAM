declare option output:method "xml";
declare option output:indent "yes";

for $libro in collection("C:\DAM\LND\Tema 6 BaseX\Base de datos Examen\libros")//libro
where string-length($libro/sinopsis) > 600
return <sinopsis>{data($libro/sinopsis)}</sinopsis>
