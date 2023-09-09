from Libs.conexao_banco import ConexaoBanco
import json


def atrelar_perfil(modelRequest):

    usuario = modelRequest['idusuario']
    id_perfil = modelRequest['idperfil']

    try:
        conexao = ConexaoBanco()
        conexao.cursor.execute('''
           UPDATE clientes SET perfil =?
           WHERE id=?
        ''', (id_perfil, usuario))

        resultado = conexao.cursor.fetchone()

        conexao.conn.commit()
        resultado = {"status": "success",
                     "message": "Perfil atrelado com sucesso!"}
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao atrelar perfil: " + str(e)}
    finally:
        conexao.fechar_conexao()

    return json.dumps(resultado)
