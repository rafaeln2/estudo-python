from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Insert,Float, ForeignKey

# DB_HOST = "localhost"
# DB_NAME = "estudo-database"
# DB_USER = "rafael_ubuntu"
# DB_PASSWORD = "1234"
# DB_PORT = "5432"  # Para PostgreSQL
# DATABASE_URL_DEFAULT = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# engine = create_engine('postgresql+psycopg2://rafael_ubuntu:1234@localhost:5432/estudo_database', echo=True)

engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)

things = Table(
    "things",
    meta,
    Column("id", Integer, primary_key=True),
    Column("description", String, nullable=False),
    Column("value", Float),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False), #owner
)

meta.create_all(engine)

conn = engine.connect()

# # Insert data
# # insert_statement = people.insert().values(name="John Doe", age=30)
# insert_statement = Insert(people).values(name="John Doe", age=30)
# result = conn.execute(insert_statement)
# conn.commit()
# print(f"Inserted row ID: {result.inserted_primary_key}")


#update data
update_statement = users.update().where(users.c.id == 1).values(age=25)
update_result = conn.execute(update_statement)
conn.commit()


#select
# select_statement = people.select
# select_result = conn.execute(select_statement())
# for row in select_result.fetchall():
#     print(row)
    
#delete
delete_statement = users.delete().where(users.c.age == 25)
delete_result = conn.execute(delete_statement)
conn.commit()

select_statement = users.select
select_result = conn.execute(select_statement)
for row in select_result.fetchall():
    print(row)

# select_all = conn.execute(people.select()).fetchall()
# for row in select_all:
#     select_all(row)

# Insert data with fk
insert_statement = Insert(things).values(description="Sample Thing", value=10.5, user_id=2)
result = conn.execute(insert_statement)
conn.commit()
select_statement = users.select().where(users.c.id == 2)
select_result = conn.execute(select_statement)
for row in select_result.fetchall():
    print(row)

# insert list of data
insert_people = users.insert().values([
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 22},
])  
insert_things = things.insert().values([
    {"description": "Thing 1", "value": 15.0, "user_id": 4},
    {"description": "Thing 2", "value": 25.0, "user_id": 2},
    {"description": "Thing 3", "value": 35.0, "user_id": 3},
])
result = conn.execute(insert_people)
conn.commit()
select_statement = users.select()
select_result = conn.execute(select_statement)
for row in select_result.fetchall():
    print(row)