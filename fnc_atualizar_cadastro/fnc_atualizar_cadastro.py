from Libs.conexao_banco import ConexaoBanco
import json


def atualizar_cadastro(modelRequest):

    nome = modelRequest['nome'].lower()
    telefone = modelRequest['telefone'].lower()
    email = modelRequest['email'].lower()

    try:
        conexao = ConexaoBanco()
        conexao.cursor.execute('''
            UPDATE clientes set nome=?, telefone=?, email=?
        ''', (nome, telefone, email))

        conexao.conn.commit()
        resultado = {"status": "success",
                     "message": "Cliente atualizado com sucesso!"}
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao atualizar cliente: " + str(e)}
    finally:
        conexao.fechar_conexao()

    return json.dumps(resultado)
