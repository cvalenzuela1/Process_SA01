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