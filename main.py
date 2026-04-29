import services.cadastro_service as cd
import services.entrada_saida_service as es
import repositories.mysql_repository as db
from time import sleep


def menu():
    print("="*50)
    print("Sistema de Controle de Veículos - MySQL")
    print("="*50)

    while True:

        print("\n0 - Para sair")
        print("1 - Cadastrar veiculo")
        print("2 - Registrar entrada")
        print("3 - Registrar saída")
        print("4 - Buscar veículo")
        print("5 - Listar veículos")
        print("6 - Relatório de entrada e saída")
        print("7 - Verificar TAG")
        print("8 - Editar TAG")
        print("9 - Remover Veículo")

        while True:
            try:
                get_opcao = int(input("\nDigite a opção que deseja executar: "))
                break
            except ValueError:
                print("Digite apenas números!")

        if get_opcao == 0:
            print("Saindo..."); sleep(2)
            print("Programa encerrado")
            break
        elif get_opcao == 1:
            cd.cadastrar_veiculo()
        elif get_opcao == 2:
            es.registrar_entrada()
        elif get_opcao == 3:
            es.registrar_saida()
        elif get_opcao == 4:
            cd.buscar_veiculo()
        elif get_opcao == 5:
            cd.listar_veiculos()
        elif get_opcao == 6:
            es.listar_entrada_saida()
        elif get_opcao == 7:
            cd.verificar_tag()
        elif get_opcao == 8:
            cd.editar()
        elif get_opcao == 9:
            cd.remover_veiculo()
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
