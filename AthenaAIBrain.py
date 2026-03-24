import os
import time
from google import genai
from dotenv import load_dotenv
from functions import carregarMsgs, carregarJson, criarVariaveisDeAmbiente
from google.api_core.exceptions import ResourceExhausted
from contextsFunctions import AvaliarMensagensContext, contexto_athena

"""
Camada de integração com a IA.
Responsável pela comunicação com a API, envio de contexto e tratamento de respostas.
"""

load_dotenv()
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "2"

apiKeyGemini = os.getenv("GEMINI_API_KEY")

if not apiKeyGemini:
    criarVariaveisDeAmbiente()
    load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
clienttwo = genai.Client(api_key=os.getenv('GEMINI_API_KEY_TWO'))


def EvaluateMessages(perguntaUSU): 
    contexto_formatado = f"""
{AvaliarMensagensContext}

Pergunta do usuário:
{perguntaUSU}
"""
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=contexto_formatado
        )
        return response.text
    
    except ResourceExhausted as e:
        print('Tentando uma nova solução...')
        
        time.sleep(3)
        os.system('cls')
        
        response = clienttwo.models.generate_content(
            model="gemini-2.5-flash",
            contents=contexto_formatado
        )
        return response.text
    
    except Exception as f:
        erro = str(f)
        if "API_KEY_INVALID" in erro:
            print(f'ERROR NA API: {f}')
        
            time.sleep(3)
            os.system("cls")
            os.remove(".env")
        
            print("A chave informada anteriormente é inválida.")
            print("Por favor, insira uma nova chave válida.\n")

            time.sleep(3)
            os.system("cls")
            
            criarVariaveisDeAmbiente()
        
    except Exception as e:
        print(f"Error na API : {e}")
        
            
def UtilityFunctions(perguntaUSU, contexto_msg): 
    contexto_formatado = f"""
    {contexto_msg}

    Mensagem do Usuario:
    {perguntaUSU}
    """
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=contexto_formatado
        )
        return response.text
    
    except ResourceExhausted as e: 
        print('Tentando uma nova solução...')
        
        time.sleep(3)
        os.system('cls')
        
        response = clienttwo.models.generate_content(
            model="gemini-2.5-flash",
            contents=contexto_formatado
        )
        return response.text
        
    except Exception as e:
        print(f"Error na API : {e}")


def UtilityChat(perguntaUSU): 
    ultimas_msgs = carregarMsgs() or []
    contexto_do_usuario = carregarJson() or []
    
    contexto_formatado = f"""
    {contexto_athena}
    
    contexto das mensagens trocadas com o usuario:{ultimas_msgs},
    o que você precisa saber sobre o usuario: {contexto_do_usuario}

    Mensagem do Usuario:
    {perguntaUSU}
    """
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=contexto_formatado
        )
        return response.text
    
    except ResourceExhausted as e: 
        print(f"Error na API")
        print('Tentando uma nova solução...')
        
        time.sleep(3)
        os.system('cls')
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contexto_formatado
        )
        return response.text
    
    except ResourceExhausted as e: 
        print(f"Error na API")
        print('Tentando uma nova solução...')
        
        time.sleep(3)
        os.system('cls')
        
        response = clienttwo.models.generate_content(
            model="gemini-3-flash-preview",
            contents=contexto_formatado
        )
        return response.text
        
    except Exception as e:
        print(f"Error na API : {e}")