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

// CHECKBOX LISTENER

var contador = 0;
function requiredToggle() {
    var x = document.querySelectorAll('input[id="checkboxNoLabelTarea"]');
    var x2 = document.querySelectorAll('input[id="fechatermino_new"]');
    // CHECKBOX
    for (let i = 0; i < x.length; i++) {
        // FECHA TERMINO
        do {
            if (x[i].checked) {
                // alert("CHECKED");
                x2[contador].setAttribute('required', '');
                contador=contador+1;
                break;
            }
            else if (!x[i].checked) {
                x2[contador].removeAttribute('required');
                contador=contador+1;
                break;
            }
            
        } while (true);
    }
    contador = 0;
    // alert("ENTRA2");
}


document.querySelector('#btnReasignarTareas').disabled = false;
function countCheckboxes() {

    // alert("ENTRA1");
    requiredToggle();
}
// END CHECKBOX LISTENER

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
        alert("radio -> "+radio.value);
        values.push(radio.value);
    });
    alert("RADIO");
    const listPersonaTarea = document.getElementById("formReasignarTareas");
    for (const key in values) {
        alert("ENTRA AL FOR");
        listPersonaTarea.innerHTML +=`<input type="hidden" id="idPersona" name="idPersona" value=${values[key]}>`;
    }
}
function getValues1() {
    
    let values1 = [];
    checkboxessave.forEach((checkbox) => {
        alert(checkbox.value);
        values1.push(checkbox.value);
        // checkbox.prop("checked", !checkbox.prop("checked"));
    });

    let valuesSplitTarea = [];
    alert("?");
    for (const key in values1) {
        alert("ENTRA: "+String(values1[key]).split("|"));
        valuesSplitTarea.push(String(values1[key]).split("|"));
    }
    // alert(valuesSplitTarea.length);
    const listPersonaTarea = document.querySelector("#formReasignarTareas");
    let contador1 = 0;
    for (const key in valuesSplitTarea) {
        contador1+=1;
        let contador2 = 0;
        do {
            alert("AJAAJAJAJA: "+fterminosave[contador2].value);
            listPersonaTarea.innerHTML += `<input type="hidden" id="tarea${contador1}" name="tarea${contador1}" value=${valuesSplitTarea[key][0]}|${fterminosave[contador2].value}>`;
            contador2+=1;
            break;
        } while (true);  
    }
    listPersonaTarea.innerHTML += `<input type="hidden" id="tareaContador" name="tareaContador" value=${contador1}>`;
    
}

let checkboxessave;
let fterminosave = [];
function guardarCheckboxes() {
    checkboxessave = document.querySelectorAll('input[id="checkboxNoLabelTarea"]:checked');
    checkboxessave.forEach(element => {
        alert("VALOR: "+element.value);
        fterminosave.push(document.querySelector(`input[name="fechatermino_new${element.value}"]`));
        let valuex = document.querySelector(`input[name="fechatermino_new${element.value}"]`);
        alert("DATO FTERMINO: "+valuex.value);
    });
}


// Obtener datos tareas
// function reasignarTareas() {
//     let valuesTarea = getValues1();
//     // alert("LEN: "+valuesTarea.length);
    
// }
// END Obtener datos tareas

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
    alert("ENTRAF0");
    for (let i = 0; i < valuesPersona.length; i++) {
        // alert("LENGTH: "+valuesPersona.length);
        // alert("VALOR TEST: "+JSON.parse(valuesPersona[i])[0].fields.nombre_persona);
        alert("ENTRAF1");
        if (i == 0) {
            alert("ENTRAF1.1");
            alert("PERSONA: "+valuesPersona[i][0].pk);
            // alert(JSON.parse(valuesPersona[i])[0].pk);
            html += `<tr>
                        <td>${(valuesPersona[i])[0].pk}</td>
                        <td>${(valuesPersona[i])[0].fields.rut_persona}</td>
                        <td>${(valuesPersona[i])[0].fields.nombre_persona} ${(valuesPersona[i])[0].fields.apellido_paterno_persona} ${(valuesPersona[i])[0].fields.apellido_materno_persona}</td>
                        <td><input class="form-check" type="radio" style="margin: 1 auto" name="radioPersona" value="${(valuesPersona[i])[0].pk}" checked></td>
                    </tr>
                    `
            alert("ENTRAF1.2");
        }
        else if (i > 0){
            alert("ENTRAF1.3");
            html += `<tr>
                        <td>${(valuesPersona[i])[0].pk}</td>
                        <td>${(valuesPersona[i])[0].fields.rut_persona}</td>
                        <td>${(valuesPersona[i])[0].fields.nombre_persona} ${(valuesPersona[i])[0].fields.apellido_paterno_persona} ${(valuesPersona[i])[0].fields.apellido_materno_persona}</td>
                        <td><input class="form-check" type="radio" style="margin: 1 auto" name="radioPersona" value="${(valuesPersona[i])[0].pk}"></td>
                    </tr>
                    `
            alert("ENTRAF1.4");
        }
        if (i == valuesPersona.length - 1) {
            html += `   </tbody>
                    </table>
                    <br>
                    `
            alert("ENTRAF1.5");
        }
        alert("ENTRAF2");
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
            getValues1();
            form.submit();
        }
    })
    return false;
}
// END Asignar tarea FORM