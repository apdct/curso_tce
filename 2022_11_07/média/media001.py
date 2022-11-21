"""
Programa média
Requisito: Este programa pega números armazenados na memória, calcula a sua
média e coloca o resultado na tela com uma frase que explique o que é o
resultado obtido.
Autor: Ana
Data: 21/11/2022
Versão: 0.0.1
"""

# Definição de funções

def entrada():
    soma = 0
    i = 0
    x = [ 1, 7, 15, 31, 6 ]
    return [soma, i, x]

def calculo_media (soma, i, x):
    while i < len(x):
        soma = soma + x[i]
        i+=1
        media = soma/len(x)
    return media

def saida (x):
    print(f"A média dos números informados é igual a {x}")

def main():
    valores = entrada()
    media = calculo_media(valores[0], valores[1], valores[2])
    saida(media)
    
main()
