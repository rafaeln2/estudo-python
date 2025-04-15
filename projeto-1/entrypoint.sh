#!/bin/bash

# Espera o banco de dados aceitar conexões (host e porta dependem do seu banco)
echo "Aguardando o banco de dados ficar pronto..."

# Espera o container 'db' na porta 5432 (PostgreSQL) — pode usar outro host/porta
while ! nc -z db 5432; do
  sleep 1
done

echo "Banco disponível. Executando migrations..."
alembic upgrade head

echo "Iniciando aplicação FastAPI com Uvicorn..."
# exec uvicorn main:app --host 0.0.0.0 --port 8000
exec "$@"