import cadastro as cd

def registrar_entrada():
    print("--- Registrar entrada ---")
    tag =  input("Digite a tag do veículo: ").strip()
    veiculo = cd.dicionario.get(tag)

    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return
    else:
        print(f"Entrada registrada com sucesso")
        print(f"{cd.tempo_real()}")
        entrada = [cd.tempo_real()]
        cd.dicionario[tag]['entrada'] = entrada
        return entrada


def registrar_saida():
    print("--- Registrar saída ---")
    tag =  input("Digite a tag do veículo: ").strip()
    veiculo = cd.dicionario.get(tag)

    if not veiculo:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")
        return
    else:
        print(f"Saida registrada com sucesso")
        print(f"{cd.tempo_real()}")
        saida = [cd.tempo_real()]
        cd.dicionario[tag]['saida'] = saida
        return saida

def listar_entrada_saida():
    print("--- Listar entrada e saída ---")
    tag = input("Digite a tag do veiculo que deseja listar: ").strip()
    if tag in cd.dicionario:
        print(f"Entrada: {cd.dicionario[tag]['entrada']}")
        print(f"Saida: {cd.dicionario[tag]['saida']}")
    else:
        print(f"Tag '{tag}' não encontrada. Cadastre o veículo primeiro")


