from Libs.conexao_banco import ConexaoBanco
from Libs import passCrypt
import json


def validar_cadastro(usuario, apartamento, email):
    try:
        query = "SELECT count(id) FROM clientes WHERE usuario='" + usuario + \
            "' or apartamento='" + apartamento + "' or email='" + email + "'"

        conexao = ConexaoBanco()
        conexao.cursor.execute(query)

        resultado = conexao.cursor.fetchone()

        if (resultado[0] > 0):
            return True  # Pelo menos um dos valores já está cadastrado
        else:
            return False  # Nenhum dos valores está cadastrado
    except Exception as e:
        print("Erro ao validar cadastro:", e)
    finally:
        conexao.fechar_conexao()


def cadastrar_cliente(modelRequest):

    usuario = modelRequest['usuario'].lower()
    password = modelRequest['senha'].lower()
    password_crypt = passCrypt.pass_encrypt(password, usuario)
    nome = modelRequest['nome'].lower()
    apartamento = modelRequest['apartamento'].lower()
    bloco = modelRequest['bloco'].lower()
    telefone = modelRequest['telefone'].lower()
    email = modelRequest['email'].lower()

    if (validar_cadastro(usuario, apartamento, email)):
        resultado = {"status": "error",
                     "message": "Erro ao cadastrar cliente, usuario, apartamento ou email já está cadastrado em nosso sistema!"}
    else:
        try:
            conexao = ConexaoBanco()
            conexao.cursor.execute('''
                INSERT INTO clientes (usuario, senha, nome, apartamento, bloco, telefone, email)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (usuario, password_crypt, nome, apartamento, bloco, telefone, email))

            conexao.conn.commit()
            resultado = {"status": "success",
                         "message": "Cliente cadastrado com sucesso!"}
        except Exception as e:
            resultado = {"status": "error",
                         "message": "Erro ao cadastrar cliente: " + str(e)}
        finally:
            conexao.fechar_conexao()

    return json.dumps(resultado)
