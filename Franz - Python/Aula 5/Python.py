# 1. O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer ( como ler 10 sensores ou processar umas lista de peças)
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1 
# for lote in range (1, 6):
#     print(f"Processando lotes número {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada!")

#     # Imagine que você queira atingir um uma meta de -produção de 5 carros e múmera´las
#     for carros in range (1, 6):
#         print(f"Produzindo carro número {carros}...")

# Exemplo 2
# for i in range (5):
#      print(i)
# Exemplo 3
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# tipospecas= ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo cabeça chata"]
# # for item in pecas:
# #     print(f"Item em estoque: {item}")
# # for item2 in tipospecas:
# #     print(f"Item em estoque: {item2}")

# #     # ou

# #     print(f"Item em estoque: {item} {tipospecas}")

# # Exemplo 4
# print("Loja de Peças")
# print("Bem-Vindo ao Sistema")
# print("Escolha uma das opções:")
# print("1- Peças")
# print("2 - Tipos de Peças")

# opção =int(input("Digite sua opção de pesquisa:"))

# if opção == 1:
#     for item in pecas:
#         print(f"Item em estoque: {item}")

# elif opção == 2:
#     for item in tipospecas:
#         print(f"Item em estoque: {item}")

# else:
#     print("Encerrando Sistema")

# Exercicio 1
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para conter de 1 a 10 e, para cada número, imprima :"Peças nº X processada com sucesso". No final, exiba "Ciclo de produção concluido".
# for i in range(1, 11):
#     print(f"Peças número {i} processada com sucesso" )
# print("Ciclo de produção concluído.")

# Exercicio 2
#Imagine a produção de frutas em uma feira. Desejo apresentar frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 banans, 5 mangas, 10 melancias e 13 abacaxi.


# print("Selecione a fruta desejada:")
# print("1- Banana")
# print("2- Manga")
# print("3- Melancia")
# print("4- Abacaxi")

# fruta = input("Digite sua opção:")
# if fruta == "1":
#     for banana in range(10):
#         print(f"Bananas fabricadas:{banana +1}")
        

# if fruta == "2":
#     for manga in range(4):
#         print(f"mangas fabricadas:{manga +1}")



# if fruta == "3":
#     for melancia in range(9):
#         print(f"melancias fabricadas:{melancia +1}")



# elif fruta == "4":
#     for abacaxi in range(12):
#         print(f"abacaxis fabricadas:{abacaxi +1}")

#Exemplo 4
#Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

# tabuada = int(input("Digite um valor:"))
# for numero in range(10):
#     resultado = numero * tabuada
#     print(f" {tabuada}x{numero} = {resultado}")

#O Laço while (Repetições Indeterminadas)
#Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
#Exemplo: Monitor de temperatura (Loop Infinito)
#Repete enquanto a temperatura estiver segura
#Início
# import time
# temperatura = 25
# while temperatura <40:
#     print(f"Temperatura atual: {temperatura} ºC. Sistema operando...")
#     time.sleep(2)
#     temperatura +=3 #Simulando o aquecimento da máquina
# print("ALERTA! Temperatura atingiu o limite. Desligando o motor...")

# # Exemplo:Menu de Interação
# # != Diferente
# opcao = ""
# while opcao !="sair" and "SAIR":
#     opcao=input ("Digite a leitura do sensor ou 'sair' para fechar: ") .upper() .lower()
#     if opcao !="sair" and "SAIR":
#         print(f"Dado '{opcao}' registrado no banco de dados.")
# print("Sistema encerrando")      

# Exercicio 5
#Monitor de Pressão Crítica (while)
#Crie um simulador onde o usuário deve digitar a pressão atual de um compressor.
#Enquanto a pressão for menor que 100 PSI, o programa continua pedindo a nova leitura.
#Assim que o usuario digitra um valor maior ou igual a 100, o loop para e exibe a mensgagem :"ALERTA"; Pressão Critica atingida!
#Desligando sistema.
# import time
# pressão =0
# v1= int(input("Valor de Pressão:"))
# while v1 <100:
#     print(f"Pressão Atual: {v1} PSI. Sistema operando...")
#     time.sleep(2)
#     pressão +=100
# print("ALERTA: Pressão Critica atingida!, desligando o sistema")

# Exercicio 5
# Criar um menu de opções com 4 itens ex: Escolher Series apresente sua escolha de séries das outras três.
#qualquer opcao diferente sair do menu
# print("Bem-Vindo ao menu de séries!")
# print("Informe a série que deseja assistir:")
# print("1- Pokemon")
# print("2- HarryPoter")
# print("3- StrangerThings")
# print("4- Cidade dos Homens")

# serie = input("Selecione sua opção:")
# if serie =="1":
#  print("Pokemon Selecionado")


# if serie =="2":
#  print("HarryPhoter Selecionado")


# if serie =="3":
#  print("StrangerThings Selecionado")


# if serie =="4":
#  print("Cidade dos homens Selecionado")

# else:  
#   print("Saindo de menu")

