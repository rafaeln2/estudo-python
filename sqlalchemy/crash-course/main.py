from sqlalchemy import create_engine, Table, Column, Integer, String, Insert,Float, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


engine = create_engine('sqlite:///mydatabase.db', echo=True) # engine prepara a conexão, depois chama ela com o Session pra abrir a conexão
Base = declarative_base() # quem lida com a criacao das tabelas. É passado no parametro quando cria uma classe nova

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    age = Column("age", Integer)
    
    things = relationship("Thing", back_populates="user_relationship") # relacionamento com a tabela Thing

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column("description", String, nullable=False)
    value = Column(Float)
    user = Column(Integer, ForeignKey("users.id"), nullable=False) #owner
    
    user_relationship = relationship("User", back_populates="things") # relacionamento com a tabela User

Base.metadata.create_all(engine) # cria as tabelas no banco de dados

Session = sessionmaker(bind=engine)
session = Session() # abre a conexão com o banco de dados

#select
print(session.query(User.name).all()) # busca todos os nomes da tabela Person

#delete
# result = session.query(Thing).filter(Thing.description == "Stuff").delete() # deleta o objeto Thing com a descrição "Stuff"
# session.commit() # salva as alterações no banco de dados 

#select all
# result = session.query(Thing).all() # busca todos os objetos Thing com a descrição "Stuff"
# print([thing.description for thing in result]) # imprime o resultado da busca, que deve ser uma lista vazia

result = session.query(User.name, Thing.description).join(Thing).all() # busca todos os nomes da tabela Person e as descrições da tabela Thing
print(result) # imprime o resultado da busca, que deve ser uma lista de tuplas com os nomes e as descrições

#update
def update_thing_and_print(User, Thing, session):
    usuario = session.query(User).filter(User.name == "charls").first() # busca o usuário com o nome "charls" no banco de dados
    new_thing = Thing(description="Stuff", value=15.0, user=usuario.id) # cria um novo objeto Thing
    session.add(new_thing) # adiciona o novo objeto Thing à sessão
    session.commit() # salva as alterações no banco de dados
    result = session.query(Thing).filter(Thing.description == "Stuff").update({"description": "New Stuff from the gumroad"}) 
    print([thing.description for thing in (session.query(Thing).filter(Thing.user == usuario.id).all())])

# update_thing_and_print(User, Thing, session) 

def adicionar_usuario_e_coisa():
    new_user = User(name="charls", age=1040)
    session.add(new_user) # adiciona o novo usuário à sessão
    session.flush() # realiza alterações sem dar commit

    usuario = session.query(User).filter(User.name == "charls").first() # busca o usuário com o nome "charls" no banco de dados
    new_thing = Thing(description="Stuff", value=15.0, user=usuario.id) # cria um novo objeto Thing
    session.add(new_thing) # adiciona o novo objeto Thing à sessão
    session.commit() # salva as alterações no banco de dados
    session.close() # fecha a sessão
    print(new_thing.user) 

