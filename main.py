# Importar arquivo .csv
import pandas
dados = pandas.read_csv("pontos_taxi.csv")

# Converter os dados para listas
lista_codigos = dados["codigo"].to_list()
lista_nomes = dados["nome"].to_list()
lista_telefone = dados["telefone"].to_list()

print(lista_nomes)

# Dados dos pontos de táxi
telefone = []
logradouro = []
numero = []
latitude = []
longitude = []



# Menu do programa
def menu():
    print("=== MENU ===")
    print("1. Listar todos os pontos de taxi")
    print("2. Informar minha localização")
    print("3. Encontrar pontos próximos")
    print("4. Buscar pontos por logradouro")
    print("5. Terminar o programa")
    opcao = int(input("Escolha uma das opcões:\n"))
    if opcao == 1:
        print("Opção 1")
    elif opcao == 2:
        print("Opção 2")
    elif opcao == 3:
        print("Opção 3")
    elif opcao == 4:
        print("Opção 4")
    elif opcao == 5:
        print("Fechando o programa")
    else:
        print("Digite um número de 1 a 5")
        print()
        menu()

# menu()