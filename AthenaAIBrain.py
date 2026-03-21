import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from functions import carregarMsgs, carregarJson
from google.api_core.exceptions import ResourceExhausted
from contextsFunctions import contexto_athena

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "2"
load_dotenv()


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
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-2.5-flash-lite')
        response = model.generate_content(contexto_formatado)
        return response.text
    
    except ResourceExhausted as e: 
        print(f"Error na API : {e}")
        print('Tentando uma nova solução...')
        
        time.sleep(3)
        os.system('cls')
        
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(contexto_formatado)
        return response.text
        
    
    except Exception as e:
        print(f"Error na API : {e}")

