'''Una empresa de comidas fast-food quiere implementar un programa para llevar 
información de sus platos y los ingredientes que estos contienen.
La estructura de datos que pretender utilizar es la siguiente:
Un diccionario con tres claves: 
comidas = { ‘entrantes’ : [ { ‘plato’ : nombre, ‘ingredientes’:[ ingr01, …ingr0n]} , 
	 	 	 	 { ‘plato’ : nombre, ‘ingredientes’:[ ingr01, …ingr0n]}
	 	 	 	 … ],
	 	 ‘pizzas : [ { ‘plato’ : nombre, ‘ingredientes’:[ ingr01, …ingr0n]} , 
	 	 	 { ‘plato’ : nombre , ‘ingredientes’:[ ingr01, …ingr0n]}
	 	 	 	 … ],
	 	 ‘pastas’ : [ { ‘plato’ : nombre, ‘ingredientes’:[ ingr01, …ingr0n]} , 
	 	 	 { ‘plato’ : nombre , ‘ingredientes’:[ ingr01, …ingr0n]}
	 	 	 	 … ] }
El valor de cada clave es una lista que contiene diccionarios con los platos que 
ofrece el restaurante. Estos diccionarios tienen dos claves: plato e ingredientes el 
primero representa el nombre del plato y el segundo una lista de los ingredientes 
que contiene.
La empresa quiere tener un menú como el siguiente:
1. Añadir plato. 
2. Buscar platos por ingredientes
3. Eliminar plato. 
4. Salir
Lo que hace cada una de las opciones

Opción 1. Añadir plato (0,5 pts)
Esta opción pide el nombre del plato a añadir y la categoría a la que pertenece. Si 
el plato ya existe se indica mensaje de error.
Si no existe, se pide mediante un bucle todos los ingredientes que tiene. Para 
salirse del bucle se debe presionar la tecla <INTRO>. Un plato debe tener al 
menos 1 ingrediente.


Opción 2. Buscar plato por ingrediente (3,0 pts)
Esta opción se ejecuta si el diccionario comidas tiene elementos, en caso 
contrario se debe indicar un mensaje de error.
Esta opción comienza mediante un bucle a pedir los ingredientes a buscar al 
usuario. De este bucle se sale si se han introducido hasta 3 ingredientes o se 
utiliza la tecla <INTRO> para salir. NO SE PUEDE PEDIR LA CATEGORÍA DEL 
PLATO.
Luego se busca en la estructura de datos todos los platos que contengan la 
totalidad de ingredientes solicitados. 
Si hay platos que cumplan con la búsqueda se deben mostrar su categoría, su 
nombre y todos los ingredientes que contiene. En caso de que no haya se debe 
mostrar la frase “NO hay platos que contengan todos los ingredientes solicitados”.

Opción 3. Eliminar plato (0,5 pts)
Esta opción pide el nombre del plato a eliminar y la categoría a la que pertenece, 
si no existe se indica mensaje de error. Si existe, se elimina de la estructura
Escriba un programa de Python que permita gestionar los platos de comida de la 
empresa.'''
comidas={}
for i in range(3):
        clave = input("Ingresa una categoria: ")
        while True:
            valor = input("Ingresa un nombre de plato: ")
            ingredientes=input("Dime un ingrediente o varios separados en blanco: ").split()
            if clave in comidas:
                comidas[clave].append({'plato': valor, 'ingredientes': ingredientes})
            else:
                        # Si la categoría no existe, crea una nueva lista con el plato
                comidas[clave] = [{'plato': valor, 'ingredientes': ingredientes}]
            salir=input("¿Quieres añadir más platos a esta categoría? (s/n): ")
            if salir.lower()=='n':
                break
print(comidas)
                    