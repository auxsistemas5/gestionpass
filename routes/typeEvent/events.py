def typeEvent(app,request,db,render_template,jsonify):
    @app.route('/gestionpass/home/typeEvent', methods=["GET"])
    def typeEvent():
        return render_template('typeEvent/index.html')