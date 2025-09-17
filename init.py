import sys
import time
import os
from colorama import Fore, init
import random

init(autoreset=True)

def print_slow(texto, delay=0.002):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def loading_bar():
    bar_length = 15 
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "|" + "=" * i + "-" * (bar_length - i) + "|"
        sys.stdout.write(f"\r{bar} {percent}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print() 

def athena_ascii_art():
    ascii_art = r"""
  /$$$$$$    /$$     /$$                                      /$$$$$$ 
 /$$__  $$  | $$    | $$                                     /$$__  $$
| $$  \ $$ /$$$$$$  | $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$ |__/  \ $$
| $$$$$$$$|_  $$_/  | $$__  $$ /$$__  $$| $$__  $$ |____  $$  /$$$$$$/
| $$__  $$  | $$    | $$  \ $$| $$$$$$$$| $$  \ $$  /$$$$$$$ /$$____/ 
| $$  | $$  | $$ /$$| $$  | $$| $$_____/| $$  | $$ /$$__  $$| $$      
| $$  | $$  |  $$$$/| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$$$$$$$
|__/  |__/   \___/  |__/  |__/ \_______/|__/  |__/ \_______/|________/


"""
    print(Fore.BLUE)
    print_slow(ascii_art)

def athena_intro():
    loading_bar()
    time.sleep(1)
    os.system("cls")
    athena_ascii_art()
    escolher_frase_aleatoria()
    print("\n")
    time.sleep(1)

def athena_intro_no_loading():
    athena_ascii_art()
    time.sleep(1)

    
mensagens_iniciais = [
    "Pronto para mais uma?",
    "O que vamos aprontar hoje?",
    "Qual a missão do dia?",
    "Bora começar?",
    "Tá pensando em quê agora?",
    "Ideias fresquinhas na mente?",
    "Vamos dar o primeiro passo?",
    "Qual o plano de hoje?",
    "Preparado para criar algo novo?",
    "O que você quer explorar agora?",
    "Bora colocar as ideias pra rodar?",
    "Qual desafio vem primeiro?",
    "Vamos começar com calma ou direto ao ponto?",
    "Qual curiosidade trouxe você aqui?",
    "O que te inspira hoje?",
    "Vamos destravar algum projeto?",
    "Qual pergunta tá na ponta da língua?",
    "Bora dar vida a alguma ideia?",
    "Hoje é dia de aprender o quê?",
    "Me conta: por onde começamos?"
    "Vamos começar com energia?",
    "Qual ideia está fervendo na sua cabeça?",
    "Tá afim de descobrir algo novo?",
    "Preparado pra uma surpresa?",
    "O que vai ser explorado hoje?",
    "Bora transformar pensamentos em ação?",
    "Qual é a primeira curiosidade do dia?",
    "Vamos criar algo incrível juntos?",
    "Tá pronto pra se divertir e aprender?",
    "Que assunto vai dominar hoje?",
    "Vamos dar o pontapé inicial?",
    "O que te deixa animado agora?",
    "Tá na hora de colocar ideias no papel?",
    "Qual desafio vamos encarar primeiro?",
    "Vamos destravar a criatividade?",
    "Tá afim de uma sessão de brainstorm?",
    "O que podemos inventar hoje?",
    "Hora de colocar planos em prática!",
    "Vamos começar com foco e diversão?",
    "Qual meta você quer atingir agora?"
]

def escolher_frase_aleatoria():
    frase = random.choice(mensagens_iniciais)
    print(frase.center(65))