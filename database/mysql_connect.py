from flask_mysqldb import MySQL

def connectdb(app):
    app.config['MYSQL_HOST'] = '10.0.255.243'
    app.config['MYSQL_USER'] = 'devtihmfs'
    app.config['MYSQL_PASSWORD'] = '@Developti'
    app.config['MYSQL_DB'] = 'bd_exusuario'

    db = MySQL(app)
    return db