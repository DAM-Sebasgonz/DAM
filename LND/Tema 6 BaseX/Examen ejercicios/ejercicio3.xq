declare option output:method "xml";
declare option output:indent "yes";

for $editorial in collection("C:\DAM\LND\Tema 6 BaseX\Base de datos Examen\editoriales")//editorial
return <info><nombre>{upper-case(data($editorial/nombre))}</nombre><telefono>{data($editorial/contacto/telefono)}</telefono></info>