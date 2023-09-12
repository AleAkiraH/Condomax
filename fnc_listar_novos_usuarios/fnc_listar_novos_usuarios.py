import json

def listar_novos_usuarios(conexao):

    try:
        cursor = conexao.cursor()
        cursor.execute('''
            select id, usuario, nome, apartamento, bloco from clientes where perfil_id is null
        ''')

        # Recupere todas as linhas retornadas pela consulta
        linhas = cursor.fetchall()

        # Crie uma lista de dicionários com os resultados
        resultado_json = [{'id': linha[0], 'usuario': linha[1], 'nome': linha[2], 'apartamento': linha[3], 'bloco': linha[4]}
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
