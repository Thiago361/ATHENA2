from functions import salvarJson, escutarMusica, limpar_json_resposta, remover_acentos
from AthenaAIBrain import EvaluateMessages, UtilityFunctions, UtilityChat
from init import athena_intro_no_loading
import json
import os
from contextsFunctions import contextoFuncaoSpotify

"""
Camada de processamento de mensagens.
Interpreta intenções do usuário e direciona para as funcionalidades apropriadas.
"""

def responder(pergunta: str) -> str:
    pergunta = remover_acentos(pergunta.lower())
    
    if "cls" in pergunta or "limpar" in pergunta:
        os.system("cls")
        athena_intro_no_loading()
        return "Tela limpa e reiniciada! 😎"
    
    elif "configuracao" in pergunta or "config" in pergunta :
        print("\nvamos fazer a sua configuração pra eu saber mais de você ☺️\n"
        "preciso que você me conte")
        nomeUsuario = input("\nseu nome ou como você gosta de ser chamado(a): ")
        cidadeUsuario = input("\nsua cidade: ")
        salvarJson(nomeUsuario, cidadeUsuario)
        os.system("cls")
        athena_intro_no_loading()

    resposta = EvaluateMessages(perguntaUSU=pergunta)
    resposta_limpa_AI = limpar_json_resposta(resposta)
    resposta_json = json.loads(resposta_limpa_AI)
    
    if resposta_json["intent"] == "chat":
        resposta_chat_raw = UtilityChat(pergunta)
        resposta_chat_raw_limpa = limpar_json_resposta(resposta_chat_raw)
        resposta_chat = json.loads(resposta_chat_raw_limpa)
        return resposta_chat["resposta"]
    
    elif resposta_json["intent"] == "spotify":
        resposta_spotify_raw = UtilityFunctions(pergunta, contextoFuncaoSpotify)
        resposta_spotify_raw_limpa = limpar_json_resposta(resposta_spotify_raw)
        resposta_spotify = json.loads(resposta_spotify_raw_limpa)
        escutarMusica(resposta_spotify["musica"])
        return resposta_spotify["frase"]
    
    
        
        
    return resposta
    
    
    
    
    
