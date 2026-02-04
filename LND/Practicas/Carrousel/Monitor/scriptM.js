const track = document.querySelector(".carousel-track");
const slides = document.querySelectorAll(".slide");
const btnDelante = document.getElementById("Btn-delante");
const btnAtras = document.getElementById("Btn-atras");

let index = 0;

btnDelante.addEventListener("click", () => {
    index++;

    if (index >= slides.length) {
        index = 0;
    }

    track.style.transform = `translateX(-${index * 100}%)`; // esto lo vi en internet y me parecio bien ponerlo asi
});

btnAtras.addEventListener("click", () => {
    index--;

    if (index < 0) {
        index = slides.length - 1;
    }

    track.style.transform = `translateX(-${index * 100}%)`; // esto lo vi en internet y me parecio bien ponerlo asi
});