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
const btn = document.querySelector('#btn');
btn.addEventListener('click', function() {
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

    alert(values);
    alert(values1);
});
// END CHECKBOX