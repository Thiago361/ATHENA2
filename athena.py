import time;
from init import athena_intro
from athenabrain import responder
from functions import carregarJson
from colorama import Fore
from functions import salvarMsg

if __name__ == "__main__":
    athena_intro()

while True: 
    pergunta = input(f"{Fore.LIGHTWHITE_EX}você: ")
    config = carregarJson()
    if not config or len(config) < 1:
        pergunta = "configuracao"
    
    if pergunta.lower() in ["sair", "exit", "quit"]:
        break
    
    resposta = responder(pergunta)
    time.sleep(0.1)
    print(f"\n{Fore.BLACK}Athena: {resposta}")
    salvarMsg(mensagemAI=resposta, mensagemUsu=pergunta)
    
    
    


    

