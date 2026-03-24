import time
from init import athena_intro
from athenaLogicResponse import responder
from functions import carregarJson, salvarMsg
from colorama import Fore, init
from rich.console import Console
from rich.panel import Panel

"""
Entry point da aplicação.
Gerencia o loop principal, entrada do usuário e exibição das respostas.
"""

init()

if __name__ == "__main__":
    athena_intro()
    
console = Console()

while True:
    pergunta = input(f"{Fore.LIGHTWHITE_EX} > ")
    print('')
    config = carregarJson()

    if not config or len(config) < 1:
        pergunta = "config"
    
    if pergunta.lower() in ["sair", "exit", "quit"]:
        break
    
    resposta = responder(pergunta)
    
    time.sleep(0.1)
    console.print(Panel(f"> {resposta}", title="Athena", border_style="grey37"))
    print('')
    
    salvarMsg(mensagemAI=resposta, mensagemUsu=pergunta)