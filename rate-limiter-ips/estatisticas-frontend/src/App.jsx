import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [stats, setStats] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/estatisticas') // ajuste a URL do seu backend
      .then(response => setStats(response.data))
      .catch(err => setError('Erro ao buscar estatísticas'));
  }, []);

  if (error) return <div>{error}</div>;
  if (!stats) return <div>Carregando estatísticas...</div>;

  return (
    <div style={{ padding: '1rem' }}>
      <h1>📊 Estatísticas de Requisições por IP</h1>
      <ul>
        {Object.entries(stats).map(([ip, contagem]) => (
          <li key={ip}>
            IP {ip} - Aceitas: {contagem.aceitas}, Rejeitadas: {contagem.rejeitadas}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;