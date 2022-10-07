// JAVASCRIPT PARA asignar_responsable.html

function filterPersona() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("filterInputPersona");
    filter = input.value.toUpperCase();
    table = document.getElementById("tablaPersona");
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

function btnCleanPersonaClick(){
    // 👇️ if you are submitting a form (prevents page reload)
    event.preventDefault();

    const filterInputPersona = document.getElementById('filterInputPersona');

    // 👇️ clear input field
    filterInputPersona.value = '';
    filterPersona();
}

function btnCleanTareaClick(){
    // 👇️ if you are submitting a form (prevents page reload)
    event.preventDefault();

    const filterInputTarea = document.getElementById('filterInputTarea');

    // 👇️ clear input field
    filterInputTarea.value = '';
    filterTarea();
}

function addPaddingBottomRow(panel) {
    var paddingBottomRow = document.getElementById("tablaDetalle");
    paddingBottomRow.style.paddingBottom = panel.scrollHeight+120+ "px";
}

function noPaddingBottomRow() {
    var paddingBottomRow = document.getElementById("tablaDetalle");
    paddingBottomRow.style.paddingBottom = "0px";
}

function updateMaxHeightPanel() {
    let activeBtn = document.getElementsByClassName("active");
    if (activeBtn.length > 0){
        var panel1 = document.getElementById("panel1");
        panel1.style.maxHeight = panel1.scrollHeight+(panel1.scrollHeight+panel1.scrollHeight/4)+"px";
        addPaddingBottomRow(panel1);
    }
}

function resetMaxHeight() {
    var panel1 = document.getElementById("panel1");
    panel1.style.maxHeight = "1000px";
    // alert("RESET WORKS");
}

function getValues(){
    let checkboxes = document.querySelectorAll('input[id="checkboxNoLabelPersona"]:checked');
    let values = [];
    checkboxes.forEach((checkbox) => {
        values.push(checkbox.value);
    });

    return values;
}

function getValues1(){
    let checkboxes1 = document.querySelectorAll('input[id="checkboxNoLabelTarea"]:checked');
    let values1 = [];
    checkboxes1.forEach((checkbox) => {
        values1.push(checkbox.value);
    });

    return values1;
}

// ACCORDION //
var acc = document.getElementsByClassName("acordeonJS");
var i;
for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
          panel.style.maxHeight = null;
          noPaddingBottomRow();
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
          addPaddingBottomRow(panel);
        }
    });
}
// END ACCORDION //

let waspressed = false;
// CHECKBOX
// USAR CHECKBOX LISTENER
const btnObtenerDatos = document.querySelector('#btnObtenerDatos');
btnObtenerDatos.addEventListener('click', function() {
    alert("HOLA");
    // Obtener valores de checkboxes
    let values = getValues();
    let values1 = getValues1();
    // Actualizar maxHeight
    updateMaxHeightPanel();
    if(waspressed === true){
        resetMaxHeight();
        waspressed = false;
    }
    // Mostrar TABLA DETALLE y botón ESCONDER TABLA
    var x = document.getElementById("tablaDetalle");
    var btn = document.getElementById("btnEsconderTabla");
    var btn1 = document.getElementById("btnAsignarTareas");
    if (x.style.display === "none" && values1.length > 0 && values.length > 0) {
        x.style.display = "";
        btn.style.display = "";
        btn1.style.display = "";
        // Llenar datos en accordion Persona
        let valuesSplit = [];
        for (const key in values) {
            valuesSplit.push(String(values[key]).split("|"));
        }
        var detallePersona = document.getElementById("detallePersona");
        for (const key in valuesSplit) {
            detallePersona.textContent ="Nombre: "+valuesSplit[key][1] +" "+ valuesSplit[key][2] +" "+ valuesSplit[key][3]+"                Rut: "+valuesSplit[key][0];
        }
        // Llenar datos en accordion Tarea
        let valuesSplit1 = [];
        for (const key in values1) {
            valuesSplit1.push(String(values1[key]).split("|"));
        }
        const list = document.getElementById("panelData");
        list.innerHTML = "";
        for (const key in valuesSplit1) {
            list.innerHTML += `<tr>
                                    <td>${valuesSplit1[key][1]}</td>
                                    <td><textarea class="form-control" cols="13" rows="2">${valuesSplit1[key][2]}</textarea></td>
                                    <td>${valuesSplit1[key][3]}</td>
                                    <td>${valuesSplit1[key][4]}</td>
                               </tr>`;
        }
    }
    alert("HOLA2");
});
// END CHECKBOX

// Esconder tabla detalle
function esconderTabla() {
    $("#tablaDetalle").hide("slow");
    $("#btnEsconderTabla").hide();
    $("#btnAsignarTareas").hide();
    $("#detallePersona").toggleClass("active");
    alert("HOLA3");
    // var panel = document.getElementById("panel1");
    // if (panel.style.maxHeight) {
    //     panel.style.maxHeight = null;
    //     noPaddingBottomRow();
    // }
}
// END Esconder tabla detalle

// Obtener datos tareas
function asignarTareas() {
    alert("ASIGNAR TAREA");
    let valuesTarea = getValues1();
    let valuesPersona = getValues();

    let valuesSplitPersona = [];
    for (const key in valuesPersona) {
        valuesSplitPersona.push(String(valuesPersona[key]).split("|"));
    }
    const listPersonaTarea = document.getElementById("formAsignarTareas");
    for (const key in valuesSplitPersona) {
        listPersonaTarea.innerHTML +=`<input type="hidden" id="persona${valuesSplitPersona[key][4]}" value=${valuesSplitPersona[key][4]}>`;
        // alert("PERSONA: "+valuesSplitPersona[key][4]);
    }
    
    let valuesSplitTarea = [];
    for (const key in valuesTarea) {
        valuesSplitTarea.push(String(valuesTarea[key]).split("|"));
    }
    let contador = 0;
    for (const key in valuesSplitTarea) {
        listPersonaTarea.innerHTML += `<input type="hidden" id="tarea${valuesSplitTarea[key][0]}" value=${valuesSplitTarea[key][0]}>`;
        contador+=1;
        // alert("TAREAS: "+valuesSplitTarea[key][0]);
    }
    listPersonaTarea.innerHTML += `<input type="hidden" id="tareaContador" value=${contador}>`;
}
// END Obtener datos tareas