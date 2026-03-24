import unicodedata
import time
import os

def limpar_json_resposta(resposta: str) -> str:
    if not resposta:
        return ""

    resposta = resposta.replace("```json", "").replace("```", "")

    resposta = resposta.strip()

    inicio = resposta.find("{")
    fim = resposta.rfind("}")

    if inicio == -1 or fim == -1:
        return ""

    return resposta[inicio:fim+1]

def remover_acentos(texto: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ) 
    
def criarVariaveisDeAmbiente(): 
    print("✧ Inicializando interface neural...")
    time.sleep(1)
    print("Para prosseguir com a síntese, valide sua identidade digital.")
    time.sleep(1)

    AttChavekeyGemini = input("▮ Autenticação (API Key Gemini): ")

    with open(".env", "a") as f: 
        f.write(f"\nGEMINI_API_KEY={AttChavekeyGemini}")

    os.system("cls")

    while True: 
        print("\n✧ Módulo de redundância detectado...")
        time.sleep(1)
        print("Para evitar interrupções durante o uso da ATHENA, você pode adicionar uma chave secundária da API.")
        time.sleep(1)
        print("Cada chave possui um limite de requisições. Ao registrar uma segunda chave, o sistema alterna automaticamente entre elas, permitindo um uso contínuo por mais tempo.\n")
        time.sleep(1)

        print("▮ Deseja registrar uma chave adicional? (Y/N)")
        print("▮ Ou digite 'desistir' para cancelar esta etapa.")
        adicionarSegundaChave = input("> ")

        if adicionarSegundaChave.lower() == "y":
            os.system("cls")

            print("✧ Iniciando protocolo de autenticação secundária...")
            time.sleep(1)

            AttSecondChavekeyGemini = input("▮ Autenticação (API Key Secundária): ")

            with open(".env", "a") as f: 
                f.write(f"\nGEMINI_API_KEY_TWO={AttSecondChavekeyGemini}")

            os.system("cls")
            print("✧ Chave secundária integrada com sucesso.")
            time.sleep(1)
            break

        elif adicionarSegundaChave.lower() == "n" or "desistir":
            print("\n✧ Operando com apenas uma chave de acesso.")
            time.sleep(1)
            break

        else:
            os.system("cls")
            print("⚠ Entrada inválida. Responda com Y ou N.")