

import logging
import sys
import time

import config
from supabase_client import buscar_contatos
from zapi_client import enviar_mensagem

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("disparo")


def montar_mensagem(nome: str) -> str:
    """Monta a mensagem personalizada com o nome do contato."""
    return f"Olá, {nome.strip()} tudo bem com você?"


def main() -> int:
    logger.info("Iniciando disparo de mensagens.")

    try:
        config.validar()
    except config.ConfigError as erro:
        logger.error("Configuração incompleta: %s", erro)
        return 1

    try:
        contatos = buscar_contatos()
    except Exception as erro:
        logger.error("Não consegui buscar os contatos no Supabase: %s", erro)
        return 1

    if not contatos:
        logger.warning("Nenhum contato cadastrado. Nada pra enviar.")
        return 0

    enviados = 0
    falhas = 0

    for indice, contato in enumerate(contatos):
        nome = contato.get("nome")
        telefone = contato.get("telefone")

        if not nome or not telefone:
            logger.warning("Contato com dados incompletos, pulando: %s", contato)
            falhas += 1
            continue

        mensagem = montar_mensagem(nome)

        try:
            enviar_mensagem(telefone, mensagem)
            logger.info("Mensagem enviada para %s (%s).", nome, telefone)
            enviados += 1
        except Exception as erro:
            logger.error("Falha ao enviar para %s (%s): %s", nome, telefone, erro)
            falhas += 1

        # Pausa entre os envios, menos depois do último contato
        if indice < len(contatos) - 1:
            time.sleep(config.INTERVALO_ENTRE_ENVIOS)

    logger.info("Fim do disparo. Enviadas: %d | Falhas: %d", enviados, falhas)
    return 0 if falhas == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
