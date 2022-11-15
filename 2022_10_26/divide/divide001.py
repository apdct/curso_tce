"""Programa divide
Requisito: Crie um programa que leia dois números inteiros do teclado, calcule
a razão do primeiro e o segundo e escreva na tela o resultado.
Autor: Ana Paula C.
Versão: 0.0.1
"""

# Entrada
print("Este programa calcula a razão entre dois números dados pelo usuário.\n")
numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador: "))

# Processamento
razao = numerador / denominador

# Saída
print(f"\nA razão entre {numerador} e {denominador} é igual a {razao}.")
