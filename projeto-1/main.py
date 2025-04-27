from fastapi import FastAPI
from controller import UsuarioController, CursoController, AuthController, MensageriaController

app = FastAPI()

app.include_router(UsuarioController.router_publico, prefix="/usuarios")
app.include_router(UsuarioController.router, prefix="/usuarios")
app.include_router(CursoController.router, prefix="/cursos")
app.include_router(AuthController.router, prefix="/auth")
app.include_router(MensageriaController.router_publico, prefix="/mensageria")