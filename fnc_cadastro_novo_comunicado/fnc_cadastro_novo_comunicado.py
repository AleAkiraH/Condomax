import json

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
                    cursor.execute('''
                        DELETE FROM comunicados_anexos
                        WHERE id = ?
                    ''', (id_inserido,))
                    conexao.commit()
                except Exception as e:
                    print("Erro ao excluir registro:", str(e))
                finally:
                    conexao.close()

    if resultado["status"] == "success":
        resultado["ids_inseridos"] = ids_inseridos

    return json.dumps(resultado)


def cadastrar_comunicado(titulo, descricao, idsanexos, conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO comunicados (titulo, descricao, idsanexos) VALUES ('"+titulo+"', '"+descricao+"', '"+str(idsanexos)+"')")

        conexao.commit()
        resultado = {"status": "success",
                     "message": "Comunicado inserido com sucesso!"}
        print(resultado)
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao cadastrar cliente: " + str(e)}
        print(resultado)
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }
    finally:
        conexao.close()


def cadastrar_novo_comunicado(modelRequest, conexao):

    modelRequest = json.loads(modelRequest['body'])
    titulo = modelRequest['titulo']
    descricao = modelRequest['descricao']
    anexos_bs64 = modelRequest['anexos_bs64']

    anexos_cadastrados = cadastrar_anexos(anexos_bs64, conexao)

    idsanexos = json.dumps(json.loads(anexos_cadastrados)["ids_inseridos"])
    resultado = cadastrar_comunicado(titulo, descricao, idsanexos, conexao)

    return resultado
