import zipfile
import boto3

import sys
sys.path.insert(0, 'C:\\GIT\\Condomax\\Libs')
from awskey import getcredentials
aws_access_key_id, aws_secret_access_key, aws_region = getcredentials()

def atualizar_lambda():
    # Nome da função Lambda e nome do arquivo ZIP
    function_name = 'fnc_listar_perfis'
    zip_file_name = function_name + '.zip'

    if (function_name == 'RENOMEARAQUI'):
        print("Voce esqueceu de renomear.")
    else:
        # Criar um cliente para o AWS Lambda
        lambda_client = boto3.client('lambda', region_name=aws_region,
                                    aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        # Nome da função Lambda a ser atualizada
        existing_function_name = function_name

        # Ler o conteúdo do arquivo ZIP
        with open(zip_file_name, 'rb') as zip_file:
            zip_contents = zip_file.read()

        # Atualizar o código da função Lambda
        lambda_client.update_function_code(
            FunctionName=existing_function_name,
            ZipFile=zip_contents
        )

        print(f'Função Lambda "{existing_function_name}" atualizada com sucesso.')

atualizar_lambda()
