from flask import Flask #app
from flask import request # recebe informaçãoes do usuario
from flask import jsonify #transforma dicionario em json

app = Flask(__name__) # cria o app
@app.route('/api', methods=["Post"]) #endpoint Api
def calcula_imc():
    resp = request.get_json() # recebe a informação do usúario
    peso, altura = resp["peso"], resp["altura"] # recebe as informações em variaveis
    resultado = round(peso/altura**2,2)#calculo do imc
    return jsonify({"resultado" : resultado})#resultado retornado em json


if __name__ == "__main__":
    app.run()



