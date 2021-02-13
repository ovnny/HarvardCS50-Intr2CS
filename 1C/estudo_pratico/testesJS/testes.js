const frente = document.getElementById("frente");
const tras = document.getElementById("tras");

frente.addEventListener("click", function(){
    tras.style.zIndex = 1
    frente.style.zIndex = 0
})