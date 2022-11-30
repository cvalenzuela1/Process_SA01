// JAVASCRIPT PARA asignar_responsable.html

function filterTarea() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("filterInputTarea");
    filter = input.value.toUpperCase();
    table = document.getElementById("tablaTarea");
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

function btnCleanTareaClick(){
    // 👇️ if you are submitting a form (prevents page reload)
    event.preventDefault();

    const filterInputTarea = document.getElementById('filterInputTarea');

    // 👇️ clear input field
    filterInputTarea.value = '';
    filterTarea();
}

function getValues1(){
    let checkboxes1 = document.querySelectorAll('input[id="checkboxNoLabelTarea"]:checked');
    let values1 = [];
    checkboxes1.forEach((checkbox) => {
        values1.push(checkbox.value);
    });

    return values1;
}

// CHECKBOX LISTENER
document.querySelector('#btnReasignarTareas').disabled = true;

function countCheckboxes(){
    var x = document.querySelectorAll('input[id="checkboxNoLabelTarea"]:checked');
    if (x.length == 0) {
        document.querySelector('#btnReasignarTareas').disabled = true;
        return false
    }
    else if (x.length > 4){
        document.querySelector('#btnReasignarTareas').disabled = true;
        return false
    }
    else{
        document.querySelector('#btnReasignarTareas').disabled = false;
        return true
    }
}
// END CHECKBOX LISTENER

// Obtener datos tareas
function reasignarTareas() {
    const listPersonaTarea = document.getElementById("formReasignarTareas");
    let valuesTarea = getValues1();

    let valuesSplitTarea = [];
    for (const key in valuesTarea) {
        valuesSplitTarea.push(String(valuesTarea[key]).split("|"));
    }
    
    let contador = 0;
    for (const key in valuesSplitTarea) {
        contador+=1;
        listPersonaTarea.innerHTML += `<input type="hidden" id="tarea${contador}" name="tarea${contador}" value=${valuesSplitTarea[key][0]}>`;
    }
    listPersonaTarea.innerHTML += `<input type="hidden" id="tareaContador" name="tareaContador" value=${contador}>`;
}
// END Obtener datos tareas

// LISTA PERSONAS
function getListaPersonas() {
    let listaPersona = document.querySelectorAll('input[id="inputListaPersonas"]');
    let valuesPersona = [];
    let splitListPersona;
    listaPersona.forEach((persona) => {
        splitListPersona = persona.value;

        do {
            if (JSON.stringify(splitListPersona.indexOf("][")) > -1) {
                // alert("INDEX: "+JSON.stringify(splitListPersona.indexOf("][")));
                let index = parseInt(JSON.stringify(splitListPersona.indexOf("][")));

                // alert("ARRAY:"+JSON.stringify(splitListPersona.slice(0, index+1)));
                valuesPersona.push(JSON.parse(JSON.stringify(splitListPersona.substring(0, index+1))));
                
                splitListPersona = JSON.stringify(splitListPersona.substring(index+1));
                // alert("ARRAY CORTADO: "+splitListPersona);
            }
            else {
                // alert("ARRAY FINAL: "+splitListPersona);
                valuesPersona.push(JSON.parse(splitListPersona));
                break;
            }
           
        } while (true);

    });
    
    return valuesPersona;
}
// END LISTA PERSONAS

function getValues(){
    let radiobtn = document.querySelectorAll('input[name="radioPersona"]:checked');
    let values = [];
    radiobtn.forEach((radio) => {
        values.push(radio.value);
    });

    const listPersonaTarea = document.getElementById("formReasignarTareas");
    for (const key in values) {
        listPersonaTarea.innerHTML +=`<input type="hidden" id="idPersona" name="idPersona" value=${values[key]}>`;
    }
}

