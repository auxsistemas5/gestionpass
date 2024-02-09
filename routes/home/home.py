def viewHome(app,session,redirect,url_for,render_template):
    
    @app.route('/gestionpass/home', methods=["GET"])
    def home():
        if "username" in session:
            return render_template("home/index.html")
        return redirect(url_for("login"))
    
    @app.route('/gestionpass/home/casos', methods=["GET"])
    def casos():
        if "username" in session:
            return render_template("home/casos.html")
        return redirect(url_for("login"))