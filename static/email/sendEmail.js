$(document).ready(()=>{
    
    $('#sendEmail').click(()=>{
        
        var remitente = $('#remitenteEmail').val();
        var asunto = $('#asuntoEmail').val();
        var mensaje = $('#mensajeEmail').val();
        var adjunto = $('#adjunto')[0].files[0];

        if(remitente != "" && mensaje != " "){
            var formData = new FormData();

            formData.append('receiver_email', remitente);
            formData.append('asunto', asunto);
            formData.append('mensaje', mensaje);
            formData.append('adjunto', adjunto);
            
            $.ajax({
                type: "POST",
                url: "http://10.0.255.243:8002/gestionpass/email/send_email",
                data: formData,
                contentType: false,
                processData: false,
                success: function (response) {
                    $('.toastMessage').html('Correo enviado con exito!');
                    $('.toast').css({
                        'background-color': 'green',
                        'color': '#fff'
                    });
                    $('.toast').toast('show');
                },
                error: function (error){
                    $('.toastMessage').html('Problemas al enviar correo intente nuevamente!');
                    $('.toast').css({
                        'background-color': 'orange',
                        'color': '#fff'
                    });
                    $('.toast').toast('show');
                }
            });
        }else{
            $('.toastMessage').html('Error al enviar correo contacte a T.I');
            $('.toast').css({
                'background-color': 'red',
                'color': '#fff'
            });
            $('.toast').toast('show');
        }
    })

});