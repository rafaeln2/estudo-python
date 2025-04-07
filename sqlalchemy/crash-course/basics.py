from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import sqlite3

engine = create_engine("sqlite:///mydatabase.db", echo =True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"))

conn.commit()

session = Session(engine)
session.execute(text("INSERT INTO users (name, age) VALUES ('Alice', 30)"))
session.commit()
