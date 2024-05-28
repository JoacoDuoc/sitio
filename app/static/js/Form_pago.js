$(document).ready(function(){
    function validarNombreTitular(nombre) {
        var partesNombre = nombre.trim().split(' ');
        if (partesNombre.length < 2) {
            return false; // Al menos un nombre y un apellido
        }
        // Verificar cada parte del nombre
        for (var i = 0; i < partesNombre.length; i++) {
            // Expresión regular que verifica si hay caracteres especiales o números
            if (!partesNombre[i].match(/^[a-zA-Z]+$/)) {
                return false; // La parte del nombre contiene caracteres especiales o números
            }
        }
        return true; // Nombre del titular válido
    }

    $('#NombreTitular').on('input', function() {
        var nombre = $(this).val();
        if (validarNombreTitular(nombre)) {
            $('#mensaje').text('Nombre del titular válido');
        } else {
            $('#mensaje').text('Por favor, introduce un nombre del titular válido');
        }
    });
});

// Numero tarjeta
jQuery(document).ready(function(){
	// Listen for the input event.
	jQuery("#num_tarjeta").on('input', function (evt) {
		// Allow only numbers.
		jQuery(this).val(jQuery(this).val().replace(/[^0-9]/g, ''));
	});
});

// Cvv
jQuery(document).ready(function(){
	// Listen for the input event.
	jQuery("#cvv").on('input', function (evt) {
		// Allow only numbers.
		jQuery(this).val(jQuery(this).val().replace(/[^0-9]/g, ''));
	});
});

// Mes
jQuery(document).ready(function(){
	// Listen for the input event.
	jQuery("#mes").on('input', function (evt) {
		// Allow only numbers.
		jQuery(this).val(jQuery(this).val().replace(/[^0-9]/g, ''));
	});
});

// Año
jQuery(document).ready(function(){
	// Listen for the input event.
	jQuery("#año").on('input', function (evt) {
		// Allow only numbers.
		jQuery(this).val(jQuery(this).val().replace(/[^0-9]/g, ''));
	});
});

