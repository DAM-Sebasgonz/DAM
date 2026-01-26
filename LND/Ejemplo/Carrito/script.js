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
function mostrarCarrito() {

    lista.innerHTML = "LISTA DEL CARRITO";

    carrito.forEach((producto) => {

        let divlista = document.createElement("div");
        divlista.classList.add("elemento");

        divlista.innerHTML = `
            <strong>${producto.nombre}</strong>
            <button class="btn-mas">+</button>
            <button class="btn-menos">-</button>
            <ul>
                <li>Precio: ${producto.precio} 💰</li>
                <li>Cantidad: ${producto.cantidad}</li>
            </ul>
        `;

        let btnMas = divlista.querySelector(".btn-mas");
        let btnMenos = divlista.querySelector(".btn-menos");

        btnMas.addEventListener("click", () => {
            producto.cantidad++;
            mostrarCarrito();
            importeTotal();
        });

        btnMenos.addEventListener("click", () => {
            producto.cantidad--;

            // 🔁 reconstruir carrito sin métodos de array
            let nuevoCarrito = [];
            let i = 0;

            while (i < carrito.length) {
                if (carrito[i].cantidad > 0) {
                    nuevoCarrito.push(carrito[i]);
                }
                i++;
            }

            carrito = nuevoCarrito;

            mostrarCarrito();
            importeTotal();
        });

        lista.appendChild(divlista);
    });
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
