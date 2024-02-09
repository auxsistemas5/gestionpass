$(document).ready(()=>{
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
                    return `<a href="edit_case.php?id=${row.id}" class="btn btn-info btn-sm form-control">EDITAR</a> <a href="case_details.php?id=${row.id}" class="btn btn-success btn-sm form-control">VER</a>`;
                }
            }
            
        ]
    });
});