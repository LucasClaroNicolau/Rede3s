import json

import MySQLdb
from flask import Flask, render_template, jsonify, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
cnx = MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="admin",db="rede3sunesc")
conx = cnx.cursor()
conx.execute("CREATE TABLE IF NOT EXISTS contatos (nome VARCHAR(255), numero VARCHAR(18))")

@app.route("/adccontato", methods=['POST'])
def setContato():
    dados = request.data
    insert = json.loads(dados.decode('utf8').replace("'", '"'))
    sql = "INSERT INTO contatos (nome, numero) VALUES (%s, %s)"
    val = (""+insert.get('nome'), ""+insert.get('nome'))
    conx.execute(sql,val)
    cnx.commit()
    return ""

@app.route("/listcontatos", methods=['GET'])
def getContato():
    conx.execute("SELECT * FROM contatos;")
    contatos = conx.fetchall()
    response = []
    for t in contatos:
        o = { "nome": t[0], "numero": str(t[1])}
        response.append(o)
    return jsonify(response)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=2222)
