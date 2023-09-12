import json

def deletar_comunicado(modelRequest, conexao):
    
    modelRequest = json.loads(modelRequest['body'])
    id_comunicado = modelRequest['id_comunicado']
    excluido = 1

    try:
        cursor = conexao.cursor()
        cursor.execute("UPDATE comunicados set excluido="+str(excluido)+" where id = '"+str(id_comunicado)+"'")

        conexao.commit()
        resultado = {"status": "success",
                     "message": "Comunicado excluido com sucesso!"}
        print(resultado)
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao excluir comunicado: " + str(e)}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    finally:
        conexao.close()
