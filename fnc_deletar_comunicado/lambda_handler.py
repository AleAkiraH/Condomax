import fnc_deletar_comunicado


def lambda_handler(event, context):
    return fnc_deletar_comunicado.alterar_comunicado(event)
