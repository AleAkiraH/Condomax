import fnc_atualizar_cadastro


def lambda_handler(event, context):
    return fnc_atualizar_cadastro.alterar_comunicado(event)
