const emojisBase = ['🎮', '🎲', '🎯', '🎨', '🎭', '🎪', '🎬', '🎸'];
let tablero = [];
let cartasVolteadas = [];
let parejasEncontradas = 0;
let movimientos = 0;
let bloqueado = false;

// Duplica los emojis base y los mezcla aleatoriamente
function inicializarTablero() {
    tablero = [...emojisBase, ...emojisBase];
    
    for (let i = tablero.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        let temporal = tablero[i];
        tablero[i] = tablero[j];
        tablero[j] = temporal;
    }
}

// Crea las cartas dinámicamente en el DOM y guarda el emoji en el dataset
function pintarTablero() {
    const contenedorTablero = document.getElementById('tablero');
    contenedorTablero.innerHTML = '';

    for (let i = 0; i < tablero.length; i++) {
        const emoji = tablero[i];
        
        const carta = document.createElement('div');
        carta.className = 'carta';
        carta.dataset.emoji = emoji;
        carta.dataset.index = i;

        carta.innerHTML = `
            <div class="carta-inner">
                <div class="carta-front">?</div>
                <div class="carta-back">${emoji}</div>
            </div>
        `;

        carta.addEventListener('click', function() {
            manejarClick(carta);
        });

        contenedorTablero.appendChild(carta);
    }
}

// Maneja el clic en una carta: la voltea y llama a comparar si hay 2 cartas
function manejarClick(carta) {
    if (bloqueado) {
        return;
    }
    
    if (carta.classList.contains('volteada')) {
        return;
    }
    
    if (carta.classList.contains('encontrada')) {
        return;
    }
    
    if (cartasVolteadas.length >= 2) {
        return;
    }

    carta.classList.add('volteada');
    cartasVolteadas.push(carta);

    if (cartasVolteadas.length === 2) {
        movimientos++;
        actualizarMarcador();
        compararCartas();
    }
}

// Compara las 2 cartas volteadas y decide si son pareja o no
function compararCartas() {
    bloqueado = true;

    const carta1 = cartasVolteadas[0];
    const carta2 = cartasVolteadas[1];
    const emoji1 = carta1.dataset.emoji;
    const emoji2 = carta2.dataset.emoji;

    if (emoji1 === emoji2) {
        setTimeout(function() {
            carta1.classList.add('encontrada');
            carta2.classList.add('encontrada');
            parejasEncontradas++;
            actualizarMarcador();
            cartasVolteadas = [];
            bloqueado = false;

            if (parejasEncontradas === 8) {
                setTimeout(function() {
                    mostrarVictoria();
                }, 500);
            }
        }, 400);
        
    } else {
        setTimeout(function() {
            carta1.classList.remove('volteada');
            carta2.classList.remove('volteada');
            cartasVolteadas = [];
            bloqueado = false;
        }, 1000);
    }
}

// Actualiza el marcador de parejas y movimientos en el DOM
function actualizarMarcador() {
    document.getElementById('parejas').textContent = parejasEncontradas + '/8';
    document.getElementById('movimientos').textContent = movimientos;
}

// Muestra el mensaje de victoria cuando se encuentran todas las parejas
function mostrarVictoria() {
    const mensaje = document.getElementById('mensajeVictoria');
    mensaje.classList.add('mostrar');
}

// Reinicia el juego a su estado inicial
function reiniciarJuego() {
    parejasEncontradas = 0;
    movimientos = 0;
    cartasVolteadas = [];
    bloqueado = false;

    document.getElementById('mensajeVictoria').classList.remove('mostrar');

    inicializarTablero();
    pintarTablero();
    actualizarMarcador();
}

// Inicia el juego cuando se carga la página
document.addEventListener('DOMContentLoaded', function() {
    inicializarTablero();
    pintarTablero();
    actualizarMarcador();

    document.getElementById('btnReiniciar').addEventListener('click', function() {
        reiniciarJuego();
    });
});