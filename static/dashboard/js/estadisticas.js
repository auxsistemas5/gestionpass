$(document).ready(()=>{
    var charFilter;
    $('#viewCharFilter').click(()=>{
        var area = $('#selectFilterArea').val();
        var year = $('#selectFilterYear').val();
        console.log('click');
        $.ajax({
            type: "GET",
            url: "http://10.0.255.243:8002/api/v1/gestionpass/getAllCasesforYearAndArea/"+year+"/"+area,
            success: function (response) {
                //console.log(response);
                if(charFilter){
                    charFilter.destroy();
                }
                if ($('#barChart').length > 0) {
                    // Elemento existe, puedes crear el gráfico
                    
                    charFilter = new Chart(document.querySelector('#barChart'), {
                        type: 'bar',
                        data: {
                        labels: ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
                        datasets: [{
                            label: 'CASOS MES',
                            data: [response[0].ENERO, response[0].FEBRERO,response[0].MARZO,response[0].ABRIL,response[0].MAYO,response[0].JUNIO,response[0].JULIO,response[0].AGOSTO,response[0].SEPTIEMBRE,response[0].OCTUBRE,response[0].NOVIEMBRE,response[0].DICIEMBRE],
                            backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(255, 159, 64, 0.2)',
                            'rgba(255, 205, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(201, 203, 207, 0.2)',
                            'rgba(128, 128, 0, 0.2)',
                            'rgba(255, 0, 255, 0.2)',
                            'rgba(255, 255, 0, 0.2)',
                            'rgba(0, 128, 0, 0.2)',
                            'rgba(0, 128, 128, 0.2)'
                            ],
                            borderColor: [
                            'rgb(255, 99, 132)',
                            'rgb(255, 159, 64)',
                            'rgb(255, 205, 86)',
                            'rgb(75, 192, 192)',
                            'rgb(54, 162, 235)',
                            'rgb(153, 102, 255)',
                            'rgb(201, 203, 207)',
                            'rgb(128, 128, 0)',
                            'rgb(255, 0, 255)',
                            'rgb(255, 255, 0)',
                            'rgb(0, 128, 0)',
                            'rgb(0, 128, 128)'
                            ],
                            borderWidth: 1
                        }]
                        },
                        options: {
                        scales: {
                            y: {
                            beginAtZero: true
                            }
                        }
                        }
                    });
                } else {
                    console.error('El elemento #barChart no existe en el DOM.');
                }
                
                
            }
        });
    });

    $.ajax({
        type: "GET",
        url: "http://10.0.255.243:8002/api/v1/gestionpass/getAllCasesforStadistics",
        success: function (response) {
            if(response.length > 0){
                if ($('#pieChart').length > 0) {
                    // Elemento existe, puedes crear el gráfico
                    new Chart(document.querySelector('#pieChart'), {
                        type: 'pie',
                        data: {
                            labels: [
                            'BIOMEDICOS',
                            'EPIDEMIOLOGÍA',
                            'FARMACOVIGILANCIA',
                            'FARMACOVIGILANCIA NIQUIA',
                            'SEGURIDAD DEL PACIENTE'
                            ],
                            datasets: [{
                                data: [response[0].BIOMEDICOS, response[0].EPIDEMIOLOGÍA, response[0].FARMACOAT,response[0].FARMACONQ,response[0].SEGURIDAD],
                                backgroundColor: [
                                    '#39DD28 ',
                                    '#DAF7A6',
                                    '#FFC300',
                                    '#FF5733',
                                    '#6495ED'
                                ],
                                hoverOffset: 4
                            }]
                        }
                    });
                } 
                
            }
        }
    });
    $.ajax({
        type: "GET",
        url: "http://10.0.255.243:8002/api/v1/gestionpass/getAllCasesforMonthActually",
        success: function (response) {
            if ($('#doughnutChart').length > 0) {
                // Elemento existe, puedes crear el gráfico
                new Chart(document.querySelector('#doughnutChart'), {
                    type: 'doughnut',
                    data: {
                        labels: [
                            'BIOMEDICOS',
                            'EPIDEMIOLOGÍA',
                            'FARMACOVIGILANCIA',
                            'FARMACOVIGILANCIA NIQUIA',
                            'SEGURIDAD DEL PACIENTE'
                        ],
                        datasets: [{
                        
                        data: [response[0].BIOMEDICOS, response[0].EPIDEMIOLOGÍA, response[0].FARMACOAT,response[0].FARMACONQ,response[0].SEGURIDAD],
                        backgroundColor: [
                            '#39DD28 ',
                            '#DAF7A6',
                            '#FFC300',
                            '#FF5733',
                            '#6495ED'
                        ],
                        hoverOffset: 4
                        }]
                    }
                });
            } 
        }
    });

    
});

