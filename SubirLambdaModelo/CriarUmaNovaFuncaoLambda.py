import time
import boto3
import zipfile
import os
import json

import sys
sys.path.insert(0, 'C:\\GIT\\Condomax\\Libs')
from awskey import getcredentials
aws_access_key_id, aws_secret_access_key, aws_region = getcredentials()

def implantar_lambda():
    # Nome da função Lambda e nome do arquivo ZIP
    function_name = 'RENOMEARAQUI'
    zip_file_name = function_name+'.zip'

    if (function_name == 'RENOMEARAQUI'):
        print("Voce esqueceu de renomear.")
    else:
        # Criar um cliente para o AWS Lambda
        lambda_client = boto3.client('lambda', region_name=aws_region,
                                    aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        # Criar um cliente para o AWS IAM
        iam_client = boto3.client('iam', region_name=aws_region,
                                aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        # Criar uma função IAM para a função Lambda
        role_name = function_name+'IAM'
        assume_role_policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }

        # Nome da função IAM a ser excluída (se já existe)
        existing_role_name = function_name+'IAM'

        # Criar um cliente para o AWS IAM
        iam_client = boto3.client('iam')

        try:
            # Listar as políticas anexadas à função IAM
            attached_policies = iam_client.list_attached_role_policies(
                RoleName=existing_role_name)

            # Desanexar todas as políticas da função IAM
            for policy in attached_policies['AttachedPolicies']:
                policy_name = policy['PolicyName']
                iam_client.detach_role_policy(
                    RoleName=existing_role_name, PolicyArn=policy['PolicyArn'])
                print(
                    f'Política "{policy_name}" foi desanexada da função IAM "{existing_role_name}".')

            # Finalmente, excluir a função IAM
            iam_client.delete_role(RoleName=existing_role_name)
            print(f'Função IAM "{existing_role_name}" foi excluída com sucesso.')
        except:
            pass

        iam_client.create_role(RoleName=role_name, AssumeRolePolicyDocument=json.dumps(
            assume_role_policy_document))

        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                # Verificar se a função IAM foi criada com sucesso
                response = iam_client.get_role(RoleName=role_name)
                print(f'Função IAM "{role_name}" criada com sucesso.')
                break  # Sair do loop se a função foi criada com sucesso
            except iam_client.exceptions.NoSuchEntityException:
                # Se a função não foi encontrada, aguarde antes de tentar novamente
                if attempt < max_attempts - 1:
                    print(
                        f'Função IAM "{role_name}" ainda não foi criada. Tentativa {attempt + 1}/{max_attempts}. Aguardando...')
                    time.sleep(1000)
                else:
                    print(
                        f'Limite de tentativas atingido. A função IAM "{role_name}" não foi criada.')

        # Anexar uma política básica à função IAM (você pode personalizar isso)
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        )

        # Obter o ID da conta AWS
        response = iam_client.get_user()
        aws_account_id = response['User']['Arn'].split(':')[4]

        # Criar a função Lambda
        lambda_response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',
            Role=f'arn:aws:iam::{aws_account_id}:role/{role_name}',
            Handler=function_name+'.lambda_handler',
            Code={
                'ZipFile': open(zip_file_name, 'rb').read()
            }
        )

        print(
            f'Função Lambda criada com sucesso! ARN: {lambda_response["FunctionArn"]}')

try:
    implantar_lambda()
except:
    implantar_lambda()
