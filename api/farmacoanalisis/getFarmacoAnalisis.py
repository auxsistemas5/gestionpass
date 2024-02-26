
def httpGetFarmacoAnalisis(app,jsonify,db):

    @app.route('/api/v1/gestionpass/farmacoanalisis/getFarmacoAnalisisById/<id>')
    def getFarmacoAnalisisById():
        return ''