const botonMenu = document.getElementById('botonMenu');
const miMenu = document.getElementById('miMenu');

botonMenu.addEventListener('click', function() {
    miMenu.classList.toggle('activo');
});

const enlaces = miMenu.querySelectorAll('a');
enlaces.forEach(enlace => {
    enlace.addEventListener('click', function() {
        miMenu.classList.remove('activo');
    });
});