contextoFuncaoSpotify = """
O usuário quer tocar música no Spotify.

Sua tarefa é extrair o nome da música ou do artista mencionado na frase do usuário.

Regras:
- Retorne SOMENTE um JSON
- Não explique nada
- Não escreva texto fora do JSON
- A música deve estar na chave "musica"
- Gere/crie também uma frase curta e natural confirmando a ação

A frase deve ser algo como: (exemplos)
- "Pode deixar, vou dar play 😎"
- "Já tô colocando pra tocar 🔥"
- "Boa escolha, tocando agora 🎧"
- "Deixa comigo, já vai começar"
    (seja criativa)

Formato:
{"musica": "nome da musica ou artista", "frase": "frase gerada"}

Mensagem do usuário:
"""