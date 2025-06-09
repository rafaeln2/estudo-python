import React from 'react';

export default function AcessosPorIP({ rotas }) {
  if (!rotas || rotas.length === 0) {
    return <p>Nenhuma rota acessada disponível.</p>;
  }

  return (
    <div>
      <h3>Rotas acessadas</h3>
      <ul>
        {rotas.map((rota, index) => (
          <li key={index}>
            <strong>{rota.rota}</strong>: {rota.total_requisicoes} acessos
          </li>
        ))}
      </ul>
    </div>
  );
}
