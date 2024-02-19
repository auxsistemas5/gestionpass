

def httpPostUsuarios(app,jsonify,db,request,generate_password_hash):
    @app.route('/api/v1/gestionpass/users/addNewUser', methods=["POST"])
    def addNewUser():
        if request.method == "POST":
            nombre = request.form['nombre']
            usuario = request.form['usuario']
            contraseña = request.form['contrasena']
            rol = request.form['rol']
            area = request.form['area']
            
            hashed_password = generate_password_hash(contraseña)
            
            query = db.connection.cursor()

            try:
                query.execute("INSERT INTO users (name, username, password,role,area) VALUES (%s, %s, %s,%s,%s)", (nombre, usuario, hashed_password,rol,area))
                db.connection.commit()
                query.close()
                return jsonify({'message': 'success'}),200
            except Exception as e:
                query.close()
                return jsonify({'error': 'error'}),500