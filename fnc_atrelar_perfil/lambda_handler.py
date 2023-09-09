import fnc_atrelar_perfil


def lambda_handler(event, context):
    return fnc_atrelar_perfil.alterar_comunicado(event)
