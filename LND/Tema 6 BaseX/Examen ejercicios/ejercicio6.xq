(: 6 :)

declare option output:method "xml";
declare option output:indent "yes";

for $autor in collection("C:\DAM\LND\Tema 6 BaseX\Base de datos Examen\autores")//autor
return <pais nombre="{$autor/datos/biograficos/nacionalidad}"><nombre>{data($autor/nombre)}</nombre></pais>
