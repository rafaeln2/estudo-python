from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Insert,Float, ForeignKey, func

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

# Insert data
def insert_data(conn, users):
    # insert_statement = people.insert().values(name="John Doe", age=30)
    insert_statement = Insert(users).values(name="John Doe", age=30)
    result = conn.execute(insert_statement)
    conn.commit()
    print(f"Inserted row ID: {result.inserted_primary_key}")

# insert_data(conn)


#update data
def update_data(users, conn):
    update_statement = users.update().where(users.c.id == 1).values(age=25)
    update_result = conn.execute(update_statement)
    conn.commit()

# update_data(users, conn)


#select
def select_users(users, conn):
    select_statement = users.select
    select_result = conn.execute(select_statement())
    for row in select_result.fetchall():
        print(row)

# select_users(users, conn)
    
#delete
def delete_users_by_age(users, age, conn):
    delete_statement = users.delete().where(users.c.age == age)
    delete_result = conn.execute(delete_statement)
    conn.commit()

# delete_users_by_age(users, conn)


# Insert data with fk
def insert_things(users, things, conn):
    insert_statement = Insert(things).values(description="Sample Thing", value=10.5, user_id=2)
    result = conn.execute(insert_statement)
    conn.commit()
    select_statement = users.select().where(users.c.id == 2)
    select_result = conn.execute(select_statement)
    for row in select_result.fetchall():
        print(row)

# insert_things(users, things, conn)

# insert list of data
def insert_users_and_things(users, things):
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
    
    return insert_things,insert_people

# insert_things, insert_people = insert_users_and_things(users, things)
# conn.execute(insert_people)
# conn.commit()
# conn.execute(insert_things)
# conn.commit()

# delete_statement = things.delete()
# delete_result = conn.execute(delete_statement)
# conn.commit()


# select_statement = users.select()
# select_result = conn.execute(select_statement)
# select_things = conn.execute(things.select())
# for row in select_result.fetchall():
#     print(row)
# for row in select_things.fetchall():
#     print(row)
    
#     select_statement = users.select
#     select_result = conn.execute(select_statement())
#     for row in select_result.fetchall():
#         print(row)

# join_statement = users.join(things, users.c.id == things.c.user_id)
# select_statement = users.select().with_only_columns(users.c.name, things.c.description).select_from(join_statement)
# join_result = conn.execute(select_statement)
# for row in join_result.fetchall():
#     print(row)

# join_statement = users.join(things, users.c.id == things.c.user_id)
# group_by_statement = things.select().with_only_columns(things.c.user_id, users.c.name, func.sum(things.c.value)).select_from(join_statement).group_by(things.c.user_id).having(func.sum(things.c.value) > 20)
# result = conn.execute(group_by_statement)
# for row in result.fetchall():
#     print(row)
