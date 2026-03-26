import json
import os

# Caminho do arquivo JSON dentro da pasta data/
CAMINHO_ARQUIVO = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "dados_veiculos.json")


def carregar_dados(dicionario: dict):
    """Carrega os dados dos veículos do arquivo JSON para o dicionário."""
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            dicionario.update(dados)
            print(f"Dados carregados: {len(dados)} veículos encontrados.")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Será criado quando salvar os dados.")
        dicionario.clear()
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Iniciando com dados vazios.")
        dicionario.clear()


def salvar_dados(dicionario: dict):
    """Salva os dados dos veículos no arquivo JSON."""
    os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
    try:
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso! {len(dicionario)} veículos no arquivo.")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
