from flask import Flask, render_template, jsonify,send_file
import pandas as pd



#import modules of project
from routes.route import routes

#init database
from database.mysql_connect import connectdb

#init api restfull
from api.api import RestFullApi

app = Flask(__name__)

#init database
db = connectdb(app)

#init rastfull api
RestFullApi(app, db, jsonify)

#import the routes of project
routes(app, render_template, db,pd,send_file)


if __name__ == '__main__':
    app.run(debug=True, port=8002, host="10.0.19.162")
