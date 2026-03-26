from datetime import datetime
import pandas as pd

dicionario = {}

class Veiculo:
    def __init__(self, tag:str, morador:str, apartamento:str, placa:str, modelo:str, data_inscricao:datetime):
        self.tag = tag
        self.morador = morador
        self.apartamento = apartamento
        self.placa = placa
        self.modelo = modelo
        self.data_inscricao = data_inscricao
    
    def to_dict(self):
        return {
            "morador": self.morador,
            "apartamento": self.apartamento,
            "placa": self.placa,
            "modelo": self.modelo,
            "data-inscricao": self.data_inscricao,
            "entrada": None,
            "saida": None
        }

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
        
        dados = Veiculo(tag, morador, apartamento, placa, modelo, atual)

        dicionario[tag] = dados.to_dict()
 
def tempo_real():
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    return data_atual




def buscar_veiculo():
    while True:

        print(6*"="+" Busca de veículo "+ 6*"=")
        tag = input("Digite a tag do veículo: ")

        if tag in dicionario:
            print(f"{dicionario[tag]['modelo']}")
            print(f"{dicionario[tag]['placa']}")
            break
        else:
            print("Carro nao encontrado")


def listar_veiculos():
    print("--- Listar Veículos ---")
    if not dicionario:
        print("Nenhum veículo cadastrado.")
        return
    
    try:
        df_veiculos = pd.DataFrame.from_dict(dicionario, orient='index')
        df_veiculos.reset_index(inplace=True)
        df_veiculos.rename(columns={'index': 'tag'}, inplace=True)
        print(df_veiculos)
        return df_veiculos
    except:
        # Fallback para exibição simples sem pandas
        print(f"{'Tag':<10} {'Morador':<15} {'Apartamento':<12} {'Placa':<10} {'Modelo':<15}")
        print("-" * 70)
        
        for tag, dados in dicionario.items():
            print(f"{tag:<10} {dados['morador']:<15} {dados['apartamento']:<12} {dados['placa']:<10} {dados['modelo']:<15}")
        
        print(f"\nTotal: {len(dicionario)} veículos cadastrados.") 


def verificar_tag():
    print("--- Verificar tag ---")
    tag =  input("Digite a tag do veículo: ").strip()
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
