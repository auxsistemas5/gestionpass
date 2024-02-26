
def httpGetAnalisis(app,jsonify,db):
    
    @app.route('/api/v1/gestionpass/analisis/getAnalisisById/<int:id>', methods=["GET"])
    def getAnalisisById(id):
        query = db.connection.cursor()
        query.execute('SELECT req_analisis,descartado FROM casos WHERE id = %s', (id,))
        caso = query.fetchone()
        
        
        if caso:
            if caso[0] == "1":
                query.execute('SELECT id_caso,eval_hechos,acc_ins,fac_in_paciente,fac_contributivos,opor_mejora,condicion,clasificacion,severidad,barrera_seguridad,tipo_evento,asegurador FROM analisis WHERE id_caso = %s', (id,))
                analisis = query.fetchone()
                if analisis:
                    list_analisis = [analisis[0],analisis[1],analisis[2],analisis[3],analisis[4],analisis[5],analisis[6],analisis[7],analisis[8],analisis[9],analisis[10],analisis[11]]
                    return jsonify({'estado': 'con analisis','analisis': list_analisis})
                else:
                    return jsonify({'estado': 'sin analisis'})
                    
            elif caso[0] == "0":
                return jsonify({'estado': 'no requiere analisis'}) 
        else:
            return jsonify({'estado': 'id no encontrado'}), 404
        
        query.close()
        
    @app.route('/api/v1/gestionpass/analisis/getAseguradoras', methods=["GET"])
    def getAseguradoras():
        query = db.connection.cursor()
        query.execute('SELECT nombreAseguradora FROM aseguradoras')
        aseguradoras = query.fetchall()
        
        if aseguradoras:
            return jsonify(aseguradoras)
        else:
            return jsonify({'message': 'error'})