import fnc_cadastro_novo_comunicado


def lambda_handler(event, context):
    return fnc_cadastro_novo_comunicado.alterar_comunicado(event)
