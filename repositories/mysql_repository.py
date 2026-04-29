import mysql.connector
from mysql.connector import Error
import os 
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    try:
        conn = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
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


def listar_veiculos():
    conn = conectar_banco()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM veiculos")
    resultados = cursor.fetchall()

    for linha in resultados:
        print(linha)
    
    cursor.close()
    conn.close()


def cadastrar_veiculos(tag, morador, apartamento, placa, modelo):
    conn = conectar_banco()
    if not conn:
        return False
    
    cursor = conn.cursor()
    sql = """ 
    INSERT INTO veiculos (tag, morador , apartamento, placa, modelo, data_inscricao)
    VALUES (%s, %s, %s, %s, %s, NOW())
    """

    valores = (tag, morador, apartamento, placa, modelo)

    try:
        cursor.execute(sql, valores)
        conn.commit()
        print("Veículo cadastrado com sucesso!")
        resultado = True
    except Error as e:
        print(f"Erro ao cadastrar veículo: {e}")
        conn.rollback()
        resultado = False
    finally:
        cursor.close()
        conn.close()
    
    return resultado


def buscar_veiculos(tag):
    conn = conectar_banco()
    if not conn:
        return None
    
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM veiculos WHERE tag = %s"
    cursor.execute(sql, (tag,))

    veiculo = cursor.fetchone()
    cursor.close()
    conn.close()

    return veiculo

def tag_existe(tag):
    """Verifica se uma tag já está cadastrada no banco."""
    conn = conectar_banco()
    if not conn:
        return False
    
    cursor = conn.cursor()
    sql = "SELECT id FROM veiculos WHERE tag = %s"
    cursor.execute(sql, (tag,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return resultado is not None


def editar_veiculos(tag, campo, novo_valor):
    conn = conectar_banco()
    if not conn:
        return False
    
    campos_permitidos =  ["morador", "apartamento", "placa", "modelo"]

    if campo not in campos_permitidos:
        print("Campo inválido.")
        conn.close()
        return False
    
    cursor = conn.cursor()

    sql = f"UPDATE veiculos SET {campo} = %s WHERE tag = %s"
    valores = (novo_valor, tag)

    try:
        cursor.execute(sql, valores)
        conn.commit()

        if cursor.rowcount > 0:
            print("Veículo atualizado com sucesso!")
            resultado = True
        else:
            print("Tag não encontrada")
            resultado = False
    except Error as e:
        print(f"Erro ao atualizar veículo: {e}")
        conn.rollback()
        resultado = False
    finally:
        cursor.close()
        conn.close()
    
    return resultado

def remover_veiculos(tag):
    conn = conectar_banco()
    if not conn:
        return False
    
    cursor = conn.cursor()

    sql = "DELETE FROM veiculos WHERE tag = %s"

    try:
        cursor.execute(sql, (tag,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Veículo removido com sucesso!")
            resultado = True
        else:
            print("Tag não encontrada")
            resultado = False
    except Error as e:
        print(f"Erro ao remover veículo: {e}")
        conn.rollback()
        resultado = False
    finally:
        cursor.close()
        conn.close()
    
    return resultado


def registrar_movimentacao(tag, tipo):
    
    conn = conectar_banco()
    if not conn:
        return False
    
    cursor = conn.cursor()

    sql_busca = "SELECT id FROM veiculos WHERE tag = %s"

    try:
        cursor.execute(sql_busca, (tag,))
        resultado = cursor.fetchone()

        if not resultado:
            print("Veículo não encontrado")
            cursor.close()
            conn.close()
            return False
        
        veiculo_id = resultado[0]
        
        # Limpa espaços em branco e converte para minúsculas
        tipo_limpo = tipo.strip().lower()

        sql_insert = """
        INSERT INTO movimentacoes (veiculo_id, tipo)
        VALUES (%s, %s)
        """

        cursor.execute(sql_insert, (veiculo_id, tipo_limpo))
        conn.commit()

        print(f"{tipo.capitalize()} registrada com sucesso!")
        resultado_final = True
    except Error as e:
        print(f"Erro ao registrar movimentação: {e}")
        conn.rollback()
        resultado_final = False
    finally:
        cursor.close()
        conn.close()
    
    return resultado_final

def registrar_entrada(tag):
    return registrar_movimentacao(tag, "entrada")

def registrar_saida(tag):
    return registrar_movimentacao(tag, "saida")


def listar_movimentacoes(tag):
    """Lista as movimentações (entrada/saída) de um veículo."""
    conn = conectar_banco()
    if not conn:
        return None
    
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT m.* FROM movimentacoes m
    JOIN veiculos v ON m.veiculo_id = v.id
    WHERE v.tag = %s
    ORDER BY m.data_movimentacao DESC
    """
    
    try:
        cursor.execute(sql, (tag,))
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Erro ao listar movimentações: {e}")
        return None
    finally:
        cursor.close()
        conn.close()
