## EP3 -  Implementação de Banco de Dados em aplicação Web

Integrantes:
Lara Ayumi Nagamatsu, NUSP 9910568
Lucy Anne de Omena Evangelista, NUSP 11221776

### Arquitetura do projeto

A arquitetura do projeto segue o padrão de projetos Django, com uma pasta a mais para o armazenamento de informações do ambiente virtual utilizado.

O ambiente virtual deve ser o da sua escolha e cumprir os requisitos para o EP.

> env/       --> ambiente virtual
> mac0350db/ --> projeto
> └── mac0350/
>     ├── db.sqlite3
>     ├── ep3/  --> aplicativo
>     │   ├── admin.py
>     │   ├── apps.py
>     │   ├── __init__.py
>     │   ├── migrations/
>     │   ├── models.py  --> estrutura do banco de dados
>     │   ├── templates/ --> páginas das queries de consulta
>     │   │   ├── agregacao.html
>     │   │   ├── amostras.html
>     │   │   ├── exames.html
>     │   │   ├── pacientes.html
>     │   │   ├── perfis.html
>     │   │   ├── usuario_perfil.html
>     │   │   └── usuarios.html
>     │   ├── tests.py
>     │   ├── urls.py
>     │   └── views.py
>     ├── mac0350/ --> gerenciamento da aplicação
>     │   ├── asgi.py
>     │   ├── \__init__.py
>     │   ├── settings.py
>     │   ├── urls.py
>     │   └── wsgi.py
>     ├── manage.py
>     └── model.pdf

### Implementação do banco de dados

Na implementação deste EP a construção de tabelas é feita a partir do módulo models.py, onde há as definições de entidades, seus atributos e relacionamentos, utilizando-se os comandos python:

> python manage.py makemigrations

> python manage.py migrate

Em seguida, se pode rodar o comando abaixo para iniciar o servidor:

> python manage.py runserver

É possível acessar o banco de dados pgAdmin e verificar os dados populados a partir da interface desenvolvida neste exercício-programa.

### Como acessar as consultas

As consultas do banco de dados, feitas a partir de rede local ou a partir da VPN da USP, podem ser feitas a partir dos seguintes endereços HTTP:

- `http://127.0.0.1:8000/ep3/query_pacientes`
- `http://127.0.0.1:8000/ep3/query_usuario`
- `http://127.0.0.1:8000/ep3/query_usuario_perfil`
- `http://127.0.0.1:8000/ep3/query_perfis`
- `http://127.0.0.1:8000/ep3/query_exames`
- `http://127.0.0.1:8000/ep3/query_amostras`

Com as consultas é possível verificar os dados inseridos nas tabelas a partir da interface Django Administration.




