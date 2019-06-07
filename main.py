from flask import Flask, render_template, jsonify
from flask_restful import Api
from flask_restful.representations import json

app = Flask(__name__)
api = Api(app)

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
    app.run(host='0.0.0.0', port=2222)