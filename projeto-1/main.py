from fastapi import FastAPI
from controller import UsuarioController, CursoController

app = FastAPI()

app.include_router(UsuarioController.router, prefix="/usuarios")
app.include_router(CursoController.router, prefix="/cursos")