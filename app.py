from flask import Flask, render_template

#import modules of project
from routes.route import routes

#init database
from database.mysql_connect import connectdb

app = Flask(__name__)

#init database
db = connectdb(app)

#import the routes of project
routes(app, render_template)


if __name__ == '__main__':
    app.run(debug=True, port=8002, host="10.0.19.162")
