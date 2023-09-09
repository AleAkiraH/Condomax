import passCrypt
import json

def validar_cadastro(usuario, apartamento, email, conexao):
    print("Validando dados cliente")
    try:
        query = "SELECT count(id) FROM clientes WHERE usuario='" + usuario + \
            "' or apartamento='" + apartamento + "' or email='" + email + "'"

        cursor = conexao.cursor()  # Obtenha um cursor da conexão

        cursor.execute(query)

        resultado = cursor.fetchone()[0]
        print("dados validados")
        if (resultado > 0):
            return True  # Pelo menos um dos valores já está cadastrado
        else:
            return False  # Nenhum dos valores está cadastrado
    except Exception as e:
        print("Erro ao validar cadastro:", e)
        conexao.close()        

def cadastrar_cliente(modelRequest, conexao):
    print("Colhendo dados cliente")    
    modelRequest = json.loads(modelRequest['body'])
    usuario = modelRequest['usuario'].lower()
    password = modelRequest['senha'].lower()
    password_crypt = passCrypt.pass_encrypt(password, usuario)
    nome = modelRequest['nome'].lower()
    apartamento = modelRequest['apartamento'].lower()
    bloco = modelRequest['bloco'].lower()
    telefone = modelRequest['telefone'].lower()
    email = modelRequest['email'].lower()

    if (validar_cadastro(usuario, apartamento, email, conexao)):
        resultado = {"status": "error",
                     "message": "Erro ao cadastrar cliente, usuario, apartamento ou email já está cadastrado em nosso sistema!"}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    else:
        try:
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO clientes (usuario, senha, nome, apartamento, bloco, telefone, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (usuario, password_crypt, nome, apartamento, bloco, telefone, email))

            conexao.commit()
            resultado = {"status": "success",
                         "message": "Cliente cadastrado com sucesso!"}
            print(resultado)
            conexao.close()
            return {
                'statusCode': 200,
                'body': json.dumps(resultado)
            }
        except Exception as e:
            resultado = {"status": "error",
                         "message": "Erro ao cadastrar cliente: " + str(e)}
            print(resultado)
            conexao.close()
            return {
                'statusCode': 400,
                'body': json.dumps(resultado)
            }
