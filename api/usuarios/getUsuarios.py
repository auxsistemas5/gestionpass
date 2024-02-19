
def httpGetUsuarios(app,jsonify,db):
    @app.route('/api/v1/gestionpass/getAllUsers', methods=["GET"])
    def getAllUsers():
        query = db.connection.cursor()
        query.execute('SELECT id,name,username,role,area,estado FROM users order by id ASC')
        usuarios = query.fetchall()
        query.close()
        usuarios_list = [{'id': data[0], 'nombre': data[1],'usuario': data[2],'rol': data[3],'area': data[4],'estado': data[5]} for data in usuarios]

        return jsonify(usuarios_list)
    
    @app.route('/api/v1/gestionpass/getUserById/<id>', methods=["GET"])
    def getUserById(id):
        query = db.connection.cursor()
        query.execute('SELECT name,username,role,area,estado FROM users where id = %s',(id,))
        usuario = query.fetchone()
        query.close()
        return jsonify([usuario[0],usuario[1],usuario[2],usuario[3],usuario[4]])