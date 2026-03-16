let numeroActual = '0';
let operacionActual = null;
let numeroAnterior = '';

const display = document.getElementById('display');

function actualizarDisplay() {
    display.textContent = numeroActual;
}

function agregarNumero(numero) {
    if (numeroActual === '0') {
        numeroActual = numero;
    } else {
        numeroActual = numeroActual + numero;
    }
    actualizarDisplay();
}

function limpiar() {
    numeroActual = '0';
    operacionActual = null;
    numeroAnterior = '';
    actualizarDisplay();
}

function operar(operador) {
    if (numeroActual === '') return;

    if (numeroAnterior !== '') {
        calcularResultado();
    }

    operacionActual = operador;
    numeroAnterior = numeroActual;
    numeroActual = '';
}

function calcularResultado() {
    if (operacionActual === null || numeroAnterior === '') return;

    const anterior = parseFloat(numeroAnterior);
    const actual   = parseFloat(numeroActual);
    let resultado;

    switch (operacionActual) {
        case '+': resultado = anterior + actual; break;
        case '-': resultado = anterior - actual; break;
        case 'x': resultado = anterior * actual; break;
        case '/':
            if (actual === 0) {
                alert('No se puede dividir por cero');
                return;
            }
            resultado = anterior / actual;
            break;
    }

    numeroActual    = resultado.toString();
    operacionActual = null;
    numeroAnterior  = '';
    actualizarDisplay();
}

const botonesNumero = document.querySelectorAll('.btn-numero');
botonesNumero.forEach(boton => {
    boton.addEventListener('click', () => agregarNumero(boton.textContent));
});

const botonesOperador = document.querySelectorAll('.btn-operador');
botonesOperador.forEach(boton => {
    boton.addEventListener('click', () => operar(boton.textContent));
});

const btnBorrar = document.getElementById('btn-borrar');
btnBorrar.addEventListener('click', () => limpiar());

const btnIgual = document.getElementById('btn-igual');
btnIgual.addEventListener('click', () => calcularResultado());