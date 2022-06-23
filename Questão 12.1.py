# 12) Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes (os
# elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para multiplicação,
# multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação.

# Leitura das dimensões da matriz A ============================================================
print("\nMatriz A ","="*50)
nlinhasA = int(input("Número de linhas: "))
ncolunasA = int(input("Número de colunas: "))

# Leitura dos valores da matriz A ===============================================================
linhasA = []
for i in range (nlinhasA):
    colunasA = []
    for j in range (ncolunasA):
        colunasA.append(int(input("elemento [{}] [{}] = ".format(i,j))))
    linhasA.append(colunasA)

# Leitura das dimensões da matriz B ============================================================
print("\nMatriz B ","="*50)
nlinhasB = int(input("Número de linhas: "))
ncolunasB = int(input("Número de colunas: "))

# Leitura dos valores da matriz B ===============================================================
linhasB = []
for i in range (nlinhasB):
    colunasB = []
    for j in range (ncolunasB):
        colunasB.append(int(input("elemento [{}] [{}] = ".format(i,j))))
    linhasB.append(colunasB)

# verificação de compatibilidade entre as matrizes =====================================================
d = 0
linhasC = []
colunasC = []
if nlinhasA == nlinhasB and ncolunasA == ncolunasB:
    linhasC = []
    for i in range (nlinhasA):
        colunasC = []
        for j in range (ncolunasA):
            colunasC.append(linhasA[i][j]*linhasB[i][j])
        linhasC.append(colunasC)
        d = 1

print("\nMatriz A: ","="*50)
for i in range(nlinhasA):
    print(linhasA[i])

print("\nMatriz B: ","="*50)
for i in range(nlinhasB):
    print(linhasB[i])

if d == 1:
    print("\nMatriz C: ","="*50)
    for i in range(nlinhasA):
        print(linhasC[i])
