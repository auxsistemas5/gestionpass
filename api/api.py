def RestFullApi(app, db, jsonify):
    
    @app.route('/api/v1/gestionpass/getAllCases', methods=["GET"])
    def getAllCases():
        query = db.connection.cursor()
        query.execute('SELECT id, asignado_a,fecha_reporte,fecha_ocurrencia,funcionario_reporta, cargo_funcionario, sitio_evento,sd_reporte FROM casos order by id ASC')
        casos = query.fetchall()
        query.close()
        
        casos_list = [{'id': data[0], 'asignado': data[1],'reporte':data[2], 'ocurrencia': data[3],'funcionario': data[4],'cargo': data[5],'sitioEvento': data[6],'sitioReporte': data[7]} for data in casos]

        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getCaseById/<id>', methods=["GET"])
    def getCaseById(id):
        query = db.connection.cursor()
        query.execute('SELECT id, asignado_a,fecha_reporte,fecha_ocurrencia,funcionario_reporta, cargo_funcionario, sitio_evento,sd_reporte FROM casos where id = %s', (id,))
        casos = query.fetchall()
        query.close()
        
        casos_list = [{'id': data[0], 'asignado': data[1],'reporte':data[2], 'ocurrencia': data[3],'funcionario': data[4],'cargo': data[5],'sitioEvento': data[6],'sitioReporte': data[7]} for data in casos]

        return jsonify(casos_list)