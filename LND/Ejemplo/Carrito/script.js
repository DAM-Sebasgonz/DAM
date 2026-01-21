const lista = document.getElementById("lista-carrito");

let carrito = [];

let producto1 = {
    nombre: "Asus TUF 8400F",
    precio: 1034,
    cantidad: 2
}

let producto2 = {
    nombre: "Iphone 17",
    precio: 1400,
    cantidad: 4
}

let producto3 = {
    nombre: "Logitech G733",
    precio: 130,
    cantidad: 2
}

//Funcion para mostrar el nombre precio y cantidad de los articulos
function mostrarCarrito(){

    lista.innerHTML = `ALGO`;
    let contador = 0;

    while (contador < carrito.length){
        //creo elemento div
        let divlista = document.createElement("div");

        //modifica html
        divlista.innerHTML = `El nombre del ${contador+1}º es <strong>${carrito[contador].nombre}</strong><br>
        El precio del ${contador+1}º es ${carrito[contador].precio}💰<br>
        La cantidad del ${contador+1}º es ${carrito[contador].cantidad}<br><hr><hr>`

        //añade una clase
        divlista.classList.add("elemento-lista") 

        //hace hijo el elemento
        lista.appendChild(divlista); 

        contador++;
    }
        
}


//Funcion que calcule el importe total
//producto1.precio * producto1.cantidad + produtcto2.precio * producto2.cantiodad.. ........
function importeTotal()
{
    let contador = 0;
    let total = 0;
    
    while (contador < carrito.length)
    {
        total += carrito[contador].precio * carrito[contador].cantidad;
        contador ++;
    }

    document.write(`El total es ${total}💰`)
}


carrito.push(producto1);
carrito.push(producto2);
carrito.push(producto3);


mostrarCarrito();
importeTotal();