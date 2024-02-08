import openpyxl

def generateExcel(app,db,pd,send_file):
    @app.route('/gestionpass/generateExcel/<tipo>/<fechaInicio>&<fechaFin>', methods=["GET"])
    def generateExcel(tipo, fechaInicio, fechaFin):
        try:
            # Ejecutar la consulta SQL para recuperar los datos
            with db.connection.cursor() as query:
                if tipo == "reporte":
                    query.execute("SELECT id, fecha_reporte,fecha_ocurrencia,funcionario_reporta,cargo_funcionario,doc_paciente,nom_paciente,ape_paciente,descripcion_evento,sitio_evento,sd_reporte, serie, marca, lote, asignado_a, peso_paciente,tipoEvento, edad,genero,m_sospechoso,m_concomitante,v_administracion,fecha_inicio, dosis,f_administracion,suspendido, diagnostico, informacion FROM  casos WHERE fecha_reporte BETWEEN %s AND %s", (fechaInicio, fechaFin))
                elif tipo == "ocurrencia":
                    query.execute("SELECT id, fecha_reporte,fecha_ocurrencia,funcionario_reporta,cargo_funcionario,doc_paciente,nom_paciente,ape_paciente,descripcion_evento,sitio_evento,sd_reporte, serie, marca, lote, asignado_a, peso_paciente,tipoEvento, edad,genero,m_sospechoso,m_concomitante,v_administracion,fecha_inicio, dosis,f_administracion,suspendido, diagnostico, informacion  FROM casos WHERE fecha_ocurrencia BETWEEN %s AND %s", (fechaInicio, fechaFin))

                data = query.fetchall()

                # Convertir los datos a un DataFrame de pandas
                df = pd.DataFrame(data, columns=[col[0] for col in query.description])

            # Ajustar el ancho de las columnas automáticamente
            excel_file = 'datosFiltrados.xlsx'
            writer = pd.ExcelWriter(excel_file, engine='openpyxl')  # Utiliza 'openpyxl' como motor
            df.to_excel(writer, index=False)
            writer.book.encoding = 'utf-8'
            
            for column in df:
                column_width = max(df[column].astype(str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column) + 1
                writer.sheets['Sheet1'].column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width = column_width

            # Guardar el archivo Excel
            writer.close() # Llama al método 'save()' en el objeto 'writer'

            # Devolver el archivo Excel como respuesta
            return send_file(excel_file, as_attachment=True)

        except Exception as e:
            return f"Error al generar el archivo Excel: {str(e)}"
        
        
    @app.route('/gestionpass/generateExcelAllCases/<tipo>', methods=["GET"])
    def generateExcelAllCases(tipo):
        try:
            # Ejecutar la consulta SQL para recuperar los datos
            with db.connection.cursor() as query:
                if tipo == "todos":
                    query.execute("SELECT id, fecha_reporte,fecha_ocurrencia,funcionario_reporta,cargo_funcionario,doc_paciente,nom_paciente,ape_paciente,descripcion_evento,sitio_evento,sd_reporte, serie, marca, lote, asignado_a, peso_paciente,tipoEvento, edad,genero,m_sospechoso,m_concomitante,v_administracion,fecha_inicio, dosis,f_administracion,suspendido, diagnostico, informacion FROM casos")
                
                data = query.fetchall()

                # Convertir los datos a un DataFrame de pandas
                df = pd.DataFrame(data, columns=[col[0] for col in query.description])

            # Ajustar el ancho de las columnas automáticamente
            excel_file = 'datosFiltrados.xlsx'
            writer = pd.ExcelWriter(excel_file, engine='openpyxl')  # Utiliza 'openpyxl' como motor
            df.to_excel(writer, index=False)
            writer.book.encoding = 'utf-8'
            
            for column in df:
                column_width = max(df[column].astype(str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column) + 1
                writer.sheets['Sheet1'].column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width = column_width

            # Guardar el archivo Excel
            writer.close() # Llama al método 'save()' en el objeto 'writer'

            # Devolver el archivo Excel como respuesta
            return send_file(excel_file, as_attachment=True,mimetype='application/vnd.ms-excel')

        except Exception as e:
            return f"Error al generar el archivo Excel: {str(e)}"