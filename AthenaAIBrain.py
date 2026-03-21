import os
import time
from google import genai
from dotenv import load_dotenv
from functions import carregarMsgs, carregarJson
from google.api_core.exceptions import ResourceExhausted
from contextsFunctions import contexto_athena

load_dotenv()
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "2"

apiKeyGemini = os.getenv("GEMINI_API_KEY")

if not apiKeyGemini:
    print("🔑 Configuração necessária")
    print("Para continuar, informe sua API key do Gemini.")
    AttChavekeyGemini = input("👉 API Key: ")
    with open(".env", "a") as f: 
        f.write(f"\nGEMINI_API_KEY={AttChavekeyGemini}")
    load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def enviarMsgAi(perguntaUSU): 
    ultimas_msgs = carregarMsgs() or []
    contexto_do_usuario = carregarJson() or []
    
    contexto_formatado = f"""
{contexto_athena}

oque você precisa saber sobre o usuario:{contexto_do_usuario} 

Histórico das últimas mensagens pra contexto da conversa:
{ultimas_msgs}

Pergunta do usuário:
{perguntaUSU}
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=contexto_formatado
        )
        return response.text
    
    except ResourceExhausted as e: 
        print(f"Error na API : {e}")
        print('Tentando uma nova solução...')
        
        time.sleep(3)
        os.system('cls')
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contexto_formatado
        )
        return response.text
        
    except Exception as e:
        print(f"Error na API : {e}")