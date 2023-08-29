from Libs.conexao_banco import ConexaoBanco
import json


def listar_novos_usuarios():

    try:
        conexao = ConexaoBanco()
        conexao.cursor.execute('''
            select id, usuario, nome, apartamento, bloco from clientes where perfil is null
        ''')

        # Recupere todas as linhas retornadas pela consulta
        linhas = conexao.cursor.fetchall()

        # Crie uma lista de dicionários com os resultados
        resultado_json = [{'id': linha[0], 'usuario': linha[1], 'nome': linha[2], 'apartamento': linha[3], 'bloco': linha[4]}
                          for linha in linhas]

        # Converta a lista de dicionários em JSON
        resultado = json.dumps(resultado_json, indent=4)
    except Exception as e:
        resultado = {
            "status": "error",
            "message": "Erro ao fazer login: " + str(e)
        }
    finally:
        conexao.fechar_conexao()

    return resultado
