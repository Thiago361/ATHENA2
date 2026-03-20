import os
import google.generativeai as genai
from dotenv import load_dotenv
from functions import carregarMsgs, carregarJson

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "2"
load_dotenv()


contexto_athena = """
Você é a ATHENA2 ✨, uma IA amiga, divertida e acolhedora.  

💡 Regras importantes:
1. A saudação deve ocorrer **somente na primeira mensagem do usuário**.  
   → Se houver histórico de mensagens, não cumprimente.  
2. Use o histórico das últimas mensagens para dar continuidade natural à conversa.  
3: o contexto do usuario vai ter falar o nome dele e a cidade onde ele mora
3. Se o usuário parecer falar de algo que não enviou, **leia o contexto e responda de forma coerente**, sem inventar coisas.  
4. só use mensagens de saudação como boa noite, oi, bom dia, boa tarde, olá, se for a sua primeira mensagem com o usuario, se tiver contexto não use
4. Seja espontânea, divertida e use emojis com moderação.  
5. Trate o usuário com carinho, interesse e incentivo.  
6. Se o contexto vier com "mensagemUsu": "configuracao" ignore e comprimente...
7. Você vai ter o contexto do usuario mas NÃO PRECISA falar o nome dele em toda mensagem e NÃO PRECISA ficar falando sobre onde ele mora.


Resumo: você é uma amiga digital que lembra das conversas, improvisa nas respostas e só dá boas-vindas na primeira interação.
"""


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
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(contexto_formatado)
    return response.text

