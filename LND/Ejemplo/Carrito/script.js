const lista = document.getElementById("carrito");
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
        })

    })
}

function anadirCarrito(nombre, precio){
    carrito.push(new Producto(nombre, precio, 1));
}

//Funcion para mostrar el nombre precio y cantidad de los articulos
function mostrarCarrito(){

    lista.innerHTML = " ";
    let contador = 0;

    while (contador < carrito.length){
        //creo elemento div
        let divlista = document.createElement("div");

        //modifica html
        divlista.innerHTML = `El nombre del ${contador+1}º es <strong>${carrito[contador+1].nombre}</strong><br>
        El precio del ${contador+1}º es ${carrito[contador].precio}<br>
        La cantidad del ${contador+1}º es ${carrito[contador].cantidad}<br><hr><hr>`

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

    document.write(`El total es ${total}`)
}

cargarBotones();


