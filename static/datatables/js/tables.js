$(document).ready(()=>{
    $('#table_case').on('click','#caso-detalles', function(){
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

                    var nuevaCadena = response[14].substring(3);
                    var imagenSerialize = 'static/'+nuevaCadena
                    $('#evidenciaCaso').html(`<img src="${imagenSerialize}">`);
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
    
    if ($.fn.DataTable.isDataTable('#table_case')) {
        $('#table_case').DataTable().destroy();
    }
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
                    return `<button data-id=${row.id} id="caso-editar" class="btn btn-info btn-sm "><i class="bi bi-pencil-fill"></i></button> <button id="caso-detalles" data-id=${row.id} class="btn btn-success btn-sm "><i class="bi bi-eye-fill"></i></button>`;
                }
            }
            
        ],
        createdRow: function(row, data,dataIndex){
            if(!data.asignado){
                $(row).find('td:eq(1)').css('background-color', 'orange');
                data.asignado = 'SIN ASIGNAR';
            }
        }
    });
    $('#table_case').on('click','#caso-editar', function(){
        
        var id = $(this).data('id');
        $('#modalEditarCasoUsuario').modal('show');
        $('#nueva_fecha').hide();
        $('#datosUsuarioSeleccionado').hide();
        setTimeout(()=>{
                    
            $('#loaderSpiner').hide();
            $('#datosUsuarioSeleccionado').show();
        },2000)
        $.ajax({
            type: "GET",
            url: "http://10.0.255.243:8002/api/v1/gestionpass/getAllCaseById/"+id,
            success: function (response) {
                
                $('#datosUsuarioSeleccionado').hide();
                setTimeout(()=>{
                    
                    $('#loaderSpiner').hide();
                    $('#datosUsuarioSeleccionado').show();
                },2000)
                $('#editarFechaReporte').val(response[1]);
                $('#editarFechaOcurrencia').val(response[2]);
                $('#editarFuncionario').val(response[3]);
                $('#editarCargo').val(response[4]);
                $('#editarDocumento').val(response[5]);
                $('#editarNombrePaciente').val(response[6]);
                $('#editarApellido').val(response[7]);
                $('#editarDescripcion').val(response[8]);
                $('#editarSitioEvento').val(response[9]);
                $('#editarSitioReporte').val(response[10]);
                $('#editarSerie').val(response[11]);
                $('#editarMarca').val(response[12]);
                $('#editarLote').val(response[13]);
                $('#editarAnalisis').val(response[30]);
                $('#editarDescarte').val(response[29]);
                $('#editarAsignado').val(response[28]);
                $('#editarEvento').val(response[15]);
                $('#editarPeso').val(response[16]);
                $('#editarEdad').val(response[17]);
                $('#editarGenero').val(response[18]);

                $('#editarSospechoso').val(response[19]);
                $('#editarConcomitante').val(response[20]);
                $('#editarAdministracion').val(response[21]);
                $('#editarInicio').val(response[22]);
                $('#editarDosis').val(response[23]);
                $('#editarFrecuencia').val(response[24]);
                $('#editarSuspendio').val(response[25]);
                $('#editarDiagnostico').val(response[26]);
                $('#editarEvolucion').val(response[27]);
                $('#buttonActualizar').html(`<button type="button" data-id="${id}" id="botonActualizarCaso" class="form-control btn btn-warning"><b>ACTUALIZAR</b></button>`)
                  
                $('#botonActualizarCaso').click(function() {
                    var id = $(this).data('id');
                    FormData = {
                        id: id,
                        funcionario: $('#editarFuncionario').val(),
                        cargo: $('#editarCargo').val(),
                        documento : $('#editarDocumento').val(),
                        nombrePaciente : $('#editarNombrePaciente').val(),
                        apellidoPaciente : $('#editarApellido').val(),
                        descripcion : $('#editarDescripcion').val(),
                        sitioEvento : $('#editarSitioEvento').val(),
                        sitioReporte : $('#editarSitioReporte').val(),
                        serie : $('#editarSerie').val(),
                        marca : $('#editarMarca').val(),
                        lote : $('#editarLote').val(),
                        analisis : $('#editarAnalisis').val(),
                        descarte : $('#editarDescarte').val(),
                        asignado: $('#editarAsignado').val(),
                        evento: $('#editarEvento').val(),
                        peso: $('#editarPeso').val(),
                        edad: $('#editarEdad').val(),
                        genero: $('#editarGenero').val(),
                        sospechoso: $('#editarSospechoso').val(),
                        concomitante: $('#editarConcomitante').val(),
                        administracion: $('#editarAdministracion').val(),
                        inicio: $('#editarInicio').val(),
                        dosis: $('#editarDosis').val(),
                        frecuencia: $('#editarFrecuencia').val(),
                        suspendido: $('#editarSuspendio').val(),
                        diagnostico:  $('#editarDiagnostico').val(),
                        evolucion: $('#editarEvolucion').val()
                    }
                    $.ajax({
                        type: "POST",
                        url: "http://10.0.255.243:8002/api/v1/gestionpass/cases/updateCaseById/"+id,
                        data: FormData,
                        dataType: "json",
                        success: function (response) {
                            
                            if(response.message == "success"){
                                $('.toastMessage').html('Caso actualizado con exito');
                                $('.toast').css({
                                    'background-color': 'green',
                                    'color': '#fff'
                                });
                                $('#modalEditarCasoUsuario').modal('hide');
                                $('#table_case').DataTable().ajax.reload();
                            }
                            if(response.message == "error"){
                                $('.toastMessage').html('No se pudo actualizar los datos');
                                $('.toast').css({
                                    'background-color': 'orange',
                                    'color': '#fff'
                                });
                                $('#modalEditarCasoUsuario').modal('hide');
                            }
                        },
                        error: function(error){
                            $('.toastMessage').html('Error al intentar actualizar comuniquese con T.I');
                            $('.toast').css({
                                'background-color': 'red',
                                'color': '#fff'
                            });
                            $('#modalEditarCasoUsuario').modal('hide');
                        }
                        
                    });
                    $('.toast').toast('show');
                });
                
            }
        });
        
        
    });
    

    
});

