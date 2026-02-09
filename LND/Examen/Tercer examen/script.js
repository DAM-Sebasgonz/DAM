// 1. VARIABLES GLOBALES
const simbolosOriginales = ["🦁", "🐯", "🐻", "🐨", "🐼", "🐸", "🐙", "🦄"];

let tablero = [];  //Lo usaremos para guardar todos los simbolos del tablero        
let cartasVolteadas = [];  //Se guardan las cartas volteadas aquí hay que cargarlo y vaciarlo cuando toque
let movimientos = 0; //Sirve para contar el numero de movimientos(cada vez que se levantan dos cartas se debe sumar 1)      
let paresEncontrados = 0; //Sirve para aumentar el numero de pares encontrados en caso de llegar al numero de simbolos se gana 
let bloqueado = false; //Sirve para bloquear el tablero y que no levanten mas de dos cartas    

// Referencias al HTML
const contenedorTablero = document.getElementById('tablero-juego');
const displayMovimientos = document.getElementById('movimientos');
const modalVictoria = document.getElementById('modal-victoria');

// 2. FUNCIONES 

// PASO 1: LÓGICA DE DATOS
function crearTableroLogico() {

    // TAREA A: Duplicar los símbolos para tener 8 pares (16 cartas)

    simbolosOriginales.forEach(simbolo => {
        tablero.push(simbolo);
        tablero.push(simbolo);
    });

    //Barajar (Desordenar) el array 'tablero' aleatoriamente
    tablero.sort(() => Math.random() - 0.5);
    
    
    console.log("Tablero generado:", tablero);
}

// PASO 2: DIBUJAR EN EL HTML
function dibujarTableroHTML() {
    contenedorTablero.innerHTML = ''; // Limpieza inicial

    // TAREA B: Recorrer el array 'tablero' y crear el HTML usa foreach(simbolo)
    
    tablero.forEach((simbolo) => {
        let carta = document.createElement("div")
        carta.classList.add("carta")

        carta.innerHTML = `
            <div class="contenido-carta">
                <div class="cara-frontal">?</div>
                <div class="cara-trasera">${simbolo}</div>
            </div>`

        contenedorTablero.appendChild(carta)

        carta.addEventListener("click",() => {
            manejarClick(carta)});
    });

        //1.Crea un elemento div y añade la clase carta  
        //2. Guardar el símbolo real en un dataset () 
        //3. Crear el HTML interno (Frontal y Trasera) (AQUI NO HAY QUE HACER NADA)
        // 4. Añadir evento click que llame a 'manejarClick' a traves de () => {manejarClick(carta)}
        // 5. Añadir al contenedor

}

// PASO 3: GESTIONAR EL CLIC
function manejarClick(carta) {

    
 
    // TAREA C: Validaciones de seguridad
        // Si está bloqueado O la carta ya está volteada O ya fue encontrada volvemos, para ello se usan las clases voletada y encontrada

    // TAREA D: Voltear carta
        // 1. Añadir clase volteado
        // 2. Guardar en memoria

    // TAREA E: Control de turno (Si hay 2 cartas volteadas)
        // 1. Bloquear el tablero para que no pulsen una tercera
        // 2. Aumentar movimientos y actualizar pantalla
        // 3. Llamar a verificarPar() con retraso de 1 segundo esto se hace para que de tiempo a la animación
        setTimeout(verificarPar, 1000);
}

// PASO 4: VERIFICAR SI SON IGUALES
function verificarPar() {

    let carta1 = cartasVolteadas[0]
    let carta2 = cartasVolteadas[1]

    if 
    (carta1.dataset.simbolo == carta2.dataset.simbolo){
        carta1.classList.add("volteada")
        carta2.classList.add("volteada")
        paresEncontrados += 1
        bloqueado == true
    } 
    else {
        carta1.classList.add("encontrada")
        carta2.classList.add("encontrada")
        bloqueado == false
    }

    
    // TAREA F: Recuperar las 2 cartas del array y guardarlas en dos variables
    
    // TAREA G: Comparar sus dataset.simbolo

        // --- COINCIDENCIA ---
            // Añadir clase 'encontrada' a ambas
            // Aumentar contador de pares encontrados
            // Verificar Victoria y mostrar al panel de victoria quita la clase oculta
        
        // --- NO COINCIDENCIA ---
        // Quitar clase 'volteada' a ambas cartas
    
    // TAREA H: Limpieza final vaciamos el array de cartasVolteadas y desbloqueamos
}

// 3. INICIO DEL JUEGO 
crearTableroLogico();
dibujarTableroHTML();