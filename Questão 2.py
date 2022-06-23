# 2) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os
# números.

numero = []
soma = 0
produto = 1
for i in range (5):
    numero.append(int(input("Número {}: ".format(i+1))))
    produto = produto * numero[i]
soma = sum(numero)
print("Soma: ",soma)
print("Multiplicação dos números: {}".format(produto))
for i in range(5):
    print("Número {}: ".format(i+1), numero[i])