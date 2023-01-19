console.log("string")
var data = JSON.parse('{{ plot_data|safe }}');

Plotly.newPlot('myDiv',data);