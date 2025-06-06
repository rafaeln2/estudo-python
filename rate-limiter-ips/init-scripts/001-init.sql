CREATE TABLE log_requisicoes (
    id SERIAL PRIMARY KEY,
    ip TEXT NOT NULL,
    rota TEXT NOT NULL,
    status BOOLEAN NOT NULL,  -- TRUE = aceito, FALSE = rejeitado
    criado_em TIMESTAMP NOT NULL
);