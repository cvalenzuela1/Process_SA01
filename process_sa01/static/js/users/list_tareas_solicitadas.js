// JAVASCRIPT PARA list_tareas_solicitadas.html
function aceptarTarea(form){
    var formData = new FormData(form);

    form_object = Object.fromEntries(formData);
    Swal.fire({
        "titleText": "Título de tarea: "+form_object["titulo"],
        "html": `<div class='row' style="width: 463px">
                    <div class='col-4'>
                        Descripción:
                    </div>
                    <div class='col-8'>
                        <textarea class='form-control' readonly>${form_object["descripcion"]}</textarea>
                    </div>
                </div>
                <br>
                <div class='row' style="width: 463px">
                    <div class='col-6' style="margin-left:-8px">
                        &nbsp;&nbsp;&nbsp;Desde: &nbsp;${form_object["finicio"]}
                    </div>
                    <div class='col-6'>
                        &nbsp;&nbsp;&nbsp;Hasta: &nbsp;${form_object["ftermino"]}
                    </div>
                </div>
                <br>
                <div class='row' style="width: 463px">
                    <div class='col-6' style="margin-left:-13px">
                        &nbsp;&nbsp;&nbsp;Etiqueta: &nbsp;${form_object["etiqueta"]}
                    </div>
                    <div class='col-6'>
                        
                    </div>
                </div>
                `,
        "icon": "question",
        "showCancelButton": true,
        "showDenyButton": true,
        "cancelButtonText": "Cancelar",
        "confirmButtonText": "Aceptar",
        "denyButtonText": "Rechazar",
        "cancelButtonColor": "secondary",
        "confirmButtonColor": "green",
        "denyButtonColor": "red",
        "reverseButtons": false,
        "focusConfirm": true
    })
    .then(function(result){
        if(result.isConfirmed){
            form.submit();
        }
        else if (result.isDenied) {
            Swal.fire({
                "titleText": "Indique una justificación",
                "html": `<div class='row' style="width: 463px">
                            <div class='col-4'>
                                Descripción:
                            </div>
                            <div class='col-8'>
                                <textarea id="justificacion" class='form-control'></textarea>
                            </div>
                        </div>
                        `,
                "icon": "info",
                "showCancelButton": true,
                "cancelButtonText": "Cancelar",
                "confirmButtonText": "Rechazar",
                "cancelButtonColor": "secondary",
                "confirmButtonColor": "red",
                "reverseButtons": false,
                "focusConfirm": true
            })
            .then(function(result){
                if(result.isConfirmed) {
                    var frm = document.getElementById(`form${form_object["tarea_id"]}`);
                    window.history.pushState({}, "http://127.0.0.1:8000","/");
                    frm.action = "tareas-solicitadas-rechazar/"
                    frm.submit();
                }
            })
        }
    })
    return false;
}