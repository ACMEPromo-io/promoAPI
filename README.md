# promoAPI

    API Rest para gerenciamento de promoções.

## Stack:

- Python (API, core)
  - Django Rest Framework
  - Django Rest Swagger
  - celery (rabbitMQ)
  - Pymongo
- MongoDB(bd)
- RabbitMQ

## Requisitos

- Python 3.10.4
- RabbitMQ last version
  - Erlang
  - Gevent

## Como usar:

Faça o download do repositório, abra um terminal dentro da pasta principal e rode os seguintes comandos:

Instala dependências necessárias
'''pip install -r requirements.txt'''

Inicia o servidor
'''python manage.py runserver'''

Inicia o worker do celery (ficará disponivel para receber novas tasks e processá-las)
'''celery -A promoAPI worker -l info -P gevent'''

Após isso acesse '''http://localhost:8000/''' para visualizar os endpoints disponiveis e utilizá-los.

Caso preferir usar o SWAGGER acesse: '''http://localhost:8000/docs'''
