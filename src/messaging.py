import os
import requests
from dotenv import load_dotenv

# carrega as variáveis de ambiente
load_dotenv()

def enviar_mensagem_whatsapp(nome: str, telefone: str) -> bool:
    """
    formata a mensagem exata solicitada e envia através do Z-API.
    """
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    
    if not instance_id or not token:
        raise ValueError("As credenciais da Z-API não foram encontradas no arquivo .env")
        
    # URL de envio de texto conforme a documentação da Z-API
    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
    
    # cabeçalhos necessários para a requisição
    headers = {
        "Content-Type": "application/json"
    }
    
    # mensagem exata exigida
    mensagem_formatada = f"Olá, {nome} tudo bem com você?"
    
    # corpo da requisição
    payload = {
        "phone": telefone,
        "message": mensagem_formatada
    }
    
    # realiza o envio via POST
    resposta = requests.post(url, json=payload, headers=headers)
    
    # retorna True se o status HTTP for de sucesso (200 ou 201)
    return resposta.status_code in [200, 201]