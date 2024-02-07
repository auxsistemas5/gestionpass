def login(app, render_template):
    @app.route('/')
    def login():
        return render_template('login/index.html')
    
    
    
def register(app, render_template):
    @app.route('/register')
    def register():
        return render_template('register/index.html')