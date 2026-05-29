// 1. VARIABLES GLOBALES (Lógica)
const colores = ['verde', 'rojo', 'amarillo', 'azul'];
let secuenciaMaquina = []; 
let secuenciaJugador = []; 
let nivel = 0;

// ======================================================================
// TAREA A: Capturar elementos del DOM
// ======================================================================
// 1. Crea una constante 'spanNivel' 
// 2. Crea una constante 'mensajeEstado' 
// 3. Crea una constante 'btnInicio' 
// 4. Crea una constante 'botonesJuego' que seleccione TODOS los botones de colores

const spanNivel = document.getElementById('nivel');
const mensajeEstado = document.getElementById('mensaje-estado');
const btnInicio = document.getElementById('btn-inicio');
const botonesJuego = document.querySelectorAll('.btn-color');


// ======================================================================
// 2. FUNCIONES DEL JUEGO
// ======================================================================

function comenzarJuego() {
    // TAREA B: Reiniciar variables
    // 1. Vaciar secuenciaMaquina y secuenciaJugador (asignarles un array vacío).
    // 2. Poner la variable 'nivel' a 0.
    // 3. Llamar a la función siguienteNivel().
    mensajeEstado.innerText = "¡Sigue la secuencia!";

    nivel = 0;
    secuenciaMaquina = [];
    secuenciaJugador = [];
    siguienteNivel();
    spanNivel.innerText = nivel;

}

function siguienteNivel() {
    // TAREA C: Aumentar nivel y preparar ronda
    // 1. Aumentar la variable nivel en 1 tanto en datos como visual.
    // 2. Lo necesario para el jugador y añadir un nuevo color a la secuencia.
    // 3. Llamar a reproducirSecuencia() (ya está creada abajo).

    nivel++;
    spanNivel.innerText = nivel;
    secuenciaJugador = [];
    secuenciaMaquina.push(colores[Math.floor(Math.random() * colores.length)]);
    reproducirSecuencia();

}

function manejarClick(colorClickado) {
    // Evitamos que puedan jugar si la máquina no ha empezado

    // TAREA D: Registrar el clic del usuario
    // Pon la lógica necesario para que al hacer click registre el color que clico el usuario
    
    // 2. Ilumina el botón con la funcion auxiliar
    
    // 3. Llama a la función que verifica si ha sido el color correcto.
    
    iluminarBoton(colorClickado);
    verificarRespuesta(colorClickado);
    secuenciaJugador.push(colorClickado);
    document.write(secuenciaJugador);
    document.write(secuenciaMaquina);
}

function verificarRespuesta(indice) {
    // TAREA E: Lógica del juego 
    // 1. Haz lo necesario para verificar si el color es el correcto

    
    
        // SI ES IGUAL (CORRECTO):
            // Comprueba si hemos terminado toda la secuencia de esta ronda y en ese caso ejecuta el codigo de abajo.
            setTimeout(() => {
                mensajeEstado.innerText = "¡Sigue la secuencia!";
                siguienteNivel();
            }, 1000);
            
        // NO ES IGUAL (ERROR):
            // Cambia el texto de 'mensajeEstado' a "¡Perdiste! Juego terminado". No permitas más clicks
}

// ======================================================================
// TAREA F: Asignar Eventos (Listeners)
// ======================================================================
// 1. Permite que se pueda iniciar el juego.

// 2. Carga los botones de colores.



// ======================================================================
// --- FUNCIONES DE AYUDA ---
// ======================================================================
function iluminarBoton(color) {
    const btn = document.getElementById(color);
    btn.classList.add('iluminado');
    setTimeout(() => btn.classList.remove('iluminado'), 400);
}

function reproducirSecuencia() {
    let i = 0;
    const intervalo = setInterval(() => {
        iluminarBoton(secuenciaMaquina[i]);
        i++;
        if (i >= secuenciaMaquina.length) clearInterval(intervalo);
    }, 800);
}