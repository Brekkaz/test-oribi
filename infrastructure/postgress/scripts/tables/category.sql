CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
create table if not exists category (
    id UUID not null default (uuid_generate_v4()),
    name varchar(50) UNIQUE not null,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    deleted_at timestamptz,
    primary key (id)
);