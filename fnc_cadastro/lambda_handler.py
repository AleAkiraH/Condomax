import fnc_cadastro
import os
import mysql.connector

def lambda_handler(event, context):
    
    # Obtenha os valores das variáveis de ambiente ou forneça valores padrão
    host = 'dbcondo.col7rp2zntqo.sa-east-1.rds.amazonaws.com' # host = os.environ.get('host')
    user = 'administrador' # user = os.environ.get('user')
    password = 'administrador' # password = os.environ.get('password')
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
    
    retorno = fnc_cadastro.cadastrar_cliente(event, conexao)
    return retorno

# event = {'resource': '/cadastro', 'path': '/cadastro', 'httpMethod': 'POST', 'headers': None, 'multiValueHeaders': None, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'y995ke', 'resourcePath': '/cadastro', 'httpMethod': 'POST', 'extendedRequestId': 'K97voFFuGjQFUuQ=', 'requestTime': '09/Sep/2023:02:33:59 +0000', 'path': '/cadastro', 'accountId': '695284873308', 'protocol': 'HTTP/1.1', 'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix', 'requestTimeEpoch': 1694226839010, 'requestId': '987a8309-b307-4045-af3c-6c79c46c9364', 'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None, 'apiKey': 'test-invoke-api-key', 'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': 'arn:aws:iam::695284873308:root', 'apiKeyId': 'test-invoke-api-key-id', 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'accountId': '695284873308', 'caller': '695284873308', 'sourceIp': 'test-invoke-source-ip', 'accessKey': 'ASIA2DYRVHBOO66G7YXL', 'cognitoAuthenticationProvider': None, 'user': '695284873308'}, 'domainName': 'testPrefix.testDomainName', 'apiId': '9khxznsf72'}, 'body': '{\r\n    "usuario":"Alexsander",\r\n    "senha":"12345",\r\n    "nome":"Alexsander de Souza Ferreira",\r\n    "apartamento":"194",\r\n    "bloco":"A",\r\n    "telefone":"11982292454",\r\n    "email":"alexsandersf15@gmail.com"\r\n}', 'isBase64Encoded': False}
# lambda_handler(event, None)
