import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def emailGenerate(app,request,render_template,jsonify):
    @app.route('/gestionpass/email', methods=['GET'])
    def email():
        return render_template('email/sendEmail.html')
    
    @app.route('/gestionpass/email/send_email', methods=['POST'])
    def send_email():
        # Obtener los datos del formulario
        email_envia = "auxsistemas5@hmfs.gov.co"
        email_recibe = request.form['receiver_email']
        Asunto = request.form['asunto']
        mensaje = request.form['mensaje']
        password = "Estiverd@99" # La contraseña de la cuenta de correo electrónico remitente
        archivo_adjunto = request.files.get('adjunto')
        

        ## Configurar el mensaje de correo
        msg = MIMEMultipart()
        msg['From'] = email_envia
        msg['To'] = email_recibe
        msg['Subject'] = Asunto
        #
        # Agregar el cuerpo del mensaje
        msg.attach(MIMEText(mensaje, 'plain'))
        
        if archivo_adjunto:
            filename = archivo_adjunto.filename
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(archivo_adjunto.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename= {filename}')
            msg.attach(attachment)

        # Establecer la conexión SMTP con el servidor de Outlook
        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.starttls()  # Iniciar conexión segura
            server.login(email_envia, password)  # Iniciar sesión en la cuenta de correo electrónico remitente
            server.sendmail(email_envia, email_recibe, msg.as_string())  # Enviar el correo electrónico

        
        return jsonify({'message': 'enviado con exito'})