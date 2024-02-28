import openpyxl
import xlsxwriter

def generateExcel(app,db,pd,send_file):
    @app.route('/gestionpass/generateExcel/<tipo>/<fechaInicio>&<fechaFin>', methods=["GET"])
    def generateExcel(tipo, fechaInicio, fechaFin):
        try:
            # Ejecutar la consulta SQL para recuperar los datos
            with db.connection.cursor() as query:
                if tipo == "reporte":
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
                        CASE WHEN tipo_evento.nombre_evento IS NULL THEN "NO APLICA O DESCONOCIDO" \
                            ELSE tipo_evento.nombre_evento \
                        END AS ANALISIS_TIPO_EVENTO, \
                        analisis.asegurador as ANALISIS_ASEGURADORA FROM  casos \
                        LEFT JOIN analisis ON analisis.id_caso= casos.id \
                        LEFT JOIN tipo_evento ON analisis.tipo_evento = tipo_evento.id \
                        WHERE casos.fecha_reporte BETWEEN %s AND %s ORDER BY casos.id', (fechaInicio, fechaFin))
                    
                elif tipo == "ocurrencia":
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
                                CASE WHEN tipo_evento.nombre_evento IS NULL THEN "NO APLICA O DESCONOCIDO" \
                                    ELSE tipo_evento.nombre_evento \
                                END AS ANALISIS_TIPO_EVENTO, \
                                analisis.asegurador as ANALISIS_ASEGURADORA FROM casos \
                                LEFT JOIN analisis ON analisis.id_caso= casos.id \
                                LEFT JOIN tipo_evento ON analisis.tipo_evento = tipo_evento.id \
                                WHERE casos.fecha_ocurrencia BETWEEN %s AND %s ORDER BY casos.id', (fechaInicio, fechaFin))

                data = query.fetchall()

                # Convertir los datos a un DataFrame de pandas
                df = pd.DataFrame(data, columns=[col[0] for col in query.description])

            # Ajustar el ancho de las columnas manualmente
            excel_file = 'datosFiltrados.xlsx'
            writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')  # Utiliza 'xlsxwriter' como motor
            
            df.to_excel(writer, index=False)
            writer.book.encoding = 'utf-8'

            # Cambiar el ancho de las columnas manualmente con xlsxwriter
            column_widths = [15, 15, 15, 30, 30, 15,15,15,70,20,20,15,15,15,30,15,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]  # Lista de anchos de columna deseados
            for i, width in enumerate(column_widths):
                writer.sheets['Sheet1'].set_column(i, i, width)
                cell_format = writer.book.add_format({'text_wrap': True})
                cell_format.set_align('top')
                cell_format.set_align('center')
                writer.sheets['Sheet1'].set_column(i, i, width, cell_format=cell_format)

            # Guardar el archivo Excel
            writer.close()

            # Devolver el archivo Excel como respuesta
            return send_file(excel_file, as_attachment=True, mimetype='application/vnd.ms-excel')

        except Exception as e:
            return f"Error al generar el archivo Excel: {str(e)}"
        
        
    @app.route('/gestionpass/generateExcelAllCases/<tipo>', methods=["GET"])
    def generateExcelAllCases(tipo):
        try:
            # Ejecutar la consulta SQL para recuperar los datos
            with db.connection.cursor() as query:
                if tipo == "todos":
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
                        CASE WHEN tipo_evento.nombre_evento IS NULL THEN "NO APLICA O DESCONOCIDO" \
                            ELSE tipo_evento.nombre_evento \
                        END AS ANALISIS_TIPO_EVENTO, \
                        analisis.asegurador as ANALISIS_ASEGURADORA \
                        FROM casos \
                        LEFT JOIN analisis ON analisis.id_caso = casos.id \
                        LEFT JOIN tipo_evento ON analisis.tipo_evento = tipo_evento.id \
                        ORDER BY casos.id')
                
                data = query.fetchall()

                # Convertir los datos a un DataFrame de pandas
                df = pd.DataFrame(data, columns=[col[0] for col in query.description])

            # Ajustar el ancho de las columnas manualmente
            excel_file = 'datosFiltrados.xlsx'
            writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')  # Utiliza 'xlsxwriter' como motor
            
            df.to_excel(writer, index=False)
            writer.book.encoding = 'utf-8'

            # Cambiar el ancho de las columnas manualmente con xlsxwriter
            column_widths = [15, 15, 15, 30, 30, 15,15,15,70,20,20,15,15,15,30,15,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]  # Lista de anchos de columna deseados
            for i, width in enumerate(column_widths):
                writer.sheets['Sheet1'].set_column(i, i, width)
                cell_format = writer.book.add_format({'text_wrap': True})
                cell_format.set_align('top')
                cell_format.set_align('center')
                writer.sheets['Sheet1'].set_column(i, i, width, cell_format=cell_format)

            # Guardar el archivo Excel
            writer.close()

            # Devolver el archivo Excel como respuesta
            return send_file(excel_file, as_attachment=True, mimetype='application/vnd.ms-excel')

        except Exception as e:
            return f"Error al generar el archivo Excel: {str(e)}"
