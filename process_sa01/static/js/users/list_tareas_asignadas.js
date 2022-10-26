// JAVASCRIPT PARA list_tareas_asignadas.html
function mostrarTareaAsignada(tarea_id){
    tarea = document.getElementById(`tarea_id${tarea_id}`)
    tarea_values = tarea.value
    var tarea_split = tarea_values.split("|")
    if (tarea_split[6] != 7 ) {
        Swal.fire({
            "titleText": `Título de tarea: ${tarea_split[0]}`,
            "html": `<table style='text-align: left'>
                        <tbody>
                            <tr>
                                <td>Descripción: </td>
                                <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
                                <td><textarea class="form-control" cols="30" rows="2" readonly style='resize: none'>${tarea_split[1]}</textarea></td>
                            </tr>
                            <tr style='height: 20px'>
                            </tr>
                            <tr>
                            <td>Etiqueta: </td>
                            <td></td>
                            <td><textarea class="form-control" cols="30" rows="2" readonly style='resize: none'>${tarea_split[4]}</textarea></td>
                            </tr>
                            <tr style='height: 20px'>
                            </tr>
                            <tr>
                                <td>Desde: ${tarea_split[2]}</td>
                                <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
                                <td>Hasta: ${tarea_split[3]}</td>
                            </tr>
                        </tbody>
                    </table><br>
                    <div class="progress" title="Porcentaje de cumplimiento de la tarea: ${tarea_split[5]}%">
                        <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-label="Animated striped example" aria-valuenow="${tarea_split[5]}" aria-valuemin="0" aria-valuemax="100" style="width: ${tarea_split[5]}%"></div>
                    </div>
                    <small class="text-muted">Quedan ${tarea_split[7]} días para el fin del plazo</small>
                    `,
            "icon": "success",
            "showConfirmButton": false,
            "showCancelButton": true,
            "cancelButtonText": "Cancelar",
            "cancelButtonColor": "secondary",
        })
        return false;
    }
    else 
    {
        Swal.fire({
            "titleText": `Título de tarea: ${tarea_split[0]}`,
            "html": `<table style='text-align: left'>
                        <tbody>
                            <tr>
                                <td>Descripción: </td>
                                <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
                                <td><textarea class="form-control" cols="30" rows="2" readonly style='resize: none'>${tarea_split[1]}</textarea></td>
                            </tr>
                            <tr style='height: 20px'>
                            </tr>
                            <tr>
                            <td>Etiqueta: </td>
                            <td></td>
                            <td><textarea class="form-control" cols="30" rows="2" readonly style='resize: none'>${tarea_split[4]}</textarea></td>
                            </tr>
                            <tr style='height: 20px'>
                            </tr>
                            <tr>
                                <td>Desde: ${tarea_split[2]}</td>
                                <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
                                <td>Hasta: ${tarea_split[3]}</td>
                            </tr>
                        </tbody>
                    </table><br>
                        <div class="progress" title="Porcentaje de cumplimiento de la tarea: ${tarea_split[5]}%">
                            <div class="progress-bar progress-bar-striped progress-bar-animated bg-danger" role="progressbar" aria-label="Animated striped example" aria-valuenow="${tarea_split[5]}" aria-valuemin="0" aria-valuemax="100" style="width: ${tarea_split[5]}%"></div>
                        </div>
                    <small>Se acabo el plazo, la tarea está atrasada</small>
                    `,
            "icon": "warning",
            "showConfirmButton": false,
            "showCancelButton": true,
            "cancelButtonText": "Cancelar",
            "cancelButtonColor": "secondary",
        })
        return false;
    }
}