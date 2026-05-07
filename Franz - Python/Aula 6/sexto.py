# Lista de temperatura lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 40, 10, 85, 80]
# baixos = [10, 20, 30, 40, 50, 40, 10]


# for temp in leituras:
#      if temp > 100:
#         print(f"CRÍTICO: {temp} ºC detectado! Adicionando parada de emergencia!.")
#         break # O loop para aqui e não le os proximos valores (85, 80)
#      else: 
#         print(f"Temperatura normal operando {temp} ºC")
   
# for temp1 in baixos:
#     if temp1 < 50:
#      print (f"CRÍTICO: {temp1}ºC detectado! Adicionando parada de emergencia.")
#      break

# else:
#  print ("Sistema desligado. Aguardando manutenção")

#Exericio 2 
# materias = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materias:
#     if peca != "metal":
#         print(f"Aviso: Peça de {peca} detectada. Desviando para descarte")
#         continue
# print(f"Processando peça de {peca}. Furando e polindo...")

# print("Fim do lote de produção.")

# Exercicio 1 
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando um afalha no sensor especifica no item 5)


# from time import sleep
# for i in range(1,11):
#     if i == 5:
        
#         print(f"simulando uma falha de sensor especifica no item {5}")
#         continue
#     sleep(1)
#     print(f"listando números {i}")
# print("Fim!")

# Exercicio
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa
# from time import sleep
# vermelho= range(1,2)
# amarelo= range(1,2)
# verde= range(1,2)
# while True:
#     for sinal in vermelho:
#      sleep(2)
#     print("Vermelho- PARE!")

#     for sinal in amarelo:
#      sleep(2)
#     print("Amarelo- ATENÇÃO!")

#     for sinal in verde:
#      sleep(2)
#     print("Verde- PASSAGEM AUTORIZADA!")

# Exercício 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.
# fabrica = ("CONSUMO MÁQUINA 1:", "CONSUMO MÁQUINA 2:", "CONSUMO MÁQUINA 3:", "CONSUMO MÁQUINA 4:", "CONSUMO MÁQUINA 5:")
# total = 0

# for maquinas in fabrica:
#     v1 = int(input(f"Digite o consumo da primeiro máquina em Kwh: {maquinas} \n"))
#     print(maquinas)
#     v2 = int(input("Digite o consumo da segunda máquina em Kwh: \n"))
#     print(maquinas)
#     v3 =int(input("Digite o consumo da terceira máquina em Kwh:"))
#     v4 =int(input("Digite o consumo da quarta máquina em Kwh:"))
#     v5 =int(input("Digite o consumo da quinta máquina em Kwh:"))
#     total = v1 + v2
#     print(f"O consumo total foi de: Kwh ", total)
#     break

# Exercício 4 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for pecas in medidas:
#  if pecas> 50:
#   print(f"Peça {pecas} Aprovada...")
#  else: 
#   print(f"Peça {pecas} Rejeitada")

# Exercício 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.
# sacos = [49.5, 50.0, 51.2, 48.9, 50.5, 47.8]
# for peso in sacos:
#     if 49.0 <= peso <= 51.0:
#         print(f"Saco com peso {peso}kg: Aceitável")
#     else:
#         print(f"Saco com peso {peso}kg: Rejeitado - Fora do limite aceitável")


# O Desafio: Gestão de Ciclo Térmico
# Você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças.
# Regras do Sistema:
# O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# Para cada peça, peça ao usuário a temperatura atual (input).
# Filtro de Erro (continue): Se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de Emergência (break): Se a temperatura for maior que 150°C, o sistema deve exibir "ALERTA CRÍTICO: Risco de Explosão!", interromper o loop imediatamente e encerrar o programa.
# pecas = 0
# while pecas <5:
#     temp = float(input("Digite a temperatura da estufa:"))
#     if temp <0:
#         print("Erro de leitura no sensor. Por favor, insira uma temperatura válida.")
#         continue
#     elif temp>150:
#         print("ALERTA CRÍTICO: Risco de Explosão!")
#         break
#     else:
#         print(f"Peça {pecas +1} processada com sucesso a {temp}ºC.")
#         pecas+=1

#Exercicio 8 - Monitoramento de Vibração
# Uma máquina industrial tem um sensor de vibração que registra os seguintes valores em mm/s: [0.5, 1.2, 0.8, 2.5, 0.3, 1.0, 3.0, 0.4]. O limite de vibração aceitável é de até 1.5 mm/s.
# Crie um programa que percorra a lista de vibração e:
# - Se a vibração for maior que 1.5 mm/s, exiba "ALERTA: Vibração excessiva detectada!" e continue para a próxima leitura.
# - Se a vibração for menor ou igual a 1.5 mm/s, exiba "Vibração dentro do limite aceitável." para cada leitura.


lista= [10.5, 1.2, 0.8, 2.5, 0.3, 1.0, 3.0, 0.4]
for vibracao in lista:
    vibracao>1.5
    print(f"ALERTA: Vibração excessiva detectada!")
else:
    vibracao <=1.5
    print("Vibração dentro do limite aceitável.")
















































# from time import sleep
# valores = [0.5, 1.2, 0.8, 2.5, 0.3, 1.0, 3.0, 0.4]

# for vibração in valores:
#     sleep(1)
#     if  1.5<= vibração:
#         print(f"Vibração {vibração}mm/s: ALERTA: Vibração excessiva detectada!")
#     else:
#         print(f"Vibração {vibração}mm/s: Vibração dentro do limite aceitável!")

# Exercício 8: Sistema Inteligente de Manutenção
# Crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina.
# O programa deve classificar o estado da máquina seguindo esta hierarquia:
# Crítico (Prioridade 1): Se a pressão for maior que 100 OU as horas de uso forem maiores que 10.000.
# Mensagem: "PARADA IMEDIATA: Risco de falha catastrófica."
# Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
# Mensagem: "MANUTENÇÃO AGENDADA: Pressão acima do ideal."
# Monitoramento (Prioridade 3): Se as horas de uso forem entre 8.000 e 10.000.
# Mensagem: "AVISO: Máquina aproximando-se da revisão de 10k horas."
# Normal: Para qualquer outro caso que não se encaixe nos acima.
# Mensagem: "SISTEMA OPERAL: Todos os parâmetros dentro da normalidade."

