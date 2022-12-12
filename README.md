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

Opcionalmente, crie um ambiente virtual com: `python3 -m virtualenv venv && source venv/bin/activate`

Instale as dependências necessárias: `pip3 install -r requirements.txt`

Inicie o servidor: `python3 manage.py runserver`

Inicie o worker do celery (ficará disponivel para receber novas tasks e processá-las):`celery -A promoAPI worker -l info -P gevent`

Após isso acesse `http://localhost:8000/` para visualizar os endpoints disponiveis e utilizá-los.

Caso preferir usar o SWAGGER acesse: `http://localhost:8000/docs`
