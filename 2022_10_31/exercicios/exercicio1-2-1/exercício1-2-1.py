"""
Programa: exercício 1-2-1
Requisito: leia um número e imprima na tela o seu dobro se ele for menor do
que 10. Se o núumero for de 10 até 20, imprima a sua metade. Em qualquer
outro caso, imprima na tela que o núumero não é válido.
Autor: Ana Paula C.
Data: 16/11/2022
Versão: 0.0.1
"""

# Entrada
numero = float(input("Digite um número: "))


# Processamento
resultado = 0

if numero < 10:
    resultado = 2*numero

elif numero >= 10 and numero <=20:
    resultado = numero/2

else:
    resultado = "\nO número não é válido."

# Saída
print(resultado)
