import boto3

import sys
sys.path.insert(0, 'C:\\GIT\\Condomax\\Libs')
from awskey import getcredentials
aws_access_key_id, aws_secret_access_key, aws_region = getcredentials()

def deletar_lambda():
    # Nome da função Lambda e nome da função IAM
    function_name = 'fnc_alterar_senha'
    role_name = function_name+'IAM'

    if (function_name == 'RENOMEARAQUI'):
        print("Voce esqueceu de renomear.")
    else:
        # Criar um cliente para o AWS Lambda
        lambda_client = boto3.client('lambda', region_name=aws_region,
                                    aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        # Criar um cliente para o AWS IAM
        iam_client = boto3.client('iam', region_name=aws_region,
                                aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        # Verificar se a função Lambda existe e excluí-la, se existir
        try:
            lambda_client.delete_function(FunctionName=function_name)
            print(f'Função Lambda "{function_name}" excluída com sucesso.')
        except lambda_client.exceptions.ResourceNotFoundException:
            print(f'Função Lambda "{function_name}" não existe.')

        # Verificar se a função IAM existe e excluí-la, se existir
        try:
            # Listar as políticas anexadas à função IAM
            attached_policies = iam_client.list_attached_role_policies(
                RoleName=role_name)

            # Desanexar todas as políticas da função IAM
            for policy in attached_policies['AttachedPolicies']:
                policy_name = policy['PolicyName']
                iam_client.detach_role_policy(
                    RoleName=role_name, PolicyArn=policy['PolicyArn'])
                print(
                    f'Política "{policy_name}" foi desanexada da função IAM "{role_name}".')

            # Excluir a função IAM
            iam_client.delete_role(RoleName=role_name)
            print(f'Função IAM "{role_name}" excluída com sucesso.')
        except iam_client.exceptions.NoSuchEntityException:
            print(f'Função IAM "{role_name}" não existe.')

deletar_lambda()
