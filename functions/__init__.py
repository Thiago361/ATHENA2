# ATHENA2 - Módulo de Funções

from .saves import salvarJson, carregarJson, salvarMsg, carregarMsgs, ExcluirMsgs
from .spotify import escutarMusica
from .utils import limpar_json_resposta, remover_acentos

__all__ = ['salvarJson', 'carregarJson', 'salvarMsg', 'carregarMsgs', 'ExcluirMsgs', 'escutarMusica', 'limpar_json_resposta']
