// JAVASCRIPT PARA detalle_tareas.html
function finalizarTarea(form){
    Swal.fire({
        "titleText": "¿Estás seguro de finalizar la tarea?",
        'text': "¡Esta acción es irreversible!",
        "icon": "warning",
        "showCancelButton": true,
        "cancelButtonText": "Cancelar",
        "confirmButtonText": "Finalizar",
        "cancelButtonColor": "red",
        "confirmButtonColor": "green",
        "reverseButtons": true,
        "focusConfirm": true
    })
    .then(function(result){
        if(result.isConfirmed){
            form.submit();
        }
    })
    return false;
}

function editarTarea(form){
    Swal.fire({
        "titleText": "¿Estás seguro de editar la tarea?",
        'text': "Esta acción se puede realizar nuevamente",
        "icon": "warning",
        "showCancelButton": true,
        "cancelButtonText": "Cancelar",
        "confirmButtonText": "Editar",
        "cancelButtonColor": "red",
        "confirmButtonColor": "green",
        "reverseButtons": true,
        "focusConfirm": true
    })
    .then(function(result){
        if(result.isConfirmed){
            form.submit();
        }
    })
    return false;
}

$( function() {
    $( document ).tooltip();
} );