# 10) Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal
# da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação.

x =[]
k = 2
for i in range (3):
    y = []
    for j in range(3):
        y.append(int(input("Digite um valor: ")))
    x.append(y)
print(x)
for i in range (3):
    x[-(i-2)][i] =  x[-(i-2)][i]  * k
print(x)