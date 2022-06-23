# 5) Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
# elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

# leitura do vertor 1 =============================================================
vetor1 = []
print("\nVetor 1 ","="*50)
for i in range (10):
    vetor1.append(int(input("Elemento {}: ".format(i+1))))

# leitura do vetor 2 ================================================================
vetor2 = []
print("\nVetor 2 ","="*50)
for i in range (10):
    vetor2.append(int(input("Elemento {}: ".format(i+1))))

# processamento do vetor 3 ==========================================================
vetor3 = []
print("\nVetor 3 ","="*50)
for i in range (10):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])
print(vetor3)

