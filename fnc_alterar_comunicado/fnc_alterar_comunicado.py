from Libs.conexao_banco import ConexaoBanco
import json


def remover_anexos_antigos(idsanexos_antigos):
    try:
        conexao = ConexaoBanco()
        lista_ids = json.loads(idsanexos_antigos)
        placeholders = ','.join('?' for _ in lista_ids)

        conexao.cursor.execute('''
            DELETE FROM comunicados_anexos
            WHERE id IN ({})
        '''.format(placeholders), tuple(lista_ids))

        conexao.conn.commit()
        resultado = {"status": "success",
                     "message": "Anexos removidos com sucesso!"}
        return json.dumps(resultado)
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao remover anexos: " + str(e)}
        return json.dumps(resultado)
    finally:
        conexao.fechar_conexao()


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


def alterar_id_comunicado(titulo, descricao, idsanexos, id_comunicado):
    try:
        conexao = ConexaoBanco()
        conexao.cursor.execute('''
            update comunicados set titulo=?, descricao=?, idsanexos=?
            where id =?
            
        ''', (titulo, descricao, str(idsanexos), id_comunicado))

        conexao.conn.commit()
        resultado = {"status": "success",
                     "message": "Comunicado alterado com sucesso!"}
        return json.dumps(resultado)
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao alterar comunicado: " + str(e)}
        return json.dumps(resultado)
    finally:
        conexao.fechar_conexao()


def alterar_comunicado(modelRequest):

    titulo = modelRequest['titulo']
    descricao = modelRequest['descricao']
    anexos_bs64 = modelRequest['anexos_bs64']
    id_comunicado = modelRequest['id_comunicado']
    idsanexos_antigos = modelRequest['idsanexos_antigos']

    anexos_cadastrados = cadastrar_anexos(anexos_bs64)

    idsanexos = json.dumps(json.loads(anexos_cadastrados)["ids_inseridos"])
    remover_anexos_antigos(idsanexos_antigos)

    resultado = alterar_id_comunicado(
        titulo, descricao, idsanexos, id_comunicado)

    return resultado
