
# region imports
from datetime import datetime
from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from flask_cors import CORS
import logging
from fnc_cadastro import fnc_cadastro
from fnc_login import fnc_login
from fnc_atualizar_cadastro import fnc_atualizar_cadastro
from fnc_alterar_senha import fnc_alterar_senha
from fnc_listar_perfis import fnc_listar_perfis
from fnc_listar_novos_usuarios import fnc_listar_novos_usuarios
from fnc_atrelar_perfil import fnc_atrelar_perfil
from fnc_cadastro_novo_comunicado import fnc_cadastro_novo_comunicado
from fnc_listar_comunicados import fnc_listar_comunicados
from fnc_deletar_comunicado import fnc_deletar_comunicado
from fnc_alterar_comunicado import fnc_alterar_comunicado
# endregion

# region setup
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
socketio = SocketIO(app)

CORS(app)
# endregion

# region routes

# region Cadastro e login


@app.route('/cadastro', methods=['POST'])
def cadastro():
    modelRequest = request.json
    return fnc_cadastro.cadastrar_cliente(modelRequest)


@app.route('/login', methods=['POST'])
def login():
    modelRequest = request.json
    return fnc_login.login_cliente(modelRequest)


@app.route('/atualizar_cadastro', methods=['PUT'])
def atualizar_cadastro():
    modelRequest = request.json
    return fnc_atualizar_cadastro.atualizar_cadastro(modelRequest)


@app.route('/alterar_senha', methods=['PUT'])
def alterar_senha():
    modelRequest = request.json
    return fnc_alterar_senha.alterar_senha(modelRequest)


@app.route('/listar_perfis', methods=['GET'])
def listar_perfis():
    return fnc_listar_perfis.listar_perfis()


@app.route('/listar_novos_usuarios', methods=['GET'])
def listar_novos_usuarios():
    return fnc_listar_novos_usuarios.listar_novos_usuarios()


@app.route('/atrelar_perfil', methods=['PUT'])
def atrelar_perfil():
    modelRequest = request.json
    return fnc_atrelar_perfil.atrelar_perfil(modelRequest)


@app.route('/cadastrar_novo_comunicado', methods=['POST'])
def cadastrar_novo_comunicado():
    modelRequest = request.json
    return fnc_cadastro_novo_comunicado.cadastrar_novo_comunicado(modelRequest)


@app.route('/listar_comunicados', methods=['GET'])
def listar_comunicados():
    return fnc_listar_comunicados.listar_comunicados()


@app.route('/deletar_comunicado', methods=['POST'])
def deletar_comunicado():
    modelRequest = request.json
    return fnc_deletar_comunicado.deletar_comunicado(modelRequest)


@app.route('/alterar_comunicado', methods=['POST'])
def alterar_comunicado():
    modelRequest = request.json
    return fnc_alterar_comunicado.alterar_comunicado(modelRequest)

# endregion


@app.route('/', methods=['GET'])
def home():
    now = datetime.now()
    return jsonify({'datetime': now.strftime("%d-%m-%Y %H:%M:%S")})

# endregion


if __name__ == '__main__':
    app.run()
