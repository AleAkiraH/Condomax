import passCrypt
import json
import requests
import mysql.connector
import fnc_enviar_push_notification


def adicionar_notificacao(model_request, conexao):
    request_body = json.loads(model_request['body'])

    try:
        titulo = request_body['titulo']
        mensagem = request_body['mensagem'] 
        telefone = request_body['telefone'], 
        token = request_body['token'] 
        usuario_id = request_body['usuario_id'] 
        usuario_criador_id = request_body['usuario_criador_id']


        conexao = conexao.cursor()
        conexao.cursor.execute('''
            INSERT INTO notificacoes (titulo_mensagem, texto_mensagem, telefone, token, usuario_id, usuario_criador_ir, data_criacao)
            VALUES (?, ?, ?, now())
        ''', (titulo, mensagem, telefone, token, usuario_id, usuario_criador_id))

        conexao.conn.commit()
        resultado = {"status": "success",
                     "message": "Notificação adicionada com sucesso!"}
        
        body_notification = json.dumps({
            "to" : "" + token + "",
            "title" : "" + titulo + "",
            "body" : "" + mensagem + 
        })

        return json.dumps(resultado)
    except Exception as e:
        resultado = {"status": "error",
                     "message": "Erro ao adicionar notificação: " + str(e)}
        return json.dumps(resultado)
    finally:
        conexao.fechar_conexao()