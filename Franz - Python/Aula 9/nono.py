# 1. O Problema de Idade
# idade = input("Digite sua idade: ")
# if idade >= 18:
#     print("Você é maior de idade.")

#ITEM CORRIGIGO:
# idade =int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade. ")
# else:
#     print("Você é menor de idade. ")

#ITEM MELHORADO:
# print("===Painel de Idade===")
# idade = int(input("Informe a sua idade:\n"))
# if idade >= 18:
#     print("Você é maior de idade.")
# elif idade <18:
#     print("Você é menor de idade.")
# else:
#     print("Valor Inválido.")

#===============================================

# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

#ITEM CORRIGIDO:
# nome = "Mariana"
# print(f"Seja bem vinda {nome}!")

#ITEM MELHORADO:
#print("===Cadastro de Usuário===")
# nome_user = str(input("Informe seu nome completo:\n"))
# print(f"Seja bem-vindo(a) {nome_user}!")

#===============================================

# 3. Falta de Espaço
# numero = 10
# if numero >5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#ITEM CORRIGIDO:
# numero = 10
# if numero >5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

#ITEM MELHORADO:
# print("===Controle de Números=== ")
# numero_user = float(input("Informe o número:\n"))
# if numero_user >5:
#     print("Seu número é maior que cinco.")
# elif numero_user <=5:
#     print("Seu número é menor ou igual a cinco.")
# else:
#     print("Número Inválido.")


#===============================================

# 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario =="aluno123"
#     print("Login realizado com sucesso.")

#ITEM CORRIGIDO:
# usuario = "aluno123"
# if usuario =="aluno123":
#      print("Login realizado com sucesso.")

#ITEM MELHORADO:
# print("===Login Conta===")
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login Realizado com sucesso.")
# else:
#     print("Usuário ou senha incorretos.")

#===============================================

# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso"
#     print("Leve um guarda-chuva!")

#ITEM CORRIGIDO:
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")

#===============================================

#6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez" + pontos+ "pontos.")

# #ITEM CORRIGIDO:
# pontos = 50
# print(f"Parabéns! Você fez {pontos} .")

#ITEM MELHORADO:
# print("===Pontução===")
# pontos_usuario = float(input("Informe quantos pontos você obteve:\n"))
# print(f"Parabéns! Você fez {pontos_usuario} pontos!")

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

#ITEM CORRIGIDO:
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota == 7:
#     print("Aprovado")
# elif nota > 9:
#     print("Excelente!")

#===============================================

# 8. O Contador de 1 a 5
#Objetivo: Mostrar na tela os números 1,2,3,4 e 5
# for i in range(5):
#     print(i)

#ITEM CORRIGIDO:
#Objetivo: Mostrar na tela os números 1,2,3,4 e 5
# for i in range(6):
#     print(i)

#ITEM MELHORADO:
# print("===Impressão de Cópias")
# valor_copias= int(input("Informe o número de cópias desejadas:\n"))
# print("Imprimindo cópias...")
# for valor_copias in range(valor_copias):
#     print(valor_copias)
#===============================================

# 9. O Loop Eterno
# tentativas=1
# while tentativas <=3:
#     print("Tentando conectar...")
    
#     #O código deveria parar após 3 tentativas

#ITEM CORRIGIDO:
# tentativas=1
# while tentativas <=3:
#     print("Tentando conectar...")
#     break
#     #O código deveria parar após 3 tentativas

#===============================================

#10. A Senha Teimosa
#O programa deve pedir a senha até que o usuário digite "python123"
# senha =""
# while senha =="python123":
#     senha = input("Digite a senha secreta:")
# print("Acesso concedido!")

#ITEM CORRIGIDO:

# senha = ""

# while senha !="python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

