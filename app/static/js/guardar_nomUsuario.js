function login(){
    // Guardamos el nombre del usuario
    let nombre_usuario = document.getElementById('usuario').value;

    // Gurdamos el nombre del usuario en localStorage
    localStorage.setItem('usuario',nombre_usuario);
}

function mensaje(){
    alert('!Acceso correcto¡')
}