# Importar arquivo .csv
import pandas as pd
dados = pd.read_csv("pontos_taxi.csv", encoding='utf-8-sig')

pd.set_option('display.max_rows', None)

# Converter os dados para listas
lista_codigos = dados["codigo"].to_list()
lista_nomes = dados["nome"].to_list()
lista_telefone = dados["telefone"].to_list()
lista_logradouro = dados["logradouro"].to_list()
lista_numero = dados["numero"].to_list()
lista_latitude = dados["latitude"].to_list()
lista_longitude = dados["longitude"].to_list()

# Função para armazenar a latitude e longitude do usuário
def opcao2():
    print("Informe sua localização:")
    latitude = float(input("Digite sua latitude: "))
    longitude = float(input("Digite sua longitude: "))
    print("Localização armazenada.")
    menu()

# Menu do programa
def menu():
    print()
    print("=== MENU ===")
    print("1. Listar todos os pontos de taxi")
    print("2. Informar minha localização")
    print("3. Encontrar pontos próximos")
    print("4. Buscar pontos por logradouro")
    print("5. Terminar o programa")
    opcao = int(input("Escolha uma das opcões:\n"))

    # Listar na tela os dados de todos os pontos de taxi da cidade
    if opcao == 1:
        print(dados)
        menu()
    # Permitir que o usuário digite sua localização geográfica e armazená-la
    elif opcao == 2:
        opcao2()
    # Encontrar os 3 pontos mais próximos baseado na latitude e longitude do usuário
    elif opcao == 3:
        print()
    # Buscar pontos por logradouro
    elif opcao == 4:
        print("Opção 4")
    # Fechar o programa
    elif opcao == 5:
        print("Fechando o programa...")
    else:
        print("Digite um número de 1 a 5")
        menu()

menu()