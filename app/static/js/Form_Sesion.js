
// Validaciones de registrar usuario
function validarEmail(elemento){

    var texto = document.getElementById("typeEmailX").value;
    var regex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
    
    if (!regex.test(texto)) {
        document.getElementById("resultado").innerHTML = "Correo invalido";
    } else {
      document.getElementById("resultado").innerHTML = "";
    }
  
  }

function validarContraseña () {
   
    var p1 = document.getElementById("typePasswordX").value;
    var p2 = document.getElementById("typePasswordX2").value;
    var espacios = false;
    var cont = 0;
  
    // Este bucle recorre la cadena para comprobar
    // que no todo son espacios
      while (!espacios && (cont < p1.length)) {
          if (p1.charAt(cont) == " ")
              espacios = true;
          cont++;
      }
     
    if (espacios) {
        document.getElementById("mensaje2").className="text-danger";
		document.getElementById("mensaje2").innerHTML="La contraseña no puede tener espacion en blanco"
     return false;
    }
     
    if (p1.length == 0 || p2.length == 0) {
     alert("Los campos de la password no pueden quedar vacios");
     return false;
    }
     
    if (p1 != p2) {
        document.getElementById("mensaje3").className="text-danger";
		document.getElementById("mensaje3").innerHTML="Las contraseñas deben ser iguales";
     return false;
    } else {
     alert("Todo esta correcto");
     return true; 
    }
   }

// Validaciones de Inicio Sesion
function RecuperarEmail(elemento){

  var texto = document.getElementById("typeEmailRecoveryX").value;
  var regex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
  
  if (!regex.test(texto)) {
      document.getElementById("resultado").innerHTML = "Correo invalido";
  } else {
    document.getElementById("resultado").innerHTML = "";
  }

}

// Validacines de recuperar contraseña
function RecuperarEmail(elemento){

  var texto = document.getElementById("typeEmailRecoveryX").value;
  var regex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
  
  if (!regex.test(texto)) {
      document.getElementById("resultado").innerHTML = "Correo invalido";
  } else {
    document.getElementById("resultado").innerHTML = "";
  }

}
