"""
Programa soma Requisito: Este programa pega dois números digitados
pelo usuário, calcula a sua soma e coloca o resultado na tela com uma frase
que explique o que é o resultado obtido.
Autor: Ana
Data: 21/11/2022
Versão: 0.0.6
"""

# Definição de funções

def entrada():
    numero_1 = float(input("Digite a primeira parcela: "))
    numero_2 = float(input("Digite a segunda parcela: "))
    lista_valores = [numero_1, numero_2]
    return lista_valores

def soma(x, y):
    return x + y

def saida(x, y, z):
    print(f"A soma dos números {x} e {y} é igual a {z}.")

def main():
    """ Programa principal"""
    # Entrada
    lista_valores = entrada()
    
    # Processamento
    valor = soma(lista_valores[0], lista_valores[1])
    
    # Saída
    saida(lista_valores[0], lista_valores[1], valor)

# Chama à execução da função principal

main()
