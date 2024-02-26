$(document).ready(function () {
    var area = $('#userType').val();

    if ($.fn.DataTable.isDataTable('#casos_area')) {
        $('#casos_area').DataTable().destroy();
    }
    $('#casos_area').DataTable({
        ajax: {
            url: 'http://10.0.19.162:8002/api/v1/gestionpass/getAllCasesByArea/'+area,
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
                    return `<button data-id=${row.id} id="miCasoVer" class="btn btn-info btn-sm"><i class="bi bi-eye-fill"></i></button>
                    <button data-id=${row.id} id="miCasoRol" class="btn btn-success btn-sm"><i class="bi bi-x-diamond-fill"></i></button>`;
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
            url: "http://10.0.19.162:8002/api/v1/gestionpass/getAllCaseById/"+id,
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
                response[31] == 1? $('#incidente').html('<p>SI</p>'): $('#incidente').html('<p>NO</p>');
                   
                
            }
        });
        
    });
    $('#casos_area').on('click','#miCasoRol', function(){
        var id = $(this).data('id');
        $('#modalAnalisisCaso').modal('show')
        $('.analisisCaso').hide();
        var area = $('#clasificacionArea').val();
        if (area === "SEGURIDAD DEL PACIENTE"){

            $.ajax({
                type: "GET",
                url: "http://10.0.19.162:8002/api/v1/gestionpass/analisis/getAnalisisById/"+id,
                success: function (response) {
                    if(response.estado === "no requiere analisis"){
                        $('#mensajeRespuesta').html('<p>EL CASO ESTA DEFINIDO COMO ACCIÓN  INSEGURA QUE NO REQUIERE ANALISIS O ESTA DESCARTADO, SI DESEA REALIZAR UN ANALISIS POR FAVOR VAYA A LA EDICIÓN DEL CASO Y CAMBIE LA OPCIÓN PARA PODER GENERAR O VER EL ANALISIS</p>'); 
                        $('#mensajeRespuesta').show();
                       $('.analisisCaso').hide();
                    }
                    if(response.estado === "con analisis"){
                        
                        $('.analisisCaso').show();
                        $('#mensajeRespuesta').hide();
                        $('#crearNuevoAnalisis').hide();
                        $('#actualizarAnalisis').show();
                        $("#eventoTipo").hide();
                        $('#hechos').val(response.analisis[1]);
                        $('#barrera').val(response.analisis[9]);
                        $('#inseguras').val(response.analisis[2]);
                        $('#inherentes').val(response.analisis[3]);
                        $('#contributivos').val(response.analisis[4]);
                        $('#mejora').val(response.analisis[5]);
                        $('#condicion').val(response.analisis[6]);
                        $('#clasificacion').val(response.analisis[7]);
                        $('#severidad').val(response.analisis[8]);
                        
                        $('#aseguradoras').val(response.analisis[11]);
                        fetch("http://10.0.19.162:8002/api/v1/gestionpass/analisis/getAseguradoras")
                        .then(response => response.json())
                        .then(data => {
                            // Iterar sobre las opciones y agregarlas al select
                            data.forEach(opcion => {
                                var option = document.createElement("option");
                                option.value = opcion[0];
                                option.text = opcion[0];
                                
                                $("#aseguradoras").append(option);
                            });
                        });
                        $('#crearNuevoAnalisis').hide();
                        fetch("http://10.0.19.162:8002/api/v1/gestionpass/getAllTypeEventsFormat")
                        .then(response => response.json())
                        .then(data => {
                            // Iterar sobre las opciones y agregarlas al select
                            data.forEach(opcion => {
                                var option = document.createElement("option");
                                option.value = opcion[0];
                                option.text = opcion[1];
                                
                                $("#tipoEventoCaso").append(option);
                            });
                            $("#tipoEventoCaso").val(response[10]);
                        });
                        
                        if($('#clasificacion').val() == "EVENTO ADVERSO"){
                            $("#eventoTipo").show();
                        }else{
                            $("#eventoTipo").hide();
                            $("#tipoEventoCaso").val(0);
                        }

                        $('#clasificacion').change(function () { 
                            if($('#clasificacion').val() === "EVENTO ADVERSO"){
                                $("#eventoTipo").show();
                            }else{
                                $("#eventoTipo").hide();
                            }
                            
                        });
                        
                        
                        
                    }
                    if(response.estado === "sin analisis"){
                        $('.analisisCaso').show();
                        $('#mensajeRespuesta').html('<p>CASO SIN ANALISIS DE SEGURIDAD DEL PACIENTE</p>');
                        $('#mensajeRespuesta').show();

                        $('#hechos').val('');
                        $('#barrera').val('');
                        $('#inseguras').val('');
                        $('#inherentes').val('');
                        $('#contributivos').val('');
                        $('#mejora').val('');
                        $('#condicion').val('');
                        $('#clasificacion').val('');
                        $('#severidad').val('');
                        $('#tipoEventoCaso').val('');
                        $('#aseguradoras').val('');

                        $('#crearNuevoAnalisis').show();
                        $('#actualizarAnalisis').hide();

                        $('#crearAnalisis').click(()=>{
                            FormData={
                                id: id,
                                hechos : $('#hechos').val(),
                                barrera: $('#barrera').val(),
                                inseguras: $('#inseguras').val(),
                                inherentes : $('#inherentes').val(),
                                contributivos: $('#contributivos').val(),
                                mejora: $('#mejora').val(),
                                condicion: $('#condicion').val(),
                                clasificacion: $('#clasificacion').val(),
                                severidad: $('#severidad').val(),
                                tipoEvento: $('#tipoEventoCaso').val(),
                                aseguradoras: $('#aseguradoras').val()
                            }

                            $.ajax({
                                type: "POST",
                                url: "http://10.0.19.162:8002/api/v1/gestionpass/analisis/addAnalisis",
                                data: FormData,
                                dataType: "json",
                                success: function (response) {
                                    console.log(response);
                                    $('#casos_area').DataTable().ajax.reload();
                                    $('#modalAnalisisCaso').modal('hide')
                                }
                            });
                        });
                    }
                    $('#actualizarAnalisis').click(()=>{
                        FormData = {
                            id: id,
                            hechos : $('#hechos').val(),
                            barrera: $('#barrera').val(),
                            inseguras: $('#inseguras').val(),
                            inherentes : $('#inherentes').val(),
                            contributivos: $('#contributivos').val(),
                            mejora: $('#mejora').val(),
                            condicion: $('#condicion').val(),
                            clasificacion: $('#clasificacion').val(),
                            severidad: $('#severidad').val(),
                            tipoEvento: $('#tipoEventoCaso').val(),
                            aseguradoras: $('#aseguradoras').val()
                            
                        }
                        $.ajax({
                            type: "POST",
                            url: "http://10.0.19.162:8002/api/v1/gestionpass/analisis/updateAnalisis",
                            data: FormData,
                            dataType: "json",
                            success: function (response) {
                                if(response.message === "success"){
                                    $('.toastMessage').html('Analisis Actualizado con exito!');
                                    $('.toast').css({
                                        'background-color': 'green',
                                        'color': '#fff'
                                    });
                                    
                                    $('#casos_area').DataTable().ajax.reload();
                                    $('#modalAnalisisCaso').modal('hide')
                                }
                            },
                            error: function(error){
                                $('#modalAnalisisCaso').modal('hide')
                                $('.toastMessage').html('No se pudo actualizar comuniquese con T.I');
                                $('.toast').css({
                                    'background-color': 'red',
                                    'color': '#fff'
                                });
                                
                            }
                        });
                        $('.toast').toast('show');
                    });
                }
            });
        }
    });
});