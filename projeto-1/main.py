from config.session import get_db
from config.engine import engine
from config.base import Base
from models import Usuario, Curso, usuario_curso

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Exemplo de uso do banco
def main():
    db = get_db()
    u1 = Usuario.Usuario(nome="Charls", email="charls@email.com")
    u2 = Usuario.Usuario(nome="Sam", email="Sam@email.com")
    u3 = Usuario.Usuario(nome="Nick", email="n1ck@gmail.com")
    
    c1 = Curso.Curso(nome="Curso de Alquimia")
    c2 = Curso.Curso(nome="Como bombardear o governo americano")

    usuarios = [u1, u2, u3]
    for u in usuarios:
        print(f"{u.id} - {u.nome} - {u.email}")
        if u.nome == "Charls":
            u.cursos.append(c1)
            u.cursos.append(c2)
        elif u.nome == "Sam":
            u.cursos.append(c1)
        else:
            u.cursos.append(c2)
    db.add_all((c1, c2))
    db.add_all((usuarios[0], usuarios[1], usuarios[2]))
    db.commit()

    resultado = db.query(Usuario.Usuario).all()
    for u in resultado:
        print(f"{u.id} - {u.nome} - {u.email}")
        print([curso for curso in u.cursos])
    db.close()
    Base.metadata.drop_all(engine)

if __name__ == "__main__":
    main()