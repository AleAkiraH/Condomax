import passCrypt
import json


def alterar_senha(modelRequest, conexao):

    modelRequest = json.loads(modelRequest['body'])
    usuario = modelRequest['usuario'].lower()
    senha = modelRequest['senha'].lower()
    password_crypt = passCrypt.pass_encrypt(senha, usuario)
    resenha = modelRequest['resenha'].lower()
    repassword_crypt = passCrypt.pass_encrypt(resenha, usuario)

    if (password_crypt != repassword_crypt):
        resultado = {"status": "error",
                     "message": "As senhas e confirmação de senha não são iguais.!"}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    try:
        cursor = conexao.cursor()
        cursor.execute("UPDATE clientes SET senha ='"+password_crypt+"' WHERE usuario='"+usuario+"'")

        resultado = cursor.fetchone()

        conexao.commit()
        resultado = {"status": "success",
                     "message": "Senha atualizada com sucesso!"}
        print(resultado)
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao atualizar sua senha: " + str(e)}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    finally:
        conexao.close()
