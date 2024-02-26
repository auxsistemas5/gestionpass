
def httpPostAnalisis(app,jsonify,db,request):
    @app.route('/api/v1/gestionpass/analisis/addAnalisis', methods=["POST"])
    def addAnalisis():
        try:
            id = request.form['id']
            hechos = request.form['hechos']
            barrera = request.form['barrera']
            inseguras = request.form['inseguras']
            inherentes = request.form['inherentes']
            contributivos = request.form['contributivos']
            mejora = request.form['mejora']
            condicion = request.form['condicion']
            clasificacion = request.form['clasificacion']
            severidad = request.form['severidad']
            tipoEvento = request.form['tipoEvento']
            aseguradoras = request.form['aseguradoras']
            
            query = db.connection.cursor()
            query.execute('INSERT INTO analisis(id_caso,eval_hechos,acc_ins,fac_in_paciente,fac_contributivos,opor_mejora,condicion,clasificacion,severidad,barrera_seguridad,tipo_evento,asegurador) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (id,hechos,inseguras,inherentes,contributivos,mejora,condicion,clasificacion,severidad,barrera,tipoEvento,aseguradoras))
            
            db.connection.commit()
            query.close()
            return jsonify({'message': 'success'})
        except Exception as e:
            query.close()
            return jsonify({'message': 'error','error': e})  