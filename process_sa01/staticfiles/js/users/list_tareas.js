// JAVASCRIPT PARA list_tareas.html
// OFFCANVAS CODE
function showoffcanvas(){
    var myCollapse = document.getElementById('offcanvasExample')
    var bsCollapse = new bootstrap.Collapse(myCollapse, {
        show: true
    })
}

function hideoffcanvas(){
    var myCollapse = document.getElementById('offcanvasExample')
    var bsCollapse = new bootstrap.Collapse(myCollapse, {
        show: false
    })
}
// END OFFCANVAS CODE