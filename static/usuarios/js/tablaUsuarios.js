$(document).ready(function () {
    
    
    //valida que no haya una datatable inicializada si lo esta la destruye y la deja lista para inicializar
    if ($.fn.DataTable.isDataTable('#tabla-usuarios')) {
        $('#tabla-usuarios').DataTable().destroy();
    }
    //crea la tabla de usuarios con los datos devueltos de la api
    $('#tabla-usuarios').DataTable({
        ajax: {
            url: 'http://10.0.255.243:8002/api/v1/gestionpass/getAllUsers',
            dataSrc: ''
        },
        columns: [
            {data: 'id'},
            { data: 'nombre'},
            {data: 'usuario'},
            { data: 'rol' },
            { data: 'area' },
            {data: 'estado'},
            {
                // Personalizar la última columna
                targets: -1,
                render: function(data, type, row, meta) {
                    // genera los botones para el manejo de los datos del usuario y el cambio de contraseña
                    return `
                    <button data-id=${row.id} id="editarUsuarioContraseña" class="btn btn-info btn-sm "><i class="bi bi-key-fill"></i></button>
                    <button data-id=${row.id} id="editarUsuarioDatos" class="btn btn-warning btn-sm "><i class="ri-user-3-line"></i></button>`;
                }
            }
            
        ]
    });

    //despliega el modal para actualizar la contraseña
    $('#tabla-usuarios').on('click','#editarUsuarioContraseña', function(){
        var id = $(this).data('id');
        $('#modalEditarContraseña').modal('show');
        //al presionar el boton valida si no es vacio  
        $('#updatePassword').click(()=>{
            var contrasenaRestablecida = $('#contraseñaRest').val();
            //si esta vacio lanza la advertencia en el toast
            if(!contrasenaRestablecida){
                $('.toastMessage').html('El campo debe tener una contraseña valida');
                $('.toast').css({
                    'background-color': 'orange',
                    'color': '#fff'
                });
                //oculta el modal
                $('#modalEditarContraseña').modal('hide');
            }else{
                //al no estar vacio hace la peticion ajax put para actualizar la contraseña
                //recoge los datos para ser enviados atravez de ajax
                FormData = {user_id: id,contrasena : contrasenaRestablecida}
                $.ajax({
                    type: "POST",
                    url: "http://10.0.255.243:8002/api/v1/gestionpass/users/updatePassword",
                    data: FormData,
                    dataType: "json",
                    //devuelve el objeto response con exito o error y muestra el modal dependiendo del mensaje
                    success: function (response) {
                        if(response.message == "success"){
                            $('#contraseñaRest').val('');
                            $('#modalEditarContraseña').modal('hide');
                            $('.toastMessage').html('Contraseña actualizada con exito');
                            $('.toast').css({
                                'background-color': 'green',
                                'color': '#fff'
                            });
                        }
                        if(response.message == "error"){
                            $('#contraseñaRest').val('');
                            $('#modalEditarContraseña').modal('hide');
                            $('.toastMessage').html('No se actualizo valide nuevamente');
                            $('.toast').css({
                                'background-color': 'warning',
                                'color': '#fff'
                            });
                        }
                    },
                    error: function(error){
                        $('#modalEditarContraseña').modal('hide');
                        $('.toastMessage').html('No se pudo actualizar la contraseña comuniquese con T.I');
                        $('.toast').css({
                            'background-color': 'red',
                            'color': '#fff'
                        });
                        $('#contraseñaRest').val('');
                    }
                });
            }
            //muestra la notificacion en pantalla con el mensaje
            $('.toast').toast('show');
        });
    });
    $('#tabla-usuarios').on('click','#editarUsuarioDatos', function(){
        var id = $(this).data('id');
        $('#modalEditarUsuario').modal('show');

        $.ajax({
            type: "GET",
            url: "http://10.0.255.243:8002/api/v1/gestionpass/getUserById/"+id,
            success: function (response) {
                $('#editarNombre').val(response[0]);
                $('#editarUsuario').val(response[1]);
                $('#editarEstado').val(response[2]);
                $('#editarArea').val(response[3]);
                $('#editarEstado').val(response[4]);
            }
        });
        $('#actualizarDatosUsuarios').click(()=>{
            var nombre = $('#editarNombre').val();
            var usuario = $('#editarUsuario').val();
            var estado = $('#editarEstado').val();
            var rol = $('#editarRol').val();
            var area = $('#editarArea').val();

            if(!nombre|| !usuario ||!estado ||!rol || !area){
                $('.toastMessage').html('No pueden existir campos vacios');
                $('.toast').css({
                    'background-color': 'orange',
                    'color': '#fff'
                });
            }else{
                //console.log(id);
                FormData = {nombre:nombre,usuario:usuario,rol:rol,area: area,estado:estado}
                $.ajax({
                    type: "POST",
                    url: "http://10.0.255.243:8002/api/v1/gestionpass/users/updateDatesUser/"+id,
                    data: FormData,
                    dataType: "json",
                    success: function (response) {
                        if(response.message == "success"){
                            $('#tabla-usuarios').DataTable().ajax.reload();
                            $('.toastMessage').html('Usuario actualizado con exito');
                            $('.toast').css({
                                'background-color': 'green',
                                'color': '#fff'
                            });
                            $('#modalEditarUsuario').modal('hide');
                        }else{
                            $('.toastMessage').html('No Error al validar la actualizacion, valide de nuevo');
                            $('.toast').css({
                                'background-color': 'orange',
                                'color': '#fff'
                            });
                            $('#modalEditarUsuario').modal('hide');
                        }
                    },
                    error: function (error){
                        $('.toastMessage').html('No se pudo actualizar comuniquese con tecnología');
                        $('.toast').css({
                            'background-color': 'red',
                            'color': '#fff'
                        });
                        $('#modalEditarUsuario').modal('hide');
                    }
                });
            }
            $('.toast').toast('show');

        });
    });
    
    $('#crearNuevoUsuario').click(()=>{
        $('#modalCrearUsuario').modal('show');

        //despliega el modal para añadir un nuevo usuario al presionar el  boton
        $('#addNewUser').click(()=>{
            var nombre = $('#nuevoNombre').val();
            var usuario = $('#nuevoUsuario').val();
            var contrasena = $('#nuevoContraseña').val();
            var rol = $('#nuevoRol').val();
            var area = $('#nuevoArea').val();
            //valida que los campos no sena vacios, si lo son este genera el aviso en pantalla
            if(!nombre || !usuario || !contrasena || !rol || !area){
                $('.toastMessage').html('Revise los campos e intentelo de nuevo');
                $('.toast').css({
                    'background-color': 'orange',
                    'color': '#fff'
                });
                $('.toast').toast('show');
            }else{
                //al no ser vacio este recoge los datos json para enviarlo atravez de ajax
                FormData = {nombre : nombre,usuario: usuario,contrasena: contrasena,rol: rol, area: area}
                $.ajax({
                    type: "POST",
                    url: "http://10.0.255.243:8002/api/v1/gestionpass/users/addNewUser",
                    data: FormData,
                    dataType: "json",
                    //devuelve el mensaje segun la respuesta de la peticion
                    success: function (response) {
                        if(response.message = "success"){
                            $('.toastMessage').html('Usuario creado con exito!');
                            $('.toast').css({
                                'background-color': 'green',
                                'color': '#fff'
                            });
                            //reinicializa la tabla
                            $('#tabla-usuarios').DataTable().ajax.reload();
                            //console.log(response);
                            $('#nuevoNombre').val('');
                            $('#nuevoUsuario').val('');
                            $('#nuevoContraseña').val('');
                            $('#nuevoRol').val('');
                            $('#nuevoArea').val('');
                            $('#modalCrearUsuario').modal('hide');
                        }else{
                            $('.toastMessage').html('Error al guardar verifique o comuniquese con T.I');
                            $('.toast').css({
                                'background-color': 'red',
                                'color': '#fff'
                            });
                            //console.log(response);
                            $('#modalCrearUsuario').modal('hide');
                        }
                        $('.toast').toast('show');
                    }
                });
            }
        });
    });

});