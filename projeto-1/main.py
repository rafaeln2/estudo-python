from fastapi import FastAPI
from controller import UsuarioController, CursoController, AuthController, CeleryController

app = FastAPI()

app.include_router(UsuarioController.router_publico, prefix="/usuarios")
app.include_router(UsuarioController.router, prefix="/usuarios")
app.include_router(CursoController.router, prefix="/cursos")
app.include_router(AuthController.router, prefix="/auth")
app.include_router(CeleryController.router_publico, prefix="/mensageria")