import repositories.mysql_repository as db
from datetime import datetime


def tempo_real() -> str:
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


def registrar_entrada():
    print("--- Registrar entrada ---")
    tag = input("Digite a tag do veículo: ").strip()
    veiculo = db.buscar_veiculos(tag)

    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return None
    else:
        resultado = db.registrar_entrada(tag)
        if resultado:
            print(f"Entrada registrada com sucesso às {tempo_real()}")
        return resultado


def registrar_saida():
    print("--- Registrar saída ---")
    tag = input("Digite a tag do veículo: ").strip()
    veiculo = db.buscar_veiculos(tag)

    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return None
    else:
        resultado = db.registrar_saida(tag)
        if resultado:
            print(f"Saída registrada com sucesso às {tempo_real()}")
        return resultado


def listar_entrada_saida():
    print("--- Listar entrada e saída ---")
    tag = input("Digite a tag do veiculo que deseja listar: ").strip()
    
    veiculo = db.buscar_veiculos(tag)
    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return
    
    movimentacoes = db.listar_movimentacoes(tag)
    
    if not movimentacoes:
        print("Nenhuma movimentação registrada para este veículo.")
        return
    
    print(f"\nMovimentações do veículo {tag}:")
    print("-" * 60)
    for mov in movimentacoes:
        print(f"ID: {mov['id']} | Tipo: {mov['tipo'].upper()} | Data: {mov['data_movimentacao']}")
    print("-" * 60)
