# Importar arquivo .csv
import pandas as pd
dados = pd.read_csv("pontos_taxi.csv")
dados['telefone'] = dados['telefone'].fillna("")
dados['logradouro'] = dados['logradouro'].fillna("")
pd.set_option('display.max_rows', None)

from geopy.distance import great_circle
from heapq import nsmallest
from coordenadas import nomesRuas, ruas

lista_logradouro = dados["logradouro"].to_list()
coordenadas = (0, 0)

# Função para o usuário informar a sua localização;
def opcao2():
    global coordenadas
    print("Informe sua localização")
    print("OBS: Utilize '.' para casas decimais")
    latitude = float(input("Digite sua latitude no formato geodésico decimal: "))
    longitude = float(input("Digite sua longitude no formato geodésico decimal: "))
    coordenadas = (latitude, longitude)
    print("Localização armazenada.")
    menu()  

# Função que mostra os 3 pontos de táxis mais próximos ao usuário e as suas distâncias;
def opcao3():
    if coordenadas == (0, 0):
        print("Você não informou a sua localização na opção 2 do menu, não é possível encontrar os pontos mais próximos")
        menu()
    else:
        print("Os pontos de taxi mais próximos são:")
        posicao = -1
        todas_distancias = []
        for rua in ruas:
            posicao += 1
            distancia = great_circle(coordenadas, rua).km
            todas_distancias.append(distancia)
            menores_distancias = nsmallest(3, todas_distancias)
        print(f'{nomesRuas[todas_distancias.index(menores_distancias[0])]} está a {menores_distancias[0]:.2f}km de você')
        print(f'{nomesRuas[todas_distancias.index(menores_distancias[1])]} está a {menores_distancias[1]:.2f}km de você')
        print(f'{nomesRuas[todas_distancias.index(menores_distancias[2])]} está a {menores_distancias[2]:.2f}km de você')
        menu()
     
# Função para pegar os pontos de táxi de um determinado logradouro
def opcao4():
    buscar = input("Digite o nome do logradouro:\n").upper()
    if buscar in lista_logradouro:
        print(f"Os pontos de taxi ao longo da {buscar} são:")
        ruas_em_logradouro = dados.loc[:, ["codigo", "nome", "telefone", "logradouro", "numero", "latitude", "longitude"]][dados['logradouro'] == buscar]
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
    opcao = input("Escolha uma das opcões:\n")

    # Listar na tela os dados de todos os pontos de taxi da cidade
    if opcao == "1":
        print(dados.loc[:, ["codigo", "nome", "telefone", "logradouro", "numero", "latitude", "longitude"]])
        menu()
    # Permitir que o usuário digite sua localização geográfica e armazená-la
    elif opcao == "2":
        opcao2()
    # Encontrar os 3 pontos de táxi mais próximos do usuário baseado na latitude e longitude 
    elif opcao == "3":
        opcao3()
    # Buscar pontos por logradouro
    elif opcao == "4":
        opcao4()
    # Fechar o programa
    elif opcao == "5":
        print("Fechando o programa...")
    else:
        print("Digite um número de 1 a 5")
        menu()

menu()