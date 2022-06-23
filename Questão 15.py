# 15) Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
# caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def verificacao (inteiro):
    if inteiro >=0:
        print("P")
    else:
        print("N")
inteiro = int(input("Valor a ser verificado: "))
verificacao(inteiro)