def viewHome(app,session,redirect,url_for,render_template):
    
    @app.route('/gestionpass/home', methods=["GET"])
    def home():
        if "username" in session:
            return render_template("home/index.html")
        return redirect(url_for("login"))