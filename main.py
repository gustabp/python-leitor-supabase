import time
from dotenv import load_dotenv
from src.database import listar_contatos
from src.messaging import enviar_mensagem_whatsapp

def main():

    load_dotenv()
    
    print("Iniciando o processo de envio de mensagens...")
    
    # busca os contatos no supabase
    contatos = listar_contatos()
    
    if not contatos:
        print("Nenhum contato encontrado no banco de dados.")
        return
        
    print(f"Encontrado(s) {len(contatos)} contato(s) para envio.\n")
    
    # percorre a lista de contatos e envia as mensagens uma a uma
    for contato in contatos:
        nome = contato.get("nome")
        telefone = contato.get("telefone")
        
        print(f"Enviando mensagem para {nome} ({telefone})...")
        
        sucesso = enviar_mensagem_whatsapp(nome, telefone)
        
        if sucesso:
            print(f"Mensagem enviada com sucesso para {nome}!")
        else:
            print(f"Falha ao enviar mensagem para {nome}.")
            
        time.sleep(2)
        
    print("\nProcesso finalizado!")

if __name__ == "__main__":
    main()