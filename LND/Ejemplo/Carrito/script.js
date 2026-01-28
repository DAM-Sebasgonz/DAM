const lista = document.getElementById("carrito");
const lista2 = document.getElementById("total");
const botones = document.querySelectorAll(".btn-agregar");

let carrito = [];

class Producto {
    constructor(nombre, precio, cantidad) {
        this.nombre = nombre;
        this.precio = parseFloat(precio);
        this.cantidad = cantidad;
    }
}

function cargarBotones() {
    botones.forEach((boton) => {
        boton.addEventListener("click", () => {
            const nombre = boton.dataset.nombre;
            const precio = boton.dataset.precio;
            anadirCarrito(nombre, precio);
            mostrarCarrito();
            importeTotal();
        });
    });
}

function anadirCarrito(nombre, precio) {
    const productoExistente = carrito.find(producto => producto.nombre === nombre);
    if (productoExistente) {
        productoExistente.cantidad++;
    } else {
        carrito.push(new Producto(nombre, precio, 1));
    }
}

function sumarItem(nombre) {
    const producto = carrito.find(p => p.nombre === nombre);
    if (producto) {
        producto.cantidad++;
        mostrarCarrito();
        importeTotal();
    }
}

function restarItem(nombre) {
    const producto = carrito.find(p => p.nombre === nombre);
    
    if (producto) {
        producto.cantidad--;
        
        if (producto.cantidad === 0) {
            const index = carrito.indexOf(producto);
            carrito.splice(index, 1);
        }
        
        mostrarCarrito();
        importeTotal();
    }
}

function mostrarCarrito() {
    lista.innerHTML = `LISTA DEL CARRITO`;
    let contador = 0;

    while (contador < carrito.length) {
        let divlista = document.createElement("div");
        let nombreProducto = carrito[contador].nombre;

        divlista.innerHTML = `
            <strong>${nombreProducto}</strong>
            <button class="btn-sumar">+</button>
            <button class="btn-restar">-</button>
            <br>
            <ul>
                <li>Precio: ${carrito[contador].precio}💰</li>
                <li>Cantidad: ${carrito[contador].cantidad}</li>
            </ul>`;

        divlista.classList.add("elemento");
        lista.appendChild(divlista);

        const btnSumar = divlista.querySelector(".btn-sumar");
        btnSumar.addEventListener("click", () => sumarItem(nombreProducto));

        const btnRestar = divlista.querySelector(".btn-restar");
        btnRestar.addEventListener("click", () => restarItem(nombreProducto));

        contador++;
    }

    if(carrito.length === 0) {
        lista.innerHTML = "El carrito está vacío";
        lista2.innerHTML = "";
    }
}

function importeTotal() {
    let contador = 0;
    let total = 0;

    while (contador < carrito.length) {
        total += carrito[contador].precio * carrito[contador].cantidad;
        contador++;
    }

    lista2.innerHTML = `<h2>El <b>total</b> es: ${total}</h2>`;
}

cargarBotones();