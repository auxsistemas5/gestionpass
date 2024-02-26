from routes.manageUsers.manage import autenticacionUsuario
from routes.excelGenerate.generateExcel import generateExcel
from routes.home.home import viewHome
from routes.email.generateEmail import emailGenerate
from routes.typeEvent.events import typeEvent

def routes(app,render_template, db,pd,send_file,request,jsonify, redirect,url_for,session):
    def getDayToday():
        from datetime import datetime

        # Obtener la fecha actual
        fecha_actual = datetime.now()

        # Formatear la fecha en 'yyyy-mm-dd'
        fecha_formateada = fecha_actual.strftime('%Y-%m-%d')
        query = db.connection.cursor()
        query.execute('SELECT count(*) FROM casos where fecha_reporte = %s',(fecha_formateada,))
        countCasos = query.fetchall()
        query.close()
        cuentaCasos = countCasos[0][0]
        print(cuentaCasos)
        return cuentaCasos
    
    @app.context_processor
    def inject_dato():
        return dict(dato=getDayToday())
        
    @app.route('/', methods=["GET"])
    def index():
        return render_template('index.html')
    
   
    viewHome(app,session,redirect,url_for,render_template)
    
    autenticacionUsuario(app,render_template,request,jsonify,db,redirect,url_for,session)
    
    generateExcel(app,db,pd,send_file)
    
    emailGenerate(app,request,render_template,jsonify)
    
    typeEvent(app,request,db,render_template,jsonify)