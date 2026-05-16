# Condições lógicas
# if: "Se" a condição for verdadeira.
# elif: "Senão, se"(usado para multiplas condiçoes)
# else: "Senão"(executa se nenhuma das anteriores for verdadeira.)

# print("Verificar Maioridade")
# idade = int(input("Digite sua idade:"))

# if idade >= 18:
#     print("Você é adulto.")
# elif idade >= 16:
#     print("Você não é adulto mas pode votar")
# else:
#     print("Você é Adolescente")


# print("Loja")
# print("Bem-Vindo ao Sistema de Franz")
# print("Opções")
# print("1-Sapatos")
# print("2-Roupas")
# print("3-Perfumes")

# escolha = int(input("Digite sua escolha pelo número da opção:"))
# if escolha == 1:
#     print("Você escolheu sapatos")
#     v1 = float(input("Digite o valor do produto: "))
#     qt1 = int(input("Digite a quantidade desejada: "))
#     total = v1 * qt1
#     print("Sua compra de sapatos foi um total de:" , total)
# elif escolha == 2:
#     v3 = float(input("Digite o valor do produto: "))
#     qt3 = int(input("Digite a quantidade desejada: "))
#     total = v3 * qt3
#     print("Sua compra de Roupas foi um total de:" , total)
# elif escolha == 3:
#     v4 = float(input("Digite o valor do produto: "))
#     qt4 = int(input("Digite a quantidade desejada: "))
#     total = v4 * qt4
#     print("Sua compra de Perfumes foi um total de:" , total)
# else:
#     print("Tente novamente.")

#Exemplo 3
# print("Escolha uma opção para iniciar o sistema")
# print("Series = S")
# print('Filmes =F')
# categoria = input("Digite sua Categoria:")
# if categoria == "S":
#     print('Você escolheu por Séries')
# elif categoria == "F":
#     print('Você escolheu por Filmes')
# else:
#     print("Obrigado por escolher uma das categorias")

#Exercicio 1
#Crie um algoritmo que simule uma calculadora e que por opção permita calcular os os operadores.
#Ex: Ao escolher a opção 1, ele irá calcular a soma e assim por diante

# print ("Bem vindo a Calculadora")
# print("Escolha uma opção abaixo: ")
# print("soma = +") 
# print("substração = -") 
# print("divisão = /") 
# print("multiplicação = *") 
# escolha = input("Digite a operação desejada: ")

# if escolha == "+":
#     soma1 =float(input("Digite o primeiro valor"))
#     soma2 =float(input("Digite o segundo valor"))
#     tsoma = soma1 + soma2
#     print("O valor é:" , tsoma)

# elif escolha == "-":
#     sub1 =float(input("Digite o primeiro valor"))
#     sub2 =float(input("Digite o segundo valor"))
#     tsub = sub1 - sub2
#     print("O valor é:" , tsub)

# elif  escolha == "*":
#     mult1 =float(input("Digite o primeiro valor"))
#     mult2 =float(input("Digite o segundo valor"))
#     tmult = mult1 * mult2
#     print("O valor é:" , tmult)

# elif escolha == "/":
#     div1 =float(input("Digite o primeiro valor"))
#     div2 =float(input("Digite o segundo valor"))
#     tdiv = div1 / div2
#     print("O valor é:" , tdiv)

# #Exercicio 2
#Calculo de idade: Deve apresentar o nome, curso, data de nascimento e apresentar a idade sua no final
# nome=str(input("Digite seu nome:"))
# curso=input("Digite seu curso: ")
# nascimento=int(input("Digite seu ano:"))
# ano = 2026
# variavel= 2026 - nascimento
# print("Seu nome é:", nome,)
# print("Seu curso é:", curso)
# print("Você tem:", variavel)

#Exercicio 3
#Calcular gorjetas receba o valor da conta de um restaurante e retorne o valor da gorjeta (consdierando 10% do valor da conta)
#Atendimento em mesa com graçom 10%
#Atendimento em mesa sem garçom 5%

# print("Bem-vindo ao Restaurante")
# print("Por favor, selecione uma das opçoes abaixo: \n") 
# op1=input("- Atendimento em mesa com garçom ou sem?:")
# op2=float(input("Qual foi o valor gastado?:"))

# if op1== "com": 
#     gorjeta1=op2*(10/100)
#     valorfinal=op2+gorjeta1

#     print("O valor após a grojeta é: ", valorfinal)

# elif op1== "sem":
    
#     gorjeta2 = op2*(5/100)
#     valorfinal2=op2 + gorjeta2
    
#     print("O valor após a grojeta é: ", valorfinal2)
# else:
#     print("Por favor tente novamente")

# Exercicio 4
#Criar um sistema para calcular o sucessor e antecessor de um valor
# v1= int(input("Digite o primeiro valor"))
# v2= int(input("Digite o segundo valor"))




 





