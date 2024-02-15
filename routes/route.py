from routes.manageUsers.manage import autenticacionUsuario
from routes.excelGenerate.generateExcel import generateExcel
from routes.home.home import viewHome
from routes.email.generateEmail import emailGenerate

def routes(app,render_template, db,pd,send_file,request,jsonify, redirect,url_for,session):
    
    @app.route('/', methods=["GET"])
    def index():
        if "username" in session:
            return redirect(url_for("home"))
            
        return redirect(url_for("login"))
    
   
    viewHome(app,session,redirect,url_for,render_template)
    
    autenticacionUsuario(app,render_template,request,jsonify,db,redirect,url_for,session)
    
    generateExcel(app,db,pd,send_file)
    
    emailGenerate(app,request,render_template,jsonify)