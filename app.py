from flask import Flask, render_template, jsonify,send_file, request, redirect, url_for,session
import pandas as pd
from flask_cors import CORS
import os


#import modules of project
from routes.route import routes

#init database
from database.mysql_connect import connectdb

#init api restfull
from api.api import RestFullApi

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://10.0.255.243:8080"}})

# Generar una clave secreta aleatoria
clave_secreta = os.urandom(24)

app.secret_key = clave_secreta

#init database
db = connectdb(app)

#init rastfull api
RestFullApi(app, db, jsonify)

#import the routes of project
routes(app, render_template, db,pd,send_file, request,jsonify,redirect,url_for,session)


if __name__ == '__main__':
    app.run(debug=True, port=8002, host="10.0.255.243")
