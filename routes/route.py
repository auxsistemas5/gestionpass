from routes.manageUsers.manage import login, register
from routes.excelGenerate.generateExcel import generateExcel

def routes(app,render_template, db,pd,send_file):
    
    login(app,render_template)
    register(app, render_template)
    
    generateExcel(app,db,pd,send_file)