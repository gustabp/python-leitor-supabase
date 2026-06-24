import os
from supabase import create_client, Client
from dotenv import load_dotenv

# carrega variáveis do .env caso o arquivo seja executado diretamente
load_dotenv()

def obter_conexao_supabase() -> Client:
    """estabelece e retorna o cliente de conexão com o supabase"""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("As credenciais do Supabase não foram encontradas no arquivo .env")
        
    return create_client(url, key)

def listar_contatos():
    """busca os contatos cadastrados no supabase, limitando a no máximo 3 registros"""
    supabase = obter_conexao_supabase()
    
    # faz o select na tabela 'contatos' trazendo apenas os 3 primeiros registros
    resposta = supabase.table("contatos").select("nome, telefone").limit(3).execute()
    
    # retorna a lista de dados (dicionarios contendo nome e telefone)
    return resposta.data