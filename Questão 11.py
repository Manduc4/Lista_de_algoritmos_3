# 11) Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a soma
# das matrizes A e B.

#Criação da matriz A =======================================================
A = []
for i in range (2):
    a = []
    for j in range (2):
        a.append(int(input("Digite um número: ")))
    A.append(a)
#Criação de uma matriz B ====================================================
B = []
for i in range (2):
    b = []
    for j in range(2):
        b.append(int(input("Digite outro numero: ")))
    B.append(b)
#Soma das matrizes A e B ===================================================
C = []
for i in range (2):
    c = []
    for j in range (2):
        c.append(A[i][j]+B[i][j])
    C.append(c)
print(C)
