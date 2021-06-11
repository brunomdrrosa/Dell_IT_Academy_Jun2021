# Importar arquivo .csv
import pandas as pd
dados = pd.read_csv("pontos_taxi.csv", encoding='utf-8')
pd.set_option('display.max_rows', None)

from geopy.distance import great_circle

# Converter os dados para listas
lista_codigos = dados["codigo"].to_list()
lista_nomes = dados["nome"].to_list()
lista_telefone = dados["telefone"].to_list()
lista_logradouro = dados["logradouro"].to_list()
lista_numero = dados["numero"].to_list()
lista_latitude = dados["latitude"].to_list()
lista_longitude = dados["longitude"].to_list()

latitude = 0
longitude = 0

# from coordenadas import rodoviaria, av_das_industrias
# Função que mostra os 3 pontos de táxis mais próximos ao usuário;
def opcao3():
    colunas = ['latitude', 'longitude']
    coordenadas = pd.DataFrame(dados, columns=colunas)
    print(coordenadas)
    
        
    # test = great_circle(teste, coordenada).km
    # print(f'A distancia de é {test:.2f}km')   
    
    # rodoviaria = (-30.02399616, -51.2194512698)
    # distancia = great_circle(teste, rodoviaria).km
    # print(f'A distancia de é {distancia:.2f}km')

# Função para pegar os pontos de taxí de uma determinada rua ou logradouro
def opcao4():
    buscar = input("Digite o nome da rua ou do logradouro:\n").upper()
    if buscar in lista_logradouro:
        print(f"Os pontos de taxi ao longo de {buscar} são:")
        ruas_em_logradouro = dados[dados['logradouro'] == buscar]
        print(ruas_em_logradouro)
        menu()
    else:
        print("Não encontramos o logradouro informado no sistema.")
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
        print("Informe sua localização:")
        latitude = float(input("Digite sua latitude: "))
        longitude = float(input("Digite sua longitude: "))
        print("Localização armazenada.")
        menu()
    # Encontrar os 3 pontos mais próximos baseado na latitude e longitude do usuário
    elif opcao == 3:
        opcao3()
    # Buscar pontos por logradouro
    elif opcao == 4:
        opcao4()
    # Fechar o programa
    elif opcao == 5:
        print("Fechando o programa...")
    else:
        print("Digite um número de 1 a 5")
        menu()

menu()