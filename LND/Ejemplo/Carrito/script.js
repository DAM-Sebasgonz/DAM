const lista = document.getElementById("carrito");
const lista2 = document.getElementById("total");
const botones = document.querySelectorAll(".btn-agregar")

let carrito = [];

class Producto {
    constructor(nombre, precio, cantidad) {
        this.nombre = nombre;
        this.precio = parseFloat(precio);
        this.cantidad = cantidad;
    }
}

//Funcion que recorra la lista de botones y les cargue un evento
function cargarBotones(){
    botones.forEach((boton) => {
        boton.addEventListener("click", () => {
            const nombre = boton.dataset.nombre;
            const precio = boton.dataset.precio
            anadirCarrito(nombre, precio) //añado el item
            mostrarCarrito(); //lo muestro
            importeTotal();
        })

    })
}

function anadirCarrito(nombre, precio){
    
    const productoExistente = carrito.find(producto => producto.nombre === nombre);
    if (productoExistente) productoExistente.cantidad++;
    else carrito.push(new Producto(nombre, precio, 1));
}

//Funcion para mostrar el nombre precio y cantidad de los articulos
function mostrarCarrito(){

    lista.innerHTML = `LISTA DEL CARRITO`;
    let contador = 0;

    while (contador < carrito.length){
        //creo elemento div
        let divlista = document.createElement("div");

        //modifica html
        divlista.innerHTML = `<strong>${carrito[contador].nombre}</strong>      
        <button ${}>+</button>
        <button ${}>-</button>
        <br>
        <ul>
            <li>Precio: ${carrito[contador].precio}💰</li>
            <li>Cantidad: ${carrito[contador].cantidad}</li>
        </ul>`

        //añade una clase
        divlista.classList.add("elemento") ;

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

    lista2.innerHTML = `<h2>El <b>total</b> es: ${total}</h2>`;
}

cargarBotones();


