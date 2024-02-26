
def httpPutCases(app,jsonify,db,request):
    
    @app.route('/api/v1/gestionpass/cases/updateCaseById/<id>', methods=["POST"])
    def updateCase(id):
        if request.method == "POST":
           
            query = db.connection.cursor()
            
            try:
                
                id = request.form['id']
                funcionario = request.form['funcionario']
                cargo = request.form['cargo']
                documento = request.form['documento']
                nombrePaciente = request.form['nombrePaciente']
                apellidoPaciente = request.form['apellidoPaciente']
                descripcion = request.form['descripcion']
                sitioEvento = request.form['sitioEvento']
                sitioReporte = request.form['sitioReporte']
                serie = request.form['serie']
                marca = request.form['marca']
                lote = request.form['lote']
                analisis = request.form['analisis']
                descarte = request.form['descarte']
                asignado = request.form['asignado']
                evento = request.form['evento']
                peso = request.form['peso']
                edad = request.form['edad']
                genero = request.form['genero']
                sospechoso = request.form['sospechoso']
                concomitante = request.form['concomitante']
                administracion = request.form['administracion']
                inicio = request.form['inicio']
                dosis = request.form['dosis']
                frecuencia = request.form['frecuencia']
                suspendido = request.form['suspendido']
                diagnostico = request.form['diagnostico']
                evolucion = request.form['evolucion']
                clasCaso = request.form['clasCaso']
                
                
                
                if analisis == "1":
                    descarte = 0
                    clasCaso = "NO"
                    
                
                
                query.execute("UPDATE casos SET funcionario_reporta = %s, cargo_funcionario = %s,doc_paciente = %s ,nom_paciente = %s,ape_paciente = %s,descripcion_evento = %s,sitio_evento = %s, sd_reporte = %s,serie =%s,marca =%s,lote=%s,asignado_a=%s,req_analisis = %s,descartado =%s,peso_paciente = %s,tipoEvento = %s,edad = %s,genero = %s,m_sospechoso =%s,m_concomitante = %s,v_administracion = %s,fecha_inicio = %s,dosis = %s,f_administracion = %s,suspendido =%s,diagnostico =%s, informacion = %s, clasAnalisis = %s WHERE id = %s", (funcionario,cargo,documento,nombrePaciente,apellidoPaciente, descripcion,sitioEvento,sitioReporte,serie,marca,lote,asignado,analisis,descarte,peso,evento,edad,genero,sospechoso,concomitante,administracion,inicio,dosis,frecuencia,suspendido,diagnostico,evolucion,clasCaso,id))
                
                db.connection.commit()
                query.close()
                return jsonify({'message': 'success'})
            except Exception as e:
                query.close()
                return jsonify({'error': e})    
    