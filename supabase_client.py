

import logging

from supabase import Client, create_client

import config

logger = logging.getLogger(__name__)


def conectar() -> Client:
    """Cria o cliente do Supabase com as credenciais do .env."""
    return create_client(config.SUPABASE_URL, config.SUPABASE_KEY)


def buscar_contatos() -> list[dict]:
    """Retorna todos os contatos cadastrados (nome e telefone)."""
    supabase = conectar()
    resposta = (
        supabase.table(config.TABELA_CONTATOS)
        .select("nome, telefone")
        .execute()
    )
    contatos = resposta.data or []
    logger.info(
        "Encontrei %d contato(s) na tabela '%s'.",
        len(contatos),
        config.TABELA_CONTATOS,
    )
    return contatos
