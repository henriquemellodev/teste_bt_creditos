import json
import boto3
import requests
import os

dynamodb = boto3.resource('dynamodb')
# Nome da Tabela
table_name = os.environ['TABLE_CNJ']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    for record in event['Records']:
        # Extrair a mensagem do SQS
        message_body = json.loads(record['body'])
        cnj = message_body['cnj']

        try:
            # Chamar API externa
            response = call_external_service(cnj)

            # Armazenar a resposta no DynamoDB
            save_to_dynamodb(cnj, response)

        except Exception as e:
            print(f"Erro ao processar CNJ {cnj}: {str(e)}")

def call_external_service(cnj):
    # Exemplo de chamada a um serviço externo
    url = f'https://api.exemplo.com/process/{cnj}'
    response = requests.get(url)

    # Tratar resposta
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na chamada ao serviço externo: {response.status_code}")

def save_to_dynamodb(cnj, response):
    # Armazenar o CNJ e a resposta no DynamoDB
    table.put_item(
        Item={
            'CNJ': cnj,
            'Resposta': response
        }
    )