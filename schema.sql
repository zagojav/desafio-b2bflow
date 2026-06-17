-- Tabela de contatos para o disparo de mensagens.
-- Rode este script no SQL Editor do Supabase.

create table if not exists contatos (
    id        bigint generated always as identity primary key,
    nome      text not null,
    telefone  text not null,
    criado_em timestamptz not null default now()
);

-- Contatos de exemplo. Troque pelos seus números de teste.
-- Telefone no formato só dígitos, com DDI: 55 + DDD + número.
insert into contatos (nome, telefone) values
    ('Marcelo', '5511999999999'),
    ('Zago',    '5511888888888');
