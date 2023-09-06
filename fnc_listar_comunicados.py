from Libs.conexao_banco import ConexaoBanco
import json


def listar_comunicados():

    try:
        conexao = ConexaoBanco()
        conexao.cursor.execute('''
            select id, titulo, descricao, idanexo, data_insercao from comunicados order by id desc
        ''')

        # Recupere todas as linhas retornadas pela consulta
        linhas = conexao.cursor.fetchall()

        resultado_json = [{'id': linha[0], 'titulo': linha[1], 'descricao': linha[2], 'idanexo': linha[3], 'data_insercao': linha[4]}
                          for linha in linhas]

        # Converta a lista de dicionários em JSON
        resultado = json.dumps(resultado_json, indent=4)
    except Exception as e:
        resultado = {
            "status": "error",
            "message": "Erro ao listar comunicados: " + str(e)
        }
    finally:
        conexao.fechar_conexao()

    return resultado
