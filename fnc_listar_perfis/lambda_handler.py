import fnc_listar_perfis


def lambda_handler(event, context):
    return fnc_listar_perfis.alterar_comunicado(event)
