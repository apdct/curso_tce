"""
Programa Maior que cinco
Requisito: Leia um número digitado pelo usuário e diga se ele é maior do que 5.
Autor: Ana Paula da C.
Data: 16/11/2022
Versão: 0.0.1
"""

# Entrada
numero = float(input("\nDigite um número real: "))

# Processamento
if numero > 5:
    frase = f"\nO número {numero} é maior que 5."
elif numero == 5:
    frase = f"\nO número {numero} é igual a 5."
else:
    frase = f"\nO número {numero} é menor que 5."

# Saída
print(frase)
