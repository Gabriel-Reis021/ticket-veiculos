import sqlite3
import os

CAMINHO_DB = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "database.db")


def _get_connection():
    return sqlite3.connect(CAMINHO_DB)


def inicializar_banco():
    """Cria a tabela de veículos se não existir."""
    with _get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS veiculos (
                tag TEXT PRIMARY KEY,
                morador TEXT,
                apartamento TEXT,
                placa TEXT,
                modelo TEXT,
                data_inscricao TEXT,
                entrada TEXT,
                saida TEXT
            )
        """)
        conn.commit()


def carregar_dados(dicionario: dict):
    """Carrega os dados do banco SQLite para o dicionário."""
    inicializar_banco()
    with _get_connection() as conn:
        cursor = conn.execute("SELECT tag, morador, apartamento, placa, modelo, data_inscricao, entrada, saida FROM veiculos")
        rows = cursor.fetchall()
        for row in rows:
            tag, morador, apartamento, placa, modelo, data_inscricao, entrada, saida = row
            dicionario[tag] = {
                "morador": morador,
                "apartamento": apartamento,
                "placa": placa,
                "modelo": modelo,
                "data-inscricao": data_inscricao,
                "entrada": [entrada] if entrada else None,
                "saida": [saida] if saida else None,
            }
    print(f"Dados carregados do SQLite: {len(rows)} veículos encontrados.")


def salvar_dados(dicionario: dict):
    """Salva os dados do dicionário no banco SQLite."""
    inicializar_banco()
    with _get_connection() as conn:
        for tag, v in dicionario.items():
            entrada = v["entrada"][0] if v.get("entrada") else None
            saida = v["saida"][0] if v.get("saida") else None
            conn.execute("""
                INSERT INTO veiculos (tag, morador, apartamento, placa, modelo, data_inscricao, entrada, saida)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(tag) DO UPDATE SET
                    morador=excluded.morador,
                    apartamento=excluded.apartamento,
                    placa=excluded.placa,
                    modelo=excluded.modelo,
                    data_inscricao=excluded.data_inscricao,
                    entrada=excluded.entrada,
                    saida=excluded.saida
            """, (tag, v["morador"], v["apartamento"], v["placa"], v["modelo"], v["data-inscricao"], entrada, saida))
        conn.commit()
    print(f"Dados salvos no SQLite! {len(dicionario)} veículos.")
