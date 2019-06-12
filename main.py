#print(request.remote_addr) comando que pega o ip do cliente
import MySQLdb
from flask import Flask, render_template, jsonify, request
from flask_restful import Api
from mysql.connector import (connection)
from flask_restful.representations import json

app = Flask(__name__)
api = Api(app)
cnx = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="admin",db="rede3sunesc")
conx = cnx.cursor()
conx.execute("CREATE TABLE IF NOT EXISTS contatos (nome VARCHAR(255), numero INT)")

@app.route("/adccontato")
def setContato():
    sql = "INSERT INTO contatos (nome, numero) VALUES (%s, %s)"
    val = ("John", "321")
    conx.execute(sql,val)
    cnx.commit()
    return ""

@app.route("/listcontatos")
def getContato():
    print(conx.execute("SELECT * FROM contatos;"))
    return "";

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/contatos', methods=['GET'])
def contatos():
    response = [{
        "nome":"Lucas Claro",
        "numero":"48998385996"
    },
    {
        "nome": "Carolina Pereira",
        "numero": "48999101231"
    }]
    return jsonify(response)


if __name__ == "__main__":
    setContato()
    #getContato()
#   app.run(host='0.0.0.0', port=2222)
