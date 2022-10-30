function mostrarContraseña() {
    var x = document.getElementById("password_usuario");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }