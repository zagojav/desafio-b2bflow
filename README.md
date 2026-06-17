# Disparo de mensagens — Supabase + Z-API

Lê os contatos cadastrados no Supabase e dispara, via Z-API, a mensagem:

> Olá, {nome} tudo bem com você?

Projeto feito para o desafio de estágio em Python da b2bflow.

## Stack

- Python 3.10+
- [Supabase](https://supabase.com) — banco dos contatos
- [Z-API](https://z-api.io) — envio no WhatsApp

## Estrutura

```
.
├── main.py             # ponto de entrada: orquestra leitura e envio
├── config.py           # carrega e valida as variáveis do .env
├── supabase_client.py  # leitura dos contatos no Supabase
├── zapi_client.py      # envio das mensagens pela Z-API
├── schema.sql          # cria a tabela de contatos
├── requirements.txt
└── .env.example
```

## 1. Banco (Supabase)

1. Crie um projeto em https://supabase.com.
2. No **SQL Editor**, rode o conteúdo do `schema.sql` — ele cria a tabela `contatos` e insere dois exemplos.
3. Troque os telefones de exemplo pelos seus números de teste. Formato: só dígitos, com DDI — `55` + DDD + número (ex.: `5511999999999`). O código também aceita número com máscara e normaliza sozinho.

> A tabela é de teste, então deixe o **RLS desligado** nela (ou crie uma policy de `select`). Com a chave anônima e o RLS ligado sem policy, a leitura volta vazia.

## 2. Variáveis de ambiente

Copie o modelo e preencha:

```bash
cp .env.example .env
```

| Variável | Onde encontrar |
|---|---|
| `SUPABASE_URL` / `SUPABASE_KEY` | Supabase → Project Settings → API (use a *anon key*) |
| `ZAPI_INSTANCE_ID` / `ZAPI_TOKEN` | painel da instância em https://app.z-api.io |
| `ZAPI_CLIENT_TOKEN` | Z-API → Segurança → token da conta (vai no header `Client-Token`) |

Antes de rodar, conecte a instância da Z-API ao WhatsApp (leitura do QR Code no painel).

## 3. Rodar

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Saída esperada:

```
10:32:01 [INFO] Iniciando disparo de mensagens.
10:32:02 [INFO] Encontrei 2 contato(s) na tabela 'contatos'.
10:32:03 [INFO] Mensagem enviada para Marcelo (5511999999999).
10:32:05 [INFO] Mensagem enviada para Zago (5511888888888).
10:32:05 [INFO] Fim do disparo. Enviadas: 2 | Falhas: 0
```
