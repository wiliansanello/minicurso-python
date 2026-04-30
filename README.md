# API PARA GERENCIAMENTO DE ACERVO DE LIVROS

## ARQUITETURA 

```
📦 projeto/
├── database/
├── model/
│   ├── entities/
│   └── repositories/
├── routes/
├── app.py
└── create_db.py
```
- **database**: Pasta com scripts e arquivo do banco de dados
- **Model**: Contém as entidades e repositórios, além do script que implementa a base declarativa, usada para comunicação com o banco de dados no propósito de realizar o mapeamento de classes da aplicação web para as entidades do banco
  - **entities**: Entidades da aplicação, declaradas para o mapeamento de classes para as tabelas (entidades) do banco
  - **repositories**: Repositório de funcionalidades da aplicação
- **routes**: Diretório destinado a guardar os arquivos de rotas de cada classe da aplicação. As rotas contém os end points (caminhos acessíveis) da API.

Scripts da raiz:
- ```app.py```: Entry point da aplicação, script principal que inicializa a aplicação web

## FERRAMENTAS ADOTADAS NO PROJETO
- **Flask**: Por ser um microframework leve e permitir a criação de uma aplicação web rapidamente e com poucas linhas de código, é uma escolha pertinente para um projeto pequeno que pode ser escalado futuramente.
- **SQLAlchemy**: ORM (Módulo que faz o mapeamento de classes para o banco de dados, permite executar comandos de manipulação de dados sem precisar escrever códigos SQL), responsável por mapear classes Python para tabelas relacionais.
- **SQLite**: Banco de dados simples e leve, ideal para iniciar aplicações escaláveis ou para pequenos projetos e provas de conceito (POC).

## FERRAMENTAS AUXILIARES NO DESENVOLVIMENTO
- **Postman**: Aplicação útil para teste e validação e APIs REST.
- **SQLite3 Studio** ou **DBeaver**: Cliente de interface gráfica para execução de comandos no banco de dados. Usada para executar o script de criação de tabelas.

## REQUISITOS PARA RODAR O PROJETO
- Python 3.13 ou superior instalado no computador
- Recomenda-se fortemente criar um ambiente virtual (usando a ferramenta venv) para execução da aplicação. Na raiz do projeto, rode os comandos ```python -m venv venv``` para criar o ambiente virtual e ```venv\Scripts\activate``` (para Windows) ```source venv/bin/activate``` para Linux e Mac OS. Segue link da documentação para mais detalhes: https://docs.python.org/pt-br/3/library/venv.html

## COMO INSTALAR 
- **Criação do banco**: Crie um arquivo .db usando o SQLite3 Studio ou DBeaver.
### Instruções para criação do banco no SQLite3 Studio
<img width="420" height="340" alt="image" src="https://github.com/user-attachments/assets/439e8336-54f4-4a52-8bb9-905f5765f664" />
<img width="390" height="470" alt="image" src="https://github.com/user-attachments/assets/0fefb088-8659-4eef-8779-ba81000587dd" />
<img width="401" height="474" alt="image" src="https://github.com/user-attachments/assets/8fe125e6-c7d8-4870-89b1-f9677b30b042" />

  
- Ache a funcionalidade de edição e execução de comandos SQL da ferramenta para executar o script ```tabela.sql``` , localizado dentro da pasta database, para criar as tabelas.
### SQL Editor no SQLite Studio

<img width="614" height="138" alt="image" src="https://github.com/user-attachments/assets/6debfa8f-7dbe-4f18-b5cd-61ad298c4042" />

  
- **Instalação de dependências**: Instala as dependências contidas no arquivo requirements.txt .
    - ```pip install -r requirements.txt``` : Recomendado 
    -  ```python -m pip install``` : Usar em ambientes com múltiplas versões do Python instaladas para garantir que o pip use o mesmo interpretador Python executado no momento.
    -  
## INICIAR A APLICAÇÃO
Acesse a pasta raiz do projeto no terminal e execute:
- ```flask --app app run``` : Recomendado 
-  ```python -m flask run``` ou ```python app.py```: Usar em ambientes com múltiplas versões do Python instaladas para garantir execução na mesma versão do interpretador Python que está rodando. 
