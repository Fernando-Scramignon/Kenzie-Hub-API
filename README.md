# Kenzie Hub

<br>

## Tabela de Conteúdos

<hr>

- [Resumo](#resumo)
- [Diagrama ER](#diagrama-er)
- [Configuração](#configuração)
	- [Banco de dados](#banco-de-dados)
	- [Ambiente virtual, dependências e migrações](#ambiente-virtual-dependências-e-migrações)
	- [Configurando variáveis de ambiente](#configurando-variáveis-de-ambiente)
	- [Rodando o projeto](#rodando-o-projeto)
- [Rotas da Api](#rotas-da-api)
    - [users - Usuários](#users)
        - [Criação de usuário](#criação-de-usuário)
		- [Autenticação](#autenticação)
		- [Listagem de usuário](#listagem-de-usuário)
	- [techs - Tecnologias](#techs)
		- [Criação de tecnologias](#criação-de-tecnologias)
		- [Listagem de tecnologias](#listagem-das-tecnologias)
		- [Deleção de tecnologias](#deleção-de-tecnologias)
		- [Edição de tecnologias](#edição-de-tecnologias)
	

<br>

## Resumo 

<hr>

Um projeto que permite o gerenciamento e exposição de tecnologias conhecidas e projetos feitos. Esta aplicação foi feita utilizando Django e Django Rest Framework, além disso é totalmente testada. O objetivo é ser uma API para uma outra aplicação Front End de mesmo nome.


URL base da aplicação: https://kenzie-hub-api-production.up.railway.app/api <br>
URL local: http://localhost:8000/api

Tecnologias:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Postgresql](https://www.postgresql.org/)


<br>

## Diagrama ER

<hr>

![Diagrama ER](kenzie_hub_ER_diagram.jpg)

<br>


## Configuração

<hr>


### Banco de dados

É preciso ter instalado [postgresql](https://www.postgresql.org/download/). Depois de configurado, é necessário criar um banco de dados para a aplicação. Para criar um banco de dados, entre no postgres com o comando abaixo, substituindo user pelo nome do seu usuário.

```bash
psql -U user
```

O comando de criação está abaixo. Substitua db_name pelo nome desejado.

```bash
CREATE DATABASE db_name;
```

<br>

### Ambiente Virtual, dependências e migrações

Primeiro abra um terminal na pasta kenzie_hub_api e crie o ambiente virtual com o comando:

```bash
python -m venv venv
```

Se você estiver utilizando windows, talvez seja necessário permitir a criação do ambiente. Use o comando abaixo:

```bash
Set-ExecutionPolicy AllSigned
```

Depois é necessário entrar no ambiente virtual.

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
.\venv\Scripts\activate
```

Agora instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Antes da aplicação funcionar, é preciso ajustar o banco de dados criado. Execute o comando abaixo para a aplicação popular o banco de dados com as tabelas necessárias.

```bash
python manage.py migrate
```

<br>

### Configurando variáveis de ambiente

Crie um arquivo chamado .env na raíz do projeto, copie o conteúdo que está no arquivo .env.example e cole no arquivo recém criado. Use as instruções no .env.example como um molde para configurar as informações do seu dotenv

<br>

### Rodando o projeto

Tudo está configurado. Para rodar a aplicação rode o comando

```bash
python manage.py runserver
```

A aplicação, caso nenhuma configuração extra tenha sido mudada, estará rodando no localhost, na porta 8000

URL local: http://localhost:8000/api

<br>

## Rotas da API

<hr>

<br>

### **users**

| Field          | Type     | Description                                     |
| -------------- | -------  | ----------------------------------------------- |
| id             | uuid     | identificador único do usuário                  |
| name           | string   | nome inteiro do usuário                         |
| email          | string   | email do usuário                                |
| password       | string   | senha do usuário                                |
| bio            | string   | breve descrição do usuário                      |
| contact        | string   | como se entrar em contato com o usuário         |
| course_modules | string   | qual módulo o usuário está                      |
| created_at     | datetime | quando o usuário foi criado                     |
| updated_at     | datetime | quando o usuário foi atualizado                 |

<br>

#### **Criação de usuário**

<hr>

Rota que permite a criação de usuários. Os campo created_at e updated_at são gerados automáticamente e os campos bio e course_module são opcionais

<br>

##### **Exemplo de requisição:**

```
POST /api/users/
Host: https://kenzie-hub-api-production.up.railway.app
Authorization: None
Content-type: application/json
```

<br>

##### **Exemplo do corpo da requisição:**


```json
{
	"email": "johndoe@gmail.com",
	"password": "abcd1234",
	"name":"John Doe",
	"contact": "linkedin/johndoe"
}
```

<br>

##### **Exemplo da resposta da requisição:**

```
201 CREATED
```

```json
{
	"id": "9f05c407-bb1f-4b03-846a-dd20201417c8",
	"name": "John",
	"email": "johndoe@gmail.com",
	"course_module": "Não especificado",
	"bio": "A cool bio",
	"contact": "linkedin",
	"created_at": "2023-05-29T19:51:06.662055Z",
	"updated_at": "2023-05-29T19:51:06.662074Z",
	"avatar_url": null,
	"techs": [],
	"works": []
}
```

<br>

#### **Autenticação**

<hr>

Rota que permite a autenticação do usuário e retorna um token que é utilizado em outras requisições.

<br>

##### **Exemplo de requisição**

```
POST /api/login
Host: https://kenzie-hub-api-production.up.railway.app
Authorization: None
Content-type: application/json
```

<br>

##### **Exemplo do corpo da requisição**

```json
{
	"email": "johndoe@gmail.com",
	"password": "abcd1234"
}
```

<br>

##### **Exemplo da resposta da requisição**

```
200 OK
```

```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NTY0OTA2OSwiaWF0IjoxNjg1Mzg5ODY5LCJqdGkiOiJkODVhNGExNDNiMTg0NThjYjg5ZDg1ZWQ2N2E4NTQ0YiIsInVzZXJfaWQiOiI5ZjA1YzQwNy1iYjFmLTRiMDMtODQ2YS1kZDIwMjAxNDE3YzgifQ.gvHnc52F41M5CiXy6bGG1xezyss_GuSPSiP-S5Qu3cI",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NDc2MjY5LCJpYXQiOjE2ODUzODk4NjksImp0aSI6Ijk5YzcxNGEyOTA3MjQ0ZWU4ZGJiZWU4ODJhNzVlYjdlIiwidXNlcl9pZCI6IjlmMDVjNDA3LWJiMWYtNGIwMy04NDZhLWRkMjAyMDE0MTdjOCJ9.lN3keDiQHUKesFzbm73lM-TWM_oQhKezfxSUooxi0K4"
}
```

<br>

#### **Listagem de usuário**

<hr>

Rota que permite a listagem das informações de um usuário. O usuário só pode ver as próprias informações.

<br>

##### **Exemplo de requisição:**

```
GET /api/users/
Host: https://kenzie-hub-api-production.up.railway.app
Authorization: Token
Content-type: application/json
```

<br>

##### **Exemplo do corpo da requisição:**


```json
sem conteúdo
```

<br>

##### **Exemplo da resposta da requisição:**

```
200 OK
```

```json
[
	{
		"id": "9f05c407-bb1f-4b03-846a-dd20201417c8",
		"name": "John",
		"email": "johndoe@gmail.com",
		"course_module": "Não especificado",
		"bio": "A cool bio",
		"contact": "linkedin",
		"created_at": "2023-05-29T19:51:06.662055Z",
		"updated_at": "2023-05-29T19:51:06.662074Z",
		"avatar_url": null,
		"techs": [
			{
				"id": "64674576-f8a2-4ce2-8c4a-6c8b766e7968",
				"title": "python",
				"status": "Avançado",
				"created_at": "2023-05-29T19:51:23.608836Z",
				"updated_at": "2023-05-29T19:51:23.608863Z"
			},
			{
				"id": "13feeab2-4676-438c-8dae-690ac9a39126",
				"title": "javascript",
				"status": "Intermediário",
				"created_at": "2023-05-29T19:52:03.944112Z",
				"updated_at": "2023-05-29T19:52:06.624025Z"
			},
			{
				"id": "08cf4cd8-4386-42df-8055-3f39d650243e",
				"title": "c++",
				"status": "Iniciante",
				"created_at": "2023-05-29T19:52:14.041790Z",
				"updated_at": "2023-05-29T19:52:14.041835Z"
			}
		],
		"works": []
	}
]
```

<br>

### **Techs**

| Field          | Type     | Description                                     |
| -------------- | -------  | ----------------------------------------------- |
| id             | uuid     | identificador único da tecnologia               |
| title          | string   | nome da tecnologia                              |
| status         | string   | o nível de habilidade do usuário na tecnologia  |
| created_at     | datetime | quando o usuário foi criado                     |
| updated_at     | datetime | quando o usuário foi atualizado                 |
| user_id        | fk       | o campo que conecta a tecnologia ao seu usuário |

<br>

#### **Criação de tecnologias**

<hr>

Rota que permite a criação de de uma tecnologia. As informações do usuário são extraídas através do token.

<br>

##### **Exemplo de requisição:**

```
POST /api/techs/
Host: https://kenzie-hub-api-production.up.railway.app
Authorization: Token
Content-type: application/json
```

<br>

##### **Exemplo do corpo da requisição:**

O campo status aceita apenas os valores: "Iniciante", "Intermediário" e "Avançado".


```json
{
	"title": "javascript",
	"status": "Avançado"
}
```

<br>

##### **Exemplo da resposta da requisição:**

```
201 CREATED
```

```json
{
	"id": "64674576-f8a2-4ce2-8c4a-6c8b766e7968",
	"title": "javascript",
	"status": "Avançado",
	"created_at": "2023-05-29T19:51:23.608836Z",
	"updated_at": "2023-05-29T19:51:23.608863Z"
}
```

<br>

#### **Listagem das tecnologias**

<hr>

Rota que permite o usuário ver suas tecnologias registradas.

<br>

##### **Exemplo de requisição:**

```
GET /api/techs/
Host: https://kenzie-hub-api-production.up.railway.app
Authorization: Token
Content-type: application/json
```

<br>

##### **Exemplo do corpo da requisição:**


```json
Sem conteúdo
```

<br>

##### **Exemplo da resposta da requisição:**

```
200 OK
```

```json
[
	{
		"id": "64674576-f8a2-4ce2-8c4a-6c8b766e7968",
		"title": "python",
		"status": "Avançado",
		"created_at": "2023-05-29T19:51:23.608836Z",
		"updated_at": "2023-05-29T19:51:23.608863Z"
	},
	{
		"id": "13feeab2-4676-438c-8dae-690ac9a39126",
		"title": "javascript",
		"status": "Intermediário",
		"created_at": "2023-05-29T19:52:03.944112Z",
		"updated_at": "2023-05-29T19:52:06.624025Z"
	}
]
```

<br>

#### **Deleção de tecnologias**

<hr>

Rota que permite o usuário deletar suas tecnologias registradas.

<br>

##### **Exemplo de requisição:**

Substitua o id pelo id da tecnologia que será deletada.

```
DELETE /api/techs/id
Host: https://kenzie-hub-api-production.up.railway.app
Authorization: Token
Content-type: application/json
```

<br>

##### **Exemplo do corpo da requisição:**


```json
Sem conteúdo
```

<br>

##### **Exemplo da resposta da requisição:**

```
204 NO CONTENT
```

```json
Sem conteúdo
```

<br>

#### **Edição de tecnologias**

<hr>

Rota que permite o usuário editar suas tecnologias registradas.

<br>

##### **Exemplo de requisição:**

Substitua o id pelo id da tecnologia que será editada.

```
PATCH /api/techs/id
Host: https://kenzie-hub-api-production.up.railway.app
Authorization: Token
Content-type: application/json
```

<br>

##### **Exemplo do corpo da requisição:**


```json
{
	"title": "Typescript",
	"status":"Intermediário"
}
```

<br>

##### **Exemplo da resposta da requisição:**

```
200 OK
```

```json
{
	"id": "377242fa-68d5-484b-877a-c7d6e8b1abc3",
	"title": "Typescript",
	"status": "Intermediário",
	"created_at": "2023-04-27T13:06:44.337917Z",
	"updated_at": "2023-05-10T01:10:15.132267Z"
}
```

<br>