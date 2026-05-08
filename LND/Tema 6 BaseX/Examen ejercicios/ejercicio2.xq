declare option output:method "xml";
declare option output:indent "yes";

for $libro in collection("C:\DAM\LND\Tema 6 BaseX\Base de datos Examen\libros")//libro
return <inventario_valor titulo="{$libro/titulo}">{data($libro/inventario/ejemplares_totales)*data($libro/inventario/precio)}</inventario_valor>