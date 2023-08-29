from Libs.conexao_banco import ConexaoBanco
from Libs import passCrypt
import json


def alterar_senha(modelRequest):

    usuario = modelRequest['usuario'].lower()
    senha = modelRequest['senha'].lower()
    password_crypt = passCrypt.pass_encrypt(senha, usuario)
    resenha = modelRequest['resenha'].lower()
    repassword_crypt = passCrypt.pass_encrypt(resenha, usuario)

    if (password_crypt != repassword_crypt):
        resultado = {"status": "error",
                     "message": "As senhas e confirmação de senha não são iguais.!"}
        return json.dumps(resultado)

    try:

        conexao = ConexaoBanco()
        conexao.cursor.execute('''
           UPDATE clientes SET senha =?
           WHERE usuario=?
        ''', (password_crypt, usuario))

        resultado = conexao.cursor.fetchone()

        conexao.conn.commit()
        resultado = {"status": "success",
                     "message": "Senha atualizada com sucesso!"}
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao atualizar sua senha: " + str(e)}
    finally:
        conexao.fechar_conexao()

    return json.dumps(resultado)
