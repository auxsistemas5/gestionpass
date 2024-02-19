import calendar
import datetime

def httpGetCasos(app,jsonify,db):
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
                        casos.sd_reporte LUGAR_REPORTE, \
                        casos.serie as SERIE, \
                        casos.marca as MARCA, \
                        casos.lote as LOTE, \
                        casos.asignado_a as CASO_ASIGNADO_A, \
                        CASE WHEN casos.req_analisis = 1 THEN "CASO REQUIERE ANALISIS" \
                        WHEN casos.req_analisis = 0 THEN "CASO NO REQUIERE ANALISIS" \
                        END AS ESTADO_ANALISIS, \
                        CASE WHEN casos.descartado = 1 THEN "CASO DESCARTADO" \
                        WHEN casos.descartado = 0 THEN "CASO NO DESCARTADO" \
                        END AS DESCARTADO, \
                        casos.peso_paciente as PESO_PACIENTE, \
                        casos.tipoEvento as TIPO_EVENTO, \
                        casos.edad as EDAD, \
                        casos.genero as GENERO, \
                        casos.m_sospechoso AS MEDICAMENTO_SOSPECHOSO, \
                        casos.m_concomitante AS MEDICAMENTO_CONCOMINANTE, \
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
        
        casos_list = [{'id': data[0],'FECHA REPORTE':format_date(data[1]), 'FECHA OCURRENCIA': format_date(data[2]),'FUNCIONARIO REPORTA': data[3],'CARGO FUNCIONARIO': data[4],'DOCUMENTO PACIENTE': data[5],'NOMBRE PACIENTE': data[6],'APELLIDOS PACIENTE': data[7],'DESCRIPCION EVENTO': data[8],'SITIO EVENTO': data[9],'LUGAR REPORTE': data[10],'SERIE': data[11],'MARCA': data[12],'LOTE': data[13],'ASIGNADO A': data[14],'ANALISIS': data[15],'DESCARTADO': data[16],'PESO PACIENTE': data[17],'TIPO EVENTO': data[18],'EDAD': data[19],'GENERO': data[20],'MEDICAMENTO SOSPECHOSO': data[21],'MEDICAMENTO CONCOMITANTE': data[22],'VIA ADMINISTRACION': data[23],'FECHA INICIO': data[24],'DOSIS': data[25],'FORMA ADMINISTRACION': data[26],'SUSPENDIDO': data[27],'DIAGNOSTICO': data[28],'INFORMACION': data[29],'EVALUACION DE HECHOS': data[30],'ACCIONES INSEGURAS': data[31],'FACTORES INHERENTES PACIENTE': data[32],'ANALISIS FACTORES CONTRIBUTIVOS': data[33],'OPORTUNIDADES DE MEJORA': data[34],'CONDICION': data[35],'CLASIFICACION': data[36],'SEVERIDAD': data[37],'BARRERA SEGUIRDAD': data[38],'TIPO EVENTO': data[39],'ASEGURADORA': data[40]} for data in casos]

        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getCaseById/<id>', methods=["GET"])
    def getCaseById(id):
        query = db.connection.cursor()
        query.execute('SELECT id, asignado_a,fecha_reporte,fecha_ocurrencia,funcionario_reporta, cargo_funcionario, sitio_evento,sd_reporte,serie,marca,lote,file FROM casos where id = %s', (id,))
        casos = query.fetchall()
        query.close()
        
        casos_list = [{'id': data[0], 'asignado': data[1],'reporte':data[2], 'ocurrencia': data[3],'funcionario': data[4],'cargo': data[5],'sitioEvento': data[6],'sitioReporte': data[7]} for data in casos]

        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getAllCaseById/<id>', methods=["GET"])
    def getAllCaseById(id):
        query = db.connection.cursor()
        query.execute('SELECT id,fecha_reporte,fecha_ocurrencia,funcionario_reporta, cargo_funcionario,doc_paciente,nom_paciente,ape_paciente,descripcion_evento,sitio_evento,sd_reporte,serie,marca,lote,file,tipoEvento,peso_paciente,edad,genero,m_sospechoso,m_concomitante,v_administracion,fecha_inicio,dosis,f_administracion,suspendido,diagnostico,informacion,asignado_a,descartado,req_analisis FROM casos where id = %s', (id,))
        casos = query.fetchone()
        query.close()
        
        casos_list = [casos[0],format_date(casos[1]), format_date(casos[2]),casos[3],casos[4],casos[5],casos[6],casos[7],casos[8],casos[9],casos[10],casos[11],casos[12],casos[13],casos[14],casos[15],casos[16],casos[17],casos[18],casos[19],casos[20],casos[21],casos[22],casos[23],casos[24],casos[25],casos[26],casos[27],casos[28],casos[29],casos[30]]

        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getAllCasesforStadistics', methods=["GET"])
    def getAllCasesforStadistics():
        query = db.connection.cursor()
        query.execute(" SELECT  SUM(CASE WHEN asignado_a = 'FARMACOVIGILANCIA' THEN 1 ELSE 0 END) AS FARMACOVIGILANCIA , \
        SUM(CASE WHEN asignado_a = 'FARMACOVIGILANCIA NIQUIA' THEN 1 ELSE 0 END) AS FARMACOVIGILANCIA_NIQUIA, \
        SUM(CASE WHEN asignado_a = 'EPIDEMIOLOGÍA' THEN 1 ELSE 0 END) AS EPIDEMIOLOGÍA, \
        SUM(CASE WHEN asignado_a = 'SEGURIDAD DEL PACIENTE' THEN 1 ELSE 0 END) AS SEGURIDAD, \
        SUM(CASE WHEN asignado_a = 'BIOMEDICOS' THEN 1 ELSE 0 END) AS BIOMEDICOS, \
        SUM(CASE WHEN asignado_a = '' THEN 1 ELSE 0 END) AS SIN_ASIGNAR \
        FROM casos")
        casos = query.fetchall()
        query.close()
        casos_list = [{'FARMACOAT': data[0], 'FARMACONQ': data[1],'EPIDEMIOLOGÍA': data[2],'SEGURIDAD': data[3],'BIOMEDICOS': data[4],'SIN ASIGNAR': data[5]} for data in casos]
        
        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getAllCasesforMonthActually', methods=["GET"])
    def getAllCasesforMonthActually():

        # Obtener el año y el mes actual
        anio_actual = datetime.datetime.now().year
        mes_actual = datetime.datetime.now().month

        # Obtener la fecha de inicio del mes actual
        fecha_inicio_mes_actual = datetime.datetime(anio_actual, mes_actual, 1)

        # Obtener el último día del mes actual
        _, ultimo_dia_mes_actual = calendar.monthrange(anio_actual, mes_actual)
        fecha_final_mes_actual = datetime.datetime(anio_actual, mes_actual, ultimo_dia_mes_actual)

        # Formatear las fechas en formato ymd
        fecha_inicio = fecha_inicio_mes_actual.strftime("%Y-%m-%d")
        fecha_final = fecha_final_mes_actual.strftime("%Y-%m-%d")
        
        query = db.connection.cursor()
        query.execute(" SELECT  SUM(CASE WHEN asignado_a = 'FARMACOVIGILANCIA' THEN 1 ELSE 0 END) AS FARMACOVIGILANCIA , \
        SUM(CASE WHEN asignado_a = 'FARMACOVIGILANCIA NIQUIA' THEN 1 ELSE 0 END) AS FARMACOVIGILANCIA_NIQUIA, \
        SUM(CASE WHEN asignado_a = 'EPIDEMIOLOGÍA' THEN 1 ELSE 0 END) AS EPIDEMIOLOGÍA, \
        SUM(CASE WHEN asignado_a = 'SEGURIDAD DEL PACIENTE' THEN 1 ELSE 0 END) AS SEGURIDAD, \
        SUM(CASE WHEN asignado_a = 'BIOMEDICOS' THEN 1 ELSE 0 END) AS BIOMEDICOS, \
        SUM(CASE WHEN asignado_a = '' THEN 1 ELSE 0 END) AS SIN_ASIGNAR \
        FROM casos where fecha_reporte BETWEEN %s AND %s",(fecha_inicio,fecha_final))

        casos = query.fetchall()
        query.close()
        
        casos_list = [{'FARMACOAT': data[0], 'FARMACONQ': data[1],'EPIDEMIOLOGÍA': data[2],'SEGURIDAD': data[3],'BIOMEDICOS': data[4],'SIN ASIGNAR': data[5]} for data in casos]
        
        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getAllCasesforYearAndArea/<year>/<area>', methods=["GET"])
    def getAllCasesforYearAndArea(year,area):
    
        query = db.connection.cursor()
        query.execute("SELECT  SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS ENERO, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS FEBRERO, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS MARZO, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS ABRIL, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS MAYO, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS JUNIO, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS JULIO,\
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS AGOSTO, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS SEPTIEMBRE, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS OCTUBRE, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS NOVIEMBRE, \
               SUM(CASE WHEN asignado_a = %s AND fecha_reporte BETWEEN %s AND %s THEN 1 ELSE 0 END) AS DICIEMBRE \
               FROM casos ",
               (area, year + '-01-01', year + '-01-31',
                area, year + '-02-01', year + '-02-29',  # Febrero tiene 28 días
                area, year + '-03-01', year + '-03-31',
                area, year + '-04-01', year + '-04-30',  # Abril tiene 30 días
                area, year + '-05-01', year + '-05-31',
                area, year + '-06-01', year + '-06-30',  # Junio tiene 30 días
                area, year + '-07-01', year + '-07-31',  # Junio tiene 30 días
                area, year + '-08-01', year + '-08-31',  # Junio tiene 30 días
                area, year + '-09-01', year + '-09-30',  # Junio tiene 30 días
                area, year + '-10-01', year + '-10-31',  # Junio tiene 30 días
                area, year + '-11-01', year + '-11-30',  # Junio tiene 30 días
                area, year + '-12-01', year + '-12-31',  # Junio tiene 30 días
                
                ))
        
        casos = query.fetchall()
        query.close()
        
        casos_list = [{'ENERO': data[0], 'FEBRERO': data[1],'MARZO': data[2],'ABRIL': data[3],'MAYO': data[4],'JUNIO': data[5],'JULIO': data[6],'AGOSTO': data[7],'SEPTIEMBRE': data[8],'OCTUBRE': data[9],'NOVIEMBRE': data[10],'DICIEMBRE': data[11]} for data in casos]
        
        return jsonify(casos_list)
    
    @app.route('/api/v1/gestionpass/getAllCasesByArea/<area>', methods=["GET"])
    def getAllCasesByArea(area):
        query = db.connection.cursor()
        query.execute('SELECT id, fecha_reporte,fecha_ocurrencia,sitio_evento,sd_reporte FROM casos where asignado_a = %s order by id ASC',(area,))
        casos = query.fetchall()
        query.close()
        
        casos_list = [{'id': data[0],'reporte':format_date(data[1]), 'ocurrencia': format_date(data[2]),'sitioEvento': data[3],'sitioReporte': data[4]} for data in casos]

        return jsonify(casos_list)