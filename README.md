# Desafio Técnico - Desenvolvimento Python

Este repositório contém a solução para o desafio técnico de integração entre **Supabase** e **Z-API** utilizando **Python**. O objetivo do projeto é ler contatos cadastrados em um banco de dados e disparar mensagens personalizadas via WhatsApp de forma automatizada.

# Funcionalidades
Integração com Supabase para consulta de dados de contatos.

Integração com Z-API para disparo automatizado de mensagens de texto.

Limitação nativa para processar até 3 registros por execução (regra do desafio).

Sistema robusto de tratamento de exceções (erros de rede, chaves inválidas, etc.).

Rastreabilidade total do fluxo com o módulo nativo de logging do Python.

# Tecnologias Utilizadas
Python 3.x

Supabase Client (Integração com Banco de Dados)

Requests (Consumo da API Rest Z-API)

Python-Dotenv (Gerenciamento seguro de variáveis de ambiente)

# Configuração e Instalação
1. Setup da Tabela no Supabase
Para estruturar o banco de dados conforme o esperado pelo script, execute a seguinte query no SQL Editor do seu projeto Supabase:

SQL
CREATE TABLE contatos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

2. Variáveis de Ambiente (.env)
Clone este repositório e, na raiz do projeto, crie um arquivo chamado .env baseando-se no modelo fornecido no .env.example:

Snippet de código:
SUPABASE_URL=seu_url_do_supabase
SUPABASE_KEY=sua_chave_public_anon_do_supabase
ZAPI_INSTANCE_ID=id_da_sua_instancia_zapi
ZAPI_TOKEN=token_da_sua_instancia_zapi

3. Instalação das Dependências
Crie e ative o seu ambiente virtual (venv) e instale as bibliotecas necessárias utilizando o requirements.txt:


Bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual (Windows)
.venv\Scripts\activate

# Ativar o ambiente virtual (Linux/Mac)
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt


# COMO EXEUTAR O PROJETO
Com o ambiente virtual ativo e o arquivo .env devidamente preenchido, basta rodar o arquivo principal na raiz do projeto:

Bash
python main.py
Você verá a saída formatada pelos logs acompanhando o status do envio para cada um dos contatos.
