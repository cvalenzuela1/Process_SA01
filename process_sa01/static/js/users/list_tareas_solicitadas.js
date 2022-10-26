// JAVASCRIPT PARA list_tareas_solicitadas.html
function aceptarTarea(form){
    var formData = new FormData(form);
    form_object = Object.fromEntries(formData);
    Swal.fire({
        "titleText": "Título de tarea: "+form_object["titulo"],
        "html": 
                `<table style='text-align: left'>
                    <tbody>
                        <tr>
                            <td>Descripción: </td>
                            <td></td>
                            <td><textarea class="form-control" cols="30" rows="2" readonly style='resize: none'>${form_object["descripcion"]}</textarea></td>
                        </tr>
                        <tr style='height: 20px'>
                        </tr>
                        <tr>
                            <td>Etiqueta: </td>
                            <td></td>
                            <td><textarea class="form-control" cols="30" rows="2" readonly style='resize: none'>${form_object["etiqueta"]}</textarea></td>
                        </tr>
                        <tr style='height: 20px'>
                        </tr>
                        <tr>
                            <td>Desde: ${form_object["finicio"]}</td>
                            <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
                            <td>Hasta: ${form_object["ftermino"]}</td>
                        </tr>
                    </tbody>
                </table>
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
                                <textarea id="justificacion" class='form-control' maxlength='250' required style='resize: none'></textarea>
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
                    var justificacion = document.getElementById("justificacion");
                    var val_justificacion = justificacion.value
                    var underscore_justificacion = val_justificacion.split(' ').join('_')
                    if(val_justificacion.length > 0){
                        var frm = document.getElementById(`form${form_object["tarea_id"]}`);
                        frm.innerHTML += `<input id='justificacion_id' name='justificacion_id' value=${underscore_justificacion} type='hidden'></input>`
                        window.history.pushState({}, "http://127.0.0.1:8000","/");
                        frm.action = "tareas-solicitadas-rechazar/"
                        frm.submit();
                    }
                    else{
                        Swal.fire({
                            "title": "Debe añadir una justificación",
                            "text": "¡Ha habido un problema!",
                            "icon": "warning"
                        })
                    }
                } 
            })
        }
    })
    return false;
}