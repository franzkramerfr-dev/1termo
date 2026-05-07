# # Revisão Somativa - Aula 7
# # Questão 1
# print("Registro de Veículo")

# modelo_veiculo = input("Informe o modelo do veículo: ")

# placa_veiculo = input("Informe a placa do veículo: ")

# print(f"Veículo {modelo_veiculo} de placa {placa_veiculo} \n registrando no sistema. Boa viagem!...")

# #Questão 2
# print("Cálculo de Autonomia")

# capacidade_tanque = float(input("Informe a capacidade do tanque em litros: "))

# consumo_medio = float(input("Digite o consumo: "))

# distancia_total = capacidade_tanque * consumo_medio

# print(f"Capacidade {capacidade_tanque} do tanque e sua distancia {consumo_medio} em média KM/L e o total {distancia_total}")

# #Questão 3 
# print("Conversor de Moeda (Frete Internacional)")

# valor_frete = float(input("Valor de frete em Dolar: "))

# conversao_real = float(input("Valor da taxa em reais: "))

# total_conversao = valor_frete * conversao_real

# print(f"O valor do frete foi {valor_frete} e a taxa aplicada foi de {conversao_real} e o total do frete {total_conversao:.2f}")#:.2f para exibir com duas cadas decimais

# print("O valor do frete foi" ,valor_frete, "e a taxa aplicada foi de",conversao_real, "e o total do frete", round(total_conversao,2))#round para exibir com duas casas decimais

# #Questão 4
# print("Média de Entregas")

# rota1= int(input("Digite a primeira rota em horas:"))

# rota2= int(input("Digite a segunda rota em horas:"))

# rota3= int(input("Digite a terceira rota em horas:"))

# media_rota = (rota1 + rota2 + rota3)
# print(f"Média de Entregas das rotas realizadas foi de {media_rota:.2f}")

# #Questão 5
# print("Monitor de Carga - Peso em toneladas")
# peso_caminhao = float(input("Informe o peso do caminhão em toneladas: "))
# if peso_caminhao <=10:
#     print("Carga Leve")
# elif 10 < peso_caminhao < 25:
#     print("Carga padrão")
# elif peso_caminhao >= 25:
#     print("ALERTA: Excesso de Peso!")
# else:
#     print("Digite outro valor: ")

# #else :
# #   print("ALERTA: Excesso de Peso! ")

# #Questão 6
# print("Classificador de Destino - Código de Cargas")
# print("Código de Cargas = N - Norte S- Sul e Outros Internacional")

# codigo_carga = input("Inserir o código da Carga em N ou S ou O: ")#lower()
# if codigo_carga == "N": #lower
#     print("Região Norte")
#     #lower() #texto minusculo
# elif codigo_carga == "S":
#     print("Região Sul")
# elif codigo_carga == "O":
#     print("Região Internacional")
# else:
#     print("Região Internacional" )

# #Questão 7
# print("===LIBERAÇÃO DE SAÍDA===")
# checklist = input("O checklist foi realizado (Concluído ou Não Concluído)")
# motorista = input("O motorista foi identificado (Sim ou Não)")
# #and = verdadeiro
# #or = verdadeiro ou falso
# if checklist == "Concluído" and  motorista == "Sim":
#     print("Iniciar Rota - Boa Viagem ")
# else: 
#     print("Voltar e realizar o Checklist! ")

# #Questão 8
# print("===CÁLCULO DE ATRASOS===")
# total_entregas = int(input("Informe o total de entregas agendadas: "))
# entregas_atraso = int(input("Informe o total de entregas realizadas com atraso: "))
# total = entregas_atraso / total_entregas

# if total >0.1:
#     print("Necessário Otimizar Rotas")
# else:   
#     print("Logística Eficiente")

# #Qustão 9
# print("===VALIDAÇÃO DE CALIBRAGEM===")
# psi: 0
# v1 = float(input("Informe a medida da pressão em PSI dos pneus: "))
# if v1 <100:
#     print("Pressão abaixo do recomendado.")
# elif v1 >110:
#     print("Pressão acima do recomendado.")
# else:
#     print("Pressão recomendada dentro do padrão.")

# #Questão 10
# print("===CONTAGEM REGRESSIVA PARA O FECHAMENTO DO PORTÃO===")
# from time import sleep
# for embarque in range(5,0,-1):
#     sleep(1)
#     print(embarque)
# print("Portão Trancado!")

# #Questão 11
# print("===Somatório de Fretes (Acumulador)===")
# faturamento = 0
# while True:
#    valor=  float(input("Informe o valor do Frete dos produtos (Digite 0 para finalizar):"))
#    if valor == 0:
#       break
#    faturamento += valor
# print(f"Faturamento total: R$ {faturamento}")

# #Questão 12
# var = 0
# print("===MONITORAMENTO DE FROTA===")
# vei1= int(input("Informe a quilometragem do veículo 1: "))
# for km in range(2,6):
#     veis=  float(input(f"Informe a quilometragem do veículo {km} registrada:"))
#     if veis > var:
#         var=var+veis
    
# print(f"A maior quilometragem foi de: {var}")

# Questão 13
# acesso_negado =0
# while acesso_negado != 3:
    
#     code= (input("Digite o código de acesso do rastreador:"))
#     if code != "track99":
#         acesso_negado= acesso_negado+1
#         print("Acesso Negado!")
#         print("Rastreamento Bloqueado")
#     elif code:
#         print("Acesso Liberado!")
#         break   
        
# Questão 14
# tanque =500
# while True:
#     print("1 - Abastecer tanque")
#     print("2 - Retirar combustível")
#     print("3 - Sair")
#     opção = input("Escolha uma opção:")
    
#     if opção =="1":
#         qtd = float(input("Quantos litros deseja adicionar?: "))
#         tanque += qtd

#     elif opção == "2":
#         qtd = float(input("Quantos litros deseja retirar? "))
#         tanque -= qtd 

#     elif opção == "3":
#         print("Encerrando sistema...")
#         break

#     else:
#         print("Opção inválida!")

# print(f"Tanque atual: {tanque} litros")

# if tanque < 50:
#     print("Reserva Crítica!")

# #Questão 15
# print("Relatório de Inspeção de Pneus")

# contagem =0
# total =5

# for pneu in range(1,6):

#     medida= float(input(f"Digite a medida do sulco do pneu {pneu} em mm"))
    
#     if medida >=1.6:
#         contagem + contagem +1
#         print("Pneu aprovado e adicionando a contagem")
#     else:
#         print("Pneu fora das medidas regulares não foi adicionado a contagem")
#     pass
# porcentagem = (contagem / total) * 100
# print(f"Tiveram {contagem} pneus aprovados hoje com uma taxa de {porcentagem} % de conformidade")
