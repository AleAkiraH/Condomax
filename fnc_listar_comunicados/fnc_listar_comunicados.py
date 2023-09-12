import json

def listar_comunicados(conexao):

    try:
        cursor = conexao.cursor()
        cursor.execute('''
            select id, titulo, descricao, idsanexos, data_insercao from comunicados where excluido = 0 order by id desc
        ''')

        # Recupere todas as linhas retornadas pela consulta
        linhas = cursor.fetchall()

        resultado_json = [{'id': linha[0], 'titulo': linha[1], 'descricao': linha[2], 'idsanexos': linha[3], 'data_insercao': linha[4]}
                          for linha in linhas]

        # Converta a lista de dicionários em JSON
        resultado = json.dumps(resultado_json, indent=4)
        print(resultado)
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
    except Exception as e:
        resultado = {
            "status": "error",
            "message": "Erro ao listar comunicados: " + str(e)
        }
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    finally:
        conexao.close()
