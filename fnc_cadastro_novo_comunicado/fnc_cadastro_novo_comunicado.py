from Libs.conexao_banco import ConexaoBanco
import json


def cadastrar_anexos(anexos_bs64):
    ids_inseridos = []
    conexao = None

    try:
        for anexo in anexos_bs64:
            try:
                conexao = ConexaoBanco()
                conexao.cursor.execute('''
                    INSERT INTO comunicados_anexos (anexos_bs64)
                    VALUES (?)
                ''', (anexo,))

                conexao.conn.commit()
                novo_id = conexao.cursor.lastrowid
                ids_inseridos.append(novo_id)

                resultado = {"status": "success",
                             "message": "Anexo inserido com sucesso!"}

            except Exception as e:
                resultado = {"status": "error",
                             "message": "Erro ao cadastrar cliente: " + str(e)}
                break
            finally:
                conexao.fechar_conexao()
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao cadastrar cliente: " + str(e)}
    finally:
        if resultado["status"] == "error" and conexao is not None:
            for id_inserido in ids_inseridos:
                try:
                    conexao.cursor.execute('''
                        DELETE FROM comunicados_anexos
                        WHERE id = ?
                    ''', (id_inserido,))
                    conexao.conn.commit()
                except Exception as e:
                    print("Erro ao excluir registro:", str(e))
                finally:
                    conexao.fechar_conexao()

    if resultado["status"] == "success":
        resultado["ids_inseridos"] = ids_inseridos

    return json.dumps(resultado)


def cadastrar_comunicado(titulo, descricao, idsanexos):
    try:
        conexao = ConexaoBanco()
        conexao.cursor.execute('''
            INSERT INTO comunicados (titulo, descricao, idsanexos)
            VALUES (?, ?, ?)
        ''', (titulo, descricao, str(idsanexos)))

        conexao.conn.commit()
        resultado = {"status": "success",
                     "message": "Comunicado inserido com sucesso!"}
        return json.dumps(resultado)
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao cadastrar cliente: " + str(e)}
        return json.dumps(resultado)
    finally:
        conexao.fechar_conexao()


def cadastrar_novo_comunicado(modelRequest):

    titulo = modelRequest['titulo']
    descricao = modelRequest['descricao']
    anexos_bs64 = modelRequest['anexos_bs64']

    anexos_cadastrados = cadastrar_anexos(anexos_bs64)

    idsanexos = json.dumps(json.loads(anexos_cadastrados)["ids_inseridos"])
    resultado = cadastrar_comunicado(titulo, descricao, idsanexos)

    return resultado
