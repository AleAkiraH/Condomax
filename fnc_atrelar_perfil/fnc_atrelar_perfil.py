import json


def atrelar_perfil(modelRequest, conexao):

    modelRequest = json.loads(modelRequest['body'])
    usuario = modelRequest['idusuario']
    id_perfil = modelRequest['idperfil']

    try:
        cursor = conexao.cursor()
        
        cursor.execute("UPDATE clientes SET perfil_id= '"+str(id_perfil)+"'   WHERE id='"+str(usuario)+"'")

        resultado = cursor.fetchone()

        conexao.commit()
        resultado = {"status": "success",
                     "message": "Perfil atrelado com sucesso!"}
        print(resultado)
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao atrelar perfil: " + str(e)}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    finally:
        conexao.close()
