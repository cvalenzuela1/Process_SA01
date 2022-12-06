// Apply chart themes
am4core.useTheme(am4themes_animated);
am4core.useTheme(am4themes_kelly);

// Create chart instance
var chart = am4core.create("chartdiv", am4charts.XYChart3D);

// Add data
chart.data = [ {
  "tipo_tarea": "Asignadas",
  "cantidad": document.getElementById("tareaPersona_asignadas").value,
  "color": am4core.color("#0acc47")
}, {
  "tipo_tarea": "En ejecución",
  "cantidad": document.getElementById("tareaPersona_ejecucion").value,
  "color": am4core.color("#4634eb")
}, {
  "tipo_tarea": "Finalizadas",
  "cantidad": document.getElementById("tareaPersona_finalizadas").value,
  "color": am4core.color("#eb0909")
}, {
  "tipo_tarea": "Atrasadas",
  "cantidad": document.getElementById("tareaPersona_atrasadas").value,
  "color": am4core.color("#ff6a00")
}];

// Create axes
var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "tipo_tarea";
categoryAxis.title.text = "Tipo de tarea";

var  valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
valueAxis.title.text = "Cantidad de tareas";

// Create series
var series = chart.series.push(new am4charts.ColumnSeries3D());
series.dataFields.valueY = "cantidad";
series.dataFields.categoryX = "tipo_tarea";
series.name = "Cantidad";
series.tooltipText = "{name}: [bold]{valueY}[/]";
series.columns.template.propertyFields.fill = "color"

chart.cursor = new am4charts.XYCursor();



// GRAFICO 2

// Apply chart themes
am4core.useTheme(am4themes_animated);
am4core.useTheme(am4themes_kelly);

// Create chart instance
var chart2 = am4core.create("chartdiv2", am4charts.XYChart3D);

// Add data
chart2.data = [ {
  "comienza_termina": "Comienzan",
  "cantidad": document.getElementById("finicio_current").value,
  "color": am4core.color("#0acc47")
}, {
  "comienza_termina": "Finalizan",
  "cantidad": document.getElementById("ftermino_current").value,
  "color": am4core.color("#eb0909")
}];

// Create axes
var categoryAxis = chart2.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "comienza_termina";
categoryAxis.title.text = "Comienzan - Finalizan";

var  valueAxis = chart2.yAxes.push(new am4charts.ValueAxis());
valueAxis.title.text = "Cantidad";

// Create series
var series = chart2.series.push(new am4charts.ColumnSeries3D());
series.dataFields.valueY = "cantidad";
series.dataFields.categoryX = "comienza_termina";
series.name = "Cantidad";
series.tooltipText = "{name}: [bold]{valueY}[/]";
series.columns.template.propertyFields.fill = "color"

chart2.cursor = new am4charts.XYCursor();