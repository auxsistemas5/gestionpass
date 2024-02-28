
def httpGetFarmacoAnalisis(app,jsonify,db):

    @app.route('/api/v1/gestionpass/farmacoanalisis/getFarmacoAnalisisById/<id>')
    def getFarmacoAnalisisById(id):
        query = db.connection.cursor()
        query.execute('SELECT id_caso,tipo,tipos_reaccion,tipos_prum,r_desencadenante,reaccion,causalidad,severidad,evento,eval_hechos,barreras_seg,acc_inseguras,fac_inherentes,fac_contributivos,opor_mejora,clasificacion_final,des_tipoEvento,aseguradora FROM farmacoanalisis WHERE id_caso = %s', (id,))
        caso = query.fetchone()
        if caso: 
            return jsonify({'message': 'success','caso':caso})
        else:
            return jsonify({'warning': 'no se encontro el farmacoanalisis'})