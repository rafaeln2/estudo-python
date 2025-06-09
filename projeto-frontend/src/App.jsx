import { useState } from "react";

function App(){
  const [message, setMessage] = useState("Mensagem variavel");

  function handleClick() {
    if (message === "Mensagem variavel") {
      setMessage("botão clicado");
    } else {
      setMessage("Mensagem variavel");
    }
  }
  return (
    <div>
      <h1>{message}</h1>
      <button onClick={handleClick}>Clique aqui</button>
    </div>
  )
}

export default App