import os
from dotenv import load_dotenv
import json

load_dotenv()
ARQUIVO = "config.json"
ARQUIVO_CONVERSAS = "contextoCvs.json"
    
def salvarJson(nome: str, cidade: str, estilobot: str, ): 
    
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError:
                config = {}
            
    config["configUsu"] = {
        "nomeUsuario": nome,
        "cidadeUsuario": cidade,
    }
    
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    
    return f"Configurações salvas ✅\nNome: {config['configUsu']['nomeUsuario']}\nCidade: {config['configUsu']['cidadeUsuario']}\n"

def carregarJson():
    if os.path.exists(ARQUIVO) and os.path.getsize(ARQUIVO) > 0:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    
    
def salvarMsg(mensagemAI, mensagemUsu): 
    
    if os.path.exists(ARQUIVO_CONVERSAS):
        with open(ARQUIVO_CONVERSAS, "r", encoding="utf-8") as f:
            try:
                conversas = json.load(f)
            except json.JSONDecodeError:
                conversas = []
            
        nova_mensagem = {
        "mensagemUsu": mensagemUsu,
        "mensagemAI": mensagemAI,
        }

        conversas.append(nova_mensagem)

    with open(ARQUIVO_CONVERSAS, "w", encoding="utf-8") as f:
        json.dump(conversas, f, indent=4, ensure_ascii=False)
        
    return "conversa salva"
    
def carregarMsgs():
    if os.path.exists(ARQUIVO_CONVERSAS) and os.path.getsize(ARQUIVO_CONVERSAS) > 0:
        with open(ARQUIVO_CONVERSAS, "r", encoding="utf-8") as f:
            return json.load(f)


