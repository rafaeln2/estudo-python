from Aggregator import prepara_dados_estatisticas
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permite requisições do frontend (localhost:3000 por exemplo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/estatisticas")
def estatisticas():
    # Sua função que gera as stats, adaptada para retornar JSON:
    stats = prepara_dados_estatisticas()
    return stats
