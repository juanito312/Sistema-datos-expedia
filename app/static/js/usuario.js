// Obtener el nombre del usuario
let sotoredUsuario = localStorage.getItem('usuario');

//Mostramos el nombre del usuario
if (sotoredUsuario) {
    document.getElementById('nombre').innerText = sotoredUsuario
}