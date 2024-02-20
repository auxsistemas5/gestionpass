

def httpPutUsuarios(app,jsonify,db,request,generate_password_hash):
    
    @app.route('/api/v1/gestionpass/users/updatePassword', methods=["POST"])
    def updatePassword():
        if request.method == "POST":
           
            query = db.connection.cursor()
            
            try:
                contraseña = request.form['contrasena']
                hashed_password = generate_password_hash(contraseña)
                
                user_id = request.form['user_id']
                query.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, user_id))
                db.connection.commit()
                query.close()
                return jsonify({'message': 'success'})
            except Exception as e:
                query.close()
                return jsonify({'error': 'error'})
            
    @app.route('/api/v1/gestionpass/users/updateDatesUser/<id>', methods=["POST"])
    def updateDatesUser(id):
        if request.method == "POST":
           
            query = db.connection.cursor()
            
            try:
                
                nombre = request.form['nombre']
                usuario = request.form['usuario']
                role = request.form['rol']
                area = request.form['area']
                estado = request.form['estado']
                
                query.execute("UPDATE users SET name = %s, username = %s,role = %s ,area = %s,estado = %s WHERE id = %s", (nombre,usuario,role,area,estado, id))
                db.connection.commit()
                query.close()
                return jsonify({'message': 'success'})
            except Exception as e:
                query.close()
                return jsonify({'error': e})
            
    