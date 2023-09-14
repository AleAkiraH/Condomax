import passCrypt
import json
import requests
import mysql.connector


def enviar_notificacao(model_request, conexao):
    request_body = json.loads(model_request['body'])

    try:
        token = request_body['to']
        titulo = request_body['title']
        mensagem = request_body['body']

        url = "https://exp.host/--/api/v2/push/send"
        
        payload = json.dumps({
            "to": ""+ token +"",
            "sound": "default",
            "title": ""+ titulo +"",
            "body": ""+ mensagem +""
        })
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        
        tryagain = 0
        
        try:
            cursor = conexao.cursor()
            cursor.execute("update notificacoes set data_envio = now(), sucesso = 1 where token = '"+token+"' and texto_mensagem = '"+mensagem+"'")
            conexao.commit()  
        except:
            tryagain = 1
        
        if (tryagain == 1):
            try:
                cursor = conexao.cursor()
                cursor.execute("update notificacoes set data_envio = now(), sucesso = 1 where token = '"+token+"' and texto_mensagem = '"+mensagem+"'")
                conexao.commit()  
            except:
                pass
        
        resultado = {
                "status": "success",
                "message": "Push notification enviado com sucesso"
            }
        
        return {
            'statusCode': 200,
            'body': json.dumps(resultado)
        }
        
    except Exception as ex:      
        resultado = {
            "status": "error",
            "message": "Erro ao enviar o push notification: " + str(ex)
        }
        return {
            'statusCode': 400,
            'body': json.dumps(resultado)
        }