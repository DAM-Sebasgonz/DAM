let carrito = [];

function agregarAlCarrito(nombre, precio) {
    carrito.push({ nombre, precio });
    mostrarCarrito();
}

function eliminarDelCarrito(indice) {
    carrito.splice(indice, 1);
    mostrarCarrito();
}

function mostrarCarrito() {
    const listaCarrito = document.getElementById('lista-carrito');
    
    if (carrito.length === 0) {
        listaCarrito.innerHTML = '<p class="carrito-vacio">El carrito está vacío</p>';
        document.getElementById('total').textContent = 'Total: €0.00';
        return;
    }

    let html = '';
    let total = 0;

    carrito.forEach((item, indice) => {
        total += item.precio;
        html += `
            <div class="item-carrito">
                <div class="item-info">
                    <div class="item-nombre">${item.nombre}</div>
                    <div class="item-precio">€${item.precio}</div>
                </div>
                <button class="btn-eliminar" onclick="eliminarDelCarrito(${indice})">Eliminar</button>
            </div>
        `;
    });

    listaCarrito.innerHTML = html;
    document.getElementById('total').textContent = `Total: €${total.toFixed(2)}`;
}