

<auditoria_legendarios>
{
  for $save in collection("rpg")/save_data
  let $legendarios := $save/inventory/item[rarity = "legendary"]
  let $numero_legendarios := count($legendarios)
  where $numero_legendarios > 0
  order by $numero_legendarios descending
  return
  <personaje name="{data($save/meta_data/char_name)}">
     <total_legendarios>{$numero_legendarios}</total_legendarios>
     {
       for $legen at $id in $legendarios 
       return
       <item_legendario id="{$id}">
         <nombre_item>{data($legen/name)}</nombre_item>
         <dureza_actual>{data($legen/durability/@current)}</dureza_actual>
       </item_legendario>
     }
  </personaje>
}
</auditoria_legendarios>