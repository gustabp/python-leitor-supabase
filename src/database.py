import os
import logging
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# configura o logger
logger = logging.getLogger(__name__)

def obter_conexao_supabase() -> Client:
    """estabelece e retorna o cliente de conexão com o Supabase."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        logger.error("Credenciais do Supabase ausentes no arquivo .env")
        raise ValueError("As credenciais do Supabase não foram encontradas no arquivo .env")
        
    return create_client(url, key)

def listar_contatos():
    """busca os contatos cadastrados no supabase, limitando a no máximo 3 registros."""
    try:
        logger.info("Conectando ao Supabase para buscar contatos...")
        supabase = obter_conexao_supabase()
        
        resposta = supabase.table("contatos").select("nome, telefone").limit(3).execute()
        
        logger.info(f"Busca realizada com sucesso. {len(resposta.data)} contatos encontrados.")
        return resposta.data
        
    except Exception as e:
        logger.error(f"Falha crítica ao interagir com o Supabase: {e}")
        # retorna uma lista vazia para o fluxo principal não quebrar por completo
        return []