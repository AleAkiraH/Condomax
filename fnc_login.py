from Libs.conexao_banco import ConexaoBanco
from Libs import passCrypt
import json
import jwt


def login_cliente(modelRequest):
    user = modelRequest['usuario'].lower()
    password = modelRequest['senha'].lower()
    password_crypt = passCrypt.pass_encrypt(password, user)

    try:
        conexao = ConexaoBanco()
        conexao.cursor.execute('''
            SELECT id, usuario FROM clientes WHERE usuario=? AND senha=?
        ''', (user, password_crypt))

        cliente = conexao.cursor.fetchone()
        if cliente:
            resultado = {
                "status": "success",
                "message": "Login bem-sucedido"
            }
        else:
            resultado = {
                "status": "error",
                "message": "Credenciais inválidas"
            }
    except Exception as e:
        resultado = {
            "status": "error",
            "message": "Erro ao fazer login: " + str(e)
        }
    finally:
        conexao.fechar_conexao()

    return resultado
