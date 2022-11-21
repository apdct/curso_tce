"""
Programa lista_compras
Requisitos: Leia uma lista de compras dada pelo usuário e coloque na tela
a lista que foi digitada.
Autor: Ana Paula C.
Data: 17/11/2022
Versão: 0.0.3
"""

# Inicialização de variáreis

lista_compras = []

# Entrada
# Uso do método append

while True:
    elemento = input("Digite um ítem para a lista de compras ou tecle X para interomper: ")
    if elemento == "X":
        break
    lista_compras.append(elemento)

        


# Saída

print(f"A lista de compras é a seguinte: {lista_compras}.")
