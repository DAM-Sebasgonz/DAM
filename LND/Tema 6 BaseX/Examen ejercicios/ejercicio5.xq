declare option output:method "xml";
declare option output:indent "yes";

(: 5 :)

for $autor in collection("C:\DAM\LND\Tema 6 BaseX\Base de datos Examen\autores")//autor
where data($autor/datos_biograficos/nacimiento/fecha) > "1901-00-00" and data($autor/datos_biograficos/nacimiento/fecha) < "2000-00-00"
return <autor nombre="{$autor/nombre}"></autor>