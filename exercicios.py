import math

# Exercicio 04: Divisão Inteira do Primeiro pelo Segundo Número
try:
    numero01 = int(input("Informe um número inteiro: "))
    numero02 = int(input("Informe outro número inteiro: "))
    resultado = numero01 // numero02
    print(resultado)
except ZeroDivisionError:
    print("Integer division or modulo by zero")
except KeyboardInterrupt:
    print("Acho que você não quis inserir um número")
except: # Generico
    print("Error")
# Exercicio 10: Área de um Círculo
"""
raio_do_circulo = float(input("Digite o raio: " ))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")
"""

# Exercicio 14: Separar Dia, Mês e Ano de uma Data
"""
data_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_data = data_usuario.split("/")
print(lista_data[0])
"""