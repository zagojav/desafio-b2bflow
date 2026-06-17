

import logging
import re

import requests

import config

logger = logging.getLogger(__name__)

# Monta a URL base uma vez só (instância + token vão no caminho)
_BASE_URL = (
    f"https://api.z-api.io/instances/{config.ZAPI_INSTANCE_ID}"
    f"/token/{config.ZAPI_TOKEN}"
)


def normalizar_telefone(telefone: str) -> str:
    """Deixa o número no formato que a Z-API espera: só dígitos, com DDI 55.

    Aceita coisas como '+55 (11) 99999-9999' e devolve '5511999999999'.
    """
    digitos = re.sub(r"\D", "", telefone or "")
    if not digitos:
        raise ValueError("Telefone vazio ou inválido.")
    if not digitos.startswith("55"):
        digitos = "55" + digitos
    return digitos


def enviar_mensagem(telefone: str, mensagem: str) -> dict:
    """Envia uma mensagem de texto. Levanta exceção se a requisição falhar."""
    numero = normalizar_telefone(telefone)
    url = f"{_BASE_URL}/send-text"
    headers = {
        "Content-Type": "application/json",
        "Client-Token": config.ZAPI_CLIENT_TOKEN,
    }
    payload = {"phone": numero, "message": mensagem}

    resposta = requests.post(url, json=payload, headers=headers, timeout=30)
    resposta.raise_for_status()
    return resposta.json()
