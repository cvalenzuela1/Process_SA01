function detalleTarea(tarea_id){
    tarea = document.getElementById(`tarea_id${tarea_id}`)
    tarea_values = tarea.value
    var tarea_split = tarea_values.split("|")
    if (tarea_split[6] != 7 ) {
        Swal.fire({
            "titleText": `${tarea_split[0]}`,
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
// RUT PERSONA FILTROS  //
// Validar si filtro es númerica y contiene guión para el rut
function validate(evt) {
    var theEvent = evt || window.event;

    // Handle paste
    if (theEvent.type === 'paste') {
        key = event.clipboardData.getData('text/plain');
    } else {
    // Handle key press
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    }
    var regex = /[0-9]|\-/;
    if( !regex.test(key) ) {
        theEvent.returnValue = false;
        if(theEvent.preventDefault) theEvent.preventDefault();
    }
}

function filterRutPersona() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("filterInputRutPersona");
    filter = input.value.toUpperCase();
    table = document.getElementById("tablaTareaPersona");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}

function btnCleanRutPersonaClick(){
    // 👇️ if you are submitting a form (prevents page reload)
    event.preventDefault();

    const filterInputRutPersona = document.getElementById('filterInputRutPersona');

    // 👇️ clear input field
    filterInputRutPersona.value = '';
    filterRutPersona();
}
// END RUT PERSONA FILTROS  //

// NOMBRE PERSONA FILTROS  //
function filterNombrePersona() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("filterInputNombrePersona");
    filter = input.value.toUpperCase();
    table = document.getElementById("tablaTareaPersona");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function btnCleanNombrePersonaClick(){
    // 👇️ if you are submitting a form (prevents page reload)
    event.preventDefault();

    const filterInputNombrePersona = document.getElementById('filterInputNombrePersona');

    // 👇️ clear input field
    filterInputNombrePersona.value = '';
    filterNombrePersona();
}

// END NOMBRE PERSONA FILTROS  //