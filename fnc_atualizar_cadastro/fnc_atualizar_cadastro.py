import json

def atualizar_cadastro(modelRequest, conexao):

    modelRequest = json.loads(modelRequest['body'])
    nome = modelRequest['nome'].lower()
    telefone = modelRequest['telefone'].lower()
    email = modelRequest['email'].lower()

    try:
        cursor = conexao.cursor()
        
        cursor.execute("UPDATE clientes set nome='"+nome+"', telefone='"+telefone+"', email='"+email+"'")

        conexao.commit()
        resultado = {"status": "success",
                     "message": "Cliente atualizado com sucesso!"}
        print(resultado)
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao atualizar cliente: " + str(e)}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    finally:
        conexao.close()
