import json
import os
import cadastro as cd


def carregar_dados():
    """Carrega os dados dos veículos do arquivo JSON"""
    caminho_arquivo = os.path.join("data", "dados_veiculos.json")
    
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            cd.dicionario.update(dados)
            print(f"Dados carregados: {len(dados)} veículos encontrados.")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Será criado quando salvar os dados.")
        cd.dicionario.clear()
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Iniciando com dados vazios.")
        cd.dicionario.clear()


def salvar_dados():
    """Salva os dados dos veículos no arquivo JSON"""
    caminho_arquivo = os.path.join("data", "dados_veiculos.json")
    
    # Garante que a pasta data existe
    os.makedirs("data", exist_ok=True)
    
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(cd.dicionario, arquivo, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso! {len(cd.dicionario)} veículos no arquivo.")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")