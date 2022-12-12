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

1. Opcionalmente, crie um ambiente virtual com: `python3 -m virtualenv venv && source venv/bin/activate`

2. Instale as dependências necessárias: `pip3 install -r requirements.txt`

3. Inicie o servidor: `python3 manage.py runserver`

4. Inicie o worker do celery (ficará disponivel para receber novas tasks e processá-las):`celery -A promoAPI worker -l info -P gevent`

5. Após isso acesse `http://localhost:8000/` para visualizar os endpoints disponiveis e utilizá-los.
   
   Caso preferir usar o SWAGGER acesse: `http://localhost:8000/docs`
