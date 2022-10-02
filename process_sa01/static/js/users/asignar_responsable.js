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

// ACCORDION //
var acc = document.getElementsByClassName("acordeonJS");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
          panel.style.maxHeight = null;
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}
// END ACCORDION //

// CHECKBOX
// USAR CHECKBOX LISTENER
const btnObtenerDatos = document.querySelector('#btnObtenerDatos');
btnObtenerDatos.addEventListener('click', function() {
    let checkboxes = document.querySelectorAll('input[id="checkboxNoLabelPersona"]:checked');
    let values = [];
    checkboxes.forEach((checkbox) => {
        values.push(checkbox.value);
    });
    
    let checkboxes1 = document.querySelectorAll('input[id="checkboxNoLabelTarea"]:checked');
    let values1 = [];
    checkboxes1.forEach((checkbox) => {
        values1.push(checkbox.value);
    });

    // Mostrar TABLA DETALLE y botón ESCONDER TABLA
    var x = document.getElementById("tablaDetalle");
    var btn = document.getElementById("btnEsconderTabla");
    if (x.style.display === "none" && values1.length > 0 && values.length > 0) {
        x.style.display = "";
        btn.style.display = ""
        // Llenar datos en accordion Persona
        let valuesSplit = [];
        for (const key in values) {
            // alert(`${key}: ${values[key]}`);
            valuesSplit.push(String(values[key]).split("|"));
        }
        var detallePersona = document.getElementById("detallePersona");
        var personaPanel = document.getElementById("personaPanel");
        for (const key in valuesSplit) {
            // alert(`${key}: ${valuesSplit[0][1]}`);
            detallePersona.textContent = valuesSplit[0][1] +" "+ valuesSplit[0][2] +" "+ valuesSplit[0][3];
            personaPanel.textContent = "Rut: "+valuesSplit[0][0]+"\r\n";
            personaPanel.textContent += "Nombre completo: "+valuesSplit[0][1]+" "+valuesSplit[0][2]+" "+valuesSplit[0][3];
        }

        // Llenar datos en accordion Tarea
        let valuesSplit1 = [];
        for (const key in values1) {
            valuesSplit1.push(String(values1[key]).split("|"));
        }
        var detalleTarea = document.getElementById("detalleTarea");
        var tareaPanel = document.getElementById("tareaPanel");
        for (const key in valuesSplit1) {
            // alert(`${key}: ${valuesSplit[0][1]}`);
            detalleTarea.textContent = "Tarea: "+valuesSplit1[0][1];
            tareaPanel.textContent = "Título: "+valuesSplit1[0][1]+"\r\n";
            tareaPanel.textContent += "Descripción: "+valuesSplit1[0][2]+"\r\n";
            tareaPanel.textContent += "Fecha inicio: "+valuesSplit1[0][3]+"\r\n";
            tareaPanel.textContent += "Fecha término: "+valuesSplit1[0][4];
        }
    }
});
// END CHECKBOX

// Esconder tabla detalle
const btnEsconderTabla = document.querySelector('#btnEsconderTabla');
btnEsconderTabla.addEventListener('click', function() {
    var x = document.getElementById("tablaDetalle");
    var btn = document.getElementById("btnEsconderTabla");
    if (x.style.display === "") {
        x.style.display = "none";
        btn.style.display = "none"
    }
});
// END Esconder tabla detalle