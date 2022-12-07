// Create chart instance
var chart = am4core.create("chartdiv", am4charts.PieChart);

// Add data
chart.data = [{
    "estado": "Activa",
    "cantidad": document.getElementById("t_activas").value,
    "color": am4core.color("#0abccc")
}, {
    "estado": "Asignada",
    "cantidad": document.getElementById("t_asignadas").value,
    "color": am4core.color("#0acc47")
}, {
    "estado": "En ejecución",
    "cantidad": document.getElementById("t_ejecucion").value,
    "color": am4core.color("#4634eb")
}, {
    "estado": "Finalizada",
    "cantidad": document.getElementById("t_finalizadas").value,
    "color": am4core.color("#eb0909")
}, {
    "estado": "Atrasada",
    "cantidad": document.getElementById("t_atrasadas").value,
    "color": am4core.color("#ff6a00")
}
];

// Add and configure Series
var pieSeries = chart.series.push(new am4charts.PieSeries());
pieSeries.dataFields.value = "cantidad";
pieSeries.dataFields.category = "estado";
pieSeries.slices.template.propertyFields.fill = "color";

chart.legend = new am4charts.Legend();


// CHART XY 

// // Apply chart themes
// am4core.useTheme(am4themes_animated);
// am4core.useTheme(am4themes_kelly);

// // Create chart instance
// var chart = am4core.create("chartdivXY", am4charts.XYChart3D);

// // Add data
// chart.data = [{
//   "country": "Lithuania",
//   "litres": 501.9,
//   "units": 250
// }, {
//   "country": "Czech Republic",
//   "litres": 301.9,
//   "units": 222
// }, {
//   "country": "Ireland",
//   "litres": 201.1,
//   "units": 170
// }, {
//   "country": "Germany",
//   "litres": 165.8,
//   "units": 122
// }, {
//   "country": "Australia",
//   "litres": 139.9,
//   "units": 99
// }, {
//   "country": "Austria",
//   "litres": 128.3,
//   "units": 85
// }, {
//   "country": "UK",
//   "litres": 99,
//   "units": 93
// }, {
//   "country": "Belgium",
//   "litres": 60,
//   "units": 50
// }, {
//   "country": "The Netherlands",
//   "litres": 50,
//   "units": 42
// }];

// // Create axes
// var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
// categoryAxis.dataFields.category = "country";
// categoryAxis.title.text = "Countries";

// var  valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
// valueAxis.title.text = "Litres sold (M)";

// // Create series
// var series = chart.series.push(new am4charts.ColumnSeries3D());
// series.dataFields.valueY = "litres";
// series.dataFields.categoryX = "country";
// series.name = "Sales";
// series.tooltipText = "{name}: [bold]{valueY}[/]";

// var series2 = chart.series.push(new am4charts.ColumnSeries3D());
// series2.dataFields.valueY = "units";
// series2.dataFields.categoryX = "country";
// series2.name = "Units";
// series2.tooltipText = "{name}: [bold]{valueY}[/]";

// // Add cursor
// chart.cursor = new am4charts.XYCursor();



// CHART PIE 2
// Create chart instance
var chart = am4core.create("chartdivPIE2", am4charts.PieChart);

// Add data
chart.data = [{
    "tipo": "Anual",
    "cantidad": document.getElementById("tflujo_anual").value,
    "color": am4core.color("#03dffc")
}, {
    "tipo": "Mensual",
    "cantidad": document.getElementById("tflujo_mensual").value,
    "color": am4core.color("#02fa0f")
}, {
    "tipo": "Semanal",
    "cantidad": document.getElementById("tflujo_semanal").value,
    "color": am4core.color("#ffa600")
}, {
    "tipo": "Diario",
    "cantidad": document.getElementById("tflujo_diario").value,
    "color": am4core.color("#f3f702")
}]

// Add and configure Series
var pieSeries1 = chart.series.push(new am4charts.PieSeries());
pieSeries1.dataFields.value = "cantidad";
pieSeries1.dataFields.category = "tipo";

// Let's cut a hole in our Pie chart the size of 40% the radius
chart.innerRadius = am4core.percent(40);

// Put a thick white border around each Slice
pieSeries1.slices.template.stroke = am4core.color("#4a2abb");
pieSeries1.slices.template.strokeWidth = 2;
pieSeries1.slices.template.strokeOpacity = 1;
pieSeries1.slices.template.propertyFields.fill = "color";

// Add a legend
chart.legend = new am4charts.Legend();

am4core.useTheme(am4themes_animated);

// Apply chart themes
am4core.useTheme(am4themes_kelly);

// Create chart instance
var chartxy = am4core.create("chartdivXY", am4charts.XYChart3D);

// Add data
chartxy.data = [ {
  "rol": "Gerente",
  "cantidad": document.getElementById("urol_gerente").value,
  "color": am4core.color("#eb0909")
}, {
  "rol": "Funcionario",
  "cantidad": document.getElementById("urol_funcionario").value,
  "color": am4core.color("#4634eb")
}, {
  "rol": "Cliente",
  "cantidad": document.getElementById("urol_cliente").value,
  "color": am4core.color("#0acc47")
}, {
  "rol": "Diseñador de procesos",
  "cantidad": document.getElementById("urol_disenador").value,
  "color": am4core.color("#f6ff00")
}];




// Create axes
var categoryAxis = chartxy.xAxes.push(new am4charts.CategoryAxis());
categoryAxis.dataFields.category = "rol";
categoryAxis.title.text = "Rol";

var  valueAxis = chartxy.yAxes.push(new am4charts.ValueAxis());
valueAxis.title.text = "Cantidad de Usuarios";

// Create series
var series = chartxy.series.push(new am4charts.ColumnSeries3D());
series.dataFields.valueY = "cantidad";
series.dataFields.categoryX = "rol";
series.name = "Cantidad de Usuarios";
series.tooltipText = "{name}: [bold]{valueY}[/]";
series.columns.template.propertyFields.fill = "color"

chartxy.cursor = new am4charts.XYCursor();