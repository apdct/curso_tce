"""
Programa soma Requisito: Este programa pega dois números difitados
pelo usuário, calcula o produto e coloca o resultado na tela com uma frase
que explique o que é o resultado obtido.
Autor: Ana
Data: 15/11/2022
Versão: 0.1.2
Correção do bug: chamar de "parcela" de parcela o que é "fator".
Inclusão de funcionalidade: informar o usuário para que serve o programa.
"""

# Entrada
print("Este programa calcula o produto de dois números dados pelo usuário.\n")
numero_1 = float(input("Digite o primeiro fator: "))
numero_2 = float(input("Digite o segundo fator: "))

# Processamento
multi = numero_1*numero_2

# Saída

print(f"A multiplicação dos números {numero_1} e {numero_2} é igual a {multi}.")
