import json

def listar_perfis(conexao):

    try:
        cursor = conexao.cursor()
        cursor.execute('''
            select id, perfil from perfis
        ''')

        # Recupere todas as linhas retornadas pela consulta
        linhas = cursor.fetchall()

        # Crie uma lista de dicionários com os resultados
        resultado_json = [{'id': linha[0], 'perfil': linha[1]}
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
            "message": "Erro ao fazer login: " + str(e)
        }
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    finally:
        conexao.close()
