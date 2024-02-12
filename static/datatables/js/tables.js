$(document).ready(()=>{
    $('#table_case').on('click','#caso-detalles', function(){
        var id = $(this).data('id');
        $('#modalDetallesCaso').modal('show');
        $.ajax({
            type: "GET",
            url: "http://10.0.255.243:8002/api/v1/gestionpass/getAllCaseById/"+id,
            success: function (response) {
                $('#fechaReporte').html(response[1]);
                $('#fechaOcurrencia').html(response[2]);
                $('#funcionario').html(response[3]);
                $('#cargo').html(response[4]);
                $('#docPaciente').html(response[5]);
                $('#nomPaciente').html(response[6]);
                $('#apePaciente').html(response[7]);
                $('#descripcionEvento').html(response[8]);
                $('#servicioEvento').html(response[9]);
                $('#servicioReporte').html(response[10]);
                console.log(response);
            }
        });
        
    });
    $('#table_case').on('click','#caso-editar', function(){
        var id = $(this).data('id');
        console.log(id);
    });
    $('#table_case').DataTable({
        ajax: {
            url: 'http://10.0.255.243:8002/api/v1/gestionpass/getAllCases',
            dataSrc: ''
        },
        columns: [
            {data: 'id'},
            {data: 'asignado'},
            { data: 'reporte'},
            {data: 'ocurrencia'},
            {data: 'funcionario'},
            {data: 'cargo'},
            { data: 'sitioEvento' },
            { data: 'sitioReporte' },
            {
                // Personalizar la última columna
                targets: -1,
                render: function(data, type, row, meta) {
                    // Aquí puedes devolver el HTML para el botón
                    return `<button data-id=${row.id} id="caso-editar" class="btn btn-info btn-sm form-control">EDITAR</button> <button id="caso-detalles" data-id=${row.id} class="btn btn-success btn-sm form-control">VER</button>`;
                }
            }
            
        ]
    });
});

