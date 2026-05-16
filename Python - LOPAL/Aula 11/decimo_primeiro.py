#Explicação de def: A palavra-chave "def" é usada em Python para definir uma função. Uma função é um bloco de código reutilizável que realiza uma tarefa específica.
#return: A palavra-chave "return" é usada para finalizar a execução de uma função e retornar um valor para o local onde a função foi chamada. O valor retornado pode ser usado poseriormente no código.

#Exemplo de função com def e return:

def nome_da_funcao(parametro1, parametro2):
    # Corpo da função (código que será executado)
    resultado = parametro1 + parametro2
    return resultado

def saudacao(nome):
    return f"Olá, {nome}!"
print(saudacao("Franz"))

def usuario():
    nome = input("Digite seu nome: ")
    return nome 
print(f"Olá, {usuario()}!")

def valores():
    print("Digite três valores: ")
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    return a, b, c
print(f"O maior valor é: {max(valores())}")

# # Reutilizando Funções
usuario()
valores()


# Conceitos Chave
#def: Indica o inicio da definição de uma função.
#Nome: Identifica a função para você chama-la depois.
#Parâmetros: Dados que a função recebe (opicional)
#return: Envia o resultado de volta para quem chamou a função.
#(opicional)

# Exercicio 1: Crie uma função que solicite ao usuário um número e retorne o dobro desse número. Em seguida, chame a função e exiba o resultado.
def calcular_dobro():
    numero_usuario = float(input("Digite um número: "))
    return numero_usuario * 2
print(calcular_dobro())