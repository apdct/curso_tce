"""
Programa soma
Requisito: Lar 4 números reais digitados pelo usuário, calcula a sua soma e
colocar o resultado na tela.
Autor: Ana Paula C.
Data: 16/11/2022
Versão: 0.0.4
"""

# Entrada

i = 0 #contador
soma = 0

while i < 4:
    numero = float(input("Digite a parcela: "))
    soma = soma + numero #acumulador
    i = i + 1
    

# Processamento


# Saída

print(f"\nA soma dos números informados é igual a {soma}.")
