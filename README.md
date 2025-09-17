# 🤖 ATHENA2 - Assistente de IA pra ser sua grande amiga

<div align="center">

![ATHENA Logo](https://img.shields.io/badge/ATHENA-CMD%20Assistant-blue?style=for-the-badge&logo=terminal)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge&logo=python)
![Google AI](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge&logo=google)

*Uma assistente de IA simples e direta para rodar no terminal, inspirada no Claude Code mas... pra conversa*

</div>

## ✨ Sobre o Projeto

ATHENA2 é um projeto **simples e minimalista** de assistente de IA conversacional desenvolvido em Python para rodar diretamente no **CMD/Terminal**. Inspirado no Claude Code, o projeto foi criado com foco na **simplicidade e praticidade**, utilizando a API do Google Gemini para criar interações naturais e amigáveis.

**🎯 Filosofia**: Simplicidade acima de tudo - sem interfaces complexas, sem dependências desnecessárias, apenas uma IA conversacional que funciona perfeitamente no terminal.

### 🎯 Características Principais

- **🖥️ Terminal-First**: Projetado especificamente para CMD/terminal
- **🤖 IA Conversacional**: Powered by Google Gemini 2.0 Flash
- **⚡ Simples e Rápido**: Sem interfaces complexas, apenas texto no terminal
- **💾 Memória de Conversas**: Salva e lembra do histórico de mensagens
- **🎨 Interface Colorida**: Terminal com cores e animações simples
- **⚙️ Configuração Mínima**: Setup rápido e direto
- **🔄 Comandos Especiais**: Limpeza de tela e configurações
- **📝 Logs de Conversa**: Armazena todas as interações em JSON

## 🚀 Instalação e Configuração

### Pré-requisitos

- **Python 3.11+** (instalado e configurado)
- **CMD/Terminal** (Windows, Linux ou Mac)
- **Conta no Google AI Studio** (gratuita)
- **Chave de API do Google Gemini** (gratuita)

> **💡 Inspiração Claude Code**: Assim como o Claude Code, este projeto prioriza a simplicidade e eficiência no terminal, sem interfaces gráficas desnecessárias.

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/ATHENA2.git
cd ATHENA2
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API Key

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_api_aqui
```

**Como obter a chave da API:**
1. Acesse [Google AI Studio](https://aistudio.google.com/)
2. Faça login com sua conta Google
3. Crie um novo projeto
4. Gere uma chave de API
5. Cole a chave no arquivo `.env`

## 🎮 Como Usar

### Executar no CMD

```bash
# Windows CMD
python athena.py

# Linux/Mac Terminal
python3 athena.py
```

### Comandos Disponíveis

- **Conversação Normal**: Digite qualquer mensagem para conversar
- **`cls` ou `limpar`**: Limpa a tela e reinicia a interface
- **`configuracao` ou `config`**: Abre o assistente de configuração
- **`sair`, `exit`, `quit`**: Encerra o programa

### Primeira Execução

Na primeira vez que executar o programa, a ATHENA irá:
1. Mostrar uma animação de carregamento no terminal
2. Solicitar configurações básicas (nome e cidade)
3. Iniciar a conversa de forma personalizada

> **🖥️ Terminal-First**: Toda a interação acontece diretamente no CMD/terminal, sem interfaces gráficas ou web.

## 📁 Estrutura do Projeto

```
ATHENA2/
├── athena.py              # Arquivo principal
├── AthenaAIBrain.py       # Lógica da IA e integração com Gemini
├── athenabrain.py         # Processamento de mensagens e comandos
├── functions.py           # Funções utilitárias (JSON, configurações)
├── init.py               # Interface e animações
├── requirements.txt      # Dependências do projeto
├── README.md            # Este arquivo
├── .env                 # Variáveis de ambiente (criar)
├── config.json          # Configurações do usuário (gerado automaticamente)
├── contextoCvs.json     # Histórico de conversas (gerado automaticamente)
└── venv/                # Ambiente virtual Python
```

## 🔧 Funcionalidades Detalhadas

### 🧠 Sistema de IA

- **Modelo**: Google Gemini 2.0 Flash
- **Personalidade**: Amigável, criativa e acolhedora
- **Memória**: Lembra do contexto das conversas anteriores
- **Respostas**: Adapta o tom conforme a importância da pergunta

### 💾 Sistema de Dados

- **Configurações**: Salvas em `config.json`
- **Conversas**: Histórico em `contextoCvs.json`
- **Persistência**: Dados mantidos entre sessões

### 🖥️ Interface Terminal

- **Cores**: Terminal colorido com colorama
- **Animações**: Loading bar e ASCII art simples
- **Formatação**: Quebras de linha e espaçamento adequado
- **Simplicidade**: Interface limpa e direta, sem elementos desnecessários

> **🎯 Inspiração Claude Code**: Assim como o Claude Code, o foco está na funcionalidade e simplicidade, não em interfaces complexas.

## 🛠️ Desenvolvimento

### Dependências Principais

- `google-generativeai`: Integração com Google Gemini
- `python-dotenv`: Gerenciamento de variáveis de ambiente
- `colorama`: Cores no terminal
- `json`: Manipulação de dados

### Estrutura de Código

- **Modular**: Cada funcionalidade em arquivo separado
- **Orientado a Funções**: Código organizado em funções específicas
- **Tratamento de Erros**: Validação de dados e arquivos
- **Documentação**: Código comentado e legível

## 📝 Exemplo de Uso

```
C:\Users\usuario\ATHENA2> python athena.py

você: Oi Athena!

Athena: E aí! 😄 Que bom te ver por aqui! Eu sou a ATHENA, sua assistente e amiga digital. Como você está se sentindo hoje?

você: Estou estudando Python

Athena: Que legal! 🐍 Python é uma linguagem incrível! Está gostando? Se precisar de alguma ajuda com código ou conceitos, pode contar comigo! ✨

você: sair

C:\Users\usuario\ATHENA2>
```

> **🖥️ Terminal Simples**: Toda a interação acontece diretamente no CMD, sem interfaces web ou gráficas complexas.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- [Google AI](https://ai.google/) pelo Gemini
- Comunidade Python
- Desenvolvedores de código aberto

---

<div align="center">

**Feito com ❤️, Python é vidaa**

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-First-green?style=for-the-badge&logo=terminal&logoColor=white)

*Simplicidade, eficiência e funcionalidade*

</div>
