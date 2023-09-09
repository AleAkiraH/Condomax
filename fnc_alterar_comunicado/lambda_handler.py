import fnc_alterar_comunicado


def lambda_handler(event, context):
    return fnc_alterar_comunicado.alterar_comunicado(event)
