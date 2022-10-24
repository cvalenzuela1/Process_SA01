// JAVASCRIPT PARA list_tareas_asignadas.html
function mostrarTareaAsignada(tarea_id){
    tarea = document.getElementById(`tarea_id${tarea_id}`)
    tarea_values = tarea.value
    var tarea_split = tarea_values.split("|")
    Swal.fire({
        "titleText": `Título de tarea: ${tarea_split[0]}`,
        "html": `<table style='text-align: left'>
                    <tbody>
                        <tr>
                            <td>Descripción: </td>
                            <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
                            <td><textarea class="form-control" readonly style='resize: none'>${tarea_split[1]}</textarea></td>
                        </tr>
                        <tr style='height: 20px'>
                        </tr>
                        <tr>
                            <td>Desde: ${tarea_split[2]}</td>
                            <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
                            <td>Hasta: ${tarea_split[3]}</td>
                        </tr>
                        <tr style='height: 20px'>
                        </tr>
                        <tr>
                            <td>Etiqueta: ${tarea_split[4]} </td>
                        </tr>
                    </tbody>
                </table>
                `,
        "icon": "success",
        "showConfirmButton": false,
        "showCancelButton": true,
        "cancelButtonText": "Cancelar",
        "cancelButtonColor": "secondary",
    })
    return false;
}