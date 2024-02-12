def RestFullApi(app, db, jsonify):
    def format_date(date):
        # Formatear la fecha en el formato deseado
        return date.strftime("%d/%m/%Y") if date else None
    
    @app.route('/api/v1/gestionpass/getAllCases', methods=["GET"])
    def getAllCases():
        query = db.connection.cursor()
        query.execute('SELECT id, asignado_a,fecha_reporte,fecha_ocurrencia,funcionario_reporta, cargo_funcionario, sitio_evento,sd_reporte FROM casos order by id ASC')
        casos = query.fetchall()
        query.close()
        
        casos_list = [{'id': data[0], 'asignado': data[1],'reporte':format_date(data[2]), 'ocurrencia': format_date(data[3]),'funcionario': data[4],'cargo': data[5],'sitioEvento': data[6],'sitioReporte': data[7]} for data in casos]

        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getAllCasesByDate', methods=["GET"])
    def getAllCasesByDate():
        query = db.connection.cursor()
        query.execute('SELECT casos.id, casos.fecha_reporte as CASO_FECHA_REPORTE, \
                        casos.fecha_ocurrencia as CASO_FECHA_OCURRENCIA, \
                        casos.funcionario_reporta as CASO_FUNCIONARIO_REPORTA ,\
                        casos.cargo_funcionario as CASO_CARGO_FUNCIONARIO,\
                        casos.doc_paciente as DOCUMENTO_PACIENTE, \
                        casos.nom_paciente as NOMBRE_PACIENTE, \
                        casos.ape_paciente as APELLIDO_PACIENTE, \
                        casos.descripcion_evento as DESCRIPCION_EVENTO, \
                        casos.sitio_evento as SITIO_EVENTO,\
                        casos.sd_reporte SITIO_REPORTE, \
                        casos.serie as SERIE, \
                        casos.marca as MARCA, \
                        casos.lote as LOTE, \
                        casos.asignado_a as CASO_ASIGNADO_A, \
                        casos.peso_paciente as PESO_PACIENTE, \
                        casos.tipoEvento as TIPO_EVENTO, \
                        casos.edad as EDAD, \
                        casos.genero as GENERO, \
                        casos.m_sospechoso , \
                        casos.m_concomitante, \
                        casos.v_administracion as VIA_ADMINISTRACION, \
                        casos.fecha_inicio as FECHA_INICIO, \
                        casos.dosis as DOSIS, \
                        casos.f_administracion as FORMA_ADMINISTRACIÓN, \
                        casos.suspendido as SUSPENDIDO, \
                        casos.diagnostico as DIAGNOSTICO, \
                        casos.informacion as INFORMACION, \
                        analisis.eval_hechos as ANALISIS_EVALUACION_DE_HECHOS, \
                        analisis.acc_ins as ANALISIS_ACCIONES_INSEGURAS , \
                        analisis.fac_in_paciente as ANALISIS_FACTORES_INHERENTES_PACIENTE, \
                        analisis.fac_contributivos as ANALISIS_FACTORES_CONTRIBUTIVOS, \
                        analisis.opor_mejora as ANALISIS_OPORTUNIDADES_MEJORA, \
                        analisis.condicion as ANALISIS_CONDICION, \
                        analisis.clasificacion as ANALISIS_CLASIFICACION, \
                        analisis.severidad as ANALISIS_SEVERIDAD, \
                        analisis.barrera_seguridad as ANALISIS_BARRERA_SEGURIDAD, \
                        analisis.tipo_evento as ANALISIS_TIPO_EVENTO, \
                        analisis.asegurador as ANALISIS_ASEGURADORA FROM  casos LEFT JOIN analisis ON analisis.id_caso= casos.id WHERE casos.fecha_reporte BETWEEN "2024-01-01" AND "2024-01-31" ORDER BY casos.id')
        casos = query.fetchall()
        query.close()
        
        casos_list = [{'id': data[0],'FECHA REPORTE':format_date(data[1]), 'FECHA OCURRENCIA': format_date(data[2]),'FUNCIONARIO REPORTA': data[3],'CARGO FUNCIONARIO': data[4],'DOCUMENTO PACIENTE': data[5],'NOMBRE PACIENTE': data[6],'APELLIDOS PACIENTE': data[7],'DESCRIPCION EVENTO': data[8],'SITIO EVENTO': data[9],'LUGAR REPORTE': data[10],'SERIE': data[11],'MARCA': data[12],'LOTE': data[13],'ASIGNADO A': data[14],'PESO PACIENTE': data[15],'TIPO EVENTO': data[16],'EDAD': data[17],'GENERO': data[18],'MEDICAMENTO SOSPECHOSO': data[19],'MEDICAMENTO CONCOMITANTE': data[20],'VIA ADMINISTRACION': data[21],'FECHA INICIO': data[22],'DOSIS': data[23],'FORMA ADMINISTRACION': data[23],'SUSPENDIDO': data[23],'DIAGNOSTICO': data[23],'INFORMACION': data[23],'EVALUACION DE HECHOS': data[23],'ACCIONES INSEGURAS': data[23],'FACTORES INHERENTES PACIENTE': data[23],'ANALISIS FACTORES CONTRIBUTIVOS': data[23],'OPORTUNIDADES DE MEJORA': data[23],'CONDICION': data[23],'CLASIFICACION': data[23],'SEVERIDAD': data[23],'BARRERA SEGUIRDAD': data[23],'TIPO EVENTO': data[23],'ASEGURADORA': data[23]} for data in casos]

        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getCaseById/<id>', methods=["GET"])
    def getCaseById(id):
        query = db.connection.cursor()
        query.execute('SELECT id, asignado_a,fecha_reporte,fecha_ocurrencia,funcionario_reporta, cargo_funcionario, sitio_evento,sd_reporte FROM casos where id = %s', (id,))
        casos = query.fetchall()
        query.close()
        
        casos_list = [{'id': data[0], 'asignado': data[1],'reporte':data[2], 'ocurrencia': data[3],'funcionario': data[4],'cargo': data[5],'sitioEvento': data[6],'sitioReporte': data[7]} for data in casos]

        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getAllCaseById/<id>', methods=["GET"])
    def getAllCaseById(id):
        query = db.connection.cursor()
        query.execute('SELECT id,fecha_reporte,fecha_ocurrencia,funcionario_reporta, cargo_funcionario,doc_paciente,nom_paciente,ape_paciente,descripcion_evento,sitio_evento,sd_reporte,serie,marca,lote FROM casos where id = %s', (id,))
        casos = query.fetchone()
        query.close()
        
        casos_list = [casos[0],format_date(casos[1]), format_date(casos[2]),casos[3],casos[4],casos[5],casos[6],casos[7],casos[8],casos[9],casos[10],casos[11],casos[12],casos[13]]

        return jsonify(casos_list)
    
    