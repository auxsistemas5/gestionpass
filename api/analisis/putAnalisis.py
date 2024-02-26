
def httpPutAnalisis(app,jsonify,db,request):
    
    @app.route('/api/v1/gestionpass/analisis/updateAnalisis', methods=["POST"])
    def updateAnalisis():
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
            query.execute('UPDATE analisis SET eval_hechos = %s ,acc_ins =%s,fac_in_paciente =%s,fac_contributivos = %s,opor_mejora = %s,condicion = %s,clasificacion =%s,severidad=%s,barrera_seguridad =%s,tipo_evento = %s,asegurador = %s  WHERE id_caso = %s', (hechos,inseguras,inherentes,contributivos,mejora,condicion,clasificacion,severidad,barrera,tipoEvento,aseguradoras,id))
            
            db.connection.commit()
            query.close()
            return jsonify({'message': 'success'})
        except Exception as e:
            query.close()
            return jsonify({'message': 'error','error': e})  
            