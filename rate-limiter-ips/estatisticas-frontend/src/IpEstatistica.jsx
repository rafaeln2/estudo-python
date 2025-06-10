import React, { useState, useEffect } from 'react';
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';

const COLORS = ['#00FF00', '#FF0000'];

export default function IpStats() {
  const [data, setData] = useState([]);
  const [selectedIp, setSelectedIp] = useState(null);
  const [rotas, setRotas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Carrega todos os IPs na montagem
  useEffect(() => {
    fetch('http://localhost:5000/estatisticas')
      .then((response) => {
        if (!response.ok) throw new Error('Erro na requisição');
        return response.json();
      })
      .then((json) => {
        const formattedData = Object.entries(json).map(([ip, stats]) => ({
          ip,
          aceitas: stats.aceitas,
          rejeitadas: stats.rejeitadas,
        }));
        setData(formattedData);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  // Ao clicar no IP, define o IP e busca todos os acessos por cada rota
  const handleIpClick = (ipObj) => {
    setSelectedIp(ipObj);
    fetch(`http://localhost:5000/acessos-rotas-por-ip?ip=${ipObj.ip}`)
      .then((res) => {
        if (!res.ok) throw new Error('Erro ao buscar rotas');
        return res.json();
      })
      .then((data) => setRotas(data))
      .catch((err) => {
        console.error(err);
        setRotas([]);
      });
  };

  if (loading) return <p>Carregando...</p>;
  if (error) return <p>Erro: {error}</p>;

  const chartData = selectedIp
    ? [
        { name: 'Aceitas', value: selectedIp.aceitas },
        { name: 'Rejeitadas', value: selectedIp.rejeitadas },
      ]
    : [];

  return (
    <div style={{ padding: 20, display: 'flex', gap: 40 }}>
      <div>
        <h2>Lista de IPs</h2>
        <ul style={{ cursor: 'pointer', listStyle: 'none', padding: 0 }}>
          {data.map((item) => (
            <li
              key={item.ip}
              onClick={() => handleIpClick(item)}
              style={{
                padding: '8px 12px',
                margin: '4px 0',
                borderRadius: 4,
                backgroundColor:
                  selectedIp?.ip === item.ip ? '#d3e0ff' : 'transparent',
              }}
            >
              {item.ip}
            </li>
          ))}
        </ul>
      </div>

      <div>
        {selectedIp ? (
          <>
            <h2>Estatísticas de {selectedIp.ip}</h2>
            <PieChart width={300} height={300}>
              <Pie
                data={chartData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                outerRadius={100}
                label
              >
                {chartData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>

            <div>
              <h3>Rotas acessadas</h3>
              <ul>
                {rotas.length === 0 ? (
                  <li>Nenhuma rota encontrada</li>
                ) : (
                  rotas.map((rota, idx) => (
                    <li key={idx}>
                      {rota.rota} — {rota.total_requisicoes} acessos
                    </li>
                  ))
                )}
              </ul>
            </div>
          </>
        ) : (
          <p>Clique em um IP para ver estatísticas</p>
        )}
      </div>
    </div>
  );
}
