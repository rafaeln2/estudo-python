import psycopg2

def with_db_connection(callback):
    conn = psycopg2.connect(
        dbname="db-rl",
        user="postgres",
        password="1234",
        host="db",
        port="5432"
    )
    try:
        cur = conn.cursor()
        result = callback(cur) 
        conn.commit()
        cur.close()
        return result
    finally:
        conn.close()
        
def registrar_log(ip, endpoint, status, timestamp):
    def inserir(cur):
        cur.execute("""
            INSERT INTO log_requisicoes (ip, rota, status, criado_em)
            VALUES (%s, %s, %s, %s);
        """, (ip, endpoint, status, timestamp))
    
    with_db_connection(inserir)

def buscar_logs_aceitos():
    def buscar(cur):
        cur.execute("SELECT * FROM log_requisicoes WHERE status IS TRUE;")
        return cur.fetchall()  

    return with_db_connection(buscar)  

def buscar_logs_rejeitados():
    def buscar(cur):
        cur.execute("SELECT * FROM log_requisicoes WHERE status IS FALSE;")
        return cur.fetchall()  

    return with_db_connection(buscar)  
