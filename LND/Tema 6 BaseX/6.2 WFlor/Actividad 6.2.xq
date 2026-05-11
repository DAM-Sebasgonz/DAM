(: for $miembro in doc("Gremio dragones.xml")//miembro
where $miembro/@clase = 'Mago' and $miembro/@nivel >= 50
return $miembro/nombre :)

(: for $miembro in doc("Gremio dragones.xml")//miembro
where $miembro/inventario/item/@tipo = 'arma'
return $miembro/nombre :)

(: for $miembro in doc("Gremio dragones.xml")//miembro
let $numItems := count($miembro/inventario/item)
where $numItems > 1
return
  <resultado>
    <nombre>{ $miembro/nombre/text() }</nombre>
    <totalItems>{ $numItems }</totalItems>
  </resultado> :)