import fnc_listar_novos_usuarios


def lambda_handler(event, context):
    return fnc_listar_novos_usuarios.alterar_comunicado(event)
