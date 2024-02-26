$(document).ready(() => {
    $('#sendEmail').click(() => {
        var remitente = $('#remitenteEmail').val();
        var asunto = $('#asuntoEmail').val();
        var mensaje = $('#mensajeEmail').val().trim(); // Utilizar trim() para eliminar espacios en blanco
        var adjunto = $('#adjunto')[0].files;

        if (remitente != "" && mensaje != "") {
            var formData = new FormData();

            formData.append('receiver_email', remitente);
            formData.append('asunto', asunto);
            formData.append('mensaje', mensaje);
            for (var i = 0; i < adjunto.length; i++) {
                formData.append('adjunto[]', adjunto[i]); // Agregar cada archivo a la lista de adjuntos
            }
            
            $.ajax({
                type: "POST",
                url: "http://10.0.19.162:8002/gestionpass/email/send_email",
                data: formData,
                contentType: false,
                processData: false,
                success: function (response) {
                    //console.log(response);
                    $('.toastMessage').html('Correo enviado con éxito!');
                    $('.toast').css({
                        'background-color': 'green',
                        'color': '#fff'
                    });
                    $('.toast').toast('show');
                },
                error: function (error){
                    $('.toastMessage').html('Problemas al enviar correo. Intente nuevamente.');
                    $('.toast').css({
                        'background-color': 'orange',
                        'color': '#fff'
                    });
                    $('.toast').toast('show');
                    //console.log(error);
                }
            });
        } else {
            $('.toastMessage').html('Error al enviar correo. Por favor, complete todos los campos.');
            $('.toast').css({
                'background-color': 'red',
                'color': '#fff'
            });
            $('.toast').toast('show');
        }
    });
});
