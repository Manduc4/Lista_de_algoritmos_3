# 4) Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do vetor.

A = []
soma = 0
for i in range(10):
    A.append(int(input("Número {}: ".format(i+1))))
    soma = soma + A[i]**2
print("Soma: ", soma)
