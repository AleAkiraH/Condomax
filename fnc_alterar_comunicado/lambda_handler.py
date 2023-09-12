import fnc_alterar_comunicado
import mysql.connector

def lambda_handler(event, context):
    
    # Obtenha os valores das variáveis de ambiente ou forneça valores padrão
    host = 'localhost' # host = os.environ.get('host')
    user = 'administrador' # user = os.environ.get('user')
    password = 'Jhe@472642947' # password = os.environ.get('password')
    database = 'DBCondo' # database = os.environ.get('database')

    # Configurar as credenciais do banco de dados
    db_config = { 
        "host": host,
        "user": user,
        "password": password,
        "database": database,
    }

    print("Conectando...")
    
    # Criar uma conexão com o banco de dados
    conexao = mysql.connector.connect(**db_config)
    
    print("Conectado ao banco de dados")
    
    retorno = fnc_alterar_comunicado.alterar_comunicado(event, conexao)
    return retorno

# event = {'resource': '/cadastro', 'path': '/cadastro', 'httpMethod': 'POST', 'headers': None, 'multiValueHeaders': None, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'y995ke', 'resourcePath': '/cadastro', 'httpMethod': 'POST', 'extendedRequestId': 'K97voFFuGjQFUuQ=', 'requestTime': '09/Sep/2023:02:33:59 +0000', 'path': '/cadastro', 'accountId': '695284873308', 'protocol': 'HTTP/1.1', 'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix', 'requestTimeEpoch': 1694226839010, 'requestId': '987a8309-b307-4045-af3c-6c79c46c9364', 'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None, 'apiKey': 'test-invoke-api-key', 'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': 'arn:aws:iam::695284873308:root', 'apiKeyId': 'test-invoke-api-key-id', 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'accountId': '695284873308', 'caller': '695284873308', 'sourceIp': 'test-invoke-source-ip', 'accessKey': 'ASIA2DYRVHBOO66G7YXL', 'cognitoAuthenticationProvider': None, 'user': '695284873308'}, 'domainName': 'testPrefix.testDomainName', 'apiId': '9khxznsf72'}, 'body': '{\r\n    "id_comunicado": 1,\r\n    "titulo": "Aqui o titulo de um novo comunicado",\r\n    "descricao": "Comunicado sobre as vagas do estacionamento, todos devem se atentar em como devem estacionar os veiculos, segue as imagens abaixo como exemplo!",\r\n    "anexos_bs64": ["base111","base112","base113"],\r\n    "idsanexos_antigos": ["27","28","29"]\r\n}', 'isBase64Encoded': False}
# lambda_handler(event, None)
