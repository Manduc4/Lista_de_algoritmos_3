# 9) Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato
# de escada.
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = []
nome = str(input("Digite seu nome: "))
nome = nome.upper()
for i in range (len(nome)+1):
    for j in range (i):
        print(nome[j],end="")
    print(" ")