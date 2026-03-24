import unicodedata

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