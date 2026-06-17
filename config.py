

import os

from dotenv import load_dotenv

load_dotenv()

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Z-API
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

# Nome da tabela de contatos (dá pra trocar pelo .env, mas o padrão já serve)
TABELA_CONTATOS = os.getenv("TABELA_CONTATOS", "contatos")

# Pausa em segundos entre um envio e outro, pra não atropelar a fila do WhatsApp
INTERVALO_ENTRE_ENVIOS = float(os.getenv("INTERVALO_ENTRE_ENVIOS", "2"))


class ConfigError(Exception):
    """Disparada quando falta alguma variável obrigatória no .env."""


def validar():
    """Confere se todas as credenciais necessárias foram preenchidas."""
    obrigatorias = {
        "SUPABASE_URL": SUPABASE_URL,
        "SUPABASE_KEY": SUPABASE_KEY,
        "ZAPI_INSTANCE_ID": ZAPI_INSTANCE_ID,
        "ZAPI_TOKEN": ZAPI_TOKEN,
        "ZAPI_CLIENT_TOKEN": ZAPI_CLIENT_TOKEN,
    }
    faltando = [nome for nome, valor in obrigatorias.items() if not valor]
    if faltando:
        raise ConfigError(
            "Faltam variáveis no .env: " + ", ".join(faltando)
        )
