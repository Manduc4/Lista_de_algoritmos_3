# Faça um programa para imprimir:
# 1
# 2 2
# 3 3 3
# .....
# n n n n n n ... n
#
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-
# ésima linha.

x = int(input("Digite um valor: "))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(i," ",end = "")
    print("")
