$(document).ready(function () {
    var area = $('#userType').val();

    if ($.fn.DataTable.isDataTable('#casos_area')) {
        $('#casos_area').DataTable().destroy();
    }
    $('#casos_area').DataTable({
        ajax: {
            url: 'http://10.0.255.243:8002/api/v1/gestionpass/getAllCasesByArea/'+area,
            dataSrc: ''
        },
        columns: [
            {data: 'id'},
            { data: 'reporte'},
            {data: 'ocurrencia'},
            { data: 'sitioEvento' },
            { data: 'sitioReporte' },
            {
                // Personalizar la última columna
                targets: -1,
                render: function(data, type, row, meta) {
                    // Aquí puedes devolver el HTML para el botón
                    return `<button data-id=${row.id} id="miCasoVer" class="btn btn-info btn-sm"><i class="bi bi-eye-fill"></i></button>`;
                }
            }
            
        ]
    });

    $('#casos_area').on('click','#miCasoVer', function(){
        var id = $(this).data('id');
        $('#loaderSpiner').show();
        $('#modalDetallesCaso').modal('show');
        $.ajax({
            type: "GET",
            url: "http://10.0.255.243:8002/api/v1/gestionpass/getAllCaseById/"+id,
            success: function (response) {
                $('#datosUsuarioSeleccionado').hide();
                setTimeout(()=>{
                    
                    $('#loaderSpiner').hide();
                    $('#datosUsuarioSeleccionado').show();
                },2000)
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
                response[11] != ""? $('#serie').html(response[11]): $('#serie').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[12] != ""? $('#marca').html(response[12]): $('#marca').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[13] != ""? $('#lote').html(response[13]): $('#lote').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                if(response[14] == ""){
                    $('#evidenciaCaso').html('<h4><span class="badge bg-info">SIN EVIDENCIA QUE MOSTRAR</span></h4>');
                }else{
                    $('#evidenciaCaso').html(`<img src="${response[14]}">`);
                }
        
                response[15] != ""? $('#tipoEvento').html(response[15]): $('#tipoEvento').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');

                response[16] != ""? $('#pesoPaciente').html(response[16]): $('#pesoPaciente').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[17] != ""? $('#edadPaciente').html(response[17]): $('#edadPaciente').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[18] != ""? $('#generoPaciente').html(response[18]): $('#generoPaciente').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');

                response[19] != ""? $('#meSospechoso').html(response[19]): $('#meSospechoso').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[20] != ""? $('#meConcominante').html(response[20]): $('#meConcominante').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[21] != ""? $('#viaAdministracion').html(response[21]): $('#viaAdministracion').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');

                response[22] != ""? $('#fechaInicio').html(response[22]): $('#fechaInicio').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[23] != ""? $('#dosis').html(response[23]): $('#dosis').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[24] != ""? $('#fecAdministracion').html(response[24]): $('#fecAdministracion').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[25] != ""? $('#suspendido').html(response[25]): $('#suspendido').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[26] != ""? $('#diagnostico').html(response[26]): $('#diagnostico').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');
                response[27] != ""? $('#informacion').html(response[27]): $('#informacion').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');   
                response[28] != ""? $('#asignado').html(response[28]): $('#asignado').html('<span class="badge bg-warning">NO ESPECIFICADO</span>');   
                response[29] == 1? $('#descartado').html('<p>SI</p>'): $('#descartado').html('<p>NO</p>');   
                response[30] == 1? $('#analisis').html('<p>SI</p>'): $('#analisis').html('<p>NO</p>');   
                
            }
        });
        
    });
});