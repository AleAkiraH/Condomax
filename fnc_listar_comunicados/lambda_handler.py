import fnc_listar_comunicados


def lambda_handler(event, context):
    return fnc_listar_comunicados.alterar_comunicado(event)
