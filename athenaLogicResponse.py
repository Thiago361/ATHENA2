import unicodedata
from functions import salvarJson, carregarJson
from AthenaAIBrain import enviarMsgAi
from init import athena_intro_no_loading
import os

def remover_acentos(texto: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

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
        
    resposta = enviarMsgAi(perguntaUSU=pergunta)
    return resposta
    
    
    
    
    
