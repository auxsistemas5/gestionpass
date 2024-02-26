def httpPostTypeEvents(app,jsonify,db,request):
    @app.route('/api/v1/gestionpass/addNewTypeEvent', methods=["POST"])
    def addNewTypeEvent():
        if request.method == "POST":
            nombre = request.form['namevent']
            query = db.connection.cursor()
            try:
                query.execute('INSERT INTO tipo_evento(nombre_evento) VALUES(%s)',(nombre,))
                db.connection.commit()
                query.close()
                return jsonify({'message': 'success'}),200
            except Exception as e:
                query.close()
                return jsonify({'message': 'error','error': e}),400