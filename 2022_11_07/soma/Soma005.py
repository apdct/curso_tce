"""
Programa soma Requisito: Este programa pega dois números digitados
pelo usuário, calcula a sua soma e coloca o resultado na tela com uma frase
que explique o que é o resultado obtido.
Autor: Ana
Data: 21/11/2022
Versão: 0.0.5
"""

# Definição de funções

def entrada():
    numero_1 = float(input("Digite a primeira parcela: "))
    numero_2 = float(input("Digite a segunda parcela: "))
    lista_valores = [numero_1, numero_2]
    return lista_valores

def soma(x, y):
    return x + y

def saida():
    print(f"A soma dos números {lista_valores[0]} e {lista_valores[1]} é igual a {valor}.")


# Programa principal

# Entrada
lista_valores = entrada()

# Processamento
valor = soma(lista_valores[0], lista_valores[1])

# Saída

saida()
