# Importar arquivo .csv
# from pandas import ExcelWriter
# from pandas import ExcelFile
# import numpy as np
import pandas as pd
dados = pd.read_csv("pontos_taxi.csv", encoding='utf-8')
dados['telefone'] = dados['telefone'].fillna("")
dados['nome'] = dados['nome'].str.replace(u"Å", "A")

# print(dados.iloc[1, 2])
pd.set_option('display.max_rows', None)

from geopy.distance import great_circle
from heapq import nsmallest
from coordenadas import nomesRuas, ruas

# Converter os dados para listas
lista_codigos = dados["codigo"].to_list()
lista_nomes = dados["nome"].to_list()
lista_telefone = dados["telefone"].to_list()
lista_logradouro = dados["logradouro"].to_list()
lista_numero = dados["numero"].to_list()
lista_latitude = dados["latitude"].to_list()
lista_longitude = dados["longitude"].to_list()

coordenadas = (0, 0)

def opcao2():
    global coordenadas
    print("Informe sua localização:")
    latitude = float(input("Digite sua latitude: "))
    longitude = float(input("Digite sua longitude: "))
    coordenadas = (latitude, longitude)
    print(coordenadas)
    print("Localização armazenada.")
    menu()
    # return coordenadas    

# Função que mostra os 3 pontos de táxis mais próximos ao usuário;
def opcao3():
    print(f"Suas coordenadas são: {coordenadas}")
    if coordenadas == (0, 0):
        print("Você não informou a sua localização na opção 2 do menu")
        menu()
    # posicao = -1
    # latitude_distancias = []
    # longitude_distancias = []
    
    # for x in range(379):
    #     posicao += 1
    #     latitude_taxi_csv = dados.at[posicao, "latitude"]
    #     longitude_taxi_csv = dados.at[posicao, "longitude"]
    #     latitude_distancias.append(latitude_taxi_csv)
    #     longitude_distancias.append(longitude_taxi_csv)
    # print(latitude_distancias)
    # print(longitude_distancias)

    # tupla = (latitude_distancias[0], longitude_distancias[0])
    # print(tupla)
    # teste = (-29.9598916, -51.0951607)  
    # distancia = great_circle(teste, tupla).km
    # print(distancia)
    else:
        posicao = -1
        todas_distancias = []
        for rua in ruas:
            posicao += 1
            # teste = (-29.9598916, -51.0951607)  
            distancia = great_circle(coordenadas, rua).km
            todas_distancias.append(distancia)
            print(f'A distância da {nomesRuas[posicao]} é de {distancia:.2f}km')

        menores_distancias = nsmallest(3, todas_distancias)
        print()
        print(f'Tem um ponto de táxi há {menores_distancias[0]:.2f}km de você')
        print(f'Tem um ponto de táxi há {menores_distancias[1]:.2f}km de você')
        print(f'Tem um ponto de táxi há {menores_distancias[2]:.2f}km de você')
        if distancia == menores_distancias:
            print(nomesRuas)
        menu()

# Função para pegar os pontos de taxí de um determinado logradouro
def opcao4():
    buscar = input("Digite o nome do logradouro:\n").upper()
    if buscar in lista_logradouro:
        print(f"Os pontos de taxi ao longo da {buscar} são:")
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
        # print(dados)
        print(dados.loc[:, ["codigo", "nome", "telefone", "logradouro", "numero", "latitude", "longitude"]])
        menu()
    # Permitir que o usuário digite sua localização geográfica e armazená-la
    elif opcao == 2:
        opcao2()
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