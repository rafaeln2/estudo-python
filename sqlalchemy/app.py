from sqlalchemy import create_engine
import psycopg2

print("foi o import")

engine = create_engine("postgresql+psycopg2://postgres:1234@127.0.0.1:5432/estudo_database", echo=True)

# engine.connect()
