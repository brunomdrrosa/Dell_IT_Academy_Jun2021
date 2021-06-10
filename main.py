# Dados dos pontos de táxi
telefone = []
logradouro = []
numero = []
latitude = []
longitude = []

# Importar arquivo .csv
import csv
with open("weather_data.csv", encoding='utf-8') as data_file:
    data = csv.reader(data_file)
    codigo_taxi = []
    nome_taxi = []
    for row in data:
        if row[0] != "codigo" and row[1] != "nome":
            codigo_taxi.append(int(row[0]))
            nome_taxi.append(row[1])
    print(codigo_taxi)        
    print(nome_taxi)



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