function getValuesCheckbox(){
    let checkboxes1 = document.querySelectorAll('input[id="checkboxTarea"]:checked');
    let values1 = [];
    checkboxes1.forEach((checkbox) => {
        values1.push(checkbox.value);
    });

    return values1;
}

function countCheckboxes(){
    var x = document.querySelectorAll('input[id="checkboxTarea"]:checked');
    if (x.length > 4){
        document.querySelector('#btnObtenerDatos').disabled = true;
    }
    else{
        document.querySelector('#btnObtenerDatos').disabled = false;
    }
}

function asignarTareasFlujo() {
    let valuesTarea = getValuesCheckbox();
    
    let valuesSplitTarea = [];
    for (const key in valuesTarea) {
        valuesSplitTarea.push(String(valuesTarea[key]).split("|"));
    }
    const listFlujoTarea = document.getElementById("formCrearFlujo");
    let contador = 0;
    for (const key in valuesSplitTarea) {
        contador+=1;
        listFlujoTarea.innerHTML += `<input type="hidden" id="tarea${contador}" name="tarea${contador}" value=${parseInt(valuesSplitTarea[key][0])}>`;
    }
    listFlujoTarea.innerHTML += `<input type="hidden" id="tareaContador" name="tareaContador" value=${contador}>`;
}
var nombre_flujo = document.querySelector("#nombre_flujo1");
var descripcion = document.querySelector("#descripcion1");
var cboxTipoFlujo = document.querySelector("#cboxTipoFlujo1");
function getValuesInputs(){
    lista = []
    lista.push(nombre_flujo.value);
    lista.push(descripcion.value);
    lista.push(cboxTipoFlujo.value);
    return lista;
}

function inputsHidden() {
    let valuesInputs = getValuesInputs();
    
    const listFlujoTarea = document.getElementById("formCrearFlujo");
    // for (let i = 0; i < valuesInputs.length; i++) {
    //     alert(valuesInputs[i]);
    // }
    listFlujoTarea.innerHTML += `<input type="hidden" id="nombre_flujo" name="nombre_flujo" value=${valuesInputs[0]}>`;
    listFlujoTarea.innerHTML += `<input type="hidden" id="descripcion" name="descripcion" value=${valuesInputs[1]}>`;
    listFlujoTarea.innerHTML += `<input type="hidden" id="cboxTipoFlujo" name="cboxTipoFlujo" value=${valuesInputs[2]}>`;
}


function asignarTareasFlujoForm(form){
    Swal.fire({
        "titleText": "¿Está seguro de crear el flujo?",
        "icon": "question",
        "showCancelButton": true,
        "cancelButtonText": "Cancelar",
        "confirmButtonText": "Crear",
        "cancelButtonColor": "grey",
        "confirmButtonColor": "blue",
        "reverseButtons": true,
        "focusConfirm": true
    })
    .then(function(result){
        if(result.isConfirmed){
            this.asignarTareasFlujo();
            this.inputsHidden();
            form.submit();
        }
    })
    return false;
}