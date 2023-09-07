from Libs.conexao_banco import ConexaoBanco
import json


def deletar_comunicado(modelRequest):

    id_comunicado = modelRequest['id_comunicado']
    excluido = True

    try:
        conexao = ConexaoBanco()
        conexao.cursor.execute('''
            UPDATE comunicados set excluido=?
            where id = ?
        ''', (excluido, id_comunicado))

        conexao.conn.commit()
        resultado = {"status": "success",
                     "message": "Comunicado excluido com sucesso!"}
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao excluir comunicado: " + str(e)}
    finally:
        conexao.fechar_conexao()

    return json.dumps(resultado)
