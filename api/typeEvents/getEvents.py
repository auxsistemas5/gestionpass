def httpGetEvents(app,jsonify,db):
    @app.route('/api/v1/gestionpass/getAllTypeEvents', methods=["GET"])
    def getAllTypeEvents():
        query = db.connection.cursor()
        query.execute('SELECT id,nombre_evento FROM tipo_evento')
        evento = query.fetchall()
        query.close()
        eventos_list = [{'id': data[0], 'nombre': data[1]} for data in evento]
        return jsonify(eventos_list)
    
    @app.route('/api/v1/gestionpass/getAllTypeEventsFormat', methods=["GET"])
    def getAllTypeEventsFormat():
        query = db.connection.cursor()
        query.execute('SELECT id,nombre_evento FROM tipo_evento')
        eventos = query.fetchall()
        query.close()
        return jsonify(eventos)