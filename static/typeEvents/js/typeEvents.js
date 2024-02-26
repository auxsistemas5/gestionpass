$(document).ready(function () {
    if ($.fn.DataTable.isDataTable('#table_typeEvent')) {
        $('#table_typeEvent').DataTable().destroy();
    }
    //crea la tabla de usuarios con los datos devueltos de la api
    $('#table_typeEvent').DataTable({
        ajax: {
            url: 'http://10.0.19.162:8002/api/v1/gestionpass/getAllTypeEvents',
            dataSrc: ''
        },
        columns: [
            {data: 'id'},
            { data: 'nombre'},
            {
                // Personalizar la última columna
                targets: -1,
                render: function(data, type, row, meta) {
                    // genera los botones para el manejo de los datos del usuario y el cambio de contraseña
                    return `
                    <button data-id=${row.id} id="" class="btn btn-info btn-sm ">EN MANTENIMIENTO</button>`
                }
            }
            
        ]
    });
    $('#newEventButton').click(function() { 
        $('#modalNewTypeEvent').modal('show');
        
    });
    $('#addNewTypeEvent').click(()=>{
        
        if($('#nameEvent').val() !== ""){
            FormData = {namevent: $('#nameEvent').val()}
            $.ajax({
                type: "POST",
                url: "http://10.0.19.162:8002/api/v1/gestionpass/addNewTypeEvent",
                data: FormData,
                dataType: "json",
                success: function (response) {
                    if(response.message == "success"){
                        $('.toastMessage').html('Tipo evento creado con Exito!');
                        $('.toast').css({
                            'background-color': 'green',
                            'color': '#fff'
                        });
                        $('#table_typeEvent').DataTable().ajax.reload();
                    }else{
                        $('.toastMessage').html('Tipo evento no creado intentelo de nuevo');
                        $('.toast').css({
                            'background-color': 'orange',
                            'color': '#fff'
                        });
                    }
                    
                    //console.log(response);
                },
                error: function(error){
                    $('.toastMessage').html('No se pudo realizar la accion comuniquese con T-I');
                    $('.toast').css({
                        'background-color': 'orange',
                        'color': '#fff'
                    });
                    console.log(error);
                }
            });
            $('.toast').toast('show');
        }else{
            console.log('error');
        }
    });
});