// Asignar tarea FORM
function reasignarTareasForm(form) {
    let valuesPersona = getListaPersonas();
    var html = `<table>
                    <thead>
                        <th style="width: 100px">ID</th>
                        <th style="width: 150px">RUT</th>
                        <th style="width: 300px">Nombre completo</th>
                        <th style="width: 80px">Acción</th>
                    </thead>
                    <tbody>
                
                `;
    for (let i = 0; i < valuesPersona.length; i++) {
        // alert("LENGTH: "+valuesPersona.length);
        // alert("VALOR TEST: "+JSON.parse(valuesPersona[i])[0].fields.nombre_persona);
        if (i == 0) {
            html += `<tr>
                        <td>${JSON.parse(valuesPersona[i])[0].pk}</td>
                        <td>${JSON.parse(valuesPersona[i])[0].fields.rut_persona}</td>
                        <td>${JSON.parse(valuesPersona[i])[0].fields.nombre_persona} ${JSON.parse(valuesPersona[i])[0].fields.apellido_paterno_persona} ${JSON.parse(valuesPersona[i])[0].fields.apellido_materno_persona}</td>
                        <td><input class="form-check" type="radio" style="margin: 1 auto" name="radioPersona" value="${JSON.parse(valuesPersona[i])[0].pk}" checked></td>
                    </tr>
                    `
        }
        else if (i > 0){
            html += `<tr>
                        <td>${JSON.parse(valuesPersona[i])[0].pk}</td>
                        <td>${JSON.parse(valuesPersona[i])[0].fields.rut_persona}</td>
                        <td>${JSON.parse(valuesPersona[i])[0].fields.nombre_persona} ${JSON.parse(valuesPersona[i])[0].fields.apellido_paterno_persona} ${JSON.parse(valuesPersona[i])[0].fields.apellido_materno_persona}</td>
                        <td><input class="form-check" type="radio" style="margin: 1 auto" name="radioPersona" value="${JSON.parse(valuesPersona[i])[0].pk}"></td>
                    </tr>
                    `
        }
        if (i == valuesPersona.length - 1) {
            html += `   </tbody>
                    </table>
                    <br>
                    `
        }
    }
    Swal.fire({
        "titleText": "Reasignar tareas",
        "html" : html,
        "icon": "question",
        "customClass": 'swal-wide',
        "showCancelButton": true,
        "cancelButtonText": "Cancelar",
        "confirmButtonText": "Continuar",
        "cancelButtonColor": "gray",
        "confirmButtonColor": "blue",
        "reverseButtons": true,
        "focusConfirm": true
    })
    .then(function(result){
        if(result.isConfirmed){
            getValues();
            reasignarTareas();
            form.submit();
            // Swal.fire({
            //     "titleText": "Indique una fecha de término nueva",
            //     "html": `<div class='row' style="width: 463px">
            //                 <div class='col-4'>
            //                     Descripción:
            //                 </div>
            //                 <div class='col-8'>
            //                     <input id="ftermino" class='form-control' type="date" required>
            //                 </div>
            //             </div>
            //             `,
            //     "icon": "info",
            //     "showCancelButton": true,
            //     "cancelButtonText": "Cancelar",
            //     "confirmButtonText": "Reasignar",
            //     "cancelButtonColor": "secondary",
            //     "confirmButtonColor": "blue",
            //     "reverseButtons": true,
            //     "focusConfirm": true
            // })
            //     .then(function(result){
            //         if(result.isConfirmed) {
            //             var ftermino = document.getElementById("ftermino");
            //             var val_ftermino = ftermino.value;
            //             var ftermino_date = ftermino.valueAsDate;
            //             ftermino_date = ftermino_date.toLocaleDateString('en-us', { year:"numeric", month:"numeric", day:"numeric"});
            //             var underscore_ftermino = val_ftermino.split(' ').join('_');
            //             if(val_ftermino.length > 0){
            //                 let currentDate = new Date();
            //                 currentDate = currentDate.getFullYear()+"-"+currentDate.getMonth()+"-"+currentDate.getDate();
            //                 // alert("current: "+currentDate);
            //                 // alert(Date.parse(ftermino_date)-Date.parse(currentDate));
            //                 if (Date.parse(ftermino_date)-Date.parse(currentDate) > 0) {
            //                     var frm = document.getElementById("formReasignarTareas");
            //                     frm.innerHTML += `<input id='fecha_termino_new' name='fecha_termino_new' value=${underscore_ftermino} type='hidden'></input>`;
            //                     window.history.pushState({}, "http://127.0.0.1:8000","/");
            //                     frm.action = "tareas-reasignarTarea/";
            //                     frm.submit();
            //                 }
            //                 else {
            //                     Swal.fire({
            //                         "title": "Debe añadir una fecha de término mayor a la actual",
            //                         "text": "¡Ha habido un problema!",
            //                         "icon": "warning"
            //                     })
            //                 }
                            
            //             }
            //             else{
            //                 Swal.fire({
            //                     "title": "Debe añadir una fecha de término nueva",
            //                     "text": "¡Ha habido un problema!",
            //                     "icon": "warning"
            //                 })
            //             }
            //         } 
            //     })
            // }
        }
    })
    return false;
}
// END Asignar tarea FORM