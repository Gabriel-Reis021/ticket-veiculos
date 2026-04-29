from datetime import datetime
from models.veiculo import Veiculo
import repositories.mysql_repository as db

def tempo_real() -> str:
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


def cadastrar_veiculo():
    try:
        qtd_veiculos = int(input("Digite a quantidade de veiculos que voce deseja cadastrar: "))
    except ValueError:
        print("Digite apenas números!")
        return

    for i in range(qtd_veiculos):
        while True:
            tag = input(f"Digite a {i+1}º tag do veículo: ").strip()
            if db.tag_existe(tag):
                print("Tag já cadastrada!")
            else:
                break
        morador = input("Digite o nome do morador: ")
        apartamento = input("Digite o apartamento: ")
        placa = input(f"Digite a placa do {i+1}º veículo: ")
        modelo = input(f"Digite o modelo do {i+1}º veículo: ")
        
        db.cadastrar_veiculos(tag, morador, apartamento, placa, modelo)


def buscar_veiculo():
    while True:
        print(6*"="+" Busca de veículo "+6*"=")
        tag = input("Digite a tag do veículo: ").strip()

        veiculo = db.buscar_veiculos(tag)
        if veiculo:
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Placa: {veiculo['placa']}")
            print(f"Morador: {veiculo['morador']}")
            print(f"Apartamento: {veiculo['apartamento']}")
            break
        else:
            print("Carro nao encontrado")


def listar_veiculos():
    print(6*"="+" Listar Veículos "+6*"=")
    
    conn = db.conectar_banco()
    if not conn:
        print("Erro ao conectar ao banco de dados.")
        return None
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM veiculos")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not resultados:
        print("Nenhum veículo cadastrado.")
        return None

    try:
        import pandas as pd
        df_veiculos = pd.DataFrame(resultados)
        print(df_veiculos)
        return df_veiculos
    except Exception:
        print(f"{'Tag':<10} {'Morador':<15} {'Apartamento':<12} {'Placa':<10} {'Modelo':<15}")
        print("-" * 70)
        for veiculo in resultados:
            print(f"{veiculo['tag']:<10} {veiculo['morador']:<15} {veiculo['apartamento']:<12} {veiculo['placa']:<10} {veiculo['modelo']:<15}")
        print(f"\nTotal: {len(resultados)} veículos cadastrados.")
        return None


def verificar_tag():
    print(6*"="+" Verificar TAG "+6*"=")
    tag = input("Digite a tag do veículo: ").strip()
    veiculo = db.buscar_veiculos(tag)

    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return
    else:
        print(f"Tag '{tag}' encontrada")
        print(f"Morador: {veiculo['morador']}")
        print(f"Apartamento: {veiculo['apartamento']}")
        print(f"Placa: {veiculo['placa']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Data de inscrição: {veiculo['data_inscricao']}")


def remover_veiculo():
    print(6*"="+" Remover Veiculo "+6*"=")
    tag = input("Digite a tag do veículo: ").strip()
    veiculo = db.buscar_veiculos(tag)

    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return
    else:
        db.remover_veiculos(tag)

def editar():
    print(6*"="+" Editar Veiculo "+6*"=")

    #loop até encontrar uma tag válida
    while True:
        tag = input("Digite a tag que deseja editar: ").strip()
        tag_capturada = db.buscar_veiculos(tag)

        if not tag_capturada:
            print(f"Tag '{tag}' não encontrada. Cadastre ou insira uma tag válida")
            continue
        else:
            break # sai do loop quando achar uma tag válida

    #loop de edição
    print(6*"="+" Modo de edição  "+6*"=")
    
    veiculo = tag_capturada

    print("\n--- Dados atuais do veículo ---")
    print(f"Morador: {veiculo['morador']}")
    print(f"Apartamento: {veiculo['apartamento']}")
    print(f"Placa: {veiculo['placa']}")
    print(f"Modelo: {veiculo['modelo']}")
    
    while True:
        print("\nDigite (0) para sair")
        print("Digite (1) para editar o morador")
        print("Digite (2) para editar apartamento")
        print("Digite (3) para editar placa do veículo")
        print("Digite (4) para editar modelo do veículo")
        
        try:
            opcao = int(input("Digite a opção que deseja executar: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        
        if opcao == 0:
            break
        elif opcao == 1:
            novo_morador = input("Digite o nome do novo morador: ")
            db.editar_veiculos(tag, "morador", novo_morador)
        elif opcao == 2:
            novo_apartamento = input("Digite o número do novo apartamento: ")
            db.editar_veiculos(tag, "apartamento", novo_apartamento)
        elif opcao == 3:
            nova_placa = input("Digite a nova placa: ")
            db.editar_veiculos(tag, "placa", nova_placa)
        elif opcao == 4:
            novo_modelo = input("Digite o nome do novo modelo do veículo: ")
            db.editar_veiculos(tag, "modelo", novo_modelo)
        else:
            print("Opção inválida")
    
    veiculo_atualizado = db.buscar_veiculos(tag)
    print(f"\nTAG atualizada com sucesso!")
    print(f"Morador: {veiculo_atualizado['morador']}")
    print(f"Apartamento: {veiculo_atualizado['apartamento']}")
    print(f"Placa: {veiculo_atualizado['placa']}")
    print(f"Modelo: {veiculo_atualizado['modelo']}")

    