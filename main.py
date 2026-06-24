import time
import logging
from dotenv import load_dotenv
from src.database import listar_contatos
from src.messaging import enviar_mensagem_whatsapp

# configuração global de Logs (exibe no formato: ANO-MÊS-DIA HORA - NÍVEL - MENSAGEM)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

def main():
    load_dotenv()
    
    logger.info("Iniciando o processo de envio de mensagens de ponta a ponta...")
    
    contatos = listar_contatos()
    
    if not contatos:
        logger.warning("Nenhum contato foi processado ou a lista retornou vazia devido a falhas.")
        return
        
    logger.info(f"Total de {len(contatos)} contato(s) carregado(s) para processamento.\n")
    
    for contato in contatos:
        nome = contato.get("nome")
        telefone = contato.get("telefone")
        
        if not nome or not telefone:
            logger.warning("Contato com dados incompletos encontrado no banco. Pulando...")
            continue
            
        logger.info(f"Processando envio para: {nome} ({telefone})")
        
        sucesso = enviar_mensagem_whatsapp(nome, telefone)
        
        if not sucesso:
            logger.error(f"Não foi possível entregar a mensagem para {nome}. Verifique os logs anteriores.")
            
        # intervalo de segurança entre envios
        time.sleep(2)
        
    logger.info("Processo finalizado com sucesso!")

if __name__ == "__main__":
    main()