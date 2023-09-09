import fnc_alterar_senha


def lambda_handler(event, context):
    return fnc_alterar_senha.alterar_comunicado(event)
