from datetime import datetime
from models.veiculo import Veiculo

# Estado compartilhado do sistema (dicionário central de veículos)
dicionario: dict = {}

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
            tag = input(f"Digite a {i+1}º tag do veículo: ")
            if tag in dicionario:
                print("Tag já cadastrada!")
            else:
                break
        morador = input("Digite o nome do morador: ")
        apartamento = input("Digite o apartamento: ")
        placa = input(f"Digite a placa do {i+1}º veículo: ")
        modelo = input(f"Digite o modelo do {i+1}º veículo: ")
        atual = tempo_real()

        veiculo = Veiculo(tag, morador, apartamento, placa, modelo, atual)
        dicionario[tag] = veiculo.to_dict()


def buscar_veiculo():
    while True:
        print(6*"="+" Busca de veículo "+6*"=")
        tag = input("Digite a tag do veículo: ")

        if tag in dicionario:
            print(f"{dicionario[tag]['modelo']}")
            print(f"{dicionario[tag]['placa']}")
            break
        else:
            print("Carro nao encontrado")


def listar_veiculos():
    print(6*"="+" Listar Veículos "+6*"=")
    if not dicionario:
        print("Nenhum veículo cadastrado.")
        return

    try:
        import pandas as pd
        df_veiculos = pd.DataFrame.from_dict(dicionario, orient='index')
        df_veiculos.reset_index(inplace=True)
        df_veiculos.rename(columns={'index': 'tag'}, inplace=True)
        print(df_veiculos)
        return df_veiculos
    except Exception:
        print(f"{'Tag':<10} {'Morador':<15} {'Apartamento':<12} {'Placa':<10} {'Modelo':<15}")
        print("-" * 70)
        for tag, dados in dicionario.items():
            print(f"{tag:<10} {dados['morador']:<15} {dados['apartamento']:<12} {dados['placa']:<10} {dados['modelo']:<15}")
        print(f"\nTotal: {len(dicionario)} veículos cadastrados.")


def verificar_tag():
    print(6*"="+" Verificar TAG "+6*"=")
    tag = input("Digite a tag do veículo: ").strip()
    veiculo = dicionario.get(tag)

    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return
    else:
        print(f"Tag '{tag}' encontrada")
        print(f"Morador: {veiculo['morador']}")
        print(f"Apartamento: {veiculo['apartamento']}")
        print(f"Placa: {veiculo['placa']}")
        print(f"Modelo: {veiculo['modelo']}")


def remover_veiculo():

    print(6*"="+" Remover Veiculo "+6*"=")
    tag = input("Digite a tag do veículo: ").strip()
    veiculo = dicionario.get(tag)

    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return
    else:
        veiculo_removido = dicionario.pop(tag)
        print(f"Veiculo removido com sucesso: {veiculo_removido} ")

def editar():
     
    print(6*"="+" Editar Veiculo "+6*"=")

    #loop até encontrar uma tag válida
    while True:
        tag = input("Digite a tag que deseja editar: ").strip()
        tag_capturada = dicionario.get(tag)

        if not tag_capturada:
            print(f"Tag '{tag}' não encontrada. Cadastre ou insira uma tag válida")
            continue
        else:
            break # sai do loop quando achar uma tag válida

    #loop de edição
    print(6*"="+" Modo de edição  "+6*"=")
    
    veiculo = dicionario[tag]

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
            dicionario[tag]["morador"] = novo_morador
        elif opcao == 2:
            novo_apartamento = input("Digite o número do novo apartamento: ")
            dicionario[tag]["apartamento"] = novo_apartamento
        elif opcao == 3:
            nova_placa = input("Digite a nova placa: ")
            dicionario[tag]["placa"] = nova_placa
        elif opcao == 4:
            novo_modelo = input("Digite o nome do novo modelo do veículo: ")
            dicionario[tag]["modelo"] = novo_modelo
        else:
            print("Opção inválida")
    
    print(f"TAG atualizada com sucesso: {dicionario[tag]}")

    