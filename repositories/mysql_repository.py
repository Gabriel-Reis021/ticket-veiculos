import mysql.connector

def conectar_banco():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "****",
            database = "ticket_veiculos"

        )
        return conn
    except Error as e:
        print(f"Erro ao conectar no MySql: {e}")
        return None


if __name__ == "__main__":
    conn = conectar_banco()
    if conn:
        print("Conectado com sucesso!")
        conn.close()