from werkzeug.security import generate_password_hash
from api.casos.getCasos import httpGetCasos
from api.casos.putCasos import httpPutCases

from api.usuarios.getUsuarios import httpGetUsuarios
from api.usuarios.postUsuarios import httpPostUsuarios
from api.usuarios.putUsuarios import httpPutUsuarios

from api.analisis.getAnalisis import httpGetAnalisis
from api.analisis.postAnalisis import httpPostAnalisis
from api.analisis.putAnalisis import httpPutAnalisis

from api.farmacoanalisis.getFarmacoAnalisis import httpGetFarmacoAnalisis

from api.typeEvents.getEvents import httpGetEvents
from api.typeEvents.postTypeEvents import httpPostTypeEvents

def RestFullApi(app, db, jsonify,request,session):
    
    httpGetCasos(app,jsonify,db)
    httpPutCases(app,jsonify,db,request)
    
    httpGetUsuarios(app,jsonify,db)
    httpPostUsuarios(app,jsonify,db,request,generate_password_hash)
    httpPutUsuarios(app,jsonify,db,request,generate_password_hash)
    
    httpGetAnalisis(app,jsonify,db)
    httpPostAnalisis(app,jsonify,db,request)
    httpPutAnalisis(app,jsonify,db,request)
    
    httpGetFarmacoAnalisis(app,jsonify,db)
    
    httpGetEvents(app,jsonify,db)
    httpPostTypeEvents(app,jsonify,db,request)
    
        
    