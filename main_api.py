import json
import boto3
import os

sqs = boto3.client('sqs')

# URL da Requisição
queue_url = os.environ['QUEUE_URL']

def lambda_handler(event, context):
    try:
        # Parsear o corpo da requisição
        body = json.loads(event['body'])
        cnj = body.get('cnj')

        # Validação do CNJ
        if not validate_cnj(cnj):
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'CNJ inválido.'})
            }

        # Enviar CNJ para SQS
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps({'cnj': cnj})
        )

        return {
            'statusCode': 202,
            'body': json.dumps({'message': 'CNJ recebido com sucesso.'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Erro interno.', 'error': str(e)})
        }

def validate_cnj(cnj):
    # Exemplo simples: deve ter 20 caracteres
    return len(cnj) == 20