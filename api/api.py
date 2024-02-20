from werkzeug.security import generate_password_hash
from api.casos.getCasos import httpGetCasos
from api.casos.putCasos import httpPutCases
from api.usuarios.getUsuarios import httpGetUsuarios
from api.usuarios.postUsuarios import httpPostUsuarios
from api.usuarios.putUsuarios import httpPutUsuarios

def RestFullApi(app, db, jsonify,request):
    
    httpGetCasos(app,jsonify,db)
    httpPutCases(app,jsonify,db,request)
    
    httpGetUsuarios(app,jsonify,db)
    httpPostUsuarios(app,jsonify,db,request,generate_password_hash)
    httpPutUsuarios(app,jsonify,db,request,generate_password_hash)
    
        
    