import json
import sqlite3
from flask import Flask, render_template, jsonify, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

cnx = sqlite3.connect('rede3s.db', check_same_thread=False)
conx = cnx.cursor()


@app.route("/adccontato", methods=['POST'])
def setContato():
    dados = request.data
    insert = json.loads(dados.decode('utf8').replace("'", '"'))
    conx.execute("INSERT INTO contatos (nome, numero) VALUES (?, ?)", (insert.get('nome'), insert.get('numero')))
    cnx.commit()
    return ""

@app.route("/rmvcontato", methods=['POST'])
def rmvContato():
    dados = request.data
    remove = json.loads(dados.decode('utf8').replace("'", '"'))
    conx.execute("DELETE FROM contatos WHERE id=?", [str(remove)])
    cnx.commit()
    return ""

@app.route("/listcontatos", methods=['GET'])
def getContato():
    conx.execute("select * from contatos;")
    contatos = conx.fetchall()
    response = []
    for t in contatos:
        o = {"id":t[0], "nome": t[1], "numero": str(t[2])}
        response.append(o)
    return jsonify(response)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2222)
