// 1. VARIABLES DE ESTADO (GLOBALES)
let numeroActual = '0';     // El número que se ve en pantalla mientras escribes
//trabajamos como string para concatenar más facil (se concantena un string con +)
let operacionActual = null; // Guardará +, -, x, /
let numeroAnterior = " ";    // Guardará el primer número antes de pulsar el operador

// Referencia al Display
const display = document.getElementById('display');

// 2. FUNCIONES LÓGICAS

// TAREA A: Función para actualizar la pantalla
function actualizarDisplay() {
    // 1. Asigna el valor de 'numeroActual' a la pantalla
    display.textContent= numeroActual 
}

// TAREA B: Función al pulsar un número
function agregarNumero(numero) {
    // 1. Verificar: Si 'numeroActual' es estrictamente igual a '0',
    //    reemplázalo por el 'numero' recibido.
    
    // 2. Si no es '0', concatena (suma texto) el 'numero' recibido a 'numeroActual'.
    //el "." también es tratado como un numero normal se concatena
    
    // 3. Llama a actualizarDisplay()

    if (numeroActual === "0"){
        numeroActual = numero
    }
    else{
        numeroActual = numeroActual + numero
    }
    actualizarDisplay();
}

// TAREA C: Función al pulsar C (Limpiar)
function limpiar() {
    // 1. Restablece todas las variables globales a sus valores iniciales ('0', '', null)
    // 2. Llama a actualizarDisplay()
    numeroActual = "0"
    operacionActual = null
    numeroAnterior = " "
    actualizarDisplay()
}

// TAREA D: Función al pulsar operador (+, -, x, /)
function operar(operador) {
    // Validación: Si numeroActual está vacío, salimos de la función (return)

    // 1. Si ya existe un 'numeroAnterior' (encadenamiento de operaciones), 
    //    llama a calcularResultado() primero.

    // 2. Guarda el 'operador' recibido en 'operacionActual'
    
    // 3. Pasa el valor de 'numeroActual' a 'numeroAnterior'
    
    // 4. Deja 'numeroActual' vacío ('') para esperar el siguiente número

    if(numeroActual == "0"){
        return
    }
    if (numeroAnterior !== '') {
        calcularResultado();
    }

    operacionActual = operador;
    numeroAnterior = numeroActual;
    numeroActual = '';
}

// TAREA E: Función al pulsar Igual (=)
function calcularResultado() {
    // Validación: Si no hay operacionActual o no hay numeroAnterior, salimos (return)

    if (operacionActual === null || numeroAnterior === '') return;

    // 1. Convierte las variables de string a float (parseFloat)
    const anterior = parseFloat(numeroAnterior);
    const actual = parseFloat(numeroActual);
    let resultado;

    // 2. Realiza la operación matemática usando switch(operacionActual)
        // Casos: '+', '-', 'x', '/'
        // Nota: En la división, evita dividir por 0 (puedes mostrar un alert)

        switch (operacionActual) {
        case "+": resultado == anterior + actual;return;
        case "-": resultado == anterior - actual;return;
        case "x": resultado == anterior * actual;return;
        case '/':
            if (actual === 0) {
                alert('No se puede dividir por cero');
                return;
            }
            resultado = anterior / actual;
            break;
        };
    }

    // 3. Actualiza las variables para la siguiente operación:
        // - numeroActual debe ser el resultado (convertido a string (".toString()"))
        // - operacionActual vuelve a null
        // - numeroAnterior vuelve a estar vacío

        numeroActual = resultado.toString()
        operacionActual = null
        numeroAnterior = " "
    
    // 4. Llama a actualizarDisplay()
    
        actualizarDisplay()

// ----------------------------------------------------------------------
// 3. EVENTOS
// ----------------------------------------------------------------------

// TAREA F: Eventos para los NÚMEROS
// 1. Selecciona TODOS los botones con la clase '.btn-numero'
// 2. Recórrelos usando un bucle
// 3. Dentro del bucle, añade un evento del tipo que consideres oportuno
// 4. Dicho evento llama a agregarNumero con el valor del boton

const botonesNumeros = document.querySelectorAll('.btn-numero')
botonesNumeros.forEach(boton => {
    document.addEventListener("click" , () => agregarNumero(boton.textContent))
});

// TAREA G: Eventos para los OPERADORES
// 1. Selecciona TODOS los botones con la clase '.btn-operador'
// 2. Recórrelos  y añade el evento.
// 3. El evento llama a operar con su operación

const botonesOperador = document.querySelectorAll('.btn-operador');
botonesOperador.forEach(boton => {
    boton.addEventListener('click', () => operar(boton.textContent));
});

// TAREA H: Eventos para ACCIONES ÚNICAS (Igual y Borrar)
// 1. Selecciona el botón de borrar (por su ID) y añádele el evento llamando a limpiar
const btnBorrar = document.getElementById('btn-borrar');
btnBorrar.addEventListener('click', () => limpiar());
// 2. Selecciona el botón de igual (por su ID) y añádele el evento llamando a calcularResultado
const btnIgual = document.getElementById('btn-igual');
btnIgual.addEventListener('click', () => calcularResultado());
