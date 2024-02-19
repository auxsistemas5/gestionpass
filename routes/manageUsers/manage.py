from werkzeug.security import generate_password_hash, check_password_hash

def autenticacionUsuario(app,render_template,request,jsonify,db,redirect,url_for,session):

    
    @app.route('/login', methods=["GET","POST"])
    def login():
        if request.method == "POST":
            
            usuario = request.form['username']
            contraseña = request.form['password']

            query = db.connection.cursor()
            query.execute("SELECT id, name,username, password,role,area FROM users WHERE username = %s", (usuario,))
            user = query.fetchone()
            query.close()

            if user:
                password_hash = user[3]

                if check_password_hash(password_hash, contraseña):
                    session["id"] = user[0]
                    session["name"] = user[1]
                    session["username"] = user[2]
                    session["role"] = user[4]
                    session["area"] = user[5]
                    return redirect(url_for('home'))
                
                
            return redirect(url_for('login'))
            
        return render_template('login/index.html')
        
        
    @app.route('/register', methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            nombre = request.form['name']
            usuario = request.form['username']
            contraseña = request.form['password']
            hashed_password = generate_password_hash(contraseña)
            
            query = db.connection.cursor()

            try:
                query.execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)", (nombre, usuario, hashed_password))
                db.connection.commit()
                query.close()
                return redirect(url_for('login'))
            except Exception as e:
                query.close()
                return jsonify({'error': str(e)})

            
        return render_template('register/index.html')
    
    @app.route('/logout')
    def logout():
        session.pop("username", None)
        
        return redirect(url_for('login'))
    
    
    @app.route('/gestionpass/home/users', methods=["GET", "POST"])
    def users():
        return render_template('users/index.html') 