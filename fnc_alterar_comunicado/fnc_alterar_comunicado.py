import json

def remover_anexos_antigos(idsanexos_antigos, conexao):
    try:
        cursor = conexao.cursor()
        lista_ids = idsanexos_antigos
        placeholders = ','.join(['%s' for _ in lista_ids])

        sql = f'''
            DELETE FROM comunicados_anexos
            WHERE id IN ({placeholders})
        '''

        cursor.execute(sql, tuple(lista_ids))

        conexao.commit()
        resultado = {"status": "success",
                     "message": "Anexos removidos com sucesso!"}
        print(resultado)
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao remover anexos: " + str(e)}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }

def cadastrar_anexos(anexos_bs64, conexao):
    ids_inseridos = []

    try:
        for anexo in anexos_bs64:
            try:
                cursor = conexao.cursor()
                cursor.execute("INSERT INTO comunicados_anexos (anexos_bs64) VALUES ('"+anexo+"')")

                conexao.commit()
                novo_id = cursor.lastrowid
                ids_inseridos.append(novo_id)

                resultado = {"status": "success",
                             "message": "Anexo inserido com sucesso!"}
                print(resultado)
            except Exception as e:
                resultado = {"status": "error",
                             "message": "Erro ao cadastrar cliente: " + str(e)}
                print(resultado)
                break
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao cadastrar cliente: " + str(e)}
        print(resultado)
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

    if resultado["status"] == "success":
        resultado["ids_inseridos"] = ids_inseridos

    return json.dumps(resultado)


def alterar_id_comunicado(titulo, descricao, idsanexos, id_comunicado, conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("update comunicados set titulo='"+titulo+"', descricao='"+descricao+"', idsanexos='"+str(idsanexos)+"' where id ='"+str(id_comunicado)+"'")

        conexao.commit()
        resultado = {"status": "success",
                     "message": "Comunicado alterado com sucesso!"}
        print(resultado)
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao alterar comunicado: " + str(e)}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    finally:
        conexao.close()


def alterar_comunicado(modelRequest, conexao):

    modelRequest = json.loads(modelRequest['body'])
    titulo = modelRequest['titulo']
    descricao = modelRequest['descricao']
    anexos_bs64 = modelRequest['anexos_bs64']
    id_comunicado = modelRequest['id_comunicado']
    idsanexos_antigos = modelRequest['idsanexos_antigos']

    anexos_cadastrados = cadastrar_anexos(anexos_bs64, conexao)

    idsanexos = json.dumps(json.loads(anexos_cadastrados)["ids_inseridos"])
    remover_anexos_antigos(idsanexos_antigos, conexao)

    resultado = alterar_id_comunicado(
        titulo, descricao, idsanexos, id_comunicado, conexao)

    return resultado
