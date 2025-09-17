import sys
import time
import os
from colorama import Fore, init

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
    time.sleep(1)

def athena_intro_no_loading():
    athena_ascii_art()
    time.sleep(1)

def athena_intro_no_loading_ai():
    ascii_art_ai = r"""
    /$$$$$$    /$$     /$$                                                                            
 /$$__  $$  | $$    | $$                                                                            
| $$  \ $$ /$$$$$$  | $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$         /$$$$$$   /$$$$$$  /$$  /$$  /$$
| $$$$$$$$|_  $$_/  | $$__  $$ /$$__  $$| $$__  $$ |____  $$       /$$__  $$ /$$__  $$| $$ | $$ | $$
| $$__  $$  | $$    | $$  \ $$| $$$$$$$$| $$  \ $$  /$$$$$$$      | $$  \ $$| $$$$$$$$| $$ | $$ | $$
| $$  | $$  | $$ /$$| $$  | $$| $$_____/| $$  | $$ /$$__  $$      | $$  | $$| $$_____/| $$ | $$ | $$
| $$  | $$  |  $$$$/| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$      |  $$$$$$$|  $$$$$$$|  $$$$$/$$$$/
|__/  |__/   \___/  |__/  |__/ \_______/|__/  |__/ \_______/       \____  $$ \_______/ \_____/\___/ 
                                                                   /$$  \ $$                        
                                                                  |  $$$$$$/                        
                                                                   \______/                               
"""
    print(Fore.BLUE)
    print_slow(ascii_art_ai)
    time.sleep(1)

# Teste
if __name__ == "__main__":
    athena_intro()
