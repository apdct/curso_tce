"""
Programa soma
Requisito: Ler um conjunto de números reais digitados pelo usuário, calcular
a soma deles e colocar o resultado na tela.
Autor: Ana Paula C.
Data: 16/11/2022
Versão: 0.0.5
"""

# Entrada e Processamento de dados

soma = 0

while True:
    numero = input("Digite a parcela ou pressione a tecla X para interromper: ")
    if numero == "X":
        break
    soma = soma + float(numero)
    
    



# Saída

print(f"\nA soma dos números informados é igual a {soma}.")
