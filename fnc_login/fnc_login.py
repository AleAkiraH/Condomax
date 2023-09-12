import passCrypt
import json

def login_cliente(modelRequest, conexao):
    modelRequest = json.loads(modelRequest['body'])
    user = modelRequest['usuario'].lower()
    password = modelRequest['senha'].lower()
    password_crypt = passCrypt.pass_encrypt(password, user)

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, usuario FROM clientes WHERE usuario='"+user+"' AND senha='"+password_crypt+"'")

        cliente = cursor.fetchone()[0]
        conexao.close()
        if cliente > 0:
            resultado = {
                "status": "success",
                "message": "Login bem-sucedido"
            }
            print(resultado)
            return {
            'statusCode': 200,
            'body': json.dumps(resultado)
            }
        else:
            resultado = {
                "status": "error",
                "message": "Credenciais inválidas"
            }
            print(resultado)
            return {
            'statusCode': 400,
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
