import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def enviar_mensagem_whatsapp(nome: str, telefone: str) -> bool:
    """
    formata a mensagem exata solicitada e envia através da Z-API.
    """
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    
    if not instance_id or not token:
        logger.error("Credenciais da Z-API ausentes no arquivo .env")
        raise ValueError("As credenciais da Z-API não foram encontradas no arquivo .env")
        
    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
    headers = {"Content-Type": "application/json"}
    mensagem_formatada = f"Olá, {nome} tudo bem com você?"
    payload = {"phone": telefone, "message": mensagem_formatada}
    
    try:
        # define um timeout de 10 segundos para a requisição não ficar travada infinitamente
        resposta = requests.post(url, json=payload, headers=headers, timeout=10)
        
        # levanta um erro caso o status HTTP seja de erro
        resposta.raise_for_status()
        
        logger.info(f"Sucesso ao enviar mensagem para {nome}.")
        return True
        
    except requests.exceptions.Timeout:
        logger.warning(f"Tempo limite esgotado ao tentar enviar mensagem para {nome}.")
        return False
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"Erro HTTP da Z-API ao enviar para {nome}: {http_err} - Resposta: {resposta.text}")
        return False
    except Exception as e:
        logger.error(f"Erro inesperado ao enviar mensagem para {nome}: {e}")
        return False