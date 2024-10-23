Projeto Processador de CNJ
Este projeto implementa um serviço serverless na AWS que recebe números do Cadastro Nacional de Justiça (CNJ), processa essas informações através de uma API, realiza chamadas a um serviço externo e armazena as respostas em uma base de dados.

Tecnologias Utilizadas
AWS Lambda
Amazon API Gateway
Amazon SQS (Simple Queue Service)
Amazon DynamoDB
Boto3 (SDK da AWS para Python)
Requests (para chamadas HTTP)
Arquitetura
A arquitetura do sistema é composta pelos seguintes componentes:

API Gateway: Recebe requisições HTTP e direciona para a função Lambda.
AWS Lambda (Recepção do CNJ): Função que valida o CNJ e envia para a fila SQS.
AWS SQS: Fila que gerencia as requisições de forma assíncrona.
AWS Lambda (Processamento do SQS): Função que processa as mensagens da fila, faz a chamada para o serviço externo e armazena os dados no DynamoDB.
DynamoDB: Banco de dados NoSQL que armazena o CNJ e a resposta do serviço externo.
CloudWatch: Monitoramento e logging.
Pré-requisitos
Conta na AWS
AWS CLI configurado
Python 3.x
Bibliotecas: boto3, requests
Configuração do Ambiente
Passo 1: Criar a Tabela DynamoDB
Acesse o console do DynamoDB.
Crie uma nova tabela chamada CNJTable (ou outro nome de sua escolha) com uma chave primária chamada CNJ.
Passo 2: Criar a Fila SQS
Acesse o console do SQS.
Crie uma nova fila e anote a URL da fila.
Passo 3: Criar Funções Lambda
Função de Recepção do CNJ:

Crie uma nova função Lambda com o código da API de recepção do CNJ.
Adicione a variável de ambiente QUEUE_URL com a URL da fila SQS.
Função de Processamento do SQS:

Crie uma nova função Lambda com o código de processamento do SQS.
Adicione as variáveis de ambiente DYNAMODB_TABLE com o nome da tabela DynamoDB.
Passo 4: Configurar o API Gateway
Acesse o console do API Gateway.
Crie uma nova API REST.
Defina um novo método POST que aponte para a função Lambda de recepção do CNJ.
Habilite CORS se necessário.
Passo 5: IAM Roles
Certifique-se de que as funções Lambda têm as permissões necessárias para acessar SQS e DynamoDB. Você pode criar uma política personalizada ou usar as políticas gerenciadas pela AWS.
Executando o Projeto
Inicie a aplicação configurando as funções Lambda e a API Gateway conforme descrito acima.

Envie uma requisição POST para o endpoint da API Gateway utilizando uma ferramenta como Postman ou curl:

bash
Copiar código
curl -X POST <API_GATEWAY_URL> -H "Content-Type: application/json" -d '{"cnj": "12345678901234567890"}'
Verifique o DynamoDB para garantir que o CNJ e a resposta do serviço externo foram armazenados corretamente.

Observabilidade
Utilize o AWS CloudWatch para monitorar logs e métricas das funções Lambda e da fila SQS.